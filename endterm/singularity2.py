from tkinter import *
from tkinter import messagebox
import test_gui

alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Singular():
    def __init__(self):
        self.gui_singular_input, self.gui_singular_output = None, None
        self.frame_singular_output, self.frame_singular_input = None, None
        self.frame_singular_menu = None
        self.singular_matrix = []
        self.rows, self.cols = None, None
        self.matrix = []
        self.singularity = StringVar()
        self.m_dimensions = None
        self.determinant_value = None

        #we close the main window so we won't have too much windows on screen, open new window to input matrix
        #test_gui.root.withdraw()
        self.gui_singular_menu = Toplevel()
        self.gui_singular_menu.title("Singularity")
        self.gui_singular_menu.resizable(False, False)

        self.frame_singular_menu = Frame(self.gui_singular_menu, bg= 'Black', highlightbackground='black', highlightthickness=1)
        self.frame_singular_menu.grid(row=0, column=0, padx=5, pady=5)

        Label(self.frame_singular_menu, text='Enter matrix dimensions:', font=('Segoe 15', 10, 'bold'), bg= 'Black', fg="White").grid(row=4, column=1)
        self.m_dimensions = IntVar()
        OptionMenu(self.frame_singular_menu, self.m_dimensions, *range(1, 8)).grid(row=4, column=2)#we gonna take from 1 to 7 dimension in consideration
        #dimenstion_entry = Entry(self.frame_singular_menu, self.m_dimensions).grid(row=4, column=2)
        #self.m_dimensions = dimenstion_entry.get()
        Button(self.frame_singular_menu, text='Enter', padx=16, pady=5,relief =GROOVE, bd= 0, fg="White", bg="Black", command=self.input_singular_matrix).grid(row=5, column=2)
        #self.gui_singular_menu.protocol("WM_DELETE_WINDOW", test_gui.root.destroy)
        self.gui_singular_menu.mainloop()

    

    def output_matrix(self):
        # create window
        self.gui_singular_input.destroy()
        self.gui_singular_output = Toplevel()
        self.gui_singular_output.title("Singularity")
        self.gui_singular_output.resizable(False, False)

        self.frame_singular_output = Frame(self.gui_singular_output, highlightbackground='black', highlightthickness=1)
        self.frame_singular_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Button(self.frame_singular_output, text="Back", width=4, command=self.back_to_menu).grid(
            row=self.rows + 10,
            column=1)

        # display user input
        Label(self.frame_singular_output, text='Input:', font=('arial', 10, 'bold'), underline=0).grid(row=1, column=1)
        for i in range(self.rows):
            for j in range(self.cols):
                Label(self.frame_singular_output, text=self.matrix[i][j], bd=5).grid(row=i + 1, column=j + 2)

        Label(self.frame_singular_output, text='Determinant:', font=('arial', 10, 'bold'), underline=0).grid(row=1,
                                                                                                       column=self.cols * 2)
        
        det_matrix= self.determinant_value
        Label(self.frame_singular_output, text=det_matrix, font=('arial', 10, 'bold'), underline=0).grid(row=1,
                                                                                                       column=self.cols * 4)
        singularity_value= self.singularity
        Label(self.frame_singular_output, text=singularity_value, font=('arial', 10, 'bold'), underline=0).grid(row=2,
                                                                                                       column=self.cols * 4)
        
        self.gui_singular_output.protocol("WM_DELETE_WINDOW", test_gui.Menu.destroy)
        self.gui_singular_output.mainloop()

    def input_singular_matrix(self):
            self.gui_singular_menu.withdraw()
            self.gui_singular_input = Toplevel(self.gui_singular_menu)
            self.gui_singular_input.title("Singularity of Matrix")
            self.gui_singular_input.resizable(False, False)

            self.frame_singular_input = Frame(self.gui_singular_input, highlightbackground='black', highlightthickness=1)
            self.frame_singular_input.pack(fill=BOTH, expand=True, padx=5, pady=5)

            Label(self.frame_singular_input, text="Enter matrix:", font=('Segoe UI', 15, 'bold')).grid(row=1, column=1)
            
            self.rows, self.cols = (self.m_dimensions.get(), self.m_dimensions.get())
            self.matrix_entries = [[Entry(self.frame_singular_input) for _ in range(self.cols)] for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix_entries[i][j].grid(row=i+2, column=j+2)
                    
            submit_matrix_button = Button(self.frame_singular_input, text="Submit Matrix", command=self.process_matrix)
            submit_matrix_button.grid(row=self.rows+2, columnspan=self.cols+2)
            self.gui_singular_input.protocol("WM_DELETE_WINDOW", test_gui.Menu.destroy)
            self.gui_singular_input.mainloop()
    def process_matrix(self):
        self.matrix = []
        for row in self.matrix_entries:
            row_values = []
            for entry in row:
                try:
                    value = float(entry.get())
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numeric values for all matrix entries.")
                    return
                row_values.append(value)
            self.matrix.append(row_values)

        messagebox.showinfo("Matrix", f"You entered the matrix:\n{self.matrix}")

    def singularity_check(self):
        matrix = self.matrix
        i , j= self.rows , self.cols
        singularity_status = ""
        def minor(matrix, i , j):
            lis=[]
            for k in range(len(matrix)):
                if k==i:
                    continue
                else:
                    for s in range(len(matrix)):
                        if s==j:
                            continue
                        else:
                            lis.append(matrix[k][s])
                    matrix.append(lis)
                    lis=[]
            return matrix
        
        def dt(matrix):
            length = self.rows
            if length==1:
                return matrix[0][0]
            if length==2:
                return int(matrix[0][0])*int(matrix[1][1]) - int(matrix[0][1])*int(matrix[1][0])
            det=0
            for k in range(length):
                det += (int(matrix[0][k]) * (-1)**k) * dt(minor(matrix,0,k))
            return det
        
        if dt(self)==0:
            singularity_status ="Singular"
        else:
            singularity_status = "Not Singular"
        
        self.singularity = singularity_status
        self.determinant_value = dt(self.matrix)
        self.output_matrix()
        det= str(self.determinant_value)
        message = str(self.singularity)
        print(det, message)
        #messagebox.showinfo("Message Box", message)
    

    def back_to_menu(self):
        self.gui_singular_output.destroy()
        #test_gui.root.deiconify()

