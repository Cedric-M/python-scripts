import subprocess
import re

my_command=["ping", "-t", "www.google.com"]
my_process=subprocess.Popen(my_command, stdout=subprocess.PIPE, 
stderr=subprocess.PIPE)

while True:
    line = my_process.stdout.readline() #read a line - one ping in this case
    line = line.decode("utf-8") #decode the byte literal to string
    line = re.sub("(?s).*?(time=.*ms).*", "\\1", line) #find time=xxms in the string and use only that

    print(line)