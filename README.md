Submission Proyek Akhir MLOps: Pengembangan dan Pengoperasian Sistem Machine Learning
***

|                         | Deskripsi |
| ----------------------- | --------- |
| Dataset                 |     [Credit Risk](https://www.kaggle.com/datasets/laotse/credit-risk-dataset) |
| Masalah                 |       Bagaimana ke depan Bank bisa mengurangi kredit bermasalah  |
| Solusi machine learning |       Mendeteksi nasabah yang berpotensi kredit macet   |
| Metode pengolahan       |      Data awal dalam format CSV akan menjadi masukan untuk end-to-end machine learning pipeline(*Tensorflow Extended*). Fitur numerik dipetakan ke interval \[0,1\] sementara fitur kategorikal dipetakan menjadi bilangan bulat positif yang sesuai dengan nilai unik fitur tersebut. Keluarannya dalam bentuk bilangan biner 0 (tidak berpotensi) atau 1 (berpotensi kredit bermasalah). Untuk Pipeline Orchestrator menggunakan Apache Beam      |
| Arsitektur Model        |  Sequentials ANN: Multi layer Perceptron. Digunakan Tuner untuk hyper-parameter tuning     |
| Metrik evaluasi         |    Memaksimalkan nilai akurasi dataset evaluasi        |
| Performa model          |       val_binary_accuracy = 0.83    |
| Opsi deployment         |   Menggunakan Server-side deployment. Tipe model serving yang digunakan adalah dengan container Docker|
| Web app                 |  Docker iamge yang menyimpan serving_model hasil traning kemudian diunggah ke platform Heroku lewat [situs ini]( )yang bisa      |
| Monitoring              |           |






