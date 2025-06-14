"""
In Cookiecutter, the **pre_gen_project hook** runs after the template
repository has been cloned and checked out (including any `--checkout`
tag/branch), but before the project is rendered (i.e., before your
template files are copied and variables are substituted).
"""

import subprocess
from pathlib import Path

print("cwd:", Path.cwd())

template_name = "{{ cookiecutter.__directory }}"
tags = subprocess.check_output(
    ["git", "tag", "-l", f"'{template_name}/*'", "--sort", "v:refname"],
    text=True,
).splitlines()
print(tags)

# latest_tag = tags[-1][0]
# print(latest_tag)

# Write to a JSON file in the template root (will be copied to the generated project)
# with open("cookiecutter_prehook_context.json", "w") as f:
#     json.dump({"latest_tag": latest_tag}, f)
