# Chess.com Time Alert — durum

## Son oturumlar
- 2026-11-20: v1.3 — 60/45/30 sn eşik geçişinde tak-tak (iki vuruş: alçalan sine + boğuk gürültü). Eşik geçişi yalnız saat akarken;
  1:00 ile başlayan oyunda 60'ta çalmaz (geçiş yok). Sahte saatle 5 senaryo denendi (1:30, 1:00, rakip→ben, bitmiş oyun, sıra rakipte).
- 2026-11-19: Eklenti yazıldı (MV3, Chromium + Firefox 140+): alttaki saat `.clock-component.clock-bottom`, sıra `clock-player-turn`
  (chess.com oyun sayfasında ölçüldü); bip yalnız sıra sendeyken VE süre son 1.3 sn'de azaldıysa (bitmiş oyunda sınıf kalıyor).
  Yeşil-siyah kronometre + piyon ikonu. Firefox imza paketi `D:\REPOS\Chess\sure-uyarisi-firefox.zip` (kullanıcı Firefox kullanmıyor, imzalatılmadı).
  GitHub'da public yayın: `ckilincer/chess.com-time-alert`.

## Sırada
- Gerçek bir oyunda 20 sn altına inildiğinde sesin duyulduğunu kullanıcıdan teyit et.
