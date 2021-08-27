from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root=Tk()
root.minsize(650,650)

imglabel = Label(root,highlightthickness=2, relief=SOLID)
imglabel.place(relx=0.3,rely=0.13)

imgpath=""
img=""
def openimg():
    global imgpath
    global img
    imgpath = filedialog.askopenfilename(title="Open File",
                                         filetypes=(("Image Files", "*.jpg *.tiff *.png *.jpeg"),))
    print(imgpath)
    img = ImageTk.PhotoImage(Image.open(imgpath))
    imglabel['image'] = img
    print("image opened")
    
openbtn = Button(root,font=('courier',11),text="Open Image",command=openimg)
openbtn.place(relx=0.5,rely=0.1,anchor=CENTER)

rotabtn = Button(root,font=('courier',11),text="Rotate")
rotabtn.place(relx=0.5,rely=1.0,anchor=CENTER)

root.mainloop()