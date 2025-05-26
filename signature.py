import tkinter as tk
from tkinter import filedialog, messagebox

# Create main window
window = tk.Tk()
window.title("Digital Signage by Integration Department PTPKM")
window.geometry("700x500")

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

signage_button = tk.Button(
    button_frame1, 
    text="Upload file for \nDigital Signage", 
    font=("Times New Roman", 12),
    width=20,
    height=2,
    command=lambda: messagebox.showinfo("Info", "Digital Signage button clicked")
)
signage_button.pack(side="left", padx=20, pady=5)

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

verification_button = tk.Button(
    button_frame2, 
    text="Upload file for \nDigital Verification", 
    font=("Times New Roman", 12),
    width=20,
    height=2,
    command=lambda: messagebox.showinfo("Info", "Digital Verification button clicked")
)
verification_button.pack(side="left", padx=20, pady=5)

# Run the app
window.mainloop()