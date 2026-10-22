from flask import Flask
from pathlib import Path
import threading

from app.services.runtime import RuntimeManager
from app.services.instance import InstanceManager

app = Flask(__name__)
runtime = RuntimeManager(Path("./runtime/"))

@app.route("/")
def home():
    instances = []

    for port in range(9050, 9053):
        instance = InstanceManager(runtime_dir=runtime.dir, port=port)
        instance.create()
        instances.append(instance)

    for instance in instances:
        instance.start()
        
    return "routl working"