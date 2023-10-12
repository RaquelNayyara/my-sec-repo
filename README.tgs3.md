--- TUGAS 3 ---

1. Apa perbedaan antara form POST dan form GET dalam Django?

Form POST adalah metode yang digunakan untuk mengirimkan nilai atau data ke server untuk proses lebih lanjut. Data yang dikirimkan tidak terlihat di URL browser. Sebagai contoh, ketika ingin menyimpan atau memperbarui data di server, form POST digunakan. Sebagai ilustrasi, saat mengirimkan informasi dari formulir pendaftaran pengguna atau ketika ingin memperbarui profil pengguna, Anda dapat menggunakan form POST.

Pada kondisi tertentu, seperti "if form.is_valid() and request.method == "POST"", kode ini memeriksa apakah formulir valid dan apakah metode permintaan adalah POST. Jika kondisinya benar, formulir akan disimpan dengan menggunakan "form.save()" dan pengguna akan diarahkan kembali ke halaman utama menggunakan "return HttpResponseRedirect(reverse('main:show_main'))".

Form.is_valid() adalah metode pada objek formulir Django yang memeriksa apakah data yang diterima dari permintaan adalah valid sesuai dengan aturan validasi yang telah didefinisikan di formulir. Sedangkan request.method == "POST" memeriksa apakah metode permintaan adalah POST, memastikan bahwa tindakan ini hanya dilakukan jika permintaan adalah tipe POST. Form.save() akan menyimpan data yang telah dikirim untuk disimpan dalam basis data formulir. Setelah itu, akan ada perintah return yang akan mengarahkan ke URL tertentu.

Sementara itu, Form GET digunakan untuk mengambil data dari server dan menampilkannya dalam URL. Data yang dikirimkan melalui form GET akan terlihat dalam URL, berguna untuk permintaan yang hanya membutuhkan informasi dari server tanpa melakukan perubahan pada data yang ada. Sebagai contoh, saat ingin melakukan pencarian atau penyaringan berdasarkan kriteria tertentu.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

- XML (Extensible Markup Language) adalah bahasa penanda yang diciptakan untuk memungkinkan pengguna mendefinisikan struktur data secara bebas. Dalam XML, tanda penanda seperti <tag> digunakan untuk membedakan elemen dan atribut data dalam dokumen. Data diatur dalam hierarki yang terdiri dari elemen, atribut, dan nilai. XML memisahkan data dari presentasi dan memainkan peran penting dalam pertukaran data antar platform. Fleksibilitasnya dalam menentukan struktur data sesuai dengan kebutuhan aplikasi adalah salah satu keunggulan utama XML.

- JSON (JavaScript Object Notation) merupakan format pertukaran data yang ringan dan mudah dibaca oleh manusia maupun mesin. JSON menggunakan pasangan kunci-nilai untuk mewakili data, dan data diorganisir dalam bentuk objek dan array. Sebagai contoh, representasi JSON bisa berupa { "nama": "John Doe", "umur": 30 }. JSON umum digunakan dalam komunikasi antara server dan klien, terutama dalam pengembangan web dan aplikasi. Keunggulan JSON terletak pada efisiensi dan kemudahan pengolahan struktur data, baik yang sederhana maupun kompleks.

- HTML (HyperText Markup Language) adalah bahasa penanda yang digunakan untuk membuat halaman web. HTML mengandung elemen-elemen yang mendefinisikan struktur dan tampilan konten pada halaman web. Elemen-elemen ini diatur dalam hierarki dan mewakili bagian-bagian seperti teks, gambar, tautan, dan elemen lainnya. HTML juga menggunakan tag untuk mengorganisir konten dan memberikan instruksi kepada browser web tentang cara menampilkan halaman. Browser web menerjemahkan tag HTML untuk menciptakan tampilan visual yang dapat diakses oleh pengguna.

Perbedaan utama antara XML, JSON, dan HTML terletak pada struktur data. XML menggunakan tag, atribut, dan nilai untuk mengorganisir data dengan fleksibilitas definisi struktur. Sementara itu, JSON menggunakan pasangan kunci-nilai, objek, dan array, lebih berfokus pada efisiensi pertukaran data di web. Di sisi lain, HTML berfokus pada presentasi konten dan tampilan di browser web, mengorganisir konten menggunakan elemen dan tag. Tujuan penggunaannya juga berbeda: XML untuk pertukaran data antar platform dan penyimpanan konfigurasi, JSON untuk pertukaran data ringan antar aplikasi dan server, terutama di web, sementara HTML digunakan untuk membuat halaman web dan menampilkan konten di browser. Memahami perbedaan ini memungkinkan pengembang untuk memilih format yang sesuai dengan kebutuhan aplikasi mereka dalam hal pertukaran dan representasi data.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

- Pertukaran data yang efisien
JSON mempercepat proses pertukaran data dengan menyediakan struktur data yang lebih sederhana dan padat. Tujuannya adalah meminimalkan waktu pemrosesan data sehingga server dapat segera menampilkan informasi kepada pengguna.
- Interpretasi data yang lebih intuitif bagi manusia
JSON memudahkan interpretasi data ke dalam bahasa manusia. Meskipun komputer hanya dapat memproses data dalam bentuk kode biner, JSON memfasilitasi penerjemahan data ini ke teks yang dapat dimengerti oleh manusia, mempermudah dalam melakukan perbaikan atau penambahan kode.
- Format yang mudah dipahami dan terstruktur
JSON mengusung format yang lebih terstruktur, memudahkan dalam pencarian dan pengubahan kode. Dengan ini, pengguna hanya perlu memasukkan teks dalam bahasa yang mereka mengerti, mempermudah proses pengembangan.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Langkah pertama adalah membuat base.html sebagai kerangka umum dan menyisipkannya ke dalam templates. Kemudian, menambahkan struktur formulir untuk menerima data produk baru. Dibuat juga fungsi baru di dalam views.py, yaitu create product, yang akan menerima permintaan (request) sebagai parameter dan menghasilkan formulir untuk menambahkan data. Setelah itu, dilakukan penyesuaian pada fungsi "show_main" yang telah ada. Selanjutnya, ditambahkan rute baru untuk mengakses fungsi yang baru dibuat.

Langkah berikutnya adalah membuat file HTML baru yang bertugas menampilkan formulir yang sudah dibuat, serta melakukan penyesuaian pada berkas main.html. Kemudian, diperluas dengan menambahkan fungsi-fungsi yang akan diimplementasikan dalam format XML dan JSON. Dilanjutkan dengan menambahkan rute baru untuk mengakses fungsi-fungsi tersebut. Setelah itu, diperlukan penambahan fungsi-fungsi untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON. Terakhir, jalur-jalur baru ditambahkan pada berkas urls.py sesuai dengan fungsi-fungsi baru yang telah dibuat.


SCREENSHOT POSTMAN
<img src="/tgs3//1.jpg">
<img src="/tgs3//2.jpg">
<img src="/tgs3//3.jpg">
<img src="/tgs3//4.jpg">
<img src="/tgs3//5.jpg">