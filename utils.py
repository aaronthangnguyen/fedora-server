import subprocess


def run_command(command):
    """Run a shell command and return its output."""
    try:
        result = subprocess.run(
            command, shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr}")
        return None
