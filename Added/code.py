firstfile = 'final_sunmission/generations_11.txt'

for i in range (1,5):
        
    cc = i+7
    secondfile = "generations1306_7th/generations_" + str(i) + ".txt"
    # opening first file in append mode and second file in read mode 
    f1 = open(firstfile, 'a+') 
    f2 = open(secondfile, 'r') 
    
    # appending the contents of the second file to the first file 
    f1.write("generation " + str(cc) + "\n\n")
    f1.write(f2.read()) 
    f1.write("\n===========================================================>\n\n")
    # relocating the cursor of the files at the beginning 
    f1.seek(0) 
    f2.seek(0) 
    
    f2.close() 
# closing the files 
f1.close()