import subprocess
command="uvicorn main:app --reload --port 5000"
subprocess.run(command.split())