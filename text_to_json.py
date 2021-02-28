import json 
import os
# the file to be converted to  
# json format 
filename = []
filename.append('./code/generations/generations_0.txt')
filename.append('./code/generations/generations_1.txt')
filename.append('./code/generations/generations_2.txt')
filename.append('./code/generations/generations_3.txt')
filename.append('./code/generations/generations_4.txt')
filename.append('./code/generations/generations_5.txt')
filename.append('./code/generations/generations_6.txt')
filename.append('./code/generations/generations_7.txt')
filename.append('./code/generations/generations_8.txt')
filename.append('./code/generations/generations_9.txt')


dict1 = {} 
i=0
os.mkdir("code/generations_test")
# creating dictionary 
for file in filename :
    text ='['
    with open(file) as fh: 
        for line in fh: 
            text = text + line+','
        text = text + "]"
    file_name_test = "code/generations_test/" + "generations_" + str(i) + ".json"
    out_file = open(file_name_test, "w") 
    json.dump(text, out_file, indent = 4, sort_keys = False) 
    out_file.close()
    i=i+1