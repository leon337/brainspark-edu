from flask import request, render_template
from app import app
import requests
import os

@app.route("/agente1", methods=["GET", "POST"])
def agente1():
    resultado = None
    if request.method == "POST":
        tema = request.form.get("tema")

        prompt = (
            f"Crie um conteúdo educativo em português com esse formato:\n"
            f"Título:\nIntrodução:\nSeção 1:\nSeção 2:\nSeção 3:\n\n"
            f"Tema: {tema}\n"
        )

        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": 300},
            "options": {"wait_for_model": False}
        }

        headers = {
            "Authorization": f"Bearer {app.config['HUGGINGFACE_TOKEN']}"
        }

        try:
            response = requests.post(
                "https://api-inference.huggingface.co/models/google/flan-t5-small",
                headers=headers,
                json=payload
            )

            if response.status_code == 200:
                resultado = response.json()[0]['generated_text']
            else:
                resultado = f"Erro ao acessar a API: {response.status_code}"
        except Exception as e:
            resultado = f"Erro inesperado: {str(e)}"

    return render_template("agente1.html", acao="Criação de ideias de conteúdo", resultado=resultado)
