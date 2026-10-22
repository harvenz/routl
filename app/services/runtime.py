from pathlib import Path
from app.services.instance import InstanceManager

class RuntimeManager:
    def __init__(self, dir: Path):
        self.dir = dir