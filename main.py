from flask import Flask, render_template, Response, jsonify, request
import cv2
import numpy as np
from keras.models import load_model
import librosa
import tempfile

app = Flask(__name__)

goruntu_model = load_model('my-epochs/duygu-goruntu-epochs.h5')
ses_model = load_model('my-epochs/duygu-ses-epochs.h5')

yuz_algilayici = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

duygu_etiketleri = ["Kızgın", "İğrenmiş", "Korkmuş", "Mutlu", "Nötr", "Üzgün", "Şaşırmış"]

kamera = cv2.VideoCapture(0)

duygu_sonucu = None

def cerceve_isle(cerceve):
    gri = cv2.cvtColor(cerceve, cv2.COLOR_BGR2GRAY)
    yuzler = yuz_algilayici.detectMultiScale(gri, 1.3, 5)
    for (x, y, w, h) in yuzler:
        yuz_resmi = gri[y:y + h, x:x + w]
        yeniden_boyut = cv2.resize(yuz_resmi, (48, 48))
        normalize = yeniden_boyut / 255.0
        yeniden_sekil = np.reshape(normalize, (1, 48, 48, 1))
        sonuc = goruntu_model.predict(yeniden_sekil)
        etiket = np.argmax(sonuc, axis=1)[0]

        global duygu_sonucu
        duygu_sonucu = {
            'label': duygu_etiketleri[etiket],
            'score': float(np.max(sonuc)) * 10  # Skoru 0-10 aralığına çevir
        }
        break
    ret, buffer = cv2.imencode('.jpg', cerceve)
    return buffer.tobytes()

def ses_isle(dosya_yolu):
    try:
        ses, sr = librosa.load(dosya_yolu, sr=None, res_type='kaiser_fast')
        mfcc = librosa.feature.mfcc(y=ses, sr=sr, n_mfcc=40)
        mfcc = np.mean(mfcc.T, axis=0)
        mfcc = np.expand_dims(mfcc, axis=0)
        mfcc = np.expand_dims(mfcc, axis=2)
        tahminler = ses_model.predict(mfcc)
        skor = np.max(tahminler) * 10
        duygu_index = np.argmax(tahminler)
        duygu = duygu_etiketleri[duygu_index]
        return {'score': skor, 'emotion': duygu}
    except Exception as e:
        print(f"Ses işleme sırasında hata oluştu: {dosya_yolu}, Hata: {e}")
        return {'score': 0, 'emotion': 'Hata'}

def video_akisi():
    while True:
        success, cerceve = kamera.read()
        if not success:
            break
        else:
            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + cerceve_isle(cerceve) + b'\r\n'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(video_akisi(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/emotion')
def duygu_al():
    global duygu_sonucu
    return jsonify(duygu_sonucu)

@app.route('/audio_emotion', methods=['POST'])
def ses_duygu():
    if 'audio_file' not in request.files:
        return jsonify({'error': 'Ses dosyası yüklenmedi'})

    dosya = request.files['audio_file']
    if dosya.filename == '':
        return jsonify({'error': 'Ses dosyası yüklenmedi'})

    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_dosya:
        dosya.save(temp_dosya.name)
        global ses_duygu_sonucu
        ses_duygu_sonucu = ses_isle(temp_dosya.name)
    return jsonify(ses_duygu_sonucu)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
