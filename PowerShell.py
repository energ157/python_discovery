import subprocess

def Powershell_execution(command):
    output = subprocess.run(["powershell", "-Command",command],
    capture_output = True,
    text = True,
    creationflags = subprocess.CREATE_NO_WINDOW
    )

    return output.stdout
