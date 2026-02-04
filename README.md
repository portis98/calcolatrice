# CALCOLATRICE CON PIPELINE DI OPERAZIONI
Progetto per il corso di Full Stack Developer di ITS Olivetti anno 2 - ed. 2025-2026

Progetto di calcolatrice in ptython che esegue una serie di operazioni aritmetiche. Viene definita una pipeline su github che produce una immagine docker con l'applicazione su Docker Hub.

Si utilizza la metodologia TDD (Test Driven Development) per lo sviluppo dell'applicazione, con l'utilizzo di pytest per i test e uv per la gestione dell'ambiente virtuale e delle dipendenze.

L'applicazione viene eseguita in :

- locale con l'ambiente virtuale uv
- in un container docker basato su alpine linux
- in un docker compose
- in un cluster k3s locale

## UV
```shell
uv venv
```
## Attivare l'ambiente virtuale
```shell
source .venv/bin/activate  (Linux/Mac)
.venv\Scripts\activate    (Windows) 
```
## Installare dipendenze
```shell
uv pip compile requirements/requirements-test.in -o requirements/requirements-test.txt
uv pip compile requirements/requirements.in -o requirements/requirements.txt
uv pip install -r requirements/requirements-test.txt
uv pip install -r requirements/requirements.txt
```
## Utilizzo
```shell
uv run python calcolatrice.py
python3 calcolatrice.py
```
## Esecuzione dei test
```shell
pytest -v
```

## Dockerfile

Per costruire l'immagine Docker locale
```shell
docker build -f Dockerfile.debian -t calcolatrice:debian .
docker build -f Dockerfile.alpine -t calcolatrice:alpine .
```
Per eseguire il container
```shell
docker run -it --rm calcolatrice:debian
docker run -it --rm calcolatrice:alpine
```

Per costrire l'immagine Docker e caricarla su DockerHub
```shell
docker build -f Dockerfile.alpine -t poldis98/fullstack-calcolatrice:alpine .
docker push poldis98/fullstack-calcolatrice:alpine
```
Per costruire una immagine multi archittettura e caricare su Docker Hub
```shell
docker buildx build --platform linux/amd64,linux/arm64 -f Dockerfile.alpine -t poldis98/fullstack-calcolatrice:alpine --push .
```

## Aggiunti workflow GitHub action

- pytest.yml: esecuzione dei test con pytest
