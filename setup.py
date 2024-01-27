import subprocess, sys

sys.path.append('/usr/lib/python3/dist-packages/')

try:
    # Attempt to import the apt module
    import apt
except ImportError:
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "-y", "python3-apt"])
    import apt

cache = apt.cache.Cache()
cache.update()

subprocess.run(["pip", "install", "ansible"])