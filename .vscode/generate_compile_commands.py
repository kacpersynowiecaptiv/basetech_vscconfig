#%%
import json
import os
from subprocess import call

file_path = os.path.realpath(__file__).rsplit('\\', 1)[0]

#%%
with open(f'{file_path}\\project_settings.json') as launch_template:
    settings = launch_template.read()
# %%
parsed_settings = json.loads(settings)
# %%
workspace_name = parsed_settings['general']['workspace_name']
compilation_path = f"{file_path}\\..\\{parsed_settings['general']['msw_relative_path']}"
real_path = file_path.split('.vscode')[0]
clangd_tool_path = f'{real_path}..\\clangd_files\\'

#%%
import re

rep = {
    "/cygdrive/c/ghs/comp_201815//ccrh850.exe": "clang -D__CHAR_BIT=8 -D__SHRT_BIT=16 -D__INT_BIT=32 -D__LONG_BIT=64 -D_SIZE_T",
    "/cygdrive/c": "C:",
    "-c99": "-std=c99",
    "-cpu=rh850g3kh": "-mcpu=rh850g3kh",
    "-needprototype": "",
    "--no_commons": "",
    "-noobj": "",
    "-pragma_asm_inline": "",
    "--long_long": "",
    "-fsoft": "",
    "-registermode=32": "",
    "-Osize": "",
    "--no_wrap_diagnostics": "",
    "-preprocess_assembly_files": "",
    "-fpu": "-mfpu",
    "-fsingle": "",
    "-floatsingle": "",
    "-time64": "",
}

rep = dict((re.escape(k), v) for k, v in rep.items()) 
pattern = re.compile("|".join(rep.keys()))

#%% Call make (all_no_miau) and save output to further processing
with open(f'{clangd_tool_path}compilelog_unparsed.log', 'w') as compile_log:
    call(["make", '-C', f'{compilation_path}', 'all_no_miau', '-Bnwk'], stdout=compile_log)

compile_raw = []

with open(f'{clangd_tool_path}compilelog_unparsed.log', 'r') as compile_log:
    text = compile_log.read()
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
#%%
with open(f'{clangd_tool_path}compilelog_parsed.log', 'w') as compile_log:
    compile_log.write(text)
# %%
call(["compiledb", '--parse', f'{clangd_tool_path}compilelog_parsed.log'])
call(["cp", 'compile_commands.json', f'{clangd_tool_path}'])
call(["mv", 'compile_commands.json', f'{clangd_tool_path}\\compile_commands_build.json'])

## UNIT TEST FRAMEWORK
rep_test = {
    "/usr/bin/gcc": "gcc",
    "/cygdrive/c": "C:",
    "\\": "/",
    "-c99": "-std=c99",
    "-cpu=rh850g3kh": "-mcpu=rh850g3kh",
    "-needprototype": "",
    "--no_commons": "",
    "-noobj": "",
    "-pragma_asm_inline": "",
    "--long_long": "",
    "-fsoft": "",
    "-registermode=32": "",
    "-Osize": "",
    "--no_wrap_diagnostics": "",
    "-preprocess_assembly_files": "",
    "-fpu": "-mfpu",
    "-fsingle": "",
    "-floatsingle": "",
    "-time64": "",
}

rep_test = dict((re.escape(k), v) for k, v in rep_test.items()) 
pattern = re.compile("|".join(rep_test.keys()))
#%%
with open(f'{clangd_tool_path}compilelog_unparsed_test.log', 'w') as compile_log:
    call(["make", '-C', f'{compilation_path}', 'miau', '-Bnwk'], stdout=compile_log)

compile_raw = []

with open(f'{clangd_tool_path}compilelog_unparsed_test.log', 'r') as compile_log:
    text = compile_log.read()
    text = pattern.sub(lambda m: rep_test[re.escape(m.group(0))], text)
#%%
with open(f'{clangd_tool_path}compilelog_parsed_test.log', 'w') as compile_log:
    compile_log.write(text)
# %%
call(["compiledb", '--parse', f'{clangd_tool_path}compilelog_parsed_test.log'])
call(["mv", 'compile_commands.json', f'{clangd_tool_path}\\compile_commands_test.json'])