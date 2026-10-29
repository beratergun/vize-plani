# COURSE ANALYSIS

## Öncelik modeli

Puan = aciliyet %35 + zorluk %25 + not ağırlığı %20 + önkoşul bağımlılığı %10 + birikmiş eksik %10 (başlangıçta 0). Sınavına ≤3 gün kalan ders puandan bağımsız 1. sıradadır; ≤7 gün kalan ders kalan arasında öne çıkar. Oranlar gerekçeli başlangıç değerleridir; birikmiş eksik arttıkça (Postponed/yanlış) o dersin payı büyür. Yakın bir sınav için çalışırken zor dersler tamamen bırakılmaz (her gün ≥1 min görev).

| Ders | Zorluk | Önkoşul bağı | Not |
|---|---|---|---|
| BIO110 | 3/5 | 0.3 | Introduction to Modern Biology |
| CMPE371 | 5/5 | 1.0 | Signals and Systems |
| CMPE327 | 4/5 | 0.8 | Automata / Theory of Computation |
| CMPE421 | 4/5 | 0.5 | Artificial Intelligence |
| CMPE453 | 4/5 | 0.6 | Microprocessors (ATmega328P / STM32) |
| CMPE499 | 2/5 | 0.0 | Summer Training (rapor + video) |

## BIO110 — Introduction to Modern Biology

- **Değerlendirme:** Midterm 1 %25 · Midterm 2 %25 · Proje sunumu %20 · Final %30 (+5 puan: ≥%70 devam — otomatik varsayılmadı)
- **Tarihler:** Midterm 1: 3 Kas (kullanıcı teyitli) · Midterm 2: 26/27 Kas (gün teyit bekliyor) · Proje: 10–31 Ara (15–20 slayt, bireysel) · Final: duyurulacak
- **Önkoşullar:** Yok; ama kimya/hücre temelini sıfırdan kur (B01–B03 önce).
- **Çalışma yaklaşımı:** Kavram → şema → karşılaştırma tablosu → aktif hatırlama (flashcard) → konu testi
- **Riskler:** Konu hacmi büyük (9 konu / 5 gün); ezber yığılması. Çözüm: şema+flashcard+gün sonu test.
- **Syllabus akışı:** W1 First Meeting · 8/9 Eki: Chemical Context of Life, Water and Life, Carbon · 15/16 Eki: Large Biological Molecules, Tour of the Cell, Membrane · 22/23 Eki: Metabolism, Cellular Respiration, Photosynthesis · Midterm 1 (3 Kas — kullanıcı tarihi) · 12/13 Kas: Cell Cycle, Mendel, Chromosomal Basis, Molecular Basis of Inheritance · 19/20 Kas: Gene Expression, Regulation, DNA Tools · 26/27 Kas: Midterm 2 · 3/4 Ara: Descent with Modification, Evolution of Populations · 10/11 Ara–31 Ara: Project Presentations

## CMPE371 — Signals and Systems

- **Değerlendirme:** Midterm %30 · Final %40 · Quiz %15 · Homework %15
- **Tarihler:** HW1: 2–6 Kas haftası (teyit) · Midterm: 23–27 Kas (teyit) · Quiz 1: 7–11 Ara (teyit) · Final: duyurulacak
- **Önkoşullar:** Karmaşık sayılar/Euler, trigonometri, üstel, türev-integral (30–31 Eki).
- **Çalışma yaklaşımı:** Önkoşul → çözümlü örnek → kolaydan zora problem (çözüme bakmadan) → yanlış analizi
- **Riskler:** En zor ders; bilgi birikimli. Yalnız izleyerek öğrenilmez → her blokta problem çöz.
- **Syllabus akışı:** W1 Intro · W2 Sinusoids · W3 Special Signals, System Properties · W4–5 LTI Systems · W6 Differential/Difference Equations (HW1) · W7 CTFS · W8 CTFT · W9 Midterm (23–27 Kas) · W10 DTFS · W11 DTFT (Quiz 1) · W12 Filtering · W13 Sampling · W14 Z-Transform · Final haftası (tarih duyurulacak)

## CMPE327 — Automata / Theory of Computation

