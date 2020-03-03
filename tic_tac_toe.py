from tkinter import *
from functools import partial
from itertools import product
import random
from time import time, sleep


root = Tk()
root.title("Tic-Tac")
matrix = []
x_text = "X"
o_text = "O"
isCross = True
isWork = True
button_id = []
rows_number = IntVar()
columns_number = IntVar()

rows = rows_number.get()
columns = columns_number.get()



def change(i, j):
    rows = rows_number.get()
    columns = columns_number.get()
    bname = button_id[i][j]
    global isWork
    if isWork:
        def isCross():
            global isCross
            if isCross:
                if matrix[i][j] == None or matrix[i][j] == "X":
                    matrix[i][j] = "X"
                    bname.config(text="X")
                    name_label.config(text="'0' turn")
                    isCross = False
                elif matrix[i][j] == None or matrix[i][j] == "0":
                    matrix[i][j] = "0"
                    bname.config(text="0")
                    name_label.config(text="'X' turn")
                    isCross = True
            else:
                if matrix[i][j] == None or matrix[i][j] == "0":
                    matrix[i][j] = "0"
                    bname.config(text="0")
                    name_label.config(text="'X' turn")
                    isCross = True
                elif matrix[i][j] == None or matrix[i][j] == "X":
                    matrix[i][j] = "X"
                    bname.config(text="X")
                    name_label.config(text="'0' turn")
                    isCross = False
        isCross()

        def validate_game_rows():
            global isWork
            for i in range(0, len(matrix)):
                is_rows_assembled = False
                current_rows_winner = matrix[i][0]

                if current_rows_winner == None:
                    continue

                for j in range(1, len(matrix[0])):
                    if matrix[i][j] != current_rows_winner:
                        is_rows_assembled = False
                        break
                    else:
                        is_rows_assembled = True

                if is_rows_assembled and current_rows_winner == "X":
                    isWork = False
                    name_label.config(text="X is winner")
                if is_rows_assembled and current_rows_winner == "0":
                    isWork = False
                    name_label.config(text="0 is winner")
        validate_game_rows()

        def validate_game_columns():
            global isWork
            for i in range(0, len(matrix)):
                is_columns_assembled = False
                current_columns_winner = matrix[0][i]

                if current_columns_winner == None:
                    continue

                for j in range(1, len(matrix[i])):
                    if matrix[j][i] != current_columns_winner:
                        is_columns_assembled = False
                        break
                    else:
                        is_columns_assembled = True
                        if j == rows - 1:
                            if is_columns_assembled and current_columns_winner == "X":
                                isWork = False
                                name_label.config(text="X is winner")
                            if is_columns_assembled and current_columns_winner == "0":
                                isWork = False
                                name_label.config(text="0 is winner")
        validate_game_columns()


        def validate_game_principal_diagonal():
            global isWork
            for i in range(0, len(matrix)):
                is_principal = False
                current_principal = matrix[i][i]

                if current_principal == None:
                    continue

                for j in range(0, len(matrix)):
                    if current_principal != matrix[j][j]:
                        is_principal = False
                        break
                    else:
                        is_principal = True


                if is_principal and current_principal == "X":
                    isWork = False
                    name_label.config(text="X is winner")
                if is_principal and current_principal == "0":
                    isWork = False
                    name_label.config(text="0 is winner")
        validate_game_principal_diagonal()


        def validate_game_second_diagonal():
            global isWork

            for i in range(0, len(matrix)):
                is_second = False
                current_second = matrix[i][(len(matrix)-1)-i]

                if is_second == None:
                    continue

                for j in range(0, len(matrix)):
                    if current_second != matrix[j][(len(matrix)-1)-j]:
                        is_second = False
                        break
                    else:
                        is_second = True

                if is_second and current_second == "X":
                    isWork = False
                    name_label.config(text="X is winner")
                if is_second and current_second == "0":
                    isWork = False
                    name_label.config(text="X is winner")
        validate_game_second_diagonal()

name_label = Label(root, text="X turn", width=10, font="Arial 9")

def end_game():
        global isWork
        global isCross
        name_label.config(text="X turn")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "X" or matrix[i][j] == "0" and not None:
                    matrix[i][j] = None
                bname = button_id[i][j]
                bname.config(text="")
                isWork = True
        isCross = not isCross




rows_number = IntVar()
columns_number = IntVar()
sequence_number = IntVar()

def get_buttons():
    name_label.place(x=2, y=3)
    ok_button.destroy()
    rows_label.destroy()
    columns_label.destroy()
    which_rows.destroy()
    which_columns.destroy()
    rows = rows_number.get()
    columns = columns_number.get()
    for i in range(0, rows):
        button_id.append([])
        matrix.append([])
        for j in range(0, columns):
            matrix[i].append(None)
            btn_press = Button(root, text=" ", bg="#FFB6C1", width=4, height=2, command=partial(change, i, j))
            btn_press.grid(row=i, column=j, sticky="n,e,s,w", ipadx=10, ipady=5, padx=10, pady=20)
            button_id[i].append(btn_press)
    btn_restart = Button(root, text="Restart",bg="#DDA0DD", width=4, height=2, command=end_game)
    btn_restart.grid(row=rows + 1, column=columns//2, ipadx=10, ipady=5, padx=10, pady=20)


rows_label = Label(root, text="Enter number of rows")
columns_label = Label(root, text="Enter number of columns")
what_sequence_label = Label(root, text="Enter number of sequence")

which_rows = Entry(root, textvariable=rows_number)
which_columns = Entry(root, textvariable=columns_number)
what_sequence = Entry(root, textvariable=sequence_number)

rows_label.grid(row=0, column=0, sticky="w")
columns_label.grid(row=1, column=0, sticky="w")
what_sequence_label.grid(row=2, column=0, sticky="w")
which_rows.grid(row=0,column=2, padx=5, pady=5)
which_columns.grid(row=1,column=2, padx=5, pady=5)
what_sequence.grid(row=2,columns=4, padx=5, pady=5)
ok_button = Button(text="Ok", command=partial(get_buttons))
ok_button.grid(row=3, column=2, padx=5, pady=5, sticky="e")



root.mainloop()
