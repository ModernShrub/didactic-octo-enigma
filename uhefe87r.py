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
    imgpath= ""
    imgpath = filedialog.askopenfilename(title="Open File",
                                         filetypes=(("Image Files", "*.jpg *.tiff *.png *.jpeg"),))
    print(imgpath)
    img = ImageTk.PhotoImage(Image.open(imgpath))
    imglabel['image'] = img
    print("image opened")
    
    
def rotatate():
    global imgpath
    global img
    img = Image.open(imgpath)
    img = img.rotate(180)
    img = ImageTk.PhotoImage(img)
    imglabel['image'] = img
    
openbtn = Button(root,font=('courier',11),text="Open Image",command=openimg)
openbtn.place(relx=0.5,rely=0.1,anchor=CENTER)

rotabtn = Button(root,font=('courier',11),text="Rotate",command=rotatate)
rotabtn.place(relx=0.5,rely=0.95,anchor=CENTER)

root.mainloop()