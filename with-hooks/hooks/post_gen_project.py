"""
Copies the cookiecutter_replay file to the project directory
"""

import json
from pathlib import Path


def remove_excluded_keys(data):
    """
    Recursively remove excluded_keys from a dictionary (including nested dicts).
    """
    excluded_keys = ["_template", "_output_dir", "_repo_dir"]
    if isinstance(data, dict):
        return {
            k: remove_excluded_keys(v)
            for k, v in data.items()
            if k not in excluded_keys
        }
    elif isinstance(data, list):
        return [remove_excluded_keys(item, excluded_keys) for item in data]
    else:
        return data


src = Path.cwd().parent / "{{ cookiecutter.__directory }}.json"
dst = Path.cwd() / ".cookiecutter_replay.json"
dst.parent.mkdir(parents=True, exist_ok=True)

with open(src, "r") as src, open(dst, "w") as dst:
    data = json.load(src)
    data_filtered = remove_excluded_keys(data)
    json.dump(data_filtered, dst, indent=2)
