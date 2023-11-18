function BriefConcept()
{
    return(
        <span className="BriefConcept">
            <span className="Header">Konsep Singkat</span>
            <span className="SubHeader">CBIR</span>
            <p className="Text">
                CBIR (<i>Content Based Image Retrieval System</i>) adalah suatu metode pencarian citra atau gambar dengan melakukan perbandingan 
                antara gambar <i>query</i> dengan gambar pada <i>database</i> berdasarkan informasi yang ada pada gambar. Dalam Tugas Besar ini, 
                kami melakukan perbandingan dalam parameter warna dan tekstur gambar. Proses ini dimulai dengan ekstraksi
                fitur-fitur penting dari gambar, seperti warna, tekstur, dan bentuk. Setelah fitur-fitur tersebut
                diekstraksi, mereka diwakili dalam bentuk vektor atau deskripsi numerik yang dapat
                dibandingkan dengan gambar lain. Kemudian, CBIR menggunakan algoritma pencocokan
                untuk membandingkan vektor-fitur dari gambar yang dicari dengan vektor-fitur gambar dalam
                dataset. Hasil dari pencocokan ini digunakan untuk mengurutkan gambar-gambar dalam
                dataset dan menampilkan gambar yang paling mirip dengan gambar yang dicari. Proses CBIR
                membantu pengguna dalam mengakses dan mengeksplorasi koleksi gambar dengan cara yang
                lebih efisien, karena tidak memerlukan pencarian berdasarkan teks atau kata kunci, melainkan
                berdasarkan kesamaan nilai citra visual antara gambar-gambar tersebut.
            </p>
            <span className="SubHeader">1. Colour</span>
            <p className="Text">
                CBIR dengan parameter warna dilakukan dengan mengubah bentuk RGB (<i>Red,Green,Blue</i>) dari sebuah gambar menjadi histogram
                warna, yaitu frekuensi berbagai warna pada ruang tertentu, dengan tujuan melihat distribusi dari warna, sehingga tidak dapat melihat
                objek spesifik atau bahkan posisi warna yang didistribusikan. Histogram warna dapat dihitung dengan menghitung piksel yang menyatakan nilai warna pada setiap
                interval. Fitur warna mencakup histogram warna global dan histogram warna blok.
                Proses ini dilakukan dengan langkah berikut:
                <ol>
                    <li>Normalisasi nilai RGB gambar menjadi [0,1]</li>
                    <li>Mencari Cmax (nilai maksimum RGB ternormalisasi), Cmin (nilai minimum RGB ternormalisasi), dan <i>delta</i> (Selisih dari Cmax dan Cmin)</li>
                    <li>Mencari nilai HSV (<i>Hue,Saturation,Value</i>) dengan rumusnya tersendiri</li>
                    <li>Bandingkan nilai HSV dari gambar yang diberikan dengan <i>dataset</i> yang ada dengan <i>cosine similarity</i></li>
                </ol>
            </p>
            <span className="SubHeader">2. Texture</span>
            <p className="Text">
            CBIR dengan perbandingan tekstur dilakukan menggunakan suatu matriks yang dinamakan <i>co-occurrence matrix</i> untuk dapat diproses dalam skala lebih kecil, lebih mudah,
            dan lebih cepat. Setelah mendapatkan <i>co-occurence matrix</i>, buat <i>symmetric matrix</i> dengan menjumlahkan <i>co-occurence matrix</i> dengan tranpose-nya, yang kemudian diubah
            lagi menjadi <i>matrix normalization</i>. Langkah-langkah yang dilakukan sebagai berikut:
            <ol>
                <li>Konversi warna gambar menjadi <i>grayscale</i> karena tidak penting dalam parameter tekstur</li>
                <li>Kuantifikasikan nilai <i>grayscale</i> karena tingkat kemiripan gambar dapat dinilai dari kekasaran teksturnya yang juga dikompresi untuk mengurangi operasi</li>
                <li>Bentuk <i>co-occurence matrix</i></li>
                <li>Dari <i>co-occurence matrix</i> akan didapatkan 3 nilai (<i>contrast, homogeneity, entropy</i>) yang kemudian dibuat menjadi sebuah vektor untuk menghitung kemiripan</li>
                <li>Bandingkan vektor gambar yang diberikan dengan <i>dataset</i> yang ada menggunakan <i>cosine similarity</i></li>
            </ol>
            </p>
        </span>
    );
}

export default BriefConcept;