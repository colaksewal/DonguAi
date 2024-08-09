Türkçe atasözleri ve deyimlerini anlamlarına göre işlemlerden geçirip, kullanıcıdan alınan bir metine en benzer atasözünü bulmayı amaçlamaktayız, bu amacımız doğrultusunda yaptığımız işlemler aşağıda yer almaktadır. 

1. **Veri Ön İşleme**:
   - Gereksiz sütunlar kaldırılıyor.
   - Metinler küçük harfe dönüştürülüyor.
   - Noktalama işaretleri ve stopwords (gereksiz kelimeler) temizleniyor.

2. **Lemmatization**:
   - `Zeyrek` kütüphanesi kullanılarak kelimelerin kök halleri (lemma) elde ediliyor.

3. **Embedding**:
   - `BERT` modeli kullanılarak her bir cümle için vektör temsilleri (embedding'ler) oluşturuluyor.

4. **Kullanıcıdan Girdi Alma**:
   - Kullanıcıdan bir metin alınıyor, bu metnin embedding'i hesaplanıyor ve veri kümesindeki diğer embedding'lerle karşılaştırılıyor.

5. **En Benzer Sözün Bulunması**:
   - Kosinüs benzerliği kullanılarak en yakın atasözü ve anlamı bulunuyor ve ekrana yazdırılıyor.


data_exploration.ipynb datamızın ilk hali hakkında bilgiler içermektedir.

