from datetime import datetime
startTime = datetime.now()

# contains function checks to see if an item or a list of items is inside a given list.
# returns true if items are present and false otherwise.
def contains(list, item):
    z = 0
    for x in range(0, len(item)):
        for y in range(0, len(list)):
            if (item[x] == list[y]) :
                z += 1
                break
    if (z == len(item)):
        return True
    return False

# function checks to see if the support values of two lists are the same.
# returns false if the supports equal and true otherwise
def check_support(a, b):
    if (a == b):
        return True
    return False

# function compares the length of two lists.
# returns true if the list length is the length of the item plus one and false otherwise.
def check_k_plus_1(list, item):
    if (len(list) == len(item) + 1):
        return True
    return False

# creates two lists to hold the closed and maximum item sets
closed_itemsets = []
maximum_itemsets = []

# function takes an list of frequent item sets as input and puts the closed and maximum itemsets in their respective lists
def check_closed_max (itemset):
    for x in range(1, len(itemset), 2):
        has_super = False
        same_support = False
        for y in range(1, len(itemset), 2):
            if (check_k_plus_1(itemset[y],itemset[x])):
                # checks if the length of itemset[y] is the length of the itemset[x] plus one
                # if it length is k+1 than we need to check if it is a superset, otherwise we skip it.
                if(contains(itemset[y],itemset[x])):
                    # check to see if itemset[y] is a superset of itemset[x]
                    has_super = True
                    if(check_support(itemset[y-1],itemset[x-1])):
                        # compares the support of itemset[y] and itemset[x]
                        # if the supports are equal, itemset[x] is not closed.
                        same_support = True
                        break

        if(has_super == False):
            # if a item set has no frequent super set than it must be closed and maximum.
            closed_itemsets.append(itemset[x])
            maximum_itemsets.append(itemset[x])
        if(has_super == True and same_support == False):
            closed_itemsets.append(itemset[x])

# uses the code writen in A1_vrzhao_20233835_code_fp to generate the frequent item sets.

# creating 2 lists that will hold the formatted dataset
transactions = []
transaction = []

# Opening the dataset and formatting it
with open('freq_items_dataset.txt', 'r') as f:
    for line in f:
        items = line.split()
        # pulling a single line or transaction and putting it in items using spaces a delimiters
        for item in items:
            transaction.append(item)
            # appending each item in items to the list transactions to from a list of items in a single transaction
        transactions.append(transaction)
        # appends each transaction into transactions forming a list of lists
        transaction = []
        # resetting the value of transactions

from fp_growth import find_frequent_itemsets
# importing the fp-tree library

frequent_sets = []

for itemset in find_frequent_itemsets(transactions, 100, include_support=True):
    # running creating an item set that satisfied a min-sup of 100 from our transaction list
    frequent_sets.append(itemset[1])
    # appends the amount of support an itemset has to the list frequency_sets
    frequent_sets.append(itemset[0])
    # appends the itemset to the list frequent_sets

# runs the function that checks for closed and maximum itemsets using the frequent itemset we just mined.
check_closed_max(frequent_sets)

# prints the closed and maximum itemsets
print "Closed Item Sets" + '\n'
print closed_itemsets
print "Maximum Item Sets" + '\n'
print maximum_itemsets

print datetime.now() - startTime
# calculates and prints the run time

print len(closed_itemsets)
print len(maximum_itemsets)
# print the amount of closed and maximum itemsets found

import csv

# writes the closed itemsets to a csv.
with open('closed_sets.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
    wr.writerow(closed_itemsets)

# writes the maximum itemsets to a csv.
with open('Maximum_sets.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
    wr.writerow(maximum_itemsets)

