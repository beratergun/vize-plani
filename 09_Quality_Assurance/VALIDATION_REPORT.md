# VALIDATION REPORT

Üretim: 2026-10-29 · 63 gün · 434 görev · 191 blok

| # | Kontrol | Sonuç | Detay |
|---|---|---|---|
| 1 | Altı dersin tamamı planda | ✅ GEÇTİ | BIO110:92, CMPE371:85, CMPE327:91, CMPE421:77, CMPE453:68, CMPE499:18 |
| 2 | 30 Ekim–31 Aralık (14. hafta sonu) her takvim günü mevcut | ✅ GEÇTİ | 63 gün |
| 3 | Görev ID'leri benzersiz | ✅ GEÇTİ | 434 görev |
| 4 | Her blok tam bir kez programlı | ✅ GEÇTİ | 191 blok |
| 5 | Syllabus'taki tüm konular (finale kadar) plan dışı kalmadı | ✅ GEÇTİ | 86 konu anahtarı; eksik: yok |
| 6 | Hiçbir gün aşırı yüklü değil (min ≤ 4,4 sa hafta içi / ext ≤ 6,7 sa) | ✅ GEÇTİ | tamam |
| 7 | Pazarlar hafta içinden yüksek kapasiteyle (≥6 sa genişletilmiş) planlı — ilk 4 hafta | ✅ GEÇTİ | 2026-11-01:8,3 sa; 2026-11-08:7,9 sa; 2026-11-15:7,7 sa; 2026-11-22:4,6 sa; 2026-11-29:5,5 sa; 2026-12-06:5,5 sa; 2026-12-13:3,1 sa; 2026-12-20:5,7 sa; 2026-12-27:3,1 sa |
| 8 | Bilgi: hafif günler (sınav öncesi/sonrası ya da boş): 2026-11-26(75), 2026-12-12(76), 2026-12-16(98), 2026-12-30(90) | ✅ GEÇTİ |  |
| 9 | BIO110, 30 Ekim–3 Kasım arası her gün 1. öncelik | ✅ GEÇTİ | BIO110; BIO110; BIO110; BIO110; BIO110 |
| 10 | Study_Plan_2026.ics: geçerli yapı, UID benzersiz, satır ≤75 oktet | ✅ GEÇTİ | 63 etkinlik |
| 11 | Exams_Deadlines_2026.ics: geçerli yapı, UID benzersiz, satır ≤75 oktet | ✅ GEÇTİ | 16 etkinlik |
| 12 | CMPE453 midterm 12 Kasım 18:00–20:00 (Europe/Istanbul) | ✅ GEÇTİ |  |
| 13 | CMPE499 teslimleri 22 ve 29 Kasım | ✅ GEÇTİ |  |
| 14 | Doğrulanmamış tarihlerin hepsi 'TEYİT BEKLİYOR' + STATUS:TENTATIVE | ✅ GEÇTİ | 6 tarih |
| 15 | Final sınavına UYDURMA tarih yazılmadı | ✅ GEÇTİ |  |
| 16 | Excel: 10 sayfa adı doğru ve XML iyi biçimli | ✅ GEÇTİ | Dashboard, Daily Tasks, Course Progress, Topic Mastery, Exam Countdown, Assignments, Revision Schedule, Mistake Log, Slide Coverage, Weekly Reviews |
| 17 | Excel: Daily Tasks satır sayısı = görev sayısı | ✅ GEÇTİ | 434/434 |
| 18 | Excel: formüllerdeki sayfa referansları mevcut sayfalara işaret ediyor | ✅ GEÇTİ | Course Progress, Daily Tasks, Exam Countdown, Topic Mastery |
| 19 | sync_from_xlsx: değiştirilen durum doğru okunuyor | ✅ GEÇTİ | 2026-10-30-01 → Completed |
| 20 | replan (5 Kas, hiçbir şey yapılmamış varsayımı): kapasite aşılmıyor | ✅ GEÇTİ | 101 taşındı, 6 düşürüldü; aşan: yok |
| 21 | Orijinal planda her dersin öğrenme blokları tanım (önkoşul) sırasında | ✅ GEÇTİ | [] |
| 22 | replan sonrası da ders içi öğrenme sırası korunuyor (Postponed olanlar hariç) | ✅ GEÇTİ | [] |
| 23 | PDF: tüm sayfalar A4 ve sayfa sayısı makul (≤30) | ✅ GEÇTİ | 28 sayfa, MediaBox [(b'594.95996', b'841.91998')], 1046 KB |
| 24 | PDF kaynağı: Türkçe karakterler UTF-8 ve tablo taşması CSS'i | ✅ GEÇTİ |  |
| 25 | Site: veri plan.json ile aynı (gün ve görev sayısı) | ✅ GEÇTİ | 63 gün, 434 görev |
| 26 | Site: her öğrenme görevinin en az bir kaynak bağlantısı var | ✅ GEÇTİ | 83 öğrenme görevi |
| 27 | Site: tüm bağlantılar https | ✅ GEÇTİ | [] |
| 28 | Site: kaynak bağlantılarının hepsi HTTP 200 döndü | ✅ GEÇTİ | 61/61 |
| 29 | Site: önerilen videoların hepsi YouTube'da doğrulandı (oEmbed) | ✅ GEÇTİ | 138/138 video |
| 30 | Site: video başlıklarında dil dışı (Hindice vb.) anlatım yok | ✅ GEÇTİ |  |

