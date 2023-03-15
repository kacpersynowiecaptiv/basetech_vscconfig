# basetech_vscconfig
Configuration (tasks, scripts, etc) for daily basis work with Visual Studio Code and Renesans project. Short instruction:

1. Clone this repo under the same directory as msw repository.
2. Provide proper parameters to .vscode\project_settings.json (create file from project_settings_example.json), especially the general settings:
    - "workspace_name" -> name of the workspace,
    - "gdb_path" -> path to the gdb debugger (for unit test purposes),
    - "remote_build_path" -> path to the bench mapped drive (for the output build),
    - "programmer_path" -> path to the Renesans Flash Programmer,
    - "programmer_configuration_path" -> path to the programmer configuration file,
    - "hex_filename" -> name of the produced hex file,
    - "msw_relative_path" -> relative path to the msw directory from .vscode point of view
3. Run `python generate_workspace.py`
4. Intstall recommended extensions.

Enjoy (づ｡◕‿‿◕｡)づ 