import csv

with open('frequent_sets_fp.csv', 'rb') as myfile:
    rb = csv.reader(myfile, delimiter = ",")
    for row in rb:
        frequent_sets = row

with open('frequent_sets_Apr.csv', 'rb') as myfile:
    rb = csv.reader(myfile, delimiter = ",")
    for row in rb:
        frequent_sets_apr = row

with open('closed_sets.csv', 'rb') as myfile:
    rb = csv.reader(myfile, delimiter = ",")
    for row in rb:
        close_sets = row

with open('Maximum_sets.csv', 'rb') as myfile:
    rb = csv.reader(myfile, delimiter=",")
    for row in rb:
        Max_sets = row

print len(frequent_sets)/2
print len(frequent_sets_apr)
print len(close_sets)
print len(Max_sets)

