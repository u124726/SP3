from tkinter import *
import exercise_3

# Root characteristics of GUI
root_gui = Tk()
root_gui.title("Video Conversor")
root_gui.iconbitmap("upf.ico")

# Frame characteristics of GUI
myConversor = Frame(root_gui, width=600, height=320)
myConversor.pack()


# Label characteristics of GUI
Label(myConversor, text="This is a GUI to do some different conversions on Big Buck Bunny video", font=("Comic Sans MS", 12)).place(x=0, y=0)
Label(myConversor, text="Option 1) - Grayscale conversion", font=("Comic Sans MS", 10)).place(x=0, y=100)
Label(myConversor, text="Option 2) - Resize 360x240 conversion", font=("Comic Sans MS", 10)).place(x=0, y=150)
Label(myConversor, text="Option 3) - Histogram in real-time", font=("Comic Sans MS", 10)).place(x=0, y=200)
Label(myConversor, text="Option 4) - Macroblocks and motion vectors", font=("Comic Sans MS", 10)).place(x=0, y=250)

# Buttons
Button(myConversor, text="(1)", command=exercise_3.grayscale()).place(x=210, y=100)
Button(myConversor, text="(2)", command=exercise_3.size()).place(x=250, y=150)
Button(myConversor, text="(3)", command=exercise_3.yuv_hist()).place(x=215, y=200)
Button(myConversor, text="(4)", command=exercise_3.macro_and_motion()).place(x=275, y=250)

root_gui.mainloop()
