
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv(
        "WELCOME_MESSAGE",
        "Bienvenue dans notre application Docker !"
    )
    return f"""
    <html>
        <head>
            <title>Mini Projet Docker</title>
        </head>
        <body>
            <h1>{message}</h1>
            <p>Application web conteneurisée avec Docker et Flask.</p>
            <p>Version : 1.0.1</p>
            <a href="/about">À propos du projet</a>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "OK"}, 200

@app.route("/about")
def about():
    return {
        "application": "Mini Projet Docker",
        "version": "1.0.1",
        "framework": "Flask",
        "containerized": True
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
