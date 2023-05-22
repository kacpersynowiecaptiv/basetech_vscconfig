#%%
import glob
import json
import os
from subprocess import call
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("config")

args = parser.parse_args()

file_path = os.path.realpath(__file__).rsplit('\\', 1)[0]

if args.config == 'miau':
    call(["cp", f'{file_path}\\..\\..\\clangd_files\\compile_commands_test.json', f'{file_path}\\..\\..\\clangd_files\\compile_commands.json'])
elif args.config == 'all_no_miau':
    call(["cp", f'{file_path}\\..\\..\\clangd_files\\compile_commands_build.json', f'{file_path}\\..\\..\\clangd_files\\compile_commands.json'])