#%%
import glob
import json
import os

file_path = os.path.realpath(__file__).rsplit('\\', 1)[0]
# %%
exe_files_list = glob.glob(f'{file_path}\\..\\Test\\out\\bin\\*.exe')
test_path_str = '${workspaceFolder}\\Test\\out\\bin\\'
suite_names = [x.split('\\')[-1].split('.exe')[0] for x in exe_files_list]
#%%
with open(f'{file_path}\\launch_template.json') as launch_template:
    content = launch_template.read()
with open(f'{file_path}\\project_settings.json') as launch_template:
    settings = launch_template.read()
# %%
parsed_json = json.loads(content)
parsed_settings = json.loads(settings)
# %%
configurations = parsed_json['configurations']
configurations[0]['miDebuggerPath'] = parsed_settings['general']['gdb_path']
# %%
multiple_configurations = [configurations[0] for i in range(len(suite_names))]
# %%
updated_configurations = [{**config, "name": suite_name, 'program': f'{test_path_str}{suite_name}.exe'} for config, suite_name in zip(multiple_configurations, suite_names)]
# %%
with open(f'{file_path}\\launch.json', 'w') as f:
    json.dump({"version": parsed_json['version'], "configurations": updated_configurations}, f)
