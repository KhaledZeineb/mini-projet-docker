
# Mini-projet Docker – Application Flask

## 1. Présentation

Ce projet consiste à conteneuriser une application web Flask avec Docker et à publier ses différentes versions sur Docker Hub.

L'application permet :
- D'afficher une page d'accueil personnalisable.
- De vérifier l'état de santé de l'application.
- D'afficher les informations de l'application avec la route `/about`.

## 2. Technologies utilisées

- Python 3.12
- Flask 3.1.2
- Docker
- Docker Hub

## 3. Structure du projet

```text
mini-projet-docker/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## 4. Construction de l'image

Pour construire la version initiale :

```bash
docker build -t mini-projet-docker:1.0.0 .
```

Pour construire la nouvelle version :

```bash
docker build -t mini-projet-docker:1.0.1 .
```

## 5. Exécution du conteneur

```bash
docker run -d \
  --name mini-projet-container \
  -p 8080:5000 \
  --memory=256m \
  --cpus=0.5 \
  -e WELCOME_MESSAGE="Bienvenue dans notre application Docker !" \
  mini-projet-docker:1.0.1
```

## 6. Routes disponibles

| Route | Description |
|---|---|
| `/` | Page d'accueil |
| `/health` | Vérification de l'état de l'application |
| `/about` | Informations sur l'application |

## 7. Vérification

```bash
curl http://localhost:8080
curl http://localhost:8080/health
curl http://localhost:8080/about
```

## 8. Gestion des ressources

Le conteneur est lancé avec :
- Mémoire maximale : 256 Mo.
- CPU : 0.5.

Pour consulter les statistiques :

```bash
docker stats --no-stream mini-projet-container
```

## 9. Publication sur Docker Hub

Dépôt Docker Hub :

https://hub.docker.com/r/zeinebkhaled/mini-projet-docker

Versions publiées :
- `1.0.0` : version initiale.
- `1.0.1` : version améliorée avec la route `/about`.
- `1.0` : alias de la dernière version `1.0.1`.

Pour télécharger la dernière version :

```bash
docker pull zeinebkhaled/mini-projet-docker:1.0
```

## 10. Optimisation

Le Dockerfile copie `requirements.txt` et installe les dépendances avant de copier le code source.

Cette organisation permet de réutiliser le cache Docker lorsque seul le code de l'application change.
