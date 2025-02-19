import tensorflow as tf
import json
from tensorflow.keras.preprocessing.text import Tokenizer, tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Embedding, LSTM, Dense, SpatialDropout1D, Conv1D, MaxPool1D, SimpleRNN, Bidirectional, Reshape, Conv2D, MaxPooling2D, TimeDistributed
from tensorflow.keras import regularizers
import numpy as np
import os

max_len = 200
embedding_dim = 200

# Loading pretrained tokenizer
with open(os.path.join(os.path.dirname(__file__), 'tokenizer.json')) as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)
word_index = tokenizer.word_index

# Loading embedding matrix
with open(os.path.join(os.path.dirname(__file__), 'embedding.in.npy'), 'rb') as f:
    embedding_matrix = np.load(f)

# Loading model
regr_model = Sequential([
    Embedding(input_dim=len(word_index) + 1, 
              output_dim=embedding_dim, 
              weights=[embedding_matrix], 
              input_length=max_len, 
              trainable=False),
    Conv1D(filters=20, kernel_size = 3, activation="relu", padding = 'same'),
    MaxPool1D(strides = 2),
    Conv1D(filters=30, kernel_size = 3, activation="relu", padding = 'same'),
    MaxPool1D(strides = 2),
    LSTM(40),
    Dense(1, activation='linear')
])
regr_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
regr_model.build(input_shape=(None, 200))
regr_model.load_weights(os.path.join(os.path.dirname(__file__), 'cnn_lstm_regr.weights.h5'))

def inference(text):
    text_seq = tokenizer.texts_to_sequences([text])
    text_pad = pad_sequences(text_seq, maxlen = max_len)
    return min(max(regr_model.predict(text_pad, verbose = 0)[0][0] + 1, 1), 5)

if __name__ == "__main__":
    print(inference("I like this product."))