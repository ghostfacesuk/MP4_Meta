def save_mp4_as_hexadecimal(mp4_file, output_file):
    try:
        with open(mp4_file, 'rb') as file:
            data = file.read()
            hex_data = data.hex()

        with open(output_file, 'w') as file:
            file.write(hex_data)

        print("MP4 saved as hexadecimal text file successfully.")
    except Exception as e:
        print("Error: Failed to save MP4 as hexadecimal text file -", str(e))


def extract_numbers_between(file_path, start_value, end_value, output_file_path):
    vsd_record = []
    with open(file_path, 'r') as file:
        content = file.read()
        start_index = content.find(start_value)
        end_index = content.find(end_value)

        while start_index != -1 and end_index != -1:
            number = content[start_index:end_index + len(end_value)]
            vsd_record.append(number)
            start_index = content.find(start_value, end_index + len(end_value))
            end_index = content.find(end_value, start_index + len(start_value))

    with open(output_file_path, 'w') as output_file:
        if not vsd_record:
            output_file.write("No vsd meta data found!\n")
        else:
            for number in vsd_record:
                # Check the two characters after start_value
                start_chars = number[len(start_value):len(start_value) + 2]

                try:
                    start_chars_int = int(start_chars, 16)
                except ValueError:
                #    output_file.write("Invalid start_chars - cannot convert to integer.\n\n")
                    continue

                if start_chars == '00':
                    output_file.write("No entries found!\n\n")
                else:
                    output_file.write(f"{start_chars_int} - entries found!\n\n")

                if start_value in number:
                    number_with_newline = (
                        number[:len(start_value)] + ' - vsd' + '\n' +
                        number[len(start_value):len(start_value) + 2] + '\n' +
                        number[len(start_value) + 2:len(number) - len(end_value)] + '\n' +
                        number[len(number) - len(end_value):]
                    )
                else:
                    number_with_newline = (
                        number[:len(start_value)] + '\n' +
                        number[len(start_value):len(start_value) + 2] + '\n' +
                        number[len(start_value) + 2:len(number) - len(end_value)] + '\n' +
                        number[len(number) - len(end_value):]
                    )
                output_file.write(number_with_newline + '\n')

    print(f"Extracted numbers saved to '{output_file_path}'.")


# Example usage
mp4_file = 'example.mp4'
output_file = 'complete.txt'
start_value = "767364"
end_value = "66726565"
output_file_path = 'vsd_record.txt'

save_mp4_as_hexadecimal(mp4_file, output_file)
extract_numbers_between(output_file, start_value, end_value, output_file_path)
