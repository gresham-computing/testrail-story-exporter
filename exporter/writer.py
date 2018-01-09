import csv


def write_to_csv(filename, data):
    # Assume that these dicts all have the same shape
    headers = data[0].keys()
    with open(filename, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, headers)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    return {
        'num_records': len(data),
        'output_filename': filename
    }
