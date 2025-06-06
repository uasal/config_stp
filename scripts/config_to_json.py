import sys
import json 
from pathlib import Path
from datetime import datetime
from collections import OrderedDict
import config_stp

ROOT = Path(__file__).resolve().parent.parent

def main():
    output_path = ROOT / "src" / "config_stp" / "configs" / "config_stp.json"
    data = config_stp.load_config_values('parsed')
    ordered_data = OrderedDict()
    ordered_data["metadata"] = { "info": f"This file was autogenerated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC" }
    ordered_data.update(data)
    json_str = json.dumps(ordered_data, indent=4)
    print(json_str)
    with output_path.open("w") as f:
        f.write(json_str)

if __name__ == "__main__":
    main()
