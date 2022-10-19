from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk



# ####################### CHARTS ####################### #

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# ####################### METHODS DECRYPT - ENCRYPT ####################### #


def encrypt():
    string_to_convert = (string_entry.get())

    if len(string_to_convert) == 0:
        messagebox.showinfo(title="Empty filed", message="Please don't leave empty filed.")

    else:
        lst = []
        lst.extend(string_to_convert.upper())
        string_after_convert = ''
        for a in range(len(lst)):
            for i in MORSE_CODE_DICT:
                if i == lst[a]:
                    string_after_convert = f'{string_after_convert}{MORSE_CODE_DICT[i]} '

        result_entry.delete(0, END)
        result_entry.insert(0, string_after_convert)


def decrypt():
    string_to_convert = (string_entry.get())

    if len(string_to_convert) == 0:
        messagebox.showinfo(title="Empty filed", message="Please don't leave empty filed.")

    else:
        lst = []
        lst.extend(string_to_convert)
        string_after_split = string_to_convert.split()
        string_after_convert = ''
        for a in range(len(string_after_split)):
            for i in MORSE_CODE_DICT:
                if MORSE_CODE_DICT[i] == string_after_split[a]:
                    string_after_convert = f'{string_after_convert}{i}'

        result_entry.delete(0, END)
        result_entry.insert(0, string_after_convert)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Morse Code Converter")
window.config(padx=50, pady=50)

# Load an image in the script
img = (Image.open("morse-logo.png"))

# Resize the Image using resize method
resized_image = img.resize((300, 210))
new_image = ImageTk.PhotoImage(resized_image)


canvas = Canvas(width=200, height=200)
canvas.create_image(100, 110, image=new_image)
canvas.grid(column=1, row=0)

string_label = Label(text="Enter the string:")
string_label.grid(column=0, row=1)

string_entry = Entry(width=32)
string_entry.grid(column=1, row=1, sticky="W")
string_entry.focus()


result_label = Label(text="Translation result:")
result_label.grid(column=0, row=2)

result_entry = Entry(width=35)
result_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# Set up Menubutton

mb = Menubutton(window, text='Encrypt - Decrypt', relief='raised', width=15)
mb.grid(row=1, column=2, padx=3)
mb.menu = Menu(mb)
mb['menu'] = mb.menu
mb.menu.add_command(label="Encrypt", command=encrypt)
mb.menu.add_command(label='Decrypt', command=decrypt)


# ###Choice?

# choice=None
# def choice1():
#     global choice
#     choice='Choice 1'
# def choice2():
#     global choice
#     choice='Choice 2'
#
# def start(choice):
#     if choice=='Choice 1':
#         print('1')
#     elif choice=='Choice 2':
#         print('2')
#     # else:
#     #     #do something else since they didn't press either
#
#
# Choice_1_Button=Button(window, text='Choice 1', command=choice1) #what should it do?
# Choice_1_Button.grid(column=0, row=3)
# Choice_2_Button=Button(window, text='Choice 2', command=choice2)
# Choice_2_Button.grid(column=1, row=3)
# Start_Button=Button(window, text='Start', command=start)
# Start_Button.grid(column=2, row=3)

window.mainloop()
