from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image Slideshow Viewer")

image_path=[
    r"C:\Users\SUDEEP\OneDrive\Desktop\my photos\29.jpg",
    r"C:\Users\SUDEEP\OneDrive\Desktop\my photos\1378.jpg"
]
image_size=(720,720)
images=[Image.open(path).resize(image_size) for path in image_path]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label=tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow=cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_path)):
        update_image()

play_button=tk.Button(root,text="Play Slideshow",command=start_slideshow)
play_button.pack()

root.mainloop()