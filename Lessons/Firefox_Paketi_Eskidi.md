# Firefox Paketi Eskidi

**Özet:** Firefox için elle bir kez üretilen zip (`Chess\sure-uyarisi-firefox.zip`) git dışında kaldı ve eklenti v1.8'e çıkarken v1.2'de takıldı. Kök neden: türetilmiş bir paketin, kaynağı değiştikçe onu yeniden üreten bir mekanizması yoktu.
**Kütüphaneler:** WebExtensions MV3, Firefox `browser_specific_settings.gecko`, zipfile
**Bağlantılar:** —

---

## İçerik

### Belirti
"Her şey canlıda, GitHub'da ve REPOS'ta aynı mı" denetiminde tek uyuşmayan dosya buydu: zip içindeki `manifest.json` sürümü 1.2, klasördeki 1.8. Zip `.gitignore`'daki `*.zip` yüzünden depoya hiç girmemişti; kimse fark etmemişti.

### Kök neden
Paket 2026-11-19'da imza denemesi için elle sıkıştırılmıştı. Sonraki altı sürüm (tak-tak sesi, reklam gizleme, `reklam.css`) yalnız klasörü güncelledi; Chrome klasörü doğrudan okuduğu için eksiklik hiçbir kullanımda görünmedi.

### Nasıl ayırt edilir
```
python -c "import zipfile,json;print(json.loads(zipfile.ZipFile('firefox/sure-uyarisi-firefox.zip').read('manifest.json'))['version'])"
```
çıktısı `manifest.json`'daki `version` ile aynı olmalı. Artık `tests/test_firefox_paket.py` bunu her revizyonda kendisi yapıyor.

### Genel kural
Kaynaktan türetilen dosya (paket, derleme çıktısı) ya hiç saklanmaz ya da her gönderimde otomatik üretilir. revizyon.py `tests/test_*.py` betiklerini commit'ten ÖNCE koştuğu için, üretimi bir betik testine koymak çıktıyı aynı commit'e sokar. Çıktı deterministik olmalı (sabit zip tarihi), yoksa her gönderimde sahte değişiklik görünür.
