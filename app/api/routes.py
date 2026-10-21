from flask import Flask
from pathlib import Path
import threading

from app.services.runtime import RuntimeManager

app = Flask(__name__)
runtime = RuntimeManager(Path("./runtime/instances"))

@app.route("/")
def home():
    runtime.create(3)

    for i in range(3):
        th = threading.Thread(target=runtime.run, args=(i,))
        th.start()
        
    return "routl working"