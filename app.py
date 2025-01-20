from flask import Flask, render_template, request
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt_tab')
# Load the trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))  # This should be saved during training

# Preprocessing function
def preprocess_text(text):
    nltk.download('stopwords')
    nltk.download('wordnet')
    lemmatizer = WordNetLemmatizer()

    # Lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenization and remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words]

    return ' '.join(tokens)

# Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        # Get the input text from form
        input_text = request.form['news_text']

        # Preprocess the input text
        preprocessed_text = preprocess_text(input_text)

        # Vectorize the input text
        vectorized_text = vectorizer.transform([preprocessed_text]).toarray()

        # Predict using the model
        prediction = model.predict(vectorized_text)[0]

        # Map prediction to category
        categories = ['business', 'entertainment', 'politics', 'sport', 'tech']
        pred = categories[prediction]

    return render_template('index.html', prediction=pred)

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
