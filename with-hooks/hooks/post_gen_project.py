"""
Copies the cookiecutter_replay file from the default directory to the project directory.
Removes key-value pairs that contain user specific values
"""

import json
from pathlib import Path


def remove_excluded_keys(data):
    """
    Recursively remove excluded_keys from a dictionary (including nested dicts).
    """
    excluded_keys = ["_output_dir", "_repo_dir"]
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


replay_dir = "~/.cookiecutter_replay/"
src = Path(replay_dir).expanduser() / "{{ cookiecutter.__template_dir }}.json"
dst = (
    Path.cwd()
    / "{{cookiecutter.__project_kebab_case}}"
    / ".cookiecutter_replay.json"
)
dst.parent.mkdir(parents=True, exist_ok=True)

with open(src, "r") as src, open(dst, "w") as dst:
    data = json.load(src)
    data_filtered = remove_excluded_keys(data)
    data["cookiecutter"]["__checkout"] = "{{ cookiecutter._checkout }}"
    json.dump(data_filtered, dst, indent=2)
