import os
import numpy as np
import librosa
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.layers import Conv1D, MaxPooling1D, GRU, Dense, Dropout, BatchNormalization
def veri_yukle(dizin):
    veri = []
    etiketler = []
    for klasor_yolu, klasor_isimleri, dosya_isimleri in os.walk(dizin):
        for dosya in dosya_isimleri:
            if dosya.endswith('.wav'):
                dosya_yolu = os.path.join(klasor_yolu, dosya)
                etiket = dosya.split('-')[2]
                etiketler.append(etiket)
                veri.append(dosya_yolu)
    return veri, etiketler

def ozellik_cikar(dosya_yolu):
    ses, sr = librosa.load(dosya_yolu, res_type='kaiser_fast')
    ses = librosa.effects.pitch_shift(ses, sr=sr, n_steps=2)
    ses = librosa.effects.time_stretch(ses, rate=0.8)
    mfcc = librosa.feature.mfcc(y=ses, sr=sr, n_mfcc=40)
    mel = librosa.feature.melspectrogram(y=ses, sr=sr)
    mfcc = np.mean(mfcc.T, axis=0)
    mel = np.mean(mel.T, axis=0)
    return np.hstack((mfcc, mel))

veri, etiketler = veri_yukle("/Users/omersefaguckiran/PycharmProjects/model-omer/duygu-ses-data/ravdes")
ozellikler = np.array([ozellik_cikar(dosya) for dosya in veri])

etiket_kodlayici = LabelEncoder()
etiketler_kodlu = to_categorical(etiket_kodlayici.fit_transform(etiketler))

X_train, X_test, y_train, y_test = train_test_split(ozellikler, etiketler_kodlu, test_size=0.2, random_state=42)

def karma_model_olustur(girdi_sekli):
    model = tf.keras.models.Sequential([
        tf.keras.Input(shape=girdi_sekli),
        Conv1D(64, kernel_size=3, activation='relu'),
        MaxPooling1D(pool_size=2),
        BatchNormalization(),
        Conv1D(128, kernel_size=3, activation='relu'),
        MaxPooling1D(pool_size=2),
        BatchNormalization(),
        GRU(128, return_sequences=True),
        GRU(64),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(etiketler_kodlu.shape[1], activation='softmax')
    ])
    return model

X_train_3d = np.expand_dims(X_train, axis=2)
X_test_3d = np.expand_dims(X_test, axis=2)

karma_model = karma_model_olustur((X_train_3d.shape[1], X_train_3d.shape[2]))

karma_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

kontrol_noktasi = ModelCheckpoint('duygu-ses-epochs.keras', monitor='val_accuracy', mode='max', save_best_only=True, verbose=1)
erken_durdurma = EarlyStopping(monitor='val_loss', mode='min', patience=10, verbose=1)

karma_model_gecmisi = karma_model.fit(
    X_train_3d, y_train,
    validation_data=(X_test_3d, y_test),
    epochs=100,
    batch_size=32,
    callbacks=[kontrol_noktasi, erken_durdurma]
)

en_iyi_model = tf.keras.models.load_model('duygu-ses-epochs.keras')
en_iyi_model.save('duygu-ses-epochs.h5')

en_iyi_model = tf.keras.models.load_model('duygu-ses-epochs.h5')
en_iyi_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
kayip, dogruluk = en_iyi_model.evaluate(X_test_3d, y_test)
print(f'En iyi karmaşık model doğruluğu: {dogruluk * 100:.2f}%')
