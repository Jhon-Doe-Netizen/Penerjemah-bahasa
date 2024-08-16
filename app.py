from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ''
    if request.method == 'POST':
        # Mendapatkan teks dari form
        text_to_translate = request.form['text']
        destination_language = request.form['language']
        
        # Membuat instance Translator
        translator = Translator()
        
        # Menerjemahkan teks
        translated = translator.translate(text_to_translate, dest=destination_language)
        translation = translated.text

    # Menampilkan template dan hasil terjemahan
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
