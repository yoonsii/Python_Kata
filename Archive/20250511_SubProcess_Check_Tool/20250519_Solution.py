import subprocess
from pathlib import Path

def run_command(cmd: str) -> None:
    proc = subprocess.run(
        cmd, shell=True, capture_output=True, text=True
    )
    stdout, stderr = proc.stdout.strip(), proc.stderr.strip()
    if stdout:
        first_line = stdout.splitlines()[0]
    elif stderr:
        first_line = stderr.splitlines()[0]
    else:
        first_line = "<no output>"

    print(f"Command: {cmd}")
    print(f"Return Code: {proc.returncode}")
    print(f"Output: {first_line}\n")

def main(filename: str = "commands.txt") -> None:
    for raw in Path(filename).read_text().splitlines():
        cmd = raw.strip()
        if not cmd or cmd.startswith("#"):
            continue
        run_command(cmd)

if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "commands.txt")
