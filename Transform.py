from Extract import extract_data

data = extract_data('Raw_data/supermarket_sales new.csv')

#Transformation dataset

def normalitation_data(data):
    '''
    Normalize the data by converting all string values to lowercase and removing any leading/trailing whitespace.
    '''
    normalized_data = []
    for row in data:
        normalized_row = [item.strip().lower().replace(' ', '_') for item in row if isinstance(item, str)]
        normalized_data.append(normalized_row)
    headers = normalized_data[0]
    rows = normalized_data[1:]
    transformed_data = [dict(zip(headers, row)) for row in rows]

    return transformed_data

def filter_gender(data, gender='male'):
    '''
    Filter the data by gender.
    '''
    filtered_data = [item for item in data if item['gender'] == gender]
    return filtered_data

def transform_type(data, type_column , colunm_name):
    '''
    Transform the data based on a specific column type.
    '''
    transform = list(map(lambda x: type_column(x[colunm_name]),  data))
    return transform


print(transform_type(normalitation_data(data), float, 'unit_price'))
transformed_data = normalitation_data(data)


print(transformed_data[:5])


