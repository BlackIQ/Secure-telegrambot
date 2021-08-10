import sys
import os

version = sys.argv[1]
name = sys.argv[2]

os.system(f"fandogh image publish --version v{version}")
os.system(f"fandogh service deploy --version v{version} --image {name} --name {name}")