from datetime import datetime
startTime = datetime.now()

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

print frequent_sets
# prints the frequent sets, items in the list with odd indexes are the itemsets that are frequent
# the index of a frequent itemset minus 1 is the support for that itemset.
# the csv file is formatted with k and k+1 indexes being support and itemset pairs to make finding the closed and maximum sets easier.

print len(frequent_sets)/2
# print the number of frequent sets found

print datetime.now() - startTime
# calculates and prints the run time

import csv

# writes the frequent itemsets to a csv.
with open('frequent_sets_fp.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
    wr.writerow(frequent_sets)


