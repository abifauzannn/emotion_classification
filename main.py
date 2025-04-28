from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# --- Load Model ---
model = load_model('model/best_lstm_model_300dim_final.h5')

# --- Load Tokenizer ---
with open('tokenizer/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# --- Load LabelEncoder ---
with open('tokenizer/label_encoder.pkl', 'rb') as handle:
    le = pickle.load(handle)

# --- Set MAX_SEQUENCE_LENGTH sesuai saat training ---
MAX_SEQUENCE_LENGTH = 100

# --- FastAPI App ---
app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Hello, this is Emotion Classifier API!"}

@app.post("/predict/")
def predict_emotion(request: TextRequest):
    text = request.text
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)

    pred = model.predict(padded)
    pred_class = pred.argmax(axis=1)[0]
    emotion = le.inverse_transform([pred_class])[0]  # ← Decode angka ke label asli

    return {
        "input_text": text,
        "predicted_emotion": emotion
    }
