import os
import re

dir = os.getcwd()

for path, directory, files in os.walk(dir):

    for name in files:

        count=0

        a = re.findall(".test.",name)


        if(not a):

            if (name.endswith(".py")):

                file_path = path + "\\" + name

                f = open(file_path, 'r+',encoding='UTF8')

                for l in f.readlines():

                   if (re.findall(".assert.", l)):

                        count=count+1

                print(file_path,",",name,",",count)