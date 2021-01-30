from py_compile import compile
from glob import glob
from shutil import move

compile("src/server.py")
bytecode = glob("src/__pycache__/*.pyc")[0]
move(bytecode, "app")