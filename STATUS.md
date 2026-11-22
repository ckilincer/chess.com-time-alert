# Chess.com Time Alert — durum

**Son güncelleme:** 2026-11-22 · v1.8 (v1.7 GitHub'da `0e5c126`)

## Son oturumlar
- 2026-11-22: CLAUDE.md (bulut oturumu kuralları, D147 uyarısı kapandı) eklendi; panelde PUBLIC depo rozeti görünüyor. Gönderildi (YEŞİL).
- 2026-11-20 (4): Firefox paketi depoya alındı: `firefox/sure-uyarisi-firefox.zip` (v1.8, 7 dosya). `firefox_paket.py` manifest'in başvurduğu dosyalardan deterministik zip üretir (sabit tarih → kod aynıysa bayt bayt aynı, ölçüldü). `tests/test_firefox_paket.py` (betik testi) revizyon'da commit'ten önce paketi yeniden üretip sürüm/içeriği doğrular. Eski kök zip (`Chess\sure-uyarisi-firefox.zip`, v1.2, git dışı) kaldırılıyor. Paket Firefox'ta denenmedi.
- 2026-11-20 (3): v1.8 — `reklam.css` (content_scripts css): sağ sütun reklamı `#board-layout-ad` (/play ve oyun sayfasında ölçüldü), gizleyince düzen bozulmuyor (ekran görüntüsüyle bakıldı). chess.com sınıf adlarını değiştirirse reklam geri gelir.
- 2026-11-20 (2): Kullanıcı tak-tak'ı duymadı (bip duyuldu). Ölçüm: teşhis göstergesi `<html data-ck-sure>` (v1.4) — tak sayacı artıyordu, ses "running"; neden: 75–190 Hz vuruş dizüstü/monitör hoparlöründe çalınmıyor. v1.5 tiz (duyuldu, "daha tok olsun"), v1.6 tok 170–430 Hz ("pes"), v1.7: 330/620/1150 Hz rezonans + 2.5 kHz darbe — kullanıcı "tamam". Ses denemesi kullanıcının Chrome'unda sahte saatle (chess.com oyun sayfası, saat metni JS ile azaltılır; başta metin '--' yapılırsa eşik atlaması tak çalmaz).
- 2026-11-20: v1.3 — 60/45/30 sn eşik geçişinde tak-tak (iki vuruş: alçalan sine + boğuk gürültü). Eşik geçişi yalnız saat akarken;
  1:00 ile başlayan oyunda 60'ta çalmaz (geçiş yok). Sahte saatle 5 senaryo denendi (1:30, 1:00, rakip→ben, bitmiş oyun, sıra rakipte).
- 2026-11-19: Eklenti yazıldı (MV3, Chromium + Firefox 140+): alttaki saat `.clock-component.clock-bottom`, sıra `clock-player-turn`
  (chess.com oyun sayfasında ölçüldü); bip yalnız sıra sendeyken VE süre son 1.3 sn'de azaldıysa (bitmiş oyunda sınıf kalıyor).
  Yeşil-siyah kronometre + piyon ikonu. Firefox imza paketi `D:\REPOS\Chess\sure-uyarisi-firefox.zip` (kullanıcı Firefox kullanmıyor, imzalatılmadı).
  GitHub'da public yayın: `ckilincer/chess.com-time-alert`.

## Sırada
- Gerçek bir canlı oyunda tak-tak ve bip'in duyulduğunu kullanıcıdan teyit et (sahte saatle ikisi de duyuldu).

## Bilmeden dokunma
- Firefox paketi elle güncellenmez: `tests/test_firefox_paket.py` her revizyonda üretir. Testi silmek ya da `test: py_compile` kaydı paketi yeniden eskitir. Yeni dosya eklenirse manifest'te geçmesi yeter (paket listeyi manifest'ten okur).
- Ses frekansı ~300 Hz'in altına inmez: dizüstü/monitör hoparlörü çalmaz, uyarı sessizce kaybolur (v1.3 dersi).
- Eklenti yenilenince açık chess.com sekmesi de yenilenmeli; teşhis: konsolda `document.documentElement.dataset.ckSure`.
- Bitmiş oyunda `clock-player-turn` sınıfı kalıyor: "akıyor" kontrolü (son 1.3 sn'de azalma) kaldırılırsa eski oyunlara bakarken ses çalar.
- Depo PUBLIC: chess.com logosu, sır, kişisel veri girmez. Aktarılan görsel/SVG'de C2PA üst verisi olabilir (D166).
