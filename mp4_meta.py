def extract_numbers_between(file_path, start_value, end_value, output_file_path):
    extracted_numbers = []
    with open(file_path, 'r') as file:
        content = file.read()
        start_index = content.find(start_value)
        end_index = content.find(end_value)

        while start_index != -1 and end_index != -1:
            number = content[start_index + len(start_value):end_index]
            extracted_numbers.append(number)
            start_index = content.find(start_value, end_index + len(end_value))
            end_index = content.find(end_value, start_index + len(start_value))

    with open(output_file_path, 'w') as output_file:
        for number in extracted_numbers:
            output_file.write(number + '\n')

    print(f"Extracted numbers saved to '{output_file_path}'.")


# Usage example
file_path = 'your_file.txt'
start_value = "767364"
end_value = "66726565"
output_file_path = 'extracted_numbers.txt'

extract_numbers_between(file_path, start_value, end_value, output_file_path)
