from tkinter import Tk, Frame, Label, Button
import singularity2
import inverse


class Menu:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.master.resizable(False, False)
        self.master.title("Matrix Calculator Main Menu")
        self.master.configure(bg="black")

        self.create_main_menu()

    def create_main_menu(self):
        main_frame = Frame(self.master, bg="black")
        main_frame.grid(row=0, column=0, padx=20, pady=20)

        welcome_label = Label(main_frame, text="Welcome to the Matrix Calculator", font=("Segoe 15", 16), fg="white", bg="black")
        welcome_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        buttons_data = [
            ("Singularity" , singularity2.Singular),
            ("REF", singularity2.Singular),
            ("Cramer's Rule", singularity2.Singular),
            ("Characteristic polynom",singularity2.Singular),
            ("LU Decomposition", singularity2.Singular)
        ]

        row_num = 1
        col_num = 0

        for button_text,command_text in buttons_data:
            button = Button(main_frame, text=button_text, width=15, height=2, font=("Segoe 15", 15), relief="groove", command= command_text, fg="white", bg="black", borderwidth= 4)
            button.grid(row=row_num, column=col_num, padx=5, pady=5)

            col_num += 1
            if col_num > 1:
                col_num = 0
                row_num += 1

if __name__ == "__main__":
    root = Tk()
    app = Menu(root)
    root.mainloop()
