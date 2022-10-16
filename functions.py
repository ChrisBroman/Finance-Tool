from classes import *
from pathlib import Path
import pickle
from tabulate import tabulate
import sys

def parse_file(input_file):
    if input_file[-4:] != '.csv':
        raise Exception('Must be a csv file')
    with open(input_file, 'r') as file:
        loaded = file.read()
    array = loaded.split('\n')
    if array[-1] == '':
        del array[-1]
    transactions = []
    for item in array:
        transactions.append(item.split(','))
    for item in transactions:
        if len(item) > 3:
            del item[2]
    for item in transactions:
        if float(item[2]) > 0:
            transactions.remove(item)
    for item in transactions:
        item[2] = abs(float(item[2]))
    return transactions


def process_file(input_file):
    banking_data = []
    for item in input_file:
      banking_data.append(Transaction(item))
    return banking_data

def check_file():
    banking_data = []
    path = Path("banking.data")
    if path.is_file() == 0:
        with open('banking.data', 'wb') as file:
            pickle.dump(banking_data, file)

def load_file():
    with open('banking.data', 'rb') as file:
        banking_data = pickle.load(file)
    return banking_data

def save_file(banking_data):
    with open('banking.data', 'wb') as file:
        pickle.dump(banking_data, file)

def append_file(new_data):
    banking_data = load_file()
    banking_data += new_data
    save_file(banking_data)

def update_file():
    input_file = input("Please enter the csv file: ")
    parsed_file = parse_file(input_file)
    processed_file = process_file(parsed_file)
    append_file(processed_file)

def get_total_spending(banking_data):
    total = 0
    for item in banking_data:
        total += float(item.get_amount())
    print(round(total, 2))

def get_total_of(search, banking_data):
    total = 0
    for item in banking_data:
        if item.get_name().__contains__(search.lower()) or item.get_name().__contains__(search.upper()):
            total += float(item.get_amount())
    print(round(total, 2))

def list_transactions(banking_data):
    headers = ['ID', 'Date', 'Name', 'Amount']
    transaction_items = []
    for item in banking_data:
        transac = []
        transac.append(item.get_date())
        transac.append(item.get_name())
        transac.append(round(float(item.get_amount()),2))
        transaction_items.append(transac)
    print(tabulate(transaction_items, headers, tablefmt='simple'))

def list_transactions_of(search, banking_data):
    headers = ['ID', 'Date', 'Name', 'Amount']
    filtered_transactions = []
    total = 0
    for item in banking_data:
        if item.get_name().__contains__(search.lower()) or item.get_name().__contains__(search.upper()):
            transac = []
            transac.append(item.get_date())
            transac.append(item.get_name())
            transac.append(float(item.get_amount()))
            filtered_transactions.append(transac)
            total += float(item.get_amount())
    print(tabulate(filtered_transactions, headers, tablefmt='simple'))
    print("\nTotal expense: ${}".format(round(total, 2)))

def list_by_date(month, year, banking_data):
    year_transactions = []
    month_transactions = []

    for item in banking_data:
        date = item.get_date().split('/')
        if date[2] == str(year):
            year_transactions.append(item)

    for item in year_transactions:
        date = item.get_date().split('/')
        if date[0] == str(month):
            month_transactions.append(item)

    total = 0
    transactions = []
    for item in month_transactions:
        transac = []
        transac.append(item.get_id())
        transac.append(item.get_date())
        transac.append(item.get_name())
        transac.append(round(float(item.get_amount()),2))
        transactions.append(transac)
        total += float(item.get_amount())

    print()
    headers = ["ID", "Date", "Name", "Amount"]
    print(tabulate(transactions, headers, tablefmt='simple'))
    print("\nTotal Expenses are ${}\n".format(round(float(total), 2)))

def statistics(banking_data):
    latest_year = 0
    for item in banking_data:
        date = item.get_date().split('/')
        if int(date[2]) > latest_year:
            latest_year = int(date[2])
    print('latest year: {}'.format(latest_year))

    temp_array = []
    temp_array.append(latest_year)
    earliest_year = temp_array[0]

    for item in banking_data:
        date = item.get_date().split('/')
        if earliest_year <= int(date[2]):
            earliest_year = int(date[2]) 

    print('earliest year: {}'.format(earliest_year))

    ##########  Testing  ####################
    if earliest_year == latest_year:
        year_range = [latest_year]
    else:
        year_range = [*range(earliest_year, latest_year, 1)]
    print('year range: {}'.format(year_range))
    for year in year_range:
        months = [*range(1,13,1)]
        year_total = 0
        for item in banking_data:
            date = item.get_date().split('/')
            if str(year) == date[2]:
                year_total += float(item.get_amount())
        print('Total spent in {}: ${}\n'.format(year, round(float(year_total)), 2))
        print(months)



def analyse_file():
    banking_data = load_file()
    print('Please select one of the following options:\n')
    print('1. Get total spending')
    print('2. Get total spending from specific place')
    print('3. List all transactions')
    print('4. List all transactions from specific place')
    print('5. List transactions by date')
    print('6. Statistics Page')
    print('\n7. Back\n')
    selection = input('>> ')
    print()

    if selection == '1':
        get_total_spending(banking_data)
    elif selection == '2':
        store = input("Enter the search term: ")
        get_total_of(store, banking_data)
    elif selection == '3':
        list_transactions(banking_data)
    elif selection == '4':
        store = input("Enter the search term: ")
        list_transactions_of(store, banking_data)
    elif selection == '5':
        year = input('Please enter the year (YYYY): ')
        month = input('Please enter the month (M): ')
        list_by_date(month, year, banking_data)
    elif selection == '6':
        statistics(banking_data)
    elif selection == '7':
        return
    else:
        raise Exception('Not a valid answer')
