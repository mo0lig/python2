from tkinter import *
from tkinter import messagebox
def mat1(n,m):
    def mat2(n,m,x,y,a):
        windw.destroy()
        print("first matrix:",a)
        window = Tk()
        window.title("Matrix")
        window.geometry("700x600")
        c=list()
        lll=list()
        for i in range(n):
            for j in range(y):
                s=0
                lll.append(s)
            c.append(lll)
            lll=[]    
        texvar = []
        entries = []
        def gt_mat():
            window.destroy()
            b = []
            for i in range(x):
                b.append([])
                for j in range(y):
                    b[i].append(texvar[i][j].get())
            print("second matrix:",b)
            if m==x:
                for q in range(len(a)):
                    for w in range(len(b[0])):
                        for e in range(len(a[0])):
                            c[q][w] += a[q][e] * b[e][w]
                print("Result:")
                for g in c:
                    print(g)
            else:
                messagebox.showerror('Error','Different matrix sizes')       
        Label(window, text="Enter matrix :").place(x=20, y=20)
        xx,yy=0,0
        for i in range(x):
            texvar.append([])
            entries.append([])
            for j in range(y):
                texvar[i].append(IntVar())
                entries[i].append(Entry(window, textvariable=texvar[i][j],width=4))
                entries[i][j].place(x=59+xx, y=49+yy)
                xx += 30
            yy += 30
            xx = 0
        button= Button(window,text="Submit", width=15, command=gt_mat)
        button.place(x=260,y=240)
    
    windw = Tk()
    windw.title("Matrix")
    windw.geometry("700x600")
    text_var = []
    entries = []
    def mat():
        arr = []
        for i in range(n):
            arr.append([])
            for j in range(m):
                arr[i].append(text_var[i][j].get())
        x=int(input("x:"))
        y=int(input("y:"))
        mat2(n,m,x,y,arr)
    Label(windw, text="Enter matrix :").place(x=20, y=20)
    xx,yy=0,0
    for i in range(n):
        text_var.append([])
        entries.append([])
        for j in range(m):
            text_var[i].append(IntVar())
            entries[i].append(Entry(windw, textvariable=text_var[i][j],width=4))
            entries[i][j].place(x=60 + xx, y=50 + yy)
            xx += 30
        yy += 30
        xx = 0
    button= Button(windw,text="Submit", width=15, command=mat)
    button.place(x=260,y=240)
    windw.mainloop()

n=int(input("n:"))
m=int(input("m:"))
mat1(n,m)
