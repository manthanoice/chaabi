def get_file_types(extension_type_string, file_names):
    extension_type_pairs = extension_type_string.split(';')
    extension_to_type = {}
    for pair in extension_type_pairs:
        extension, file_type = pair.split(',')
        extension_to_type[extension] = file_type

    file_type_dict = {}
    for file_name in file_names:
        extension = file_name.split('.')[-1]
        if extension in extension_to_type:
            file_type = extension_to_type[extension]
        else:
            file_type = "unknown"
        file_type_dict[file_name] = file_type

    return file_type_dict

extension_type_string = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
file_names = ["abc.jpg", "xyz.xls", "text.csv", "123"]
file_type_dict = get_file_types(extension_type_string, file_names)
print(file_type_dict)