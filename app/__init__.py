from flask import Flask
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)
app.config['HUGGINGFACE_TOKEN'] = os.getenv("HUGGINGFACE_TOKEN")

# Importa as rotas
from app.routes import agente1
