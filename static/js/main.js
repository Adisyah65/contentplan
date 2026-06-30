// ============================================================
//  main.js — JavaScript Utama ContentPlan
//  PT. Daytama Sinergi Wisata
// ============================================================
//  File ini dimuat di SEMUA halaman melalui base.html.
//  Berisi fungsi-fungsi umum yang dipakai di banyak halaman.
// ============================================================


// ── Auto-hilangkan flash message setelah 4 detik ────────────
document.addEventListener('DOMContentLoaded', function () {
  const flashes = document.querySelectorAll('.flash');
  flashes.forEach(function (el) {
    setTimeout(function () {
      el.style.transition = 'opacity 0.4s';
      el.style.opacity    = '0';
      setTimeout(function () { el.remove(); }, 400);
    }, 4000); // 4000ms = 4 detik
  });
});


// ── Konfirmasi sebelum hapus data ───────────────────────────
// Cara pakai di HTML:
// <button onclick="return konfirmasiHapus('Nama Konten')">Hapus</button>
function konfirmasiHapus(namaItem) {
  return confirm('Yakin ingin menghapus "' + namaItem + '"?\nData yang dihapus tidak bisa dikembalikan.');
}
