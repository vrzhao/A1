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

import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
# imports pandas and mlxtend


oht = OnehotTransactions()
oht_ary = oht.fit(transactions).transform(transactions)
df = pd.DataFrame(oht_ary, columns=oht.columns_)
# transforms our list of lists into a sparse dataframe with dimensions 100000 by 1000

from mlxtend.frequent_patterns import apriori

frequent_sets = apriori(df, min_support=0.006, use_colnames=True)
print frequent_sets
# imports the apriori algorithm and runs checking for min-support of 0.006 or 0.6%
# displays all itemsets with a support greater than or equal to 0.6% of the 100000 transactions (600)

print len(frequent_sets.index)
# prints the number of frequent itemsets found

print datetime.now() - startTime
# calculates and prints the run time

# writes the frequent itemsets to a csv file.
frequent_sets.to_csv("frequent_sets_Apr.csv")