**Özet:** 30/30 kontrol geçti.

## Manuel / görsel kontroller (otomatik değil)

- PDF sayfa 1, 2, 3, 4, 27, 28 (son sürüm) ve 6 (günlük kart; önceki derlemede, biçimi sonradan değişmedi) pdf.js ile çizdirilip gözle kontrol edildi: kapak, özet, yol haritası, ders analizi, günlük kart, sınav listeleri, takip sayfası; Türkçe karakterler (ş ğ ı İ ö ü ç) doğru göründü, tablolar sayfa içinde kaldı, sayfa numaraları görünüyor. Diğer sayfalar gözle taranmadı.
- PDF'nin siyah-beyaz yazıcıda görünümü simüle edilmedi; tasarım gri tonları ve çerçeveleri kullanıyor (renk bağımlılığı yok).
- **Excel formülleri Excel/LibreOffice ile hesaplanmadı** (bu makinede kurulu değil). Yapı, sayfa adları, formül metinleri ve başlangıç (önbellek) değerleri Python ile doğrulandı; dosya `fullCalcOnLoad` ile açılışta yeniden hesaplanır. İlk açılışta bir uyarı çıkarsa bildir.
- Site: tarayıcıda (telefon genişliği) Bugün, Takvim ve ayrıntı kartı görünümleri açılıp kontrol edildi; hesap senkronu (db) yalnızca yayımlandıktan sonra çalışır ve yerelde denenemez.
- ICS dosyaları gerçek Google/Apple/Outlook'a içe aktarılmadı (hesaplara dokunulmadı); yapı RFC 5545'e göre kontrol edildi.

## Doğrulanamayan tarihler / eksik kaynaklar

- BIO110 Midterm 1 (3 Kas), CMPE327 (15 Kas), CMPE421 (20 Kas): kullanıcı teyitli; saatler ve kapsamlar belli değil, doğrulanmadı.
- CMPE371 HW1 ve Midterm günleri; BIO110 Midterm 2 günü — **Teyit Bekliyor** (yalnızca syllabus haftası biliniyor). CMPE327 Quiz-1 (syllabus W5) durumu bilinmiyor.
- CMPE499 Evaluation Form: kullanıcı teslim edildiğini bildirdi (Assignments sayfasında Completed).
- Kapsam: plan 14. haftanın sonuna (31 Aralık) kadar; final tarihleri duyurulunca plan_data.py'a eklenir.
- Hiç slayt/PDF/ders notu paylaşılmadı → SLIDE_COVERAGE_MATRIX tümü 'Materyal bekleniyor'; sayfa aralığı/soru numarası UYDURULMADI.
- Dış bağlantılar doğrulanmadı (yalnızca kaynak adları verildi).

## Bulunan ve düzeltilen sorunlar (geliştirme sırasında)

- BIO110, 30 Ekim'de 3. sıradaydı → 7 gün içindeki sınav için öncelik artırımı eklendi (şimdi 1. sıra).
- Kritik teslim işlerinin bir kısmı isteğe bağlı listedeydi → 'kritik' işareti (★) ve replan'da min'e terfi kuralı eklendi.
- Yol haritası tablosu sayfa dışına taşıyordu → yazı boyutu/satır sayısı düzeltildi; ders analizi tek sayfaya sığdırıldı.
