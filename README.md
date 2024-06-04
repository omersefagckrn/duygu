Elbette, işte proje adımlarını detaylandıran bir `README.md` dosyası:

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

## Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir issue açın.

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
```

Bu metni doğrudan GitHub'daki projenizin `README.md` dosyasına yapıştırabilirsiniz.
