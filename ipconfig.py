from subprocess import PIPE, run

my_command = "["ipconfig", "/all"]"
result = run(my_command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
print(result.stdout, result.stderr)
input("Press Enter to finish...")