import requests
import json
import sys

# runs through entire blockchain to determine amount belonging to "user"
# this script allows user to enter, save, or change the id used
# will return the balance for that user and all transactions involving said user

if __name__ == '__main__':
    # What is the server address? IE `python3 miner.py https://server.com/api/`
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    # placeholder for balance we will calculate by running through chain
    balance = 0

    # transactions involving user
    transactions = []

    # Load ID
    # change to user input
    # f = open("my_id.txt", "r")
    # user_id = f.read()
    # print("ID is", id)
    # f.close()

    user_id = input('Please enter user id')

    blockchain = requests.get(url=node + "/chain").json()

    chain = blockchain['chain']

    for block in chain:
        for transaction in block['transactions']:
            if transaction['sender'] == user_id:
                transactions.append(transaction)
                balance -= transaction['amount']
            if transaction['recipient'] == user_id:
                transactions.append(transaction)
                balance += transaction['amount']

    if len(transactions) > 0:
        print('Total amount attributable to entered user id is ', balance)
        print('')
        print('Below are all transactions involving the user ')
        print('')
        print(json.dumps(transactions, sort_keys=True, indent=4))
    else:
        print('Balance is 0, no transactions found')
