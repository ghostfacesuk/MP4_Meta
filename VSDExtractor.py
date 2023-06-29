#print("About to import tkinter as tk")
import tkinter as tk
#input("About to import ttk from tkinter")
from tkinter import ttk
#File opening interface?
root = tk.Tk()
root.withdraw() #Keep the root window from appearing
from tkinter.filedialog import askopenfilename

class Gui:
    def __init__(self, func):
        self._textbox = None

        self.root = tk.Tk()

        self.tabControl = tk.ttk.Notebook(self.root, width=1000, height=500)

        # Add the tabs to the window
        self.tabControl.add(self.tab_one(), text="All Results")
        self.tabControl.add(self.tab_two(), text="Create Test")
        self.tabControl.pack(expand=1, fill="both")

        # Bind key presses to a callback function
        self.root.bind("<Key>", func)

    # Open filename window?
    def askopenfilename():
        #tk.askopenfilename()
        pass

    # Tab 1 - All Results
    def tab_one(self):
        tabOne = tk.ttk.Frame(self.tabControl)
        scrollbar = tk.Scrollbar(tabOne)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self._textbox = tk.Text(tabOne)
        self._textbox.pack(fill=tk.BOTH, expand=True)
        self._textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self._textbox.yview)
        self._textbox.config(state=tk.DISABLED)

        return tabOne

    # Tab 2 - Create Test
    def tab_two(self):
        tabTwo = tk.ttk.Frame(self.tabControl)
        label = tk.ttk.Label(tabTwo, text="Hello.")
        label.pack()

        return tabTwo

    # Display a new line on the window
    def insert(self, to_write, overwrite=False):
        self._textbox.config(state=tk.NORMAL)
        if overwrite:
            lines = int(self._textbox.index('end-1c').split('.')[0])
            self._textbox.delete(f"{lines}.1", tk.END)
        self._textbox.insert(tk.END, to_write)
        self._textbox.config(state=tk.DISABLED)
        self._textbox.see("end")

    def start(self):
        #self.root.mainloop()
        pass

print("Please select an .mp4 file to extract VSD data from.")
import os
cwd = os.getcwd() # Get current working directory as 'cwd'
print("Current Working Directory is '" + cwd + "'.")

if os.path.exists("Output") == False:
    print("'Output' folder doesn't exist yet, will create.")
    os.mkdir("Output")
    if os.path.exists("Output") == True:
        print("Output folder successfully created.")
#Create an 'output' folder if needed

filetypes = (('.MP4 files', '*.mp4'),('All files', '*.*')) #Set up the filetypes dropdown for the window to open. It can look for '.MP4 files' or 'All files'.
filename = askopenfilename(initialdir=cwd, filetypes=filetypes) #Bring up a window in the 'Scripts' folder to get you to open a script.
print("Filename chosen is '" + filename + "'.")

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
#mp4_file = 'example.mp4'
mp4_file = filename #Set the 'mp4_file' value to the filename selected in the window earlier.
output_file = 'Output\complete.txt'
output_file_without_txt = 'Output\complete'
output_file_path = 'Output\\vsd_record.txt'
output_file_path_without_txt = 'Output\\vsd_record'
#Update the 'complete' output_file name if needed
if os.path.exists(output_file) == True:
    print("'" + output_file + "' already exists, will change output name.")
    for x in range(9999):
        potential_output_file = output_file_without_txt + str(x+2) + ".txt"
        #print("Will check if '" + potential_output_file + "' exists.")
        if os.path.exists(potential_output_file):
            #print(potential_output_file + "already exists! Must continue.")
            pass
        else:
            print(potential_output_file + " does not exist, will use this filename.")
            output_file = potential_output_file
            break
#Update the 'vsd_record' output_file name if needed
if os.path.exists(output_file_path) == True:
    print("'" + output_file_path + "' already exists, will change output name.")
    for x in range(9999):
        potential_output_file = output_file_path_without_txt + str(x+2) + ".txt"
        #print("Will check if '" + potential_output_file + "' exists.")
        if os.path.exists(potential_output_file):
            #print(potential_output_file + "already exists! Must continue.")
            pass
        else:
            print(potential_output_file + " does not exist, will use this filename.")
            output_file_path = potential_output_file
            break
start_value = "767364"
end_value = "66726565"

save_mp4_as_hexadecimal(mp4_file, output_file)
extract_numbers_between(output_file, start_value, end_value, output_file_path)
os.startfile(cwd + "\Output")#Open an Explorer window on the output folder
#x = input("I put this here to stop it closing the window!")