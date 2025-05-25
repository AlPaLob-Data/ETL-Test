import csv

def extract_data(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def extract_category(data):
    return set(item['Product line'] for item in data)

if __name__ == "__main__":
    file_path = 'Raw_data/supermarket_sales new.csv'
    data = extract_data(file_path)
    categories = extract_category(data)
