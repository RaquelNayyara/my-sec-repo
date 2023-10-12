TUGAS 6

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Dalam synchronous programming, tugas-tugas dieksekusi secara berurutan, satu per satu. Artinya, program menunggu tugas saat ini selesai sebelum melanjutkan ke tugas berikutnya. Ini mirip dengan antrian di toko atau bank, di mana setiap orang harus menunggu giliran mereka selesai sebelum orang berikutnya dapat dilayani.

Dalam asynchronous programming, program tidak menunggu operasi untuk selesai. Sebaliknya, program melanjutkan eksekusi dan dapat memeriksa hasil operasi tersebut nanti. Ini memungkinkan program untuk melakukan banyak operasi secara bersamaan tanpa harus menunggu yang satu selesai sebelum yang lain dimulai.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma Event-Driven Programming adalah pendekatan dalam pemrograman di mana alur eksekusi program ditentukan oleh kejadian atau peristiwa yang terjadi, bukan hanya urutan instruksi dalam kode program. Dalam konteks JavaScript dan penggunaan AJAX (Asynchronous JavaScript and XML) di aplikasi web, paradigma ini sangat relevan.

3. Jelaskan penerapan asynchronous programming pada AJAX.

Asynchronous JavaScript and XML (AJAX) adalah teknik dalam pengembangan web yang memungkinkan pertukaran data antara browser dan server secara asinkron tanpa memuat ulang halaman secara keseluruhan. Asynchronous programming adalah kunci dari AJAX, karena memungkinkan aplikasi untuk tetap responsif sambil menunggu respons dari server.
- Membuat Objek XMLHttpRequest:
- Mengatur Fungsi Penangan Kejadian (Event Handler)
- Membuka Koneksi (open())
- Mengirim Request (send())
- Menangani Respons dari Server
- Menangani Kesalahan (Optional)

4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).