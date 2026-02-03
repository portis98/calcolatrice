```shell
uv venv
```

```shell
source .venv/bin/activate  (Linux/Mac)
.venv\Scripts\activate    (Windows) 
```

```shell
uv pip compile requirements/requirements-test.in -o requirements/requirements-test.txt
uv pip compile requirements/requirements.in -o requirements/requirements.txt
uv pip install -r requirements/requirements-test.txt
uv pip install -r requirements/requirements.txt
```

```shell
uv run python calcolatrice.py
```

