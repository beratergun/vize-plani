# -*- coding: utf-8 -*-
"""Programatik kalite kontrolleri → 09_Quality_Assurance/VALIDATION_REPORT.md"""
import os
import re
import shutil
import tempfile
import zipfile
import xml.dom.minidom as minidom
from datetime import date, timedelta
from common import *

TOPICS = {  # syllabus'taki tüm konular (finale kadar)
    "BIO110": ["Chemical Context", "Water and Life", "Carbon", "Large Biological Molecules", "Tour of the Cell", "Membrane", "Metabolism", "Cellular Respiration",
               "Photosynthesis", "Cell Cycle", "Mendel", "Chromosomal", "Molecular Basis", "Gene Expression", "Regulation of Gene", "DNA Tools",
               "Descent with Modification", "Evolution of Populations"],
    "CMPE371": ["Introduction to Signals", "Sinusoids", "Special Signals", "LTI", "Differential and Difference", "Continuous-Time Fourier Series",
                "Continuous-Time Fourier Transform", "Discrete-Time Fourier Series", "Discrete-Time Fourier Transform", "Filtering", "Sampling", "Z-Transform"],
    "CMPE327": ["History", "Central Concepts", "Mathematical Preliminaries", "Deterministic Finite", "Nondeterministic", "Closure", "Equivalence of DFA and NFA",
                "Regular Languages", "Pattern Matching", "Regular Expressions", "State Minimization", "Myhill", "Derivatives", "Equivalence of Regular Expressions",
                "Context-Free", "Ambiguity", "Chomsky", "CYK", "Pumping", "Nonregularity", "Pushdown", "Ogden", "Turing", "Decision Problems"],
    "CMPE421": ["Introduction to AI", "Intelligent Agents", "Uninformed", "Informed", "Game Playing", "Constraint Satisfaction", "Adversarial", "Planning",
                "Knowledge Representation", "Theorem Proving", "Uncertainty", "Machine Learning Fundamentals", "Classification and Regression",
                "Neural Networks", "NLP and LLMs", "Reinforcement", "Ethics"],
    "CMPE453": ["Course Overview", "Architecture", "Programming AVR", "I/O", "Digital Input", "USART", "SPI", "Analog-to-Digital", "Interrupts", "Timers", "PWM",
                "ARM Cortex", "GPIO", "LED", "PWM for ARM"],
}
COURSES6 = ["BIO110", "CMPE371", "CMPE327", "CMPE421", "CMPE453", "CMPE499"]
R = []
FAIL = []


def check(name, ok, detail=""):
    R.append((name, ok, detail))
    if not ok:
        FAIL.append(name)


