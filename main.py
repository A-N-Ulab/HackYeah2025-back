from flask import Flask
app = Flask(__name__)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "Hello World"}