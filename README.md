Tabii ki, daha dikkatli yazılmış ve doğru linklerle güncellenmiş `README.md` dosyasını aşağıda bulabilirsiniz:

```markdown
# Duygu Tahmin Etme Projesi

Bu proje, ses ve görüntü verilerini kullanarak duyguları tahmin etmeyi amaçlamaktadır. Projede, Keras ve TensorFlow kullanılarak eğitilmiş modeller ile duygular tahmin edilmektedir. Ayrıca, Flask web uygulaması ile gerçek zamanlı duygu tahmini yapılabilmektedir.

## Gereksinimler

Projenin çalışması için gerekli Python paketlerini `requirements.txt` dosyasında bulabilirsiniz. Gerekli paketleri yüklemek için:

```sh
pip install -r requirements.txt
```

## Projenin Yapısı

- `duygu-ses-data/`: Ses verilerinin bulunduğu dizin
- `duygu-goruntu-data/`: Görüntü verilerinin bulunduğu dizin
- `model-egitim/`: Model eğitim kodlarının bulunduğu dizin
  - `ses/`: Ses verisiyle model eğitimi
  - `goruntu/`: Görüntü verisiyle model eğitimi
- `templates/`: HTML şablon dosyaları
- `main.py`: Flask web uygulamasının ana dosyası
- `requirements.txt`: Projenin bağımlılıklarını içeren dosya

## Veri Setleri ve Özellikleri

### Ses Verisi
Bu projede kullanılan ses verisi RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song) veri setinden alınmıştır. Bu veri setine aşağıdaki bağlantıdan ulaşabilirsiniz:

[RAVDESS Emotional Speech Audio](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)

Veri seti, farklı duyguları ifade eden ses dosyalarından oluşmaktadır. Her ses dosyası, konuşmacının belirli bir duyguyu ifade ettiği bir cümleyi içerir.

### Görüntü Verisi
Görüntü verisi ise FER-2013 (Facial Expression Recognition) veri setinden alınmıştır. Bu veri setine aşağıdaki bağlantıdan ulaşabilirsiniz:

[FER-2013 Facial Expression Recognition](https://www.kaggle.com/datasets/msambare/fer2013)

Veri seti, farklı duyguları ifade eden yüz ifadelerinin resimlerinden oluşmaktadır. Her resim, belirli bir duygu etiketi ile etiketlenmiştir.

### Veri Setlerini İndirme ve Hazırlama

1. Yukarıdaki bağlantılardan veri setlerini indirin.
2. `ravdess-emotional-speech-audio` klasörünü `duygu-ses-data/` dizinine taşıyın.
3. `fer2013` klasörünü `duygu-goruntu-data/` dizinine taşıyın.

## Veri Ön İşleme ve Özellik Mühendisliği

### Ses Verisi İçin:
1. **Ses Yükleme**: Librosa kullanılarak ses dosyaları yüklendi.
2. **Veri Zenginleştirme**: Ses verileri üzerinde pitch shifting ve time stretching gibi veri zenginleştirme teknikleri uygulandı.
3. **Özellik Çıkarımı**: MFCC (Mel-Frekans Kepstral Katsayıları) ve Mel spectrogram özellikleri çıkarıldı ve birleştirildi.

### Görüntü Verisi İçin:
1. **Resim Yükleme**: OpenCV kullanılarak resimler yüklendi.
2. **Ölçekleme**: Resimler 48x48 piksel boyutuna ölçeklendi.
3. **Normalizasyon**: Piksel değerleri 0-255 aralığından 0-1 aralığına normalize edildi.
4. **Özellik Çıkarımı**: Resimler, model eğitimine uygun formatta dönüştürüldü.

## Modelleme, Test ve Doğrulama

### Ses Modeli:
- **Model Mimarisi**: 1D Convolutional katmanlar, GRU katmanları ve Fully Connected katmanlar kullanılarak bir model oluşturuldu.
- **Eğitim**: Model, ses verisi üzerinde 100 epoch boyunca eğitim aldı.
- **Değerlendirme**: Modelin doğruluğu ve kaybı test verisi üzerinde değerlendirildi.

### Görüntü Modeli:
- **Model Mimarisi**: 2D Convolutional katmanlar, Pooling katmanları ve Fully Connected katmanlar kullanılarak bir model oluşturuldu.
- **Eğitim**: Model, görüntü verisi üzerinde 30 epoch boyunca eğitim aldı.
- **Değerlendirme**: Modelin doğruluğu ve kaybı test verisi üzerinde değerlendirildi.

## Dağıtım İçin: Kaynaklar, Ortam, API, Kitaplık ve Teknoloji Yığınları

### Gerekli Kaynaklar:
- **Python**: 3.9 veya üzeri
- **Keras**: 2.4.3
- **TensorFlow**: 2.4.1
- **Librosa**: 0.8.0
- **Flask**: 1.1.2

### Ortam Kurulumu:
- Sanal ortam oluşturma ve bağımlılıkları yükleme adımları yukarıda verilmiştir.

### API ve Uygulama:
- Flask web framework kullanılarak gerçek zamanlı duygu tahmini yapılmaktadır.

### Teknoloji Yığını:
- **Backend**: Python, TensorFlow, Keras
- **Frontend**: HTML, CSS, JavaScript (Flask templates kullanılarak)

## Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın

Öncelikle, projeyi GitHub'dan klonlayın:

```sh
git clone https://github.com/omersefagckrn/duygu.git
cd duygu
```

### 2. Sanal Ortam Oluşturun ve Aktif Hale Getirin

Sanal ortam oluşturun ve aktif hale getirin:

```sh
python -m venv .venv
source .venv/bin/activate  # MacOS ve Linux için
# veya
.venv\Scripts\activate  # Windows için
```

### 3. Gerekli Paketleri Yükleyin

Gerekli Python paketlerini yüklemek için:

```sh
pip install -r requirements.txt
```

### 4. Modelleri Eğitin

#### Ses Modeli Eğitimi

Ses verisiyle modeli eğitmek için:

```sh
python model-egitim/ses/ses.py
```

#### Görüntü Modeli Eğitimi

Görüntü verisiyle modeli eğitmek için:

```sh
python model-egitim/goruntu/goruntu.py
```

### 5. Flask Uygulamasını Başlatın

Flask web uygulamasını başlatmak için:

```sh
python main.py
```

Uygulama başlatıldığında, tarayıcınızda `http://127.0.0.1:5000/` adresine giderek gerçek zamanlı duygu tahminini görebilirsiniz.

## Kullanım

### Gerçek Zamanlı Görüntü Duygu Tahmini

- Webcam üzerinden alınan görüntülerle duyguların tahmin edilmesi
- Web arayüzünde tahmin edilen duygu ve skorun görüntülenmesi

### Ses Duygu Tahmini

- Yüklenen ses dosyaları üzerinden duyguların tahmin edilmesi
- Web arayüzünde tahmin edilen duygu ve skorun görüntülenmesi
