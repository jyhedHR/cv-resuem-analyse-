from flask import Flask, request, jsonify
import spacy
import os

app = Flask(__name__)

# Load Spacy model
nlp = spacy.load("en_core_web_md")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('cvText', '')
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return jsonify({"entities": entities})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=False, host='0.0.0.0', port=port)
