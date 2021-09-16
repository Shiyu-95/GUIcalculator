import tkinter as tk
from  tkinter import messagebox

window = tk.Tk()


def add_digit(digit):
    value = entry_window.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]  # когда значение пустого окна 0, то берется все кроме него
    entry_window.delete(0, tk.END)  # очищаем окно
    entry_window.insert(0, value+digit)  # метод инсерт позволяет вставить данные


def add_operation(operation):
    value = entry_window.get()
    if value[-1] in '+-*/':  # проверяем если в окне последний символ операции и мы хотим сменить операцию, то
        value = value[:-1]  # при смене операции символ предыдущей удаляется
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = entry_window.get()
    entry_window.delete(0, tk.END)
    entry_window.insert(0, value+operation)


def calculate():
    value = entry_window.get()
    if value[-1] in '+-*/':  # если мы нажимаем на равно после операции 5+ =, то чтобы не было ошибки
        value = value + value[:-1]  # мы считаем, что второе число это первое число
    entry_window.delete(0, tk.END)
    try:
        entry_window.insert(0, eval(value))  # eval позволяет считать введенные параметры как числа + операции,
# хотя подается строка
    except (NameError, SyntaxError):  # если юзер введет не разреш символы или буквы мы его предупредим
        messagebox.showerror('Attention!', 'Inter only digits! Letters were written')
        entry_window.insert(0, '0')
    except ZeroDivisionError:
        messagebox.showerror('Division by zero', 'Mathematics and common sense forbid us to divide by zero')
        entry_window.insert(0, '0')


def clear():
    entry_window.delete(0, tk.END)
    entry_window.insert(0, '0')


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=("Arial", 13), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg='red',
                     command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg='red',
                     command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg='red',
                     command=clear)


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '\x08':
        entry_window.delete(0)


window.geometry(f'240x270+100+200')
window['bg'] = '#33ffe6'
window.title("Calculator")
window.bind('<Key>', press_key)

entry_window = tk.Entry(window, justify=tk.RIGHT, font=('Arial', 15), width=15)
# justify позволяет "прижимать" данные с правой стороны
entry_window.insert(0, '0')  # когда окно ввода пустое 0 ставится по умолчанию
entry_window.grid(row=0, column=0, columnspan=4, stick='we', padx=5)  # делаем отступ по х
# span чтобы свойства применялись сразу к 3 колонкам, stick чтобы растянуть

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)  # растягиваем по всем 4 сторонам,
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)  # делаем отступ от краев и делаем рамку
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

window.grid_columnconfigure(0, minsize=60)
window.grid_columnconfigure(1, minsize=60)
window.grid_columnconfigure(2, minsize=60)
window.grid_columnconfigure(3, minsize=60)

window.grid_rowconfigure(1, minsize=60)
window.grid_rowconfigure(2, minsize=60)
window.grid_rowconfigure(3, minsize=60)
window.grid_rowconfigure(4, minsize=60)

window.mainloop()
