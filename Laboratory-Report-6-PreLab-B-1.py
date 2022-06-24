import tkinter as tk #importing tkinter
root = tk.Tk()
root.configure(background='bisque')
def pressed():
    print("Button pressed")

def create_layout(frame):
    b1=tk.Button(frame, text="Button1", bg="grey", command=pressed)
    b1.pack(side="top", anchor="w", pady="20px")
    b2=tk.Button(frame, text="Button2", bg="grey", command=pressed, padx="20px")
    b2.pack(side="left" )

frame = tk. Frame (root, background="bisque") #frame
create_layout(frame)
frame.place(anchor="nw") #packing frame in side north west
root.geometry("200x200")
root.mainloop()