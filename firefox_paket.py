"""
Firefox paketi: manifest.json'un kullandığı dosyalardan firefox/sure-uyarisi-firefox.zip üretir.

    python firefox_paket.py

Paket deterministiktir (sabit tarih, sıralı dosyalar): kod değişmediyse zip bayt bayt aynı çıkar,
git'te gereksiz değişiklik görünmez. revizyon.bat bunu tests/test_firefox_paket.py üzerinden
her gönderimde çalıştırır, yani paket elle güncellenmez.
"""
import io
import json
import pathlib
import zipfile

KOK = pathlib.Path(__file__).resolve().parent
HEDEF = KOK / "firefox" / "sure-uyarisi-firefox.zip"
SABIT_TARIH = (1980, 1, 1, 0, 0, 0)


def paket_dosyalari():
    """manifest.json'un başvurduğu dosyalar (+ manifest'in kendisi)."""
    m = json.loads((KOK / "manifest.json").read_text(encoding="utf-8"))
    dosyalar = {"manifest.json"}
    for cs in m.get("content_scripts", []):
        dosyalar.update(cs.get("js", []))
        dosyalar.update(cs.get("css", []))
    dosyalar.update(m.get("icons", {}).values())
    dosyalar.update(m.get("action", {}).get("default_icon", {}).values())
    for bg in ("service_worker", "scripts"):
        v = m.get("background", {}).get(bg)
        if v:
            dosyalar.update([v] if isinstance(v, str) else v)
    eksik = [f for f in dosyalar if not (KOK / f).is_file()]
    if eksik:
        raise SystemExit(f"manifest'te geçen dosya yok: {eksik}")
    return sorted(dosyalar), m["version"]


def paket_bayt():
    dosyalar, surum = paket_dosyalari()
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for f in dosyalar:
            zi = zipfile.ZipInfo(f, SABIT_TARIH)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, (KOK / f).read_bytes())
    return buf.getvalue(), surum, dosyalar


def uret():
    veri, surum, dosyalar = paket_bayt()
    HEDEF.parent.mkdir(exist_ok=True)
    eski = HEDEF.read_bytes() if HEDEF.exists() else None
    if eski != veri:
        HEDEF.write_bytes(veri)
    return surum, dosyalar, eski != veri


if __name__ == "__main__":
    surum, dosyalar, degisti = uret()
    print(f"firefox paketi v{surum}: {len(dosyalar)} dosya, {'güncellendi' if degisti else 'zaten güncel'} -> {HEDEF.relative_to(KOK)}")
