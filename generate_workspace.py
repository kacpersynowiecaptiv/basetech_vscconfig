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

# %%
with open(f'{relative_path}.vscode\\code-workspace_template.json') as vsc_workspace_template:
    vsc_workspace_template_content = vsc_workspace_template.read()

parsed_vsc_workspace_template_content = json.loads(vsc_workspace_template_content)
# %%
with open(f'{relative_path}.vscode\\{workspace_name}.code-workspace') as vsc_workspace:
    vsc_workspace_content = vsc_workspace.read()

parsed_vsc_workspace_content = json.loads(vsc_workspace_content)

# %% MERGE
for setting in parsed_vsc_workspace_template_content['settings']:
    parsed_vsc_workspace_content['settings'][setting] = parsed_vsc_workspace_template_content['settings'][setting]

parsed_vsc_workspace_content['extensions'] = parsed_vsc_workspace_template_content['extensions']


#%%
with open(f'{relative_path}.vscode\\{workspace_name}.code-workspace', 'w') as vsc_workspace_write:
    json.dump(parsed_vsc_workspace_content, vsc_workspace_write)