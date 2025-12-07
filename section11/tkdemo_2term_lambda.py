import tkinter as tk

# 計算機能のための変数
current_number = 0
first_term = 0
second_term = 0
result = 0
operation = 0    # 1:+  2:-  3:*  4:/

def do_plus():
    global current_number, first_term, operation
    first_term = current_number
    current_number = 0
    operation = 1

def do_minus():
    global current_number, first_term, operation
    first_term = current_number
    current_number = 0
    operation = 2

def do_mul():
    global current_number, first_term, operation
    first_term = current_number
    current_number = 0
    operation = 3

def do_div():
    global current_number, first_term, operation
    first_term = current_number
    current_number = 0
    operation = 4

def do_eq():
    global second_term, result, current_number, operation
    second_term = current_number

    if operation == 1:
        result = first_term + second_term
    elif operation == 2:
        result = first_term - second_term
    elif operation == 3:
        result = first_term * second_term
    elif operation == 4:
        if second_term == 0:
            show_number("Err")
            current_number = 0
            return
        result = first_term // second_term
    else:
        result = current_number

    current_number = 0
    show_number(result)

def key(n):
    global current_number
    current_number = current_number * 10 + n
    show_number(current_number)

def clear():
    global current_number, first_term, second_term, result, operation
    current_number = 0
    first_term = 0
    second_term = 0
    result = 0
    operation = 0
    show_number(current_number)

def show_number(num):
    e.delete(0, tk.END)
    e.insert(0, str(num))

# tkinter GUI
root = tk.Tk()
f = tk.Frame(root, bg="#ffffc0")
f.grid()

FONT = ("Helvetica", 14)

#  数字ボタン
digit_buttons = {}

# 配置位置
digit_positions = {
    7: (1,0), 8: (1,1), 9: (1,2),
    4: (2,0), 5: (2,1), 6: (2,2),
    1: (3,0), 2: (3,1), 3: (3,2),
    0: (4,0)
}

for num in range(10):
    digit_buttons[num] = tk.Button(
        f,
        text=str(num),
        command=lambda n=num: key(n),
        bg="white",
        width=2,
        height=2,
        font=FONT
    )

# 配置
for num, (r, c) in digit_positions.items():
    digit_buttons[num].grid(row=r, column=c)

# operation
bc  = tk.Button(f, text='C', command=clear, bg="red",   width=2, height=2, font=FONT)
bp  = tk.Button(f, text='+', command=do_plus,  bg="green", width=2, height=2, font=FONT)
bmi = tk.Button(f, text='-', command=do_minus, bg="green", width=2, height=2, font=FONT)
bmu = tk.Button(f, text='*', command=do_mul,   bg="green", width=2, height=2, font=FONT)
bdv = tk.Button(f, text='/', command=do_div,   bg="green", width=2, height=2, font=FONT)
be  = tk.Button(f, text='=', command=do_eq,    bg="green", width=2, height=2, font=FONT)

# 配置
bc.grid(row=1, column=3)
bp.grid(row=2, column=3)
bmi.grid(row=3, column=3)
be.grid(row=4, column=3)
bmu.grid(row=4, column=1)
bdv.grid(row=4, column=2)

# Entry
e = tk.Entry(f, font=FONT)
e.grid(row=0, column=0, columnspan=4)
clear()

root.mainloop()
