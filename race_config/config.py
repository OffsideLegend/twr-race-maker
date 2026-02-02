from typing import Dict, Any

import yaml

RaceConfig = Dict[str, Any]

def parse_config(config_file_path: str) -> RaceConfig:
    try:
        with open(config_file_path, 'r', encoding='utf-8') as file:
            # Use safe_load to avoid executing arbitrary code
            data = yaml.safe_load(file)
            if data is None:
                return {}  # Return empty dict if YAML file is empty
            if not isinstance(data, dict):
                raise ValueError("YAML content is not a dictionary.")
            return data
    except FileNotFoundError:
        print(f"Error: File '{config_file_path}' not found.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return {}