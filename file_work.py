import csv
with open("file.txt", 'w') as file:
    for i in range(10):
        file.write(str(i))
        file.write('\n')

with open("file.csv", 'w') as f:
    writer = csv.writer(f)
    for i in range(10):
        writer.wr
        
        
        
        

