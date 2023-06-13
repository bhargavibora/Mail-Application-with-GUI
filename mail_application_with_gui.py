import tkinter as tk
from tkinter import messagebox
import smtplib


def send_email():
    sender_email = entry_sender.get()
    password = entry_password.get()
    receiver_email = entry_receiver.get()
    subject = entry_subject.get()
    message = text_message.get("1.0", "end")

    smtp_server = "smtp.gmail.com"   # Replace with your SMTP server address
    smtp_port = 587  # Replace with your SMTP server port

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)

            email_content = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, receiver_email, email_content)

        messagebox.showinfo("Email Sent", "Email has been sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while sending the email: {str(e)}")


# Create the main window
window = tk.Tk()
window.title("Mail Application")

# Create and position the widgets
label_sender = tk.Label(window, text="Sender Email:")
label_sender.pack()
entry_sender = tk.Entry(window)
entry_sender.pack()

label_password = tk.Label(window, text="Password:")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

label_receiver = tk.Label(window, text="Receiver Email:")
label_receiver.pack()
entry_receiver = tk.Entry(window)
entry_receiver.pack()

label_subject = tk.Label(window, text="Subject:")
label_subject.pack()
entry_subject = tk.Entry(window)
entry_subject.pack()

label_message = tk.Label(window, text="Message:")
label_message.pack()
text_message = tk.Text(window, height=10, width=50)
text_message.pack()

button_send = tk.Button(window, text="Send Email", command=send_email)
button_send.pack()

# Run the main event loop
window.mainloop()
