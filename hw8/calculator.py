from tkinter import *
import math
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
def click(val):
    e = entry.get()
    ans = " "
    if val == "C":
        e = e[0:len(e) - 1]
        entry.delete(0, "end")
        entry.insert(0, e)
        return
    elif val == "CE":
        entry.delete(0, "end")
    elif val == "√":
        ans = math.sqrt(eval(e))
    elif val == "π":
        ans = math.pi
    elif val == "cosθ":
        ans = math.cos(math.radians(eval(e)))
    elif val == "sinθ":
        ans = math.sin(math.radians(eval(e)))
    elif val == "tanθ":
        ans = math.tan(math.radians(eval(e)))
    elif val == "2π":
        ans = 2 * math.pi
    elif val == "cosh":
        ans = math.cosh(eval(e))
    elif val == "sinh":
        ans = math.sinh(eval(e))
    elif val == "tanh":
        ans = math.tanh(eval(e))
    elif val == chr(8731):
        ans = eval(e) ** (1 / 3)
    elif val == "x\u02b8":
        entry.insert("end", "**")
        return
    elif val == "x\u00B3":
        ans = eval(e) ** 3
    elif val == "x\u00B2":
        ans = eval(e) ** 2
    elif val == "ln":
        ans = math.log2(eval(e))
    elif val == "deg":
        ans = math.degrees(eval(e))
    elif val == "rad":
        ans = math.radians(eval(e))
    elif val == "e":
        ans = math.e
    elif val == "log10":
        ans = math.log10(eval(e))
    elif val == "x!":
        ans = math.factorial(eval(e))
    elif val == chr(247):
        entry.insert("end", "/")
        return
    elif val == "=":
        ans = eval(e)
    else:
        entry.insert("end", val)
        return
    entry.delete(0, "end")
    entry.insert(0, ans)

def back():
    root.destroy()
    import login

root = Tk()
root.title("Calculator")
root.geometry("545x270")
root.config(bg=_from_rgb((160, 191, 253)))

entry = Entry(root, font=(40), bg=_from_rgb((210, 226, 255)), fg="black", width=30)
entry.grid(row=0, column=0, columnspan=8)
button_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ", "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh","4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", "7", "8", "9", chr(247), "ln", "deg","rad", "e", "0", ".", "%", "=", "log10", "(", ")", "x!"]

i,j=1,0
for k in button_list:
    button = Button(root, width=5, height=1, bd=1, text=k, bg=_from_rgb((210, 226, 255)), fg="black",font=("arial", 16), command=lambda button=k: click(button))
    button.grid(row=i, column=j, pady=1)
    j += 1
    if j > 7:
        i += 1
        j = 0
button=Button(root,text="back",command=back)
button.grid(row=8,column=1)
root.mainloop()