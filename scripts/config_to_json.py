import sys
import json 
from pathlib import Path
import config_stp

ROOT = Path(__file__).resolve().parent.parent

def main():
    output_path = ROOT / "src" / "config_stp" / "configs" / "config_stp.json"
    data = config_stp.load_config_values('parsed')
    with output_path.open("w") as f:
        json.dump(data, f, indent=2)
    print(data)

if __name__ == "__main__":
    main()
