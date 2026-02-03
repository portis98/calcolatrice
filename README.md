### CALCOLATRICE CON PIPELINE DI OPERAZIONI

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

