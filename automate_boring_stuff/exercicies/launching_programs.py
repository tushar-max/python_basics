import subprocess

#calcProc = subprocess.Popen("C:\Windows\System32\calc.exe")

#print(calcProc.poll() == None)

#print(calcProc.wait()) # Doesn't return until paint closes

#print(calcProc.poll())

"""
While it’s still running, we check whether poll() returns None ➋. It should, as the process is still running. Then we close the MS Paint program and call wait() on the terminated process ➌. Now wait() and poll()return 0, indicating that the process terminated without errors.

If you run calc.exe on Windows 10 using subprocess.Popen(), you’ll notice that wait() instantly returns even though the calculator app is still running. This is because calc.exe launches the calculator app and then instantly closes itself.
"""

# Passing Command Line Arguments to the Popen() Function
# Ill open a note paf with the text of the second argument file
#subprocess.Popen(['C:\\Windows\\notepad.exe', 'RomeoAndJulie.txt'])

