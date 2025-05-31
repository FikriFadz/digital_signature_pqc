import tkinter as tk
from tkinter import filedialog, messagebox

# Create main window
window = tk.Tk()
window.title("Digital Signage by Integration Department PTPKM")
window.geometry("750x500")

# Create a frame to hold all content
main_frame = tk.Frame(window)
main_frame.pack(pady=20)

# First section - Digital Signage
signage_frame = tk.Frame(main_frame)
signage_frame.pack(fill="x", pady=10)

# Label for Digital Signage (centered)
labeldigital = tk.Label(signage_frame, text="Digital Signage", font=("Times New Roman", 18))
labeldigital.pack()

# Button frame for Digital Signage (below label, left-aligned)
button_frame1 = tk.Frame(main_frame)
button_frame1.pack(fill="x")

signage_upload_button = tk.Button(
    button_frame1, 
    text="Upload file for \nDigital Signage", 
    font=("Times New Roman", 12),
    width=20,
    height=2,
    command=lambda: messagebox.showinfo("Info", "Digital Signage upload button clicked")
)
signage_upload_button.pack(side="left", padx=10, pady=5)

# Sign button and label for Digital Signage
def sign_signage_file():
    signage_sign_label.config(text="File signed successfully")

signage_sign_button = tk.Button(
    button_frame1, 
    text="Sign File", 
    font=("Times New Roman", 12),
    width=12,
    height=2,
    command=sign_signage_file
)
signage_sign_button.pack(side="left", padx=5, pady=5)

signage_sign_label = tk.Label(button_frame1, text="", font=("Times New Roman", 10), fg="green")
signage_sign_label.pack(side="left", padx=5, pady=5)

# Horizontal separator
separator = tk.Frame(main_frame, height=2, bg="black", width=600)
separator.pack(fill="x", pady=10)

# Second section - Digital Verification
verification_frame = tk.Frame(main_frame)
verification_frame.pack(fill="x", pady=10)

# Label for Digital Verification (centered)
labelverification = tk.Label(verification_frame, text="Digital Verification", font=("Times New Roman", 18))
labelverification.pack()

# Button frame for Digital Verification (below label, left-aligned)
button_frame2 = tk.Frame(main_frame)
button_frame2.pack(fill="x")

verification_upload_button = tk.Button(
    button_frame2, 
    text="Upload file for \nDigital Verification", 
    font=("Times New Roman", 12),
    width=20,
    height=2,
    command=lambda: messagebox.showinfo("Info", "Digital Verification upload button clicked")
)
verification_upload_button.pack(side="left", padx=10, pady=5)

# Verify button and label for Digital Verification
def verify_verification_file():
    verification_verify_label.config(text="File verified successfully")

verification_verify_button = tk.Button(
    button_frame2, 
    text="Verify File", 
    font=("Times New Roman", 12),
    width=12,
    height=2,
    command=verify_verification_file
)
verification_verify_button.pack(side="left", padx=5, pady=5)

verification_verify_label = tk.Label(button_frame2, text="", font=("Times New Roman", 10), fg="green")
verification_verify_label.pack(side="left", padx=5, pady=5)

# Run the app
window.mainloop()
