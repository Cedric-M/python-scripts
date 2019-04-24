import subprocess

my_command="ping www.google.com"
my_process=subprocess.Popen(my_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

result, error = my_process.communicate()
result = result.strip()
error = error.strip()

print ("\nResult of ping command\n")
print("-" *22)
print(result.decode('utf-8'))
print(error.decode('utf-8'))
print("-" *22)
input("Press Enter to finish...")