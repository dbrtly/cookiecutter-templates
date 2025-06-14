"""
In Cookiecutter, the **pre_gen_project hook** runs after the template
repository has been cloned and checked out (including any `--checkout`
tag/branch), but before the project is rendered (i.e., before your
template files are copied and variables are substituted).
"""

import json
import sys
from pathlib import Path

TEMPLATES_PATH = "~/.cookiecutters/"
TEMPLATES_REPO = "cookiecutter-templates"
TEMPLATE_SPEC = "with-hooks/cookiecutter.json"
REQUIRED_VARS = [
    "__project_kebab_case",
    "__project_snake_case",
    "__templates_uri",
    "__template_dir",
    "__checkout",
]


def check_required_variables(replay_filepath: str):
    with open(replay_filepath) as f:
        config = json.load(f)

    missing = [var for var in REQUIRED_VARS if var not in config]
    if missing:
        print(f"Missing required variables: {', '.join(missing)}")
        sys.exit(1)
    else:
        print("All required variables are present.")


if __name__ == "__main__":
    replay_filepath = (
        Path(TEMPLATES_PATH).expanduser() / TEMPLATES_REPO / TEMPLATE_SPEC
    )
    check_required_variables(replay_filepath)
