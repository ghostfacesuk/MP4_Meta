def extract_numbers_between(file_path, start_value, end_value, output_file_path):
    extracted_numbers = []
    with open(file_path, 'r') as file:
        content = file.read()
        start_index = content.find(start_value)
        end_index = content.find(end_value)

        while start_index != -1 and end_index != -1:
            number = content[start_index:end_index + len(end_value)]
            extracted_numbers.append(number)
            start_index = content.find(start_value, end_index + len(end_value))
            end_index = content.find(end_value, start_index + len(start_value))

    with open(output_file_path, 'w') as output_file:
        for number in extracted_numbers:
            if start_value in number:
                number_with_newline = number[:len(start_value)] + ' - vsd' + '\n' + number[len(start_value):len(start_value) + 2] + '\n' + number[len(start_value) + 2:len(number) - len(end_value)] + '\n' + number[len(number) - len(end_value):]
            else:
                number_with_newline = number[:len(start_value)] + '\n' + number[len(start_value):len(start_value) + 2] + '\n' + number[len(start_value) + 2:len(number) - len(end_value)] + '\n' + number[len(number) - len(end_value):]
            output_file.write(number_with_newline + '\n')

    print(f"Extracted numbers saved to '{output_file_path}'.")


# Usage example
file_path = 'your_file.txt'
start_value = "767364"
end_value = "66726565"
output_file_path = 'extracted_numbers.txt'

extract_numbers_between(file_path, start_value, end_value, output_file_path)

