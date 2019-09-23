# Program: genShadowpy
# Date: 19.09.23
# Develop: Neva

# Import Module
import subprocess

# Basic Variables
PASSWD_FN = "passwd.txt"
SHADOW_FN = "shadow.txt"

# Basic Functions
def genShadow(data, shadow_fn):
    f = open(shadow_fn,'w')
    for line in data:
        if line == "": continue
        command = ["mkpasswd",line]
        res = subprocess.check_output(command, stderr=subprocess.STDOUT)
        f.write(res)
    f.close()

# Main functions
def main():
    f = open(PASSWD_FN,'r')
    data = f.read().split('\n')
    f.close()
    genShadow(data, SHADOW_FN)

if __name__ == "__main__":
    main()
