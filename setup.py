import subprocess, sys, os
import getpass
from pathlib import Path

sys.path.append('/usr/lib/python3/dist-packages/')

# Set initial variables

sudo_password = getpass.getpass(prompt='sudo password: ')
current_user = getpass.getuser()
home_dir = Path.home()


# Define functions
def install_package(p):
    try:
        out, err = p.communicate(input=(sudo_password+'\n').encod(),timeout=5)
    except subprocess.TimeoutExpired:
        p.kill()

# Create venv for ansible

os.mkdir(f"${home_dir}.deployment", mode=0o750,*,dir_fd = None)

subprocess.run(['python3','-m','venv','~/.deployment/.venv/'])

# Activate venv for ansible

subprocess.run(['source','~/.deployment/.venv/bin/activate'])

subprocess.run(['pip','install','ansible'])

# try:
#     # Attempt to import the apt module
#     import apt
# except ImportError:
#     p = subprocess.Popen(['["sudo", "apt", "update"]'], stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

#     install_package(p)
#     # subprocess.run(["sudo", "apt", "update"])
#     # subprocess.run(["sudo", "apt", "install", "-y", "python3-apt"])
#     import apt

# cache = apt.cache.Cache()
# cache.update()

# # if cache['python3-venv'].is_installed:
# #     print('"python3-venv" already installed.')
# # else:
# #     subprocess.run(["sudo", "apt", "install", "-y", "python3-vevn", check=True])
# #     if cache['python3-venv'].is_installed:
# #         print('"python3-venv"' installed successfully.)

# # subprocess.run(["pip", "install", "ansible"])