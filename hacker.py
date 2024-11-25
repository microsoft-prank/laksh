import tkinter as tk

root = tk.Tk()

# Fullscreen mode
root.attributes("-fullscreen", True)

label = tk.Label(root, text="YOU'VE BEEN HACKED! Hehe", font=("Helvetica", 50), fg="red")
label.pack(expand=True)

root.after(5000, root.destroy)  # Close the window after 5 seconds

root.mainloop()



