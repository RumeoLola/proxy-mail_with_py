# imports
from tkinter import *
import smtplib
import ssl


root = Tk()
root.title("Dictionary")
root.geometry("400x600")


# frame the root window
win_frame = Frame(root)


# the message
message_box = ''
text = Text(root, font=('ariel', 16))


# email instructions
email_label = Label(win_frame, text="Enter your email/gmail and password")
email_label.pack(side=TOP)


# email address entry
email_address = Entry(win_frame, width=35)
email_address.pack(side=TOP, padx=0, pady=0)


# password entry
email_password = Entry(win_frame, width=35, show="*")
email_password.pack(side=TOP, pady=0, padx=0)


# receiver email instructions
receiver_label = Label(win_frame, text="Send message to")
receiver_label.pack(side=TOP)


# receiver email entry
receiver_email = Entry(win_frame, width=35)
receiver_email.pack(side=TOP, pady=0, padx=0)


# Meaning function
def email_sender():
    global email_address, email_password, receiver_email, text
    # get email address and password and receiver and use string method
    email_address = email_address.get()
    email_address = str(email_address)
    email_password = email_password.get()
    email_password = str(email_password)
    receiver_email = receiver_email.get()
    receiver_email = str(receiver_email)
    text = str(text)
    ssl_context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 587, context=ssl_context) as server:  # using port 465
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(email_address, email_password)
    except Exception as e:
        return print(e)


# send email instructions
send_label = Label(win_frame, text="Send message")
send_label.pack(side=LEFT)


# Meaning button
send_message = Button(win_frame, text="Send Message", command=email_sender, bg='white')
send_message.pack(side=RIGHT, padx=0, pady=0)


win_frame.pack(side=BOTTOM)
text.pack(padx=0, pady=0)
root.configure(bg='cyan')
root.mainloop()
