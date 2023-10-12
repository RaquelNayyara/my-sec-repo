--- TUGAS 5 ---

1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

- Selektor ID -> Selektor ini berfungsi untuk memilih elemen HTML berdasarkan atribut ID. Atribut ID harus bersifat unik, dan selektor ini berguna saat kita ingin menerapkan style pada elemen tertentu.
- Element Style -> Element ini berisi informasi gaya untuk dokumen atau bagian dari dokumen. Bisa dibuat dalam file yang berbeda yaitu CSS, yang nantinya file css akan dipanggil untuk menerapkan elemen dalam HTML.
- Selector Class -> Selector ini berfungsi untuk memilih elemen HTML berdasarkan atribut kelas.
- Selector Universal -> Selector ini berfungsi untuk memilih semua elemen pada HTML. Syntax yang digunakan yaitu "*". Selector ini dapat berguna ketika kita ingin menerapkan style yang sama pada seluruh elemen.

2.  Jelaskan HTML5 Tag yang kamu ketahui.

<html>: Menandai awal dan akhir dari dokumen HTML. Semua elemen HTML berada di dalam tag ini.
<head>: Berisi informasi tentang dokumen seperti judul, tautan ke stylesheet (CSS), dan meta-informasi lainnya.
<meta>: Memberikan meta-informasi tentang dokumen, seperti karakter set yang digunakan atau instruksi untuk mengambil meta-data dari server.
<style>: Dalam konteks <head>, ini adalah tempat untuk menempatkan CSS internal. Jika digunakan dalam elemen lain, itu bisa berarti teks atau skrip.
<body>: Ini berisi semua konten yang akan ditampilkan di halaman web, seperti teks, gambar, tautan, dan elemen lainnya.

3. Jelaskan perbedaan antara margin dan padding.

Margin:
- Margin adalah ruang di luar batas luar elemen.
- Margin tidak berpengaruh pada tata letak elemen tetangga lainnya. Dengan kata lain, itu adalah jarak antara elemen saat ini dengan elemen-elemen di sekitarnya.
- Margin akan membuat elemen terlihat lebih jauh dari elemen lain.

Padding:
- Padding adalah ruang di antara batas dalam elemen dan kontennya sendiri.
- Padding mempengaruhi tata letak elemen dalam dirinya sendiri, karena ia menentukan seberapa jauh konten dari batas elemen tersebut.
- Padding mempengaruhi elemen di dalamnya, tetapi tidak mempengaruhi elemen di luar elemen tersebut.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Tailwind CSS dan Bootstrap merupakan dua framework CSS yang populer yang digunakan untuk mempercepat proses pengembangan tampilan web. Kedua framework ini memiliki perbedaan mendasar. Tailwind CSS menekankan pada penggunaan utilitas dan memberikan fleksibilitas dalam desain kustom dengan memanfaatkan kelas-kelas yang telah ditentukan sebelumnya. Sementara itu, Bootstrap lebih fokus pada komponen-komponen yang siap digunakan dan responsif terhadap berbagai ukuran layar. Bootstrap juga menyediakan tema dan template yang mudah diadopsi.

Kapan sebaiknya menggunakan Tailwind CSS?
Ketika desain membutuhkan tingkat kustomisasi yang tinggi dan fleksibilitas yang besar.
Saat ingin menghasilkan kode HTML yang bersih tanpa penambahan kelas yang tidak diperlukan.

Sementara, kapan sebaiknya menggunakan Bootstrap?
Ketika tujuannya adalah membuat tampilan yang mudah digunakan dan cepat.
Bootstrap sangat cocok untuk situs web sederhana yang bersifat umum dan simpel.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Dalam mengkustomisasi, saya hanya menambahkan konten dan formulir pada struktur html yang sudah ada, yaitu yang ada pada file main, create product, edit product, login, dan register. Saya menambahkan style langsung ke dalam elemen html menggunakan atribut style. Semua properti CSS diterapkan di dalam atribut style di dalam tag HTML. Untuk designnya, saya hanya menghias dengan warna kesukaan, memberi table pada main html, menyesuaikan padding/panjang dan lebar background. Setelah itu saya selalu pastikan dan memeriksa hasilnya di browser setelah menyimpan file HTML. Saya juga menambahkan navbar pada main html, seperti yang ada pada tutorial 4. 