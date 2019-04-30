import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def say_hi():
    print("Hello!")

# button = tk.Button(frame, text="CLICK ME", fg="red", command=say_hi) # normal way
button = tk.Button(frame, text="CLICK ME", fg="red", command=lambda: print("Hello"))

button.pack(side=tk.LEFT)
root.mainloop()