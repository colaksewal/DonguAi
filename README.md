# Türkçe Atasözleri ve Deyimleri Benzerlik Sistemi

Bu proje, Flask kullanarak Türkçe atasözleri ve deyimlerinden en benzerlerini bulan bir web uygulaması sunar. Uygulama, BERT tabanlı bir dil modeli kullanarak metin gömme (embedding) ve benzerlikleri hesaplama işlemlerini gerçekleştirir.

## Gereksinimler

Projenin çalışabilmesi için aşağıdaki kütüphallerin kurulu olması gerekmektedir:

- `Flask`
- `pandas`
- `numpy`
- `torch`
- `transformers`
- `scikit-learn`
- `zeyrek`

Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:
## Kurulum ve Çalıştırma
### 1. DONGUAI-JUPYTER Dosyasını Çalıştırma
DONGUAI-JUPYTER dosyasını indirip zipten çıkardıktan sonra Jupyter Notebook'da çalıştırabilirsiniz. Bu adım,
verilerinizi hazırlamanızı ve modelinizi test etmenizi sağlar.

[Drive Linki](https://drive.google.com/file/d/1VZr0ak5jEObaCcsqPnopvuQ4fCVvWM_t/view?usp=drive_link)

## 2. Flask Uygulamasını Çalıştırma
### DONGUAI-FLASK dosyasını indirip zipten çıkardıktan sonra gerekli kütüphaneleri yükleyip Flask uygulamasını başlatabilirsiniz.

[Drive Linki](https://drive.google.com/file/d/1Kx2PUP-uc97t17cZRIkJRA5CeyR6UqN7/view?usp=sharing)

```bash
pip install Flask pandas numpy torch transformers scikit-learn zeyrek
```

Terminali açın ve gerekli kütüphaneledikten sonra:
```bash
python app.py
```
komutunu çalıştırınız. 



