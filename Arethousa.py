#Merge and join 
import csv
curriculum = '/Users/amacgown/Desktop/gamma/curricula_subcurricula.csv'
items = '/Users/amacgown/Desktop/gamma/items_curricula.csv'

with open(curriculum) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)