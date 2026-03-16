import subprocess

cmd = ['ping', 'localhost', '-c', '4']

subprocess.run(
    cmd
)