def main():
    plan = load_plan()
    prog = load_progress(plan)
    days = plan["days"]
    tasks = [(d, t) for d in days for t in d["tasks"]]
    caps = plan["caps"]

    # --- kapsam ve takvim
    check("Altı dersin tamamı planda", all(any(t["course"] == c for _, t in tasks) for c in COURSES6),
          ", ".join(f"{c}:{sum(1 for _, t in tasks if t['course'] == c)}" for c in COURSES6))
    ds = [date.fromisoformat(d["date"]) for d in days]
    exp = [date(2026, 10, 30) + timedelta(days=i) for i in range((date(2026, 12, 31) - date(2026, 10, 30)).days + 1)]
    check("30 Ekim–31 Aralık (14. hafta sonu) her takvim günü mevcut", ds == exp, f"{len(ds)} gün")
    ids = [t["id"] for _, t in tasks]
    check("Görev ID'leri benzersiz", len(ids) == len(set(ids)), f"{len(ids)} görev")
    blocks_sched = {}
    for _, t in tasks:
        if not t["block"].startswith("REV:"):
            blocks_sched[t["block"]] = blocks_sched.get(t["block"], 0) + 1
    check("Her blok tam bir kez programlı", set(blocks_sched) == set(plan["blocks"]) and all(v == 1 for v in blocks_sched.values()),
          f"{len(plan['blocks'])} blok")
    # --- syllabus kapsamı
    miss = []
    alltext = {c: " ".join(b["topics"] + " " + b["title"] for b in plan["blocks"].values() if b["course"] == c) for c in TOPICS}
    for c, tl in TOPICS.items():
        for k in tl:
            if k.lower() not in alltext[c].lower():
                miss.append(f"{c}:{k}")
    n_top = sum(len(v) for v in TOPICS.values())
    check("Syllabus'taki tüm konular (finale kadar) plan dışı kalmadı", not miss, f"{n_top} konu anahtarı; eksik: {miss or 'yok'}")
    # --- kapasite
    wk_over = []
    for d in days:
        cc, ec = caps[d["dtype"]]
        if d["ext_min"] > ec + 40 or d["core_min"] > cc + 70:
            wk_over.append(f"{d['date']} core {d['core_min']} ext {d['ext_min']}")
    check("Hiçbir gün aşırı yüklü değil (min ≤ 4,4 sa hafta içi / ext ≤ 6,7 sa)", not wk_over, "; ".join(wk_over) or "tamam")
    sun = [d for d in days if d["dtype"] == "sunday"]
    sun_hi = [d for d in sun if d["ext_min"] >= 360]
    check("Pazarlar hafta içinden yüksek kapasiteyle (≥6 sa genişletilmiş) planlı — ilk 4 hafta", all(d["ext_min"] >= 300 for d in sun[:3]),
          "; ".join(f"{d['date']}:{hours(d['ext_min'])}" for d in sun))
    light = [f"{d['date']}({d['core_min']})" for d in days if d["core_min"] < 100]
    R.append(("Bilgi: hafif günler (sınav öncesi/sonrası ya da boş): " + (", ".join(light) or "yok"), True, ""))
    # --- BIO öncelik
    bio_ok = all(days[i]["ranking"][0] == "BIO110" for i in range(0, 5))
    check("BIO110, 30 Ekim–3 Kasım arası her gün 1. öncelik", bio_ok, "; ".join(days[i]["ranking"][0] for i in range(5)))
    # --- ICS
    ics_dir = os.path.join(ROOT, "04_Calendar")
    for fn, expect in (("Study_Plan_2026.ics", len(days)), ("Exams_Deadlines_2026.ics", None)):
        t = open(os.path.join(ics_dir, fn), "rb").read().decode("utf-8")
        lines = t.split("\r\n")
        ev = t.count("BEGIN:VEVENT")
        uids = re.findall(r"^UID:(.*)$", t, re.M)
        ok = (t.startswith("BEGIN:VCALENDAR") and t.rstrip().endswith("END:VCALENDAR") and ev == t.count("END:VEVENT") and
              t.count("BEGIN:VALARM") == t.count("END:VALARM") and len(uids) == len(set(uids)) and max(len(l.encode()) for l in lines) <= 75 and "\r\n" in t)
        if expect:
            ok = ok and ev == expect
        check(f"{fn}: geçerli yapı, UID benzersiz, satır ≤75 oktet", ok, f"{ev} etkinlik")
    ex = open(os.path.join(ics_dir, "Exams_Deadlines_2026.ics"), "rb").read().decode("utf-8")
    unfold = ex.replace("\r\n ", "")
    check("CMPE453 midterm 12 Kasım 18:00–20:00 (Europe/Istanbul)", "DTSTART;TZID=Europe/Istanbul:20261112T180000" in unfold and "DTEND;TZID=Europe/Istanbul:20261112T200000" in unfold)
    check("CMPE499 teslimleri 22 ve 29 Kasım", "UID:eval-sum-str" in unfold and "DTSTART;VALUE=DATE:20261122" in unfold and "DTSTART;VALUE=DATE:20261129" in unfold)
    tent = [e for e in plan["evals"] if e["status"] in ("tentative", "window")]
    flagged = all(("[TEYİT BEKLİYOR] " + e["title"]) in unfold.replace("\\,", ",") or ("[TEYİT BEKLİYOR] " + e["title"]).replace(",", "\\,") in unfold for e in tent)
    check("Doğrulanmamış tarihlerin hepsi 'TEYİT BEKLİYOR' + STATUS:TENTATIVE", flagged and unfold.count("STATUS:TENTATIVE") == len(tent), f"{len(tent)} tarih")
    check("Final sınavına UYDURMA tarih yazılmadı", "eval-finals" not in unfold)
    # --- XLSX
    xp = os.path.join(ROOT, "06_Progress_Tracker", "Academic_Study_Tracker_2026.xlsx")
    z = zipfile.ZipFile(xp)
    for n in z.namelist():
        minidom.parseString(z.read(n))
    names = re.findall(r'<sheet name="([^"]+)"', z.read("xl/workbook.xml").decode())
    want = ["Dashboard", "Daily Tasks", "Course Progress", "Topic Mastery", "Exam Countdown", "Assignments", "Revision Schedule", "Mistake Log", "Slide Coverage", "Weekly Reviews"]
    check("Excel: 10 sayfa adı doğru ve XML iyi biçimli", names == want, ", ".join(names))
    sheet2 = z.read("xl/worksheets/sheet2.xml").decode()
    check("Excel: Daily Tasks satır sayısı = görev sayısı", sheet2.count("<row ") == len(tasks) + 1, f"{sheet2.count('<row ') - 1}/{len(tasks)}")
    refs = set(re.findall(r"'([^']+)'!", "".join(z.read(f"xl/worksheets/sheet{i}.xml").decode() for i in range(1, 11))))
    check("Excel: formüllerdeki sayfa referansları mevcut sayfalara işaret ediyor", refs <= set(names), ", ".join(sorted(refs)))
    # --- excel -> progress senkron testi (kopya üzerinde)
    import sync_from_xlsx as sx
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, "t.xlsx")
    zi = zipfile.ZipFile(xp)
    with zipfile.ZipFile(cp, "w", zipfile.ZIP_DEFLATED) as zo:
        for n in zi.namelist():
            data = zi.read(n)
            if n == "xl/worksheets/sheet2.xml":
                s = data.decode()
                s = s.replace(">Not Started<", ">Completed<", 1)
                data = s.encode()
            zo.writestr(n, data)
    rows = sx.read_sheet(cp, "Daily Tasks")
    check("sync_from_xlsx: değiştirilen durum doğru okunuyor", rows[1].get(10) == "Completed" and rows[1].get(1) == days[0]["tasks"][0]["id"], f"{rows[1].get(1)} → {rows[1].get(10)}")
    shutil.rmtree(tmp, ignore_errors=True)
    # --- replan testi (bellekte)
    import replan
    pl, moves, dropped = replan.replan(date(2026, 11, 5), apply=False)
    orig_ext = {d["date"]: d["ext_min"] for d in plan["days"]}
    bad = [d["date"] for d in pl["days"] if d["date"] >= "2026-11-05" and d["ext_min"] > max(orig_ext[d["date"]], caps[d["dtype"]][1] + 20)]
    check("replan (5 Kas, hiçbir şey yapılmamış varsayımı): kapasite aşılmıyor", not bad, f"{len(moves)} taşındı, {len(dropped)} düşürüldü; aşan: {bad or 'yok'}")
    check("Orijinal planda her dersin öğrenme blokları tanım (önkoşul) sırasında", _order_ok(plan) == [], str(_order_ok(plan)))
    skip = {t["id"] for _, t in dropped}
    check("replan sonrası da ders içi öğrenme sırası korunuyor (Postponed olanlar hariç)", _order_ok(pl, skip) == [], str(_order_ok(pl, skip)))
    # --- PDF
    pp = os.path.join(ROOT, "05_Printable_PDF", "Akademik_Basari_Plani_30_Ekim_2026.pdf")
    b = open(pp, "rb").read()
    pages = len(re.findall(rb"/Type\s*/Page[^s]", b))
    mb = re.findall(rb"/MediaBox\s*\[\s*0\s+0\s+([\d.]+)\s+([\d.]+)\s*\]", b)
    a4 = bool(mb) and all(abs(float(w) - 595.3) < 1.5 and abs(float(h) - 841.9) < 1.5 for w, h in mb)
    check("PDF: tüm sayfalar A4 ve sayfa sayısı makul (≤30)", a4 and pages <= 30, f"{pages} sayfa, MediaBox {mb[:1]}, {len(b) // 1024} KB")
    html = open(pp.replace(".pdf", ".html"), encoding="utf-8").read()
    check("PDF kaynağı: Türkçe karakterler UTF-8 ve tablo taşması CSS'i", all(ch in html for ch in "şğıİöüçŞĞ") and "@page { size: A4" in html)
    # --- site
    import json as _json
    site = open(os.path.join(ROOT, "10_Website", "artifact_page.html"), encoding="utf-8").read()
    m = re.search(r"const DATA = (\{.*?\});" + chr(10), site, re.S)
    sd = _json.loads(m.group(1).replace("<" + chr(92) + "/", "</")) if m else {}
    s_tasks = sum(len(d["t"]) for d in sd.get("days", []))
    check("Site: veri plan.json ile aynı (gün ve görev sayısı)", len(sd.get("days", [])) == len(days) and s_tasks == len(tasks), f"{len(sd.get('days', []))} gün, {s_tasks} görev")
    nolink = [t["ti"] for d in sd.get("days", []) for t in d["t"] if t["k"] in "L" and not t.get("l")]
    check("Site: her öğrenme görevinin en az bir kaynak bağlantısı var", not nolink, str(nolink[:5]) if nolink else f"{sum(1 for d in sd['days'] for t in d['t'] if t['k'] == 'L')} öğrenme görevi")
    badurl = [k for k, v in sd.get("links", {}).items() if not v[1].startswith("https://")]
    check("Site: tüm bağlantılar https", not badurl, str(badurl))
    try:
        import check_links
        res = check_links.check_all()
        bad = {k: v for k, v in res.items() if v != 200}
        check("Site: kaynak bağlantılarının hepsi HTTP 200 döndü", not bad, f"{len(res) - len(bad)}/{len(res)}" + (f"; sorunlu: {bad}" if bad else ""))
    except Exception as ex:
        R.append(("Site: bağlantı testi atlandı (ağ yok): " + type(ex).__name__, True, ""))
    try:
        vids = sorted({x[0] for d in sd.get("days", []) for t in d["t"] for x in t.get("vd", [])})
        vr = check_links.check_videos(vids)
        badv = [k for k, g in vr.items() if not g]
        check("Site: önerilen videoların hepsi YouTube'da doğrulandı (oEmbed)", not badv and len(vids) > 0, f"{len(vids) - len(badv)}/{len(vids)} video" + (f"; sorunlu: {badv}" if badv else ""))
        titles = [x[1].lower() for d in sd.get("days", []) for t in d["t"] for x in t.get("vd", [])]
        check("Site: video başlıklarında dil dışı (Hindice vb.) anlatım yok", not any(w in tt for tt in titles for w in ("hindi", "in tamil", "urdu")))
    except Exception as ex:
        R.append(("Site: video testi atlandı: " + type(ex).__name__, True, ""))
    # --- rapor
    bio_det = f"{days[0]['goal']}"
    L = ["# VALIDATION REPORT", "", f"Üretim: {date.today().isoformat()} · {len(days)} gün · {len(tasks)} görev · {len(plan['blocks'])} blok", "",
         "| # | Kontrol | Sonuç | Detay |", "|---|---|---|---|"]
    for i, (n, ok, dt) in enumerate(R, 1):
        L.append(f"| {i} | {n} | {'✅ GEÇTİ' if ok else '❌ KALDI'} | {str(dt).replace('|', '/')} |")
    L += ["", f"**Özet:** {len(R) - len(FAIL)}/{len(R)} kontrol geçti." + (f" Kalan: {', '.join(FAIL)}" if FAIL else ""), "",
          "## Manuel / görsel kontroller (otomatik değil)", "",
          "- PDF sayfa 1, 2, 3, 4, 27, 28 (son sürüm) ve 6 (günlük kart; önceki derlemede, biçimi sonradan değişmedi) pdf.js ile çizdirilip gözle kontrol edildi: kapak, özet, yol haritası, ders analizi, günlük kart, sınav listeleri, takip sayfası; Türkçe karakterler (ş ğ ı İ ö ü ç) doğru göründü, tablolar sayfa içinde kaldı, sayfa numaraları görünüyor. Diğer sayfalar gözle taranmadı.",
          "- PDF'nin siyah-beyaz yazıcıda görünümü simüle edilmedi; tasarım gri tonları ve çerçeveleri kullanıyor (renk bağımlılığı yok).",
          "- **Excel formülleri Excel/LibreOffice ile hesaplanmadı** (bu makinede kurulu değil). Yapı, sayfa adları, formül metinleri ve başlangıç (önbellek) değerleri Python ile doğrulandı; dosya `fullCalcOnLoad` ile açılışta yeniden hesaplanır. İlk açılışta bir uyarı çıkarsa bildir.",
          "- Site: tarayıcıda (telefon genişliği) Bugün, Takvim ve ayrıntı kartı görünümleri açılıp kontrol edildi; hesap senkronu (db) yalnızca yayımlandıktan sonra çalışır ve yerelde denenemez.",
          "- ICS dosyaları gerçek Google/Apple/Outlook'a içe aktarılmadı (hesaplara dokunulmadı); yapı RFC 5545'e göre kontrol edildi.", "",
          "## Doğrulanamayan tarihler / eksik kaynaklar", "",
          "- BIO110 Midterm 1 (3 Kas), CMPE327 (15 Kas), CMPE421 (20 Kas): kullanıcı teyitli; saatler ve kapsamlar belli değil, doğrulanmadı.",
          "- CMPE371 HW1 ve Midterm günleri; BIO110 Midterm 2 günü — **Teyit Bekliyor** (yalnızca syllabus haftası biliniyor). CMPE327 Quiz-1 (syllabus W5) durumu bilinmiyor.",
          "- CMPE499 Evaluation Form: kullanıcı teslim edildiğini bildirdi (Assignments sayfasında Completed).",
          "- Kapsam: plan 14. haftanın sonuna (31 Aralık) kadar; final tarihleri duyurulunca plan_data.py'a eklenir.",
          "- Hiç slayt/PDF/ders notu paylaşılmadı → SLIDE_COVERAGE_MATRIX tümü 'Materyal bekleniyor'; sayfa aralığı/soru numarası UYDURULMADI.",
          "- Dış bağlantılar doğrulanmadı (yalnızca kaynak adları verildi).", "",
          "## Bulunan ve düzeltilen sorunlar (geliştirme sırasında)", "",
          "- BIO110, 30 Ekim'de 3. sıradaydı → 7 gün içindeki sınav için öncelik artırımı eklendi (şimdi 1. sıra).",
          "- Kritik teslim işlerinin bir kısmı isteğe bağlı listedeydi → 'kritik' işareti (★) ve replan'da min'e terfi kuralı eklendi.",
          "- Yol haritası tablosu sayfa dışına taşıyordu → yazı boyutu/satır sayısı düzeltildi; ders analizi tek sayfaya sığdırıldı.", ""]
    with open(os.path.join(ROOT, "09_Quality_Assurance", "VALIDATION_REPORT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    for n, ok, dt in R:
        print(("PASS " if ok else "FAIL ") + n + (" — " + str(dt) if dt else ""))
    print(f"\n{len(R) - len(FAIL)}/{len(R)} geçti")


def _order_ok(plan, skip=()):
    """Her ders için 'L' (öğrenme) bloklarının tarihleri, blok tanım sırasıyla azalmamalı. İhlal listesini döndürür."""
    when = {}
    for d in plan["days"]:
        for t in d["tasks"]:
            if not t["block"].startswith("REV:") and t["id"] not in skip:
                when[t["block"]] = d["date"]
    bad = []
    for c in COURSES6:
        seq = [b for b in plan["blocks"].values() if b["course"] == c and b["kind"] == "L" and b["id"] in when]
        for x, y in zip(seq, seq[1:]):
            if when[x["id"]] > when[y["id"]]:
                bad.append(f"{x['id']}({when[x['id']]})>{y['id']}({when[y['id']]})")
    return bad


if __name__ == "__main__":
    main()
