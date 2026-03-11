from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Senin Hugging Face API token
HF_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbnYiOiJwcm9kdWN0aW9uIiwia2lsb1VzZXJJZCI6IjA1MDFiYjI1LTNkZTctNDU5OS05N2QyLTFiNjM1NzE3YmM3ZiIsImFwaVRva2VuUGVwcGVyIjpudWxsLCJ2ZXJzaW9uIjozLCJpYXQiOjE3NzMyNDAwNzksImV4cCI6MTkzMDkyMDA3OX0.6s-pX-zcfc13LNAkHfRd3tXF2cqnBMMBGIauIcGzCKs"

# Ücretsiz çalışan model
MODEL = "tiiuae/falcon-7b-instruct"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

    payload = {"inputs": message}

    res = requests.post(API_URL, headers=headers, json=payload)

    if res.status_code != 200:
        return jsonify({"response": f"Hugging Face API hatası: {res.status_code}"}), 500

    try:
        data = res.json()
        # Falcon-7B Instruct modeli text olarak döner
        if isinstance(data, list):
            reply = data[0].get("generated_text", "Yanıt alınamadı")
        else:
            reply = data.get("generated_text", "Yanıt alınamadı")
    except Exception as e:
        reply = "Yanıt alınamadı"
        print(e)

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)