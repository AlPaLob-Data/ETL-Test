from Extract import extract_data

# Cargar los datos desde el archivo CSV
data = extract_data('Raw_data/supermarket_sales new.csv')

def normalize_data(data):
    '''
    Normalize the data by converting all string values to lowercase and removing any leading/trailing whitespace.
    Also, convert the entire dataset into a list of dictionaries for easier manipulation.
    '''
    normalized_data = []
    headers = [item.strip().lower().replace(' ', '_') for item in data[0]]
    for row in data[1:]:
        normalized_row = {headers[i]: value.strip().lower().replace(' ', '_') if isinstance(value, str) else value
for i, value in enumerate(row)}
        normalized_data.append(normalized_row)

    return normalized_data

def filter_gender(data, gender='male'):
    '''
    Filter the data by gender.
    '''
    filtered_data = [item for item in data if item['gender'] == gender.lower()]
    return filtered_data

def transform_unit_price_type(data):
    '''
    Transform the unit_price column to float type.
    '''
    transformed_data = []
    for row in data:
        try:
            row['unit_price'] = float(row['unit_price'])
        except ValueError as e:
            print(f"Error converting unit_price: {row['unit_price']} - {e}")
            continue
        transformed_data.append(row)

    return transformed_data

# Apply transformations
normalized_data = normalize_data(data)
filtered_data = filter_gender(normalized_data)
final_data = transform_unit_price_type(filtered_data)

# Mostrar los primeros 5 registros del dataset final
print(final_data)


