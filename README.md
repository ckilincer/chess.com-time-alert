# Chess.com Time Alert — Chess.com süre uyarısı

Chess.com'da oynarken **sıra sendeyken** süren **1 dakika, 45 ve 30 saniyeye** inince kapı çalar gibi iki vuruş (tak-tak),
20 saniyenin altına inince bip çalan küçük bir tarayıcı eklentisi.
Bip sıfıra yaklaştıkça **tonu yükselir ve hızlanır** (20 sn'de saniyede bir → 0'a yakın saniyede ~9). Hamleni yapınca susar.

*A tiny browser extension that knocks twice when **your** clock on Chess.com hits 1:00, 0:45 and 0:30, and beeps below 20 seconds — the pitch rises and the beeps speed up as time runs out. English below.*

![ikon](icons/icon128.png)

## Kurulum

**Chrome, Edge, Brave, Opera, Vivaldi**

1. Depoyu indir: **Code → Download ZIP**, klasöre çıkar.
2. Tarayıcıda eklenti sayfasını aç (`chrome://extensions`, `edge://extensions` …).
3. **Geliştirici modu**'nu aç → **Paketlenmemiş öğe yükle** → çıkardığın klasörü seç.
4. Açık chess.com sekmesini yenile.

**Firefox (140+)** — `about:debugging#/runtime/this-firefox` → **Load Temporary Add-on** → `manifest.json`.
Geçici yükleme tarayıcı kapanınca silinir; kalıcı kurulum için eklenti addons.mozilla.org'da imzalatılmalıdır.

## Nasıl çalışır

- Alttaki (senin) saatini okur; uyarı yalnız **sıra sendeyken ve saat akarken** çalar.
- Rakibin saati akarken, bitmiş oyunlarda ve analizde ses yok.
- Tarayıcılar sesi sayfada bir tıklamadan sonra açar; ilk taşını oynamak yeterli.
- Ağ isteği yapmaz, veri toplamaz, hiçbir izin istemez; yalnız `https://www.chess.com/*` üzerinde çalışır.

## Ayarlar

`content.js` dosyasının başında:

| Ayar | Varsayılan |
|---|---|
| `ESIK` (uyarı eşiği, sn) | 20 |
| `SES` (0–1) | 0.25 |
| `FREK_BAS` / `FREK_SON` (Hz) | 500 / 1500 |
| `ARALIK_BAS` / `ARALIK_SON` (ms) | 1000 / 110 |
| `TAK_ESIKLER` (tak-tak anları, sn) | 60, 45, 30 |
| `TAK_SES` (0–1) | 0.8 |

Değiştirdikten sonra eklenti sayfasında eklentiyi yenile (↻).

---

## English

**Install (Chromium browsers):** Code → Download ZIP → unzip → open `chrome://extensions` → enable *Developer mode* →
*Load unpacked* → pick the folder → reload chess.com.
**Firefox 140+:** `about:debugging` → *Load Temporary Add-on* → `manifest.json`.

**How it works:** reads the bottom (your) clock; beeps only while it is your turn and the clock is running.
No network requests, no data collection, no permissions. Tweak knock points, threshold, volume, pitch and tempo at the top of `content.js`.

*Not affiliated with or endorsed by Chess.com.*

## Lisans / License

MIT — bkz. [LICENSE](LICENSE).
