#%%
import json
import os
from subprocess import call

file_path = os.path.realpath(__file__).rsplit('\\', 1)[0]
#%%
with open(f'{file_path}\\.vscode\\project_settings.json') as launch_template:
    settings = launch_template.read()
# %%
parsed_settings = json.loads(settings)
# %%
workspace_name = parsed_settings['general']['workspace_name']
relative_path = f"..\\msw\\{parsed_settings['general']['msw_relative_path']}"
# %%
call(["robocopy", f'{file_path}\\.vscode', f'{file_path}\\{relative_path}.vscode'])
os.rename(f'{relative_path}.vscode\\code-workspace_template.json', f'{relative_path}.vscode\\{workspace_name}.code-workspace')
