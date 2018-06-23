import tkinter as tk
root  = tk.Tk()
# frame = tk.Frame(root)
selected_color = 0
# frame.pack()
colors = ['black','red','green','white','yellow']
def toggle_color(rest = True):
    if(rest):
        global selected_color
        selected_color = (selected_color +1)%len(colors)
    else:
        selected_color =0
    print(selected_color)
    root.config(bg = colors[selected_color])
# def reset_color():
#     global selected_color
#     selected_color = 0
crap = tk.PhotoImage(file = 'checkerPiecesRed.png')
# root.config(bg = 'red')
toggleButton = tk.Button(root,text='a'  ,width = 10,height = 10,command =lambda :toggle_color(True))
resetButton  = tk.Button(root,text = 're-set',command =lambda :toggle_color(False))
toggleButton.pack()
resetButton.pack()
root.mainloop()
