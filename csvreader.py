import csv
with open('example.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    str1 = ','.join([str(i) for i in your_list])
print str1
