from flask import Flask
from pathlib import Path
from app.services.runtime import RuntimeManager

app = Flask(__name__)
runtime = RuntimeManager(Path("./runtime/instances"))

@app.route("/")
def home():
    runtime.create(3)
    return "routl working"