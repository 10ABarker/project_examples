# this script will read .csv files located in a file directory
# then go through the files and check the number of lines
# it will then look at the parity column for "in AG?" and count the number of N's
# if the number of N's matches the number of lines present
# the monitor name will be outputted to a file

import os
import csv
import glob

userPath = input("Enter in the path to the .csv files: ")


filesInPath = glob.glob(os.path.join(userPath, '*.csv'))
f = open("monitorOutput.txt", 'w') 
for file in filesInPath:
    if file.startswith("consolidated-"):
        print("reading file: " + file)
        inAGCol = []
        totalSumOfRows = 0
        totalSumOfNs = 0
        with open(file, newline='', encoding='utf-8-sig') as fileObject:
            reader_Obj = csv.DictReader(fileObject)
            for row in reader_Obj:
                totalSumOfRows = totalSumOfRows+1
                inAGCol.append(row['In AG?'])
            for n in inAGCol:
                if n == 'N':
                    totalSumOfNs = totalSumOfNs+1
            if totalSumOfNs == totalSumOfRows:
                f.write(file)
            else:
                continue
f.close()
print("Output file is printed in working directory: ", os.getcwd())


