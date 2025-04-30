import requests
from flask import Flask, render_template, request

app = Flask(__name__)

HF_API_KEY = "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"
MODEL = "HuggingFaceH4/zephyr-7b-beta"

@app.route("/agente1", methods=["GET", "POST"])
def agente1():
    resultado = None
    if request.method == "POST":
        tema = request.form.get("tema")

        payload = {
            "inputs": f"Crie uma ideia de conteúdo para o tema: {tema}",
            "parameters": {"max_new_tokens": 200}
        }

        headers = {
            "Authorization": f"Bearer {HF_API_KEY}"
        }

        response = requests.post(
            f"https://api-inference.huggingface.co/models/{MODEL}",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            resultado = response.json()[0]['generated_text']
        else:
            resultado = f"Erro ao acessar a API: {response.status_code}"
            

    return render_template("agente1.html", acao="Criação de ideias de conteúdo", resultado=resultado)
if __name__ == "__main__":
    app.run(debug=True)
