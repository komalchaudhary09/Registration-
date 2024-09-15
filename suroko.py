from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw

def signup():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    mobile_number = entry_mobile_number.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    agree_terms = var_agree_terms.get()
    
    if not agree_terms:
        messagebox.showerror("Terms and Conditions", "You must agree to the terms and conditions to submit.")
        return
    
    if first_name and password and confirm_password:
        if password == confirm_password:
            if password != first_name:
                messagebox.showinfo("Password Reset", f"Password reset successful for {first_name}")
            else:
                messagebox.showerror("Password Reset Error", "Password should not match the First Name.")
        else:
            messagebox.showerror("Password Reset Error", "Passwords do not match.")
    else:
        messagebox.showerror("Password Reset Error", "All information must be filled.")
    
def close_window():
    root.quit()

def show_password():
    if var_show_password.get():
        entry_password.config(show="")
        entry_confirm_password.config(show="")
    else:
        entry_password.config(show="*")
        entry_confirm_password.config(show="*")

def terms_condition():
    if var_agree_terms.get() == 1:
        messagebox.showinfo("Terms and Conditions", "You have agreed to the terms and conditions.")
    else:
        messagebox.showinfo("Terms and Conditions", "You must agree to the terms and conditions to proceed.")

def create_rounded_rectangle(width, height, radius, color):
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle(((0, 0), (width, height)), radius=radius, fill=color)
    return ImageTk.PhotoImage(image)

# for registration 
root = Tk()
root.title("SUROKO Cinemas Registration")
root.iconbitmap("suroko.ico")
root.configure(bg="#2E3133")
root.geometry("550x515")

signup_frame_width = 520
signup_frame_height = 495
signup_frame_radius = 10
signup_frame_bg = "#626465"

signup_frame_image = create_rounded_rectangle(signup_frame_width, signup_frame_height, signup_frame_radius, signup_frame_bg)

canvas = Canvas(root, width=signup_frame_width, height=signup_frame_height, bg="#2E3133", highlightthickness=0)
canvas.pack(pady=10)
canvas.create_image(1, 0, anchor="nw", image=signup_frame_image)

signup_frame = Frame(canvas, bg=signup_frame_bg, padx=20, pady=20)
signup_frame.place(x=20, y=20, width=signup_frame_width-40, height=signup_frame_height-40)

label_registration = Label(signup_frame, text="Personal Information", fg="white", bg=signup_frame_bg, font=("Arial", 18, "bold"))
label_registration.grid(row=0, column=0, padx=5, pady=5, sticky="w")

label_first_name = Label(signup_frame, text="First Name", fg="white", bg=signup_frame_bg, font=("Arial", 14))
label_first_name.grid(row=1, column=0, padx=5, pady=5, sticky="w")

label_last_name = Label(signup_frame, text="Last Name", fg="white", bg=signup_frame_bg, font=("Arial", 14))
label_last_name.grid(row=2, column=0, padx=5, pady=5, sticky="w")

label_email = Label(signup_frame, text="Email", fg="white", bg=signup_frame_bg, font=("Arial", 14))
label_email.grid(row=3, column=0, padx=5, pady=5, sticky="w")

label_mobile_number = Label(signup_frame, text="Mobile Number", fg="white", bg=signup_frame_bg, font=("Arial", 14))
label_mobile_number.grid(row=4, column=0, padx=5, pady=5, sticky="w")

label_password = Label(signup_frame, text="Password", fg="white", bg=signup_frame_bg, font=("Arial", 14))
label_password.grid(row=5, column=0, padx=5, pady=5, sticky="w")

label_confirm_password = Label(signup_frame, text="Confirm Password", fg="white", bg=signup_frame_bg, font=("Arial", 14))
label_confirm_password.grid(row=6, column=0, padx=5, pady=5, sticky="w")

entry_first_name = Entry(signup_frame, width=40)
entry_first_name.grid(row=1, column=1, padx=5, pady=5)
entry_last_name = Entry(signup_frame, width=40)
entry_last_name.grid(row=2, column=1, padx=5, pady=5)
entry_email = Entry(signup_frame, width=40)
entry_email.grid(row=3, column=1, padx=5, pady=5)
entry_mobile_number = Entry(signup_frame, width=40)
entry_mobile_number.grid(row=4, column=1, padx=5, pady=5)
entry_password = Entry(signup_frame, width=40, show="*")
entry_password.grid(row=5, column=1, padx=5, pady=5)
entry_confirm_password = Entry(signup_frame, width=40, show="*")
entry_confirm_password.grid(row=6, column=1, padx=5, pady=5)

var_show_password = IntVar()
checkbox_show_password = Checkbutton(signup_frame, text="Show Password", variable=var_show_password, command=show_password, fg="white", bg=signup_frame_bg, font=("Arial", 10))
checkbox_show_password.grid(row=7, columnspan=2, pady=5)


var_agree_terms = IntVar()
checkbox_agree_terms = Checkbutton(signup_frame, text="I agree to the terms and conditions.", variable=var_agree_terms, command=terms_condition, fg="white", bg=signup_frame_bg, font=("Arial", 10))
checkbox_agree_terms.grid(row=8, columnspan=2, pady=10)

button_submit = Button(signup_frame, text="SUBMIT", command=signup, bg="#646D76", fg="white", width=10, font=("Arial", 12))
button_submit.grid(row=9, columnspan=2, pady=10)

label_close = Label(signup_frame, text="Close", fg="white", bg=signup_frame_bg, font=("Arial", 10))
label_close.grid(row=10, columnspan=2, pady=10)
label_close.bind("<Button-1>", lambda e: close_window())

root.mainloop()
