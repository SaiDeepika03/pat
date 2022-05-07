import os
import re


m=0

dir = os.getcwd()


for path,directory,files in os.walk(dir):

    for name in files:

        count=0

        a = re.findall(".test.",name)

        if(a):

            m=m+1

            if (name.endswith(".py")):

                file_path = path+"\\"+name

                f = open(file_path,'r+')

                for line in f.readlines():

                   if (re.findall(".assert.",line)):


                        count=count+1

                print(name,",",count)


print("test files:",m)
