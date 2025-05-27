from Extract import extract_data
from Transform import *

file_path = 'Raw_data/supermarket_sales new.csv'
data = extract_data(file_path)

normalized_data = normalize_data(data)
filtered_data = filter_gender(normalized_data)
final_data = transform_unit_price_type(filtered_data)
print(final_data[:5])