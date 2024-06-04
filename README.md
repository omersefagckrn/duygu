Elbette, `README.md` dosyasına eksik kalan adımları ekleyelim. İşte güncellenmiş `README.md` dosyası:

```markdown
# Duygu Tahmin Etme Projesi

Bu proje, ses ve görüntü verilerini kullanarak duyguları tahmin etmeyi amaçlamaktadır. Projede, Keras ve TensorFlow kullanılarak eğitilmiş modeller ile duygular tahmin edilmektedir. Ayrıca, Flask web uygulaması ile gerçek zamanlı duygu tahmini yapılabilmektedir.

## Literatür ve Makale Araştırmaları

Bu projede kullanılan yöntemler ve teknikler, aşağıdaki literatür ve makalelerden esinlenilmiştir:

1. **"A Review on Speech Emotion Recognition: Datasets, Features, and Classification Models"**
   - Bu makale, konuşma duygu tanıma alanındaki mevcut veri setlerini, özellik çıkarım yöntemlerini ve sınıflandırma modellerini kapsamlı bir şekilde incelemektedir.
   - Kaynak: [Link](https://arxiv.org/abs/1906.01044)

2. **"Deep Learning for Emotion Recognition in Faces and Voices"**
   - Bu çalışma, yüz ifadeleri ve sesli ifadeler kullanarak duyguların tanınmasında derin öğrenme yöntemlerinin uygulanmasını incelemektedir.
   - Kaynak: [Link](https://ieeexplore.ieee.org/document/7508778)

## Veri Setleri ve Özellikleri

### Ses Verisi
Bu projede kullanılan ses verisi RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song) veri setinden alınmıştır. Bu veri setine aşağıdaki bağlantıdan ulaşabilirsiniz:

[RAVDESS Emotional Speech Audio](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)

Veri seti, farklı duyguları ifade eden ses dosyalarından oluşmaktadır. Her ses dosyası, konuşmacının belirli bir duyguyu ifade ettiği bir cümleyi içerir.

### Görüntü Verisi
Görüntü verisi ise FER-2013 (Facial Expression Recognition) veri setinden alınmıştır. Bu veri setine aşağıdaki bağlantıdan ulaşabilirsiniz:

[FER-2013 Facial Expression Recognition](https://www.kaggle.com/datasets/msambare/fer2013)

Veri seti, farklı duyguları ifade eden yüz ifadelerinin resimlerinden oluşmaktadır. Her resim, belirli bir duygu etiketi ile etiketlenmiştir.

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
- **Eğitim**: Model, eğitim verisi üzerinde 100 epoch boyunca eğitim aldı.
- **Değerlendirme**: Modelin doğruluğu ve kaybı test verisi üzerinde değerlendirildi.

### Görüntü Modeli:
- **Model Mimarisi**: 2D Convolutional katmanlar, Pooling katmanları ve Fully Connected katmanlar kullanılarak bir model oluşturuldu.
- **Eğitim**: Model, eğitim verisi üzerinde 100 epoch boyunca eğitim aldı.
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
