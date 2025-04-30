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
            f"Crie um conteúdo educativo em português sobre o tema abaixo com:\n"
            f"Título, Introdução, Seção 1, Seção 2, Seção 3.\n\n"
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
                "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-question-generation-ap",
                headers=headers,
                json=payload
            )

            if response.status_code == 200:
                resultado = response.json()[0]['generated_text']
            elif response.status_code == 402:
                resultado = (
                    "⚠️ Erro 402: Você atingiu o limite gratuito da API Hugging Face. "
                    "Para continuar usando, é necessário:\n"
                    "1. Gerar uma nova chave em huggingface.co\n"
                    "2. Esperar o reset diário (caso esteja em plano gratuito)\n"
                    "3. Trocar para outro modelo ou rodar localmente."
                )
            else:
                resultado = f"Erro ao acessar a API: {response.status_code}"
        except Exception as e:
            resultado = f"Erro inesperado: {str(e)}"

    return render_template("agente1.html", acao="Criação de ideias de conteúdo", resultado=resultado)
