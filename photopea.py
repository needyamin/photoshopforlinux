import tkinter as tk
from tkinter import messagebox
import webbrowser

def show_custom_message(title, message):
    msg_window = tk.Toplevel(root)
    msg_window.title(title)
    msg_window.geometry("600x350")

    title_label = tk.Label(msg_window, text=title, font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

    message_label = tk.Label(msg_window, text=message, wraplength=250, justify="center")
    message_label.pack(pady=10)

    ok_button = tk.Button(msg_window, text="OK", command=msg_window.destroy)
    ok_button.pack(pady=5)

# Example usage:
root = tk.Tk()
root.title("Download Photopea")
root.geometry("700x400")

def show_message():
    title = "Download Photopea Offline"
    message = "The creator of Photopea, a great free alternative to Photoshop, is not interested on making an offline version, so I make it for my personal uses and share it on this community. If you have any complaint then please feel free to contact needyamin@gmail.com"
    show_custom_message(title, message)
    
def download():
	url= 'https://www.ansnew.com/'
	webbrowser.open_new_tab(url)

message_button = tk.Button(root, text="Download Photopea", command=download)
message_button.pack(pady=15)

message_button = tk.Button(root, text="About This Software", command=show_message)
message_button.pack(pady=15)




root.mainloop()
