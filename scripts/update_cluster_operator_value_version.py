# This is a simple script which will be called from operator actions after release in order to keep the images in values.yaml updated
#!/usr/bin/env python3

import os
import sys
import fileinput
import re

def replace_values_image_version(file_input, image, tag):
    with fileinput.FileInput(file_input, inplace=True, backup=".bak") as file:
        cond = False
        for line in file:
            if cond is True:
                line2 = "\t\ttag: " + tag + "\n"
                cond= False
                print(line2, end="")
                continue
            if image in line:
                cond = True
                print(line, end="")
                continue
            print(line, end="")
            
            
def main():

    if len(sys.argv) != 4:
	    print("This script takes 3 arguements: the values file to update, the image name and the new tag")
	    sys.exit()

    values_file_name = sys.argv[1]
    image_name = sys.argv[2]
    tag = sys.argv[3]


    replace_values_image_version(values_file_name, image_name, tag)


# start main function
if __name__ == "__main__":
    main()