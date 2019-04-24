import subprocess

my_command=["ping", "-t", "www.google.com"]
my_process=subprocess.Popen(my_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
    print( my_process.stdout.readline() )