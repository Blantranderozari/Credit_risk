Submission Proyek Akhir MLOps: Pengembangan dan Pengoperasian Sistem Machine Learning
***

|                         | Deskripsi |
| ----------------------- | --------- |
| Dataset                 |     [Credit Risk](https://www.kaggle.com/datasets/laotse/credit-risk-dataset) |
| Masalah                 |       Bagaimana Bank bisa mengurangi kredit bermasalah  |
| Solusi machine learning |       Mendeteksi nasabah yang berpotensi kredit macet   |
| Metode pengolahan       |      Data awal dalam format CSV akan menjadi masukan untuk end-to-end machine learning pipeline(*Tensorflow Extended*). Fitur numerik dipetakan ke interval \[0,1\] sementara fitur kategorikal dipetakan menjadi bilangan bulat positif yang sesuai dengan nilai unik fitur tersebut. Keluarannya dalam bentuk bilangan biner 0 (tidak berpotensi) atau 1 (berpotensi kredit bermasalah). Untuk Pipeline Orchestrator digunakan Apache Beam      |
| Arsitektur Model        |  Sequentials ANN: Multi layer Perceptron. |
| Metrik evaluasi         |    Memaksimalkan nilai akurasi dataset evaluasi  (val_binary_accuracy)      |
| Performa model          |       val_binary_accuracy = 0.83    |
| Opsi deployment         |   Menggunakan Server-side deployment. Tipe model serving yang digunakan adalah container Docker|
| Web app                 |  Docker image yang menyimpan serving_model hasil traning kemudian diunggah ke platform Heroku yang bisa diakses via [https://model-resiko-kredit.herokuapp.com/](https://model-resiko-kredit.herokuapp.com/)     |
| Monitoring              |       Monitoring akan dilakukan di komputer lokal dengan menggunakan Prometheus dengan Grafana sebagai dashboard monitoring menggunakan container |


**Catatan**:

Beberapa saran yang diimplementasikan dalam proyek ini adalah:

1. Menerapkan prinsip clean code dalam membuat machine learning pipeline.  

2. Menyinkronkan Prometheus dengan Grafana untuk membuat dashboard monitoring yang lebih menarik. Untuk itu gunakan file docker-compose.yml, bukan Dockerfile





