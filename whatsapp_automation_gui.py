#This program uses tkinter which is built in python program

#This program will use gui in which will provide the user the input/options for automation
#Options are:

'''
Sending mails
Sending whatsapp messages
'''

from tkinter import *
import pywhatkit as kit


root = Tk()
root.title('Sample')
root.wm_iconbitmap(r'C:\Users\Samarth Pachchigar\OneDrive\Desktop\Tkinter\automation.ico')

phone_number = Entry(root,
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4,
                      width=50,)
phone_number.insert(0,'Enter the phone number with country code: ')              
phone_number.grid(row=2, column=0,padx=40,pady=20)

messages = Entry(root,
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4,
                      width=50)
messages.grid(row=3, column=0,padx=40,pady=20)
messages.insert(0, 'Enter the message: ')

hours = Entry(root,
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10, 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4,
                      width=50)
hours.grid(row=4, column=0, padx=39, pady=20)
hours.insert(0, 'Enter the hour according to 24 hour clock:  ')


minutes = Entry(root,
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10, 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4,
                      width=50)
minutes.grid(row=5, column=0, padx=39, pady=20)
minutes.insert(0, 'Enter the minute according to 24 hour clock:  ')

def send():
    global phone_number
    global messages
    global hours
    global minutes

    pn = phone_number.get()
    msg = messages.get()
    hrs = hours.get()
    mins = minutes.get()

    kit.sendwhatmsg(pn, msg, int(hrs), int(mins))
    





send_message_button = Button(root, text='Send Message', bg='lightgreen', command=lambda: send())
send_message_button.grid(row=6, column=0)


root.mainloop()