import csv


def write_to_csv(filename, data):
    """Write a list of dictionaries to a CSV file.

    It is assumes that the dicts all have the same shape, if they don't only
    the shape of the first dict in the list is used."""
    headers = data[0].keys()
    with open(filename, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, headers)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    return {
        'num_records': len(data),
        'output_filename': filename
    }
