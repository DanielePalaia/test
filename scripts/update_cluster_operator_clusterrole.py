# This is a simple script which will be called from operator actions after release in order to keep the clusterrole updated

#!/usr/bin/env python3
import fileinput
import sys
import logging

def read_clusterrole_def_file(filename):
	with fileinput.FileInput(filename) as file:
		security_role = ""
		found = False
		for line in file:
			if "apiGroups" not in line and found is False:
				continue
        
			found = True
			security_role = security_role + line
	
	security_role = security_role + "  {{- end }}\n"
	security_role = security_role + "{{- end }}\n"

	return security_role


def main():

	if len(sys.argv) != 3:
		print("This script takes 2 arguements: The cluster operator role file and the helm clusterrole file to update")
		sys.exit()

	operator_role_filename = sys.argv[1]
	helm_clusterrole_filename = sys.argv[2]

	helm_clusterrole_file = open(helm_clusterrole_filename, 'a')

	updated_security_role = read_clusterrole_def_file(filename=operator_role_filename)

	helm_clusterrole_file.write(updated_security_role)
	helm_clusterrole_file.close()


# start main function
if __name__ == "__main__":
    main()

