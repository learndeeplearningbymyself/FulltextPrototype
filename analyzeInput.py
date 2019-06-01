import subprocess, shlex

def get_output_of(command):
	args = shlex.split(command)
	return subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]
 
file_name = "data.txt"

phrase_mining_cmd = "python runPhraseMining.py {0}".format(file_name)
print(get_output_of(phrase_mining_cmd))
