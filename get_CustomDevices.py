# This script gets exececuted when `pio run -e mobiflight_mega` is run.

import subprocess
import os

Import("env")

CUSTOMDEVICES_DIR = env.subst("$PROJECT_DIR/CustomDevices")
CUSTOMDEVICES_TAG = "main"

def run_command(command):
    # Break the command into parts using a list
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing command: {stderr.decode()}")
        env.Exit(1)
    else:
        print(stdout.decode())

if not os.path.exists(CUSTOMDEVICES_DIR):
    print("Cloning Mobiflight-CustomDevices repo ...")
    run_command([
        "git", "clone", "--depth", "100",
        "--branch", CUSTOMDEVICES_TAG,
        "https://github.com/Kav-Simulations/MobiFlight-CustomDevices",
        CUSTOMDEVICES_DIR
    ])
else:
    print("Checking for Mobiflight-CustomDevices repo updates ...")
    os.chdir(CUSTOMDEVICES_DIR)
    run_command([
        "git", "pull", "origin", CUSTOMDEVICES_TAG,
        "--depth", "100"
    ])