from pathlib import Path
from uuid import uuid4
import subprocess

class InstanceManager:
    def __init__(self, port: int, runtime_dir: Path):
        # instance configuration
        self.id = uuid4().hex
        self.port = port

        # dir configuration
        self.instance_dir = runtime_dir / "instances" / self.id
        self.working_dir = self.instance_dir / "data"

    def create(self) -> None:
        self._create_config(self.port, self.instance_dir, self.working_dir)

    # generates the torrc configuration file for an instance
    @staticmethod
    def _create_config(port: int, instance_dir: Path, working_dir: Path):
        working_dir.mkdir(parents=True, exist_ok=True)

        config = "\n".join([
                f"SocksPort {port}",
                f"DataDirectory {working_dir}",
        ])

        (instance_dir / "torrc").write_text(config)

    
    def start(self) -> None:
        subprocess.Popen(["tor", "-f", str(self.instance_dir / "torrc")])
