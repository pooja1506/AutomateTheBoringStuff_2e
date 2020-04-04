import subprocess
paintProc = subprocess.Popen('c:\\Windows\\System32\\mspaint.exe')
paintProc.poll() == None
paintProc.wait() # Doesn't return until MS Paint closes.
paintProc.poll()