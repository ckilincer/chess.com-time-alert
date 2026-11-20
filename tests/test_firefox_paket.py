"""
Betik testi (revizyon.bat çalıştırır): Firefox paketini güncel koddan yeniden üretir ve doğrular.
Commit'ten önce koştuğu için güncellenen zip aynı gönderime girer; paket bir daha eskimez.
"""
import json
import pathlib
import sys
import zipfile

KOK = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK))
import firefox_paket  # noqa: E402

surum, dosyalar, degisti = firefox_paket.uret()
with zipfile.ZipFile(firefox_paket.HEDEF) as z:
    adlar = sorted(z.namelist())
    m = json.loads(z.read("manifest.json"))
    ayni = all(z.read(f) == (KOK / f).read_bytes() for f in dosyalar)

hatalar = []
if adlar != dosyalar:
    hatalar.append(f"zip içeriği {adlar} != beklenen {dosyalar}")
if m["version"] != surum:
    hatalar.append(f"zip sürümü {m['version']} != manifest {surum}")
if not ayni:
    hatalar.append("zip'teki dosyalar klasördekilerle aynı değil")
if "gecko" not in m.get("browser_specific_settings", {}):
    hatalar.append("manifest'te browser_specific_settings.gecko yok (Firefox kimliği)")

if hatalar:
    print("KALDI: " + "; ".join(hatalar))
    sys.exit(1)
print(f"ok: firefox paketi v{surum}, {len(dosyalar)} dosya ({'yeniden üretildi' if degisti else 'güncel'})")
