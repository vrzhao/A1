from datetime import datetime
# using the code from the first tutorial adapted to fit the new data
from pymining import itemmining, assocrules


class freq_mining(object):
    """docstring for ClassName"""

    def __init__(self, transactions, min_sup, min_conf):
        self.transactions = transactions  # database
        self.min_sup = min_sup  # minimum support
        self.min_conf = min_conf  # minimum support

    def freq_items(self):
        relim_input = itemmining.get_relim_input(self.transactions)
        item_sets = itemmining.relim(relim_input, self.min_sup)
        return item_sets

    def association_rules(self):
        item_sets = self.freq_items()
        rules = assocrules.mine_assoc_rules(item_sets, self.min_sup, self.min_conf)
        return rules


def main(transactions, min_sup, min_conf):
    item_mining = freq_mining(transactions, min_sup, min_conf)
    freq_items = item_mining.freq_items()
    rules = item_mining.association_rules()

    print(freq_items)
    # print the frequent sets found
    print len(freq_items)
    # print the number of frequent sets found

    import csv

    # writes the frequent itemsets to a csv.
    with open('frequent_sets_relim.csv', 'wb') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(freq_items.items())


if __name__ == "__main__":
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

    min_sup = 100
    min_conf = 0
    # assignment had no specifications for min_conf so I set it to 0 to keep it in line with the FP-Growth and Apriori

    main(transactions, min_sup, min_conf)

    print datetime.now() - startTime
    # calculates and prints the run time

