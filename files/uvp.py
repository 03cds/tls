import os
import re
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

folder = filedialog.askdirectory(title="select game folder")

if not folder:
    print("no folder selected")
    input("press  enter to exit")
    exit()

target = None

for root_dir, dirs, files in os.walk(folder):
    if "unity default resources" in files:
        target = os.path.join(root_dir, "unity default resources")
        break

if not target:
    print("unity file not found")
    input("enter to exit")
    exit()

with open(target, "rb") as f:
    data = f.read()

match = re.search(rb"\d{4,5}\.\d+\.\d+[abfcp]\d+", data)

if match:
    print("unity version:", match.group().decode())
else:
    print("version not found")

input("enter to close")