#!/bin/bash

# Nome da pasta do projeto
PROJETO="brainspark_edu"
BACKUP="$PROJETO-backup-$(date +%Y%m%d%H%M%S)"

# Se o projeto já existir, criar backup
if [ -d "$PROJETO" ]; then
    echo "Projeto existente encontrado. Criando backup em $BACKUP"
    cp -r "$PROJETO" "$BACKUP"
fi

echo "Criando/Atualizando projeto: $PROJETO"
mkdir -p $PROJETO/{static/css,static/js,templates,database}

# Criar o app.py atualizado com rotas
cat <<EOL > $PROJETO/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/agente1")
def agente1():
    return render_template("agente1.html")

@app.route("/agente2")
def agente2():
    return render_template("agente2.html")

@app.route("/agente3")
def agente3():
    return render_template("agente3.html")

@app.route("/agente4")
def agente4():
    return render_template("agente4.html")

@app.route("/agente5")
def agente5():
    return render_template("agente5.html")

@app.route("/agente6")
def agente6():
    return render_template("agente6.html")

@app.route("/agente7")
def agente7():
    return render_template("agente7.html")

@app.route("/agente8")
def agente8():
    return render_template("agente8.html")

@app.route("/agente9")
def agente9():
    return render_template("agente9.html")

@app.route("/agente10")
def agente10():
    return render_template("agente10.html")

@app.route("/historico")
def historico():
    return render_template("historico.html")

if __name__ == "__main__":
    app.run(debug=True)
EOL

# Criar requirements.txt
cat <<EOL > $PROJETO/requirements.txt
flask
EOL

# Criar README.md
cat <<EOL > $PROJETO/README.md
# BrainSpark EDU
Sistema de gerenciamento de agentes educacionais com IA.
EOL

# Criar style.css
cat <<EOL > $PROJETO/static/css/style.css
body {
    font-family: 'Arial', sans-serif;
    background-color: #f8f9fa;
    margin: 0;
    padding: 20px;
}
EOL

# Criar script.js
cat <<EOL > $PROJETO/static/js/script.js
console.log("BrainSpark EDU pronto!");
EOL

# Criar banco de dados vazio
touch $PROJETO/database/historico.db

# Criar todos os templates HTML
cd $PROJETO/templates
for pagina in index agente1 agente2 agente3 agente4 agente5 agente6 agente7 agente8 agente9 agente10 historico
do
cat <<EOL > \$pagina.html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>\${pagina^} | BrainSpark EDU</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Página \${pagina^}</h1>
    <p>Conteúdo da página \${pagina^} aqui.</p>
</body>
</html>
EOL
done
cd ../../..

echo "Projeto $PROJETO criado ou atualizado com sucesso!"
echo "Se precisar, seu backup está salvo em: $BACKUP"
