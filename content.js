// Chess.com Süre Uyarısı — alttaki (senin) saatin akarken ESIK saniyenin altına inince bip.
(() => {
  'use strict';

  // ---- Ayarlar ----
  const ESIK = 20;          // uyarı başlangıcı (saniye)
  const SES = 0.25;         // ses düzeyi 0..1
  const FREK_BAS = 500;     // 20 sn'de ton (Hz)
  const FREK_SON = 1500;    // 0 sn'de ton (Hz)
  const ARALIK_BAS = 1000;  // 20 sn'de bip aralığı (ms)
  const ARALIK_SON = 110;   // 0 sn'de bip aralığı (ms)

  let ctx = null;
  function sesBaglami() {
    if (!ctx) { try { ctx = new AudioContext(); } catch (e) { return null; } }
    if (ctx.state === 'suspended') ctx.resume().catch(() => {});
    return ctx;
  }
  // Tarayıcı sesi ancak sayfada bir tıklama/tuştan sonra açar; taş oynatmak yeterli.
  ['pointerdown', 'keydown'].forEach(t =>
    addEventListener(t, sesBaglami, { capture: true, passive: true }));

  function bip(frek, sure) {
    const c = sesBaglami();
    if (!c || c.state !== 'running') return;
    const t = c.currentTime;
    const osc = c.createOscillator();
    const g = c.createGain();
    osc.type = 'square';
    osc.frequency.value = frek;
    g.gain.setValueAtTime(0, t);
    g.gain.linearRampToValueAtTime(SES, t + 0.005);
    g.gain.setValueAtTime(SES, t + sure - 0.01);
    g.gain.linearRampToValueAtTime(0, t + sure);
    osc.connect(g).connect(c.destination);
    osc.start(t);
    osc.stop(t + sure + 0.02);
  }

  function saniye(el) {
    const m = el.textContent.match(/(?:(\d+):)?(\d+):(\d{2})(?:\.(\d))?/);
    if (!m) return null;
    return (+(m[1] || 0)) * 3600 + (+m[2]) * 60 + (+m[3]) + (m[4] ? +m[4] / 10 : 0);
  }

  let onceki = null;
  let sonAzalma = 0;

  // Saat akıyor mu: sıra sende (clock-player-turn) VE süre son 1.3 sn içinde azaldı.
  // (Bitmiş oyunda sınıf kalıyor ama süre azalmıyor → bip yok.)
  function durum() {
    const el = document.querySelector('.clock-component.clock-bottom') ||
               document.querySelector('[class*="clock-bottom"]');
    if (!el) { onceki = null; return null; }
    const s = saniye(el);
    if (s === null) return null;
    const simdi = performance.now();
    if (onceki !== null && s < onceki) sonAzalma = simdi;
    onceki = s;
    const sira = el.classList.contains('clock-player-turn');
    return { s, akiyor: sira && (simdi - sonAzalma < 1300) };
  }

  function dongu() {
    const d = durum();
    if (d && d.akiyor && d.s > 0 && d.s <= ESIK) {
      const oran = d.s / ESIK; // 1 → 0
      const frek = FREK_SON + (FREK_BAS - FREK_SON) * oran;
      const aralik = ARALIK_SON + (ARALIK_BAS - ARALIK_SON) * oran;
      bip(frek, Math.min(0.09, aralik * 0.45 / 1000));
      setTimeout(dongu, aralik);
    } else {
      setTimeout(dongu, 150);
    }
  }
  dongu();
})();
