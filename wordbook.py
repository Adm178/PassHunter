import itertools
import tkinter as tk
from tkinter import ttk
from tkinter import *

check1 = True
check2 = True
check3 = False
check4 = False

def open_wordbok_window(root):
    global check1, check2, check3, check4
    wordbok = tk.Toplevel(root)
    wordbok.title("Генератор словаря")
    wordbok.iconbitmap('images/wordbook.ico')
    screen_width = wordbok.winfo_screenwidth()
    screen_height = wordbok.winfo_screenheight()
    x = (screen_width - 425) // 2
    y = (screen_height - 550) // 2
    wordbok.geometry(f"425x490+{x}+{y}")
    wordbok.focus_set()  # Установка фокуса на окно
    wordbok.lift()  # Перемещение окна поверх других окон
    wordbok.grab_set()  # Установка окна как модального
    wordbok.resizable(False, False)

    # Комбинатор слов
    label = Label(wordbok, text="Комбинатор слов", font=("Arial", 14))
    label.place(x=130, y=5)
    label1 = Label(wordbok, text="ФИО:")
    label1.place(x=62, y=47)
    ent1 = tk.StringVar()
    entry1 = ttk.Entry(wordbok, width=45, textvariable=ent1)
    entry1.place(x=100, y=45)
    label2 = Label(wordbok, text="Дата рождения:")
    label2.place(x=5, y=77)
    ent2 = tk.StringVar()
    entry2 = ttk.Entry(wordbok, width=45, textvariable=ent2)
    entry2.place(x=100, y=75)
    label3 = Label(wordbok, text="Доп. слова:")
    label3.place(x=29, y=107)
    ent3 = tk.StringVar()
    entry3 = ttk.Entry(wordbok, width=45, textvariable=ent3)
    entry3.place(x=100, y=105)
    label4 = Label(wordbok, text="Использовать от")
    label4.place(x=5, y=148)
    ent4 = tk.StringVar()
    entry4 = ttk.Entry(wordbok, width=4, textvariable=ent4)
    entry4.place(x=105, y=145)
    label5 = Label(wordbok, text="до")
    label5.place(x=135, y=148)
    ent5 = tk.StringVar()
    entry5 = ttk.Entry(wordbok, width=4, textvariable=ent5)
    entry5.place(x=155, y=145)

    label6 = Label(wordbok, text="слов в одной комбинации")
    label6.place(x=185, y=148)
    # Подсказка 1
    help1 = ttk.Button(wordbok, text="?")
    help1.place(x=390, y=80, width=25, height=25)
    help1.bind("<Enter>", lambda event: show_tooltip(205, 70, event, "Слова разделяются через пробел\n    "
                                                                     "и не должны повторяться"))
    help1.bind("<Leave>", lambda event: hide_tooltip(event))
    # Кнопка сгенирировать
    button = ttk.Button(wordbok, text="Сгенерировать", command=lambda: combinator())
    button.place(x=320, y=180)
    # Разграничительная линия
    h_line = tk.Frame(wordbok, height=1, bg="gray", width=400)
    h_line.place(x=10, y=220)


    # Генератор случайных комбинаций
    label7 = Label(wordbok, text="Генератор случайных комбинаций", font=("Arial", 14))
    label7.place(x=50, y=225)
    # Чекбоксы
    label8 = Label(wordbok, text="Символы для генерации:")
    label8.place(x=10, y=267)
    # Чекбокс цифр
    check_var1 = BooleanVar()
    check_var1.set(check1)
    check_button = ttk.Checkbutton(wordbok, text="1234567890", variable=check_var1, style="Custom.TCheckbutton")
    check_button.place(x=5, y=290)
    # Чекбокс строчных латинских букв
    check_var2 = BooleanVar()
    check_var2.set(check2)
    check_button = ttk.Checkbutton(wordbok, text="abcdefghijklnopqrstuvwxyz", variable=check_var2, style="Custom.TCheckbutton")
    check_button.place(x=5, y=320)
    # Чекбокс прописных латинских букв
    check_var3 = BooleanVar()
    check_var3.set(check3)
    check_button = ttk.Checkbutton(wordbok, text="ABCDEFGHIJKLMNOPQRSTUVWXYZ", variable=check_var3, style="Custom.TCheckbutton")
    check_button.place(x=5, y=350)
    # Чекбокс спец. символов
    check_var4 = BooleanVar()
    check_var4.set(check4)
    check_button = ttk.Checkbutton(wordbok, text="+-/*!&$#?=@<>", variable=check_var4, style="Custom.TCheckbutton")
    check_button.place(x=5, y=380)

    # Длина пароля
    label9 = Label(wordbok, text="Длина от")
    label9.place(x=5, y=415)
    ent6 = tk.StringVar()
    entry6 = ttk.Entry(wordbok, width=4, textvariable=ent6)
    entry6.place(x=60, y=412)
    label10 = Label(wordbok, text="до")
    label10.place(x=90, y=415)
    ent7 = tk.StringVar()
    entry7 = ttk.Entry(wordbok, width=4, textvariable=ent7)
    entry7.place(x=110, y=412)
    label11 = Label(wordbok, text="символов")
    label11.place(x=140, y=415)

    # Кол-во паролей, которое будет сгенерировано
    def update_label1(*args):
        label_var1.set("Будет сгенерировано паролей: " + str(m()))
    def update_label2(*args):
        label_var2.set("Будет сгенерировано паролей: " + str(n()))

    check_var1.trace("w", update_label2)
    check_var2.trace("w", update_label2)
    check_var3.trace("w", update_label2)
    check_var4.trace("w", update_label2)
    ent1.trace("w", update_label1)
    ent2.trace("w", update_label1)
    ent3.trace("w", update_label1)
    ent4.trace("w", update_label1)
    ent5.trace("w", update_label1)
    ent6.trace("w", update_label2)
    ent7.trace("w", update_label2)

    label_var1 = tk.StringVar()
    label12 = Label(wordbok, textvariable=label_var1)
    label12.place(x=5, y=185)
    label_var2 = tk.StringVar()
    label13 = Label(wordbok, textvariable=label_var2)
    label13.place(x=5, y=455)

    # Кнопка сгенирировать
    button = ttk.Button(wordbok, text="Сгенерировать", command=lambda: generator())
    button.place(x=320, y=450)

    # Комбинатор
    def combinator():
        words = []
        words.extend(entry1.get().split())
        words.extend(entry2.get().split())
        words.extend(entry3.get().split())

        result_dict = {}

        for i in range(int(ent4.get()), int(ent5.get())+1):
            for subset in itertools.combinations(words, i):
                for perm in itertools.permutations(subset):
                    result_dict[''.join(perm)] = True


        with open("wordbook.txt", "w") as f:
            for result in result_dict.keys():
                f.write(result + '\n')
    # Генератор
    def generator():
        len_alf = ""
        len_alf += "1234567890" if check_var1.get() else ""
        len_alf += "abcdefghijklmnopqrstuvwxyz" if check_var2.get() else ""
        len_alf += "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if check_var3.get() else ""
        len_alf += "!@#$%^&*+=-?~" if check_var4.get() else ""

        result_dict = {}
        if ent6.get() != '' and ent7.get() != '' and int(ent6.get()) <= int(ent7.get()):
            for i in range(int(ent6.get()), int(ent7.get()) + 1):
                for subset in itertools.combinations(len_alf, i):
                    for perm in itertools.permutations(subset):
                        result_dict[''.join(perm)] = True

        with open("wordbook.txt", "w") as f:
            for result in result_dict.keys():
                f.write(result + '\n')

    def show_tooltip(c_x, c_y, event, text):
        global tooltip
        tooltip = tk.Toplevel(root)
        ttk.Style().configure("Tooltip.TLabel", background="white")
        tooltip.wm_overrideredirect(True)  # Убираем рамку окна
        tooltip.geometry(f"{c_x}x{c_y}+{x}+{y}")
        tooltip.wm_geometry(f"+{event.x_root + 10}+{event.y_root - 40}")  # Позиционируем окно подсказки
        tooltip.configure(bg='white')

        label = ttk.Label(tooltip, text="Справка", style="Tooltip.TLabel")
        label.place(x=72, y=5)
        label = ttk.Label(tooltip, text=text, style="Tooltip.TLabel")
        label.place(x=10, y=25)


    def hide_tooltip(event):
        tooltip.destroy()

    def n():
        sum_pass = 0
        len_alf = 0
        len_alf += 10 if check_var1.get() else 0
        len_alf += 26 if check_var2.get() else 0
        len_alf += 26 if check_var3.get() else 0
        len_alf += 13 if check_var4.get() else 0
        if ent6.get() != '' and ent7.get() != '' and int(ent6.get()) <= int(ent7.get()):
            for i in range(int(ent6.get()), int(ent7.get())+1):
                sum_pass += len_alf ** i
            return sum_pass
        return 0

    def m():
        words = []
        words.extend(entry1.get().split())
        words.extend(entry2.get().split())
        words.extend(entry3.get().split())
        sum_pass = 0
        if ent4.get() != '' and ent5.get() != '':
            if ent1.get() != '' or ent2.get() != '' or ent3.get() != '':
                if len(words) >= int(ent5.get()) and int(ent4.get()) <= int(ent5.get()):
                    for i in range(int(ent4.get()), int(ent5.get()) + 1):
                        n = len(words)
                        r = i
                        Fn = 1
                        Fnr = 1

                        for j in range(1, n + 1):
                            Fn *= j
                        for j in range(1, n - r + 1):
                            Fnr *= j

                        sum_pass += Fn / Fnr

        return int(sum_pass)