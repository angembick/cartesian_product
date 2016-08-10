import subprocess
import cartesian_products


input_var = raw_input("Enter a string of sets (eg {a,b}{c,d} ) : ")
print ("you entered " + input_var)

cmd = 'echo ' + input_var 
bash_result = " ".join(cartesian_products.flatten_string_to_list(input_var))
code_result = subprocess.check_output('echo '+ input_var, shell=True)[:-1]

print "code generated product: " + code_result
print "bash generated product: " + bash_result

if bash_result == code_result:
  print "The code correctly replicated the Bash shells output"
else:
  print "The code failed to replicate the exact same output as the Bash shell"