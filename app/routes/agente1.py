from flask import request, render_template
from app import app
import requests
import os

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
            "Authorization": f"Bearer {app.config['HUGGINGFACE_TOKEN']}"
        }

        response = requests.post(
            "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            resultado = response.json()[0]['generated_text']
        else:
            resultado = f"Erro ao acessar a API: {response.status_code}"

    return render_template("agente1.html", acao="Criação de ideias de conteúdo", resultado=resultado)
