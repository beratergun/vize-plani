# -*- coding: utf-8 -*-
"""plan.json + progress.json + resources.py -> 10_Website/index.html (tek dosya, çevrimdışı da açılır).
Aynı dosya claude.ai'da Artifact olarak da yayımlanır (db yeteneği ile telefon-bilgisayar senkronu)."""
import json
import os
from common import *
import resources as R
import questions as Q
import syllabus as SY

VIDEOS = {}
_vp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos.json")
if os.path.exists(_vp):
    VIDEOS = json.load(open(_vp, encoding="utf-8"))
GBAN = ["hindi", "in tamil", "urdu"]   # Türkçe/İngilizce dışı anlatımlar
BANV = {"M3": ["pcf8574"], "A9": ["table filling"]}   # elle ayıklanan alakasız/tekrar videolar
GRADE = {"BIO110": [["Midterm 1", 25], ["Midterm 2", 25], ["Proje sunumu", 20], ["Final", 30]], "CMPE371": [["Midterm", 30], ["Final", 40], ["Quiz", 15], ["Homework", 15]],
         "CMPE421": [["Homework", 30], ["Midterm", 30], ["Final", 40]], "CMPE499": [["Rapor", 70], ["Sunum", 30]], "CMPE327": [], "CMPE453": []}
TEMPLATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site_template.html")
GROUP = {"L": "L", "P": "P", "R": "R", "W": "W", "V": "V", "T": "T"}


def how_for(task, blk):
    k = task["kind"]
    if k == "L":
        key = "L_BIO" if task["course"] == "BIO110" else "L_TECH"
    else:
        key = k
    prac = (blk or {}).get("practice", "")
    return [s.format(practice=prac) for s in R.HOW[key]], R.DONE.get(k, "")


def main():
    plan = load_plan()
    prog = load_progress(plan)
    links_used = {}
    days = []
    for d in plan["days"]:
        tasks = []
        for t in d["tasks"]:
            blk = plan["blocks"].get(t["block"])
            item = dict(id=t["id"], c=t["course"], x=0 if t["tier"] == "core" else 1, m=t["minutes"], p=t["priority"], k=t["kind"],
                        ti=t["title"], cr=1 if t.get("critical") else 0)
            if t["kind"] == "T":
                ids = t["block"].replace("REV:", "").split(",")
                rev = []
                for b in ids:
                    bl = plan["blocks"].get(b)
                    if not bl:
                        continue
                    main_l = R.M.get(b, ([], [], [], ""))[0]
                    for lid in main_l[:1]:
                        links_used[lid] = 1
                    rev.append([bl["title"], main_l[0] if main_l else ""])
                item["rev"] = rev
                item["h"], item["dn"] = R.HOW["T"], R.DONE["T"]
            else:
                item["w"], item["pr"], item["b"] = blk["what"], blk["practice"], t["block"]
                main_l, sup, prac, yt = R.M.get(t["block"], ([], [], [], ""))
                ls = [["Ana kaynak", i] for i in main_l] + [["Destek", i] for i in sup] + [["Uygulama", i] for i in prac]
                seen, out = set(), []
                for r, i in ls:
                    if i not in seen:
                        seen.add(i)
                        out.append([r, i])
                        links_used[i] = 1
                item["l"] = out
                if yt:
                    item["yt"] = yt
                item["h"], item["dn"] = how_for(t, blk)
                if t["block"] in Q.QS:
                    item["qs"] = [[a, b] for a, b in Q.QS[t["block"]]]
                vids = [v for v in VIDEOS.get(t["block"], []) if not any(x in v["t"].lower() for x in BANV.get(t["block"], []) + GBAN)]
                if vids:
                    item["vd"] = [[v["id"], v["t"], v["ch"], v["d"]] for v in vids]
                if t["block"] == "V1":
                    item["v"] = [s.strip() for s in blk["what"].split(";")]
            tasks.append(item)
        days.append(dict(d=d["date"], wd=d["weekday"], g=d["goal"], ph=d["phase"], rk=d["ranking"][:3], cm=d["core_min"], em=d["ext_min"], t=tasks))
    for ids in R.COURSE_HOME.values():
        for i in ids:
            links_used[i] = 1
    evals = [dict(id=e["id"], c=e["course"], t=e["title"], d=e["date"], e=e["end"], tm=e.get("time"), s=e["status"], n=e["note"]) for e in plan["evals"] if e["date"]]
    courses = {c: dict(n=m["name"], s=m["short"], diff=m["diff"], meth=m["method"]) for c, m in plan["courses"].items() if c != "GENEL"}
    data = dict(start=plan["start"], end=plan["end"], courses=courses, evals=evals, weeks=plan["weeks"], phases=plan["phases"], days=days,
                links={k: [R.LINKS[k][0], R.LINKS[k][1], R.LINKS[k][2]] for k in links_used}, home=R.COURSE_HOME, grade=GRADE, lms=R.LMS, syl=SY.as_json(), w0=SY.W0.isoformat(),
                topics=[dict(id=b["id"], c=b["course"], t=b["title"], u=(R.M.get(b["id"], ([], [], [], ""))[0] or [""])[0]) for b in plan["blocks"].values() if b["kind"] == "L"])
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = open(TEMPLATE, encoding="utf-8").read()
    assert "/*__DATA__*/null" in tpl
    out_dir = os.path.join(ROOT, "10_Website")
    os.makedirs(out_dir, exist_ok=True)
    frag = tpl.replace("/*__DATA__*/null", js)
    # Artifact için parça (doctype/html/head/body yok); yerel kullanım için tam belge
    open(os.path.join(out_dir, "artifact_page.html"), "w", encoding="utf-8").write(frag)
    path = os.path.join(out_dir, "index.html")
    open(path, "w", encoding="utf-8").write('<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>' + frag + "</body></html>")
    print(f"Site yazıldı: {os.path.getsize(path) // 1024} KB, {len(days)} gün, {sum(len(x['t']) for x in days)} görev, {len(links_used)} bağlantı")


if __name__ == "__main__":
    main()
