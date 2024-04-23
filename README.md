Install Python3.10.10 [Python DL](https://www.python.org/downloads/)
pip install fastapi[all]

```bash
 $ python -m venv venv
 $ source venv/bin/activate or .\venv\Scripts\activate  (Windows)
 deactivatecd
 $ pip install -r requirements.txt

docker-compose up -d --build
```

uvicorn main:app --reload
