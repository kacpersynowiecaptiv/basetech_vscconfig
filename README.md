# basetech_vscconfig
```*WARNING! Currently the documentation is a draft version!```

Configuration (tasks, scripts, etc) for daily basis work with Visual Studio Code and Renesans project. Includes configuration of clangd for VSC. Short instruction:

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
4. Now the directory structure (on top level) should look like below:
```
.
├── basetech_vscconfig
├── clangd_files
└── msw
```
* basetech_vscconfig -> this repo
* clangd_files -> configuration for clangd, compile_commands.json
* msw -> project repo
5. Install recommended extensions.
6. Install clangd by following the instructions from clangd extension (https://github.com/clangd/vscode-clangd). The extension should automatically redirect to clangd tool installation, follow the default settings. Set clangd as default provider, instead of IntelliCode.
7. Install compiledb tool (https://github.com/nickdiego/compiledb), and add it to the PATH
```
pip install compiledb
```
8. In msw repo (open it as workspace, from msw\.vscode\"workspace_name".code-workspace) run "generate configuration" task (Terminal -> Run Task..).

## Working with code, tasks

Now, after successful instalation of the basetech_vscconfig it should be possible to take full advantage of the clangd and vsc tasks. Short description of the prepared tasks (they should be visible on the bottom bar):
* **Build** - make project, run compilation and produce hex file,
* **Clean build** - make clean,
* **Re-build** - make clean, and then make project,
* **Test** - build and run test suites specified in project_settings.json ("test_inputs"."testModules" property - default all),
* **Program** - program the board with produced hex (programmer_path, programmer_configuration_path, hex_filename parameters needed),
* **Build and program** - run **Build**, and then **Program**,
* **Test selected test suite** - run one of the test suites, specified in Makefile.modules.mk,
* **Copy to bench** - copy out directory to remote pc, path specified in project_settings.json,
* **generate clangd config** or **generate compile_commands.json** - run generate_compile_commands.py to recreate clangd configuration, should be exectuted after adding a new component, or source file to the project,
* **switch clangd config** - there are two compile_commands.json for the project. By default it is created from standard make command and follows the source code. But we can switch to unit test framework, with stubs and fff as the source of clangd features.

Enjoy (づ｡◕‿‿◕｡)づ 
