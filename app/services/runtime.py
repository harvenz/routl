from pathlib import Path
import subprocess

class RuntimeManager:
    def __init__(self, dir: Path):
        self.dir = dir

    def create(self, num: int) -> None:
        for i in range(num):
            instance_dir = self.dir / format(i, "02x")
            data_dir = instance_dir / "data"

            data_dir.mkdir(parents=True, exist_ok=True)
            self._create_config(i, instance_dir, data_dir)

    # generates the torrc configuration file for an instance
    @staticmethod
    def _create_config(index: int, instance_dir: Path, data_dir: Path):
        (instance_dir / "torrc").write_text("\n".join([
                f"SocksPort {9050 + index}",
                "NewCircuitPeriod 15",
                "MaxCircuitDirtiness 600",
                f"DataDirectory {data_dir}",
            ]),
        )

    def run(self, id: int):
        instance_dir = self.dir / format(id, "02x")

        subprocess.run(["tor", "-f", str(instance_dir) + "/" + "torrc"], 
                       capture_output=True, text=True)