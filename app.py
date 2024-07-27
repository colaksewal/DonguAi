from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from textblob import TextBlob

app = Flask(__name__)

# NLTK durak kelimeleri yükleme
nltk.download('stopwords')
from nltk.corpus import stopwords
turkish_stopwords = stopwords.words('turkish')

# Veri setini yükleme
df = pd.read_csv('data/data.csv')

# Metin verilerini birleştirme (sozum ve anlami)
df['text'] = df['sozum'] + " " + df['anlami']

# Metin verilerini ön işleme
def preprocess_text(text):
    text = text.lower()
    words = text.split()
    words = [word for word in words if word not in turkish_stopwords]
    return ' '.join(words)

df['cleaned_text'] = df['text'].apply(preprocess_text)

# Özellik çıkarımı (TF-IDF vektörizasyon)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['cleaned_text'])

# Duygu analizi fonksiyonu
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        processed_input = preprocess_text(user_input)
        sentiment_score = analyze_sentiment(user_input)
        input_vector = vectorizer.transform([processed_input])
        cos_similarities = cosine_similarity(input_vector, X).flatten()
        top_n = 5  # En uygun 5 atasözü önerisi
        top_n_indices = np.argsort(cos_similarities)[-top_n:][::-1]
        recommendations = df.iloc[top_n_indices]
        
        # Duygu analizi sonucu filtreleme
        filtered_recommendations = recommendations.copy()
        if sentiment_score < 0:
            # Negatif duygular için önerileri filtreleme
            filtered_recommendations = recommendations[recommendations['text'].str.contains('kötü|olumsuz|zorluk', case=False)]
        elif sentiment_score > 0:
            # Pozitif duygular için önerileri filtreleme
            filtered_recommendations = recommendations[recommendations['text'].str.contains('iyi|olumlu|başarı', case=False)]
        
        # Kaydetme işlemi
        if 'save' in request.form:
            with open('saved_recommendations.txt', 'w', encoding='utf-8') as f:
                for index in top_n_indices:
                    f.write(f"{df.iloc[index]['sozum']} ({df.iloc[index]['anlami']})\n")
            return redirect(url_for('index'))
        
        return render_template('index.html', recommendations=filtered_recommendations.to_dict(orient='records'))

    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