- **Değerlendirme:** Quiz-1/2, Midterm, Final (ağırlıklar syllabus'ta görünmüyor)
- **Tarihler:** Midterm: 15 Kas (kullanıcı teyitli; saat belli değil) · Quiz-1: syllabus W5 (durum doğrula) · Quiz-2: 14–18 Ara (teyit) · Final: duyurulacak
- **Önkoşullar:** Küme, ilişki, fonksiyon, tümevarım/çelişki ile ispat (A1).
- **Çalışma yaklaşımı:** Otomat çizme → örnek/karşı örnek üretme → dönüşüm algoritmaları → kısa ispat yazma
- **Riskler:** İspat ve dönüşüm algoritmalarında hata birikir; DFA/NFA'yı el ile çok çiz.
- **Syllabus akışı:** W1 History/Central Concepts · W2 Math Prelim, DFA · W3 NFA, Closure · W4 DFA≡NFA · W5 Regular Languages, Pattern Matching, Regex, DFA Minimization (Quiz-1) · W6 Minimization, Myhill–Nerode, Derivatives · W7 Myhill–Nerode, Derivatives, Equivalence of REs · W8 DFA Equivalence, CFG, Ambiguity · Midterm (15 Kas — kullanıcı tarihi) · W9–10 CNF, CYK, Pumping Lemma, Non-regularity · W11–12 PDA, Ogden (Quiz-2) · W13–14 Turing Machines, Decision Problems · Final

## CMPE421 — Artificial Intelligence

- **Değerlendirme:** Homework %30 · Midterm %30 · Final %40 · Katılım bonus
- **Tarihler:** Midterm: 20 Kasım (kullanıcı teyitli; saat belli değil) · Homework tarihleri syllabus'ta yok · Final: duyurulacak
- **Önkoşullar:** Temel olasılık, grafik/ağaç gösterimi, temel Python (opsiyonel).
- **Çalışma yaklaşımı:** Algoritmayı elle yürüt (arama ağacı, tablo) → karşılaştır → küçük Python deneyi (opsiyonel)
- **Riskler:** Midterm kapsamı belirsiz; arama algoritmalarını elle yürüt, karşılaştırma tablosu çıkar.
- **Syllabus akışı:** W1 Intro · W2 Agents/Problem Solving · W3 Uninformed Search · W4 Informed Search · W5 Game Playing · W6 CSP/Adversarial · W7 Planning · W8 KR + Theorem Proving · W9 Uncertainty · Midterm (20 Kas — kullanıcı tarihi) · W10 ML Fundamentals + Classification/Regression · W11 NN/Deep Learning · W12 NLP/LLMs · W13 RL · W14 Ethics/XAI/Responsible AI + Review · Final

## CMPE453 — Microprocessors (ATmega328P / STM32)

- **Değerlendirme:** Midterm 12 Kas 18:00–20:00 (kesin) · diğer ağırlıklar syllabus'ta yok
- **Tarihler:** Midterm: 12 Kasım 2026 18:00–20:00 · Lab 1–6 (donanım varsayılmadı) · Final: duyurulacak
- **Önkoşullar:** İkilik/onaltılık, bit işlemleri, temel C.
- **Çalışma yaklaşımı:** Register haritası → bit işlemleri → kod okuma/yazma (kağıt üstünde) → davranış yorumlama
- **Riskler:** Donanım yok → kağıt üstünde register/kod izleme; kapsam doğrulanmalı.
- **Syllabus akışı:** W1 Overview + ATmega328P · W2 Programming AVR · W3 AVR I/O (Lab1) · W4 Digital Input (Lab2) · W5 USART · W6 SPI, I2C (Lab3) · W7 ADC · Midterm 12 Kas 18:00–20:00 · W8 Interrupts · W9 Timers (Lab4) · W10 PWM · W11 ARM Cortex/STM32 Discovery · W12 GPIO + LED (Lab5) · W13 PWM for ARM (Lab6) · Final

## CMPE499 — Summer Training (rapor + video)

- **Değerlendirme:** Rapor %70 · Sunum %30
- **Tarihler:** STR: 22 Kas (Pazar) · Video: 29 Kas (Pazar) · Evaluation Form: 7 Eki (teslim edildi)
- **Önkoşullar:** Bölüm rapor yönergesi/şablonu (materyal bekleniyor).
- **Çalışma yaklaşımı:** Taslak → revizyon → format/kaynakça kontrolü → erken teslim
- **Riskler:** Son güne bırakma riski. Plan: STR 20 Kas, video 25 Kas yükleme; iç kontrol 19 Kas.
- **Syllabus akışı:** Report %70 · Presentation %30 · Evaluation Form 7 Eki (teslim edildi) · STR 22 Kas · Video 29 Kas

## Örtük tarih/kapsam kararları

- BIO110 Midterm 1 kapsamı **B01–B09** (syllabus 5/6 Kas satırına kadar olan konular) varsayıldı; 30 Ekim'de doğrulanır.
- CMPE453 Midterm kapsamı W1–W7 (ADC dahil) varsayıldı; Interrupts (W8) sonrası.
- CMPE327 (15 Kas) / CMPE421 (20 Kas) vize kapsamları W1–W8 / W1–W9 varsayıldı; tarih netleşince daraltılır.
- CMPE371 Midterm W1–W8 (CTFT dahil) varsayıldı.
