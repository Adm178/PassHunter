import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

# Значения по умолчанию
input_text1 = 3.2
input_text2 = 5.8
input_text3 = 6
input_text4 = 32
input_text5 = 3
input_text6 = 0.5
array = ["pass", "login", "key", "secret", "email"]
check1 = True
check2 = True
check3 = True
check4 = True
check5 = True
check6 = False
check7 = False

def open_settings_window(root):
    global input_text1, input_text2, input_text3, input_text4, input_text5, input_text6, array
    global check1, check2, check3, check4, check5, check6, check7
    # Настройки окна настроек
    settings = tk.Toplevel(root)
    settings.title("Настройки")
    settings.iconbitmap('images/settings.ico')
    screen_width = settings.winfo_screenwidth()
    screen_height = settings.winfo_screenheight()
    x = (screen_width - 425) // 2
    y = (screen_height - 355) // 2
    settings.geometry(f"425x355+{x}+{y}")
    settings.focus_set()  # Установка фокуса на окно
    settings.lift()  # Перемещение окна поверх других окон
    settings.grab_set()  # Установка окна как модального
    settings.resizable(False, False)

    # Фукнции для работы тектовой подсказки в полях ввода
    def on_entry_click(event, input_entry, placeholder_text):
        if input_entry.get() == placeholder_text:
            input_entry.delete(0, tk.END)
            input_entry.config(fg='black')
    def on_focus_out(event, input_entry, placeholder_text):
        if input_entry.get() == '':
            input_entry.insert(0, placeholder_text)
            input_entry.config(fg='gray')

    # Энтропия от и до
    set_label1 = Label(settings, text="Энтропия от")
    set_label1.place(x=5, y=5)
    set_entry1 = tk.Entry(settings, width=4, fg='gray')
    placeholder1 = str(input_text1)
    set_entry1.insert(0, placeholder1)
    set_entry1.bind("<FocusIn>", lambda event: on_entry_click(event, set_entry1, placeholder1))
    set_entry1.bind("<FocusOut>", lambda event: on_focus_out(event, set_entry1, placeholder1))
    set_entry1.place(x=85, y=5)

    set_label2 = Label(settings, text="до")
    set_label2.place(x=117, y=5)
    set_entry2 = tk.Entry(settings, width=4, fg='gray')
    placeholder2 = str(input_text2)
    set_entry2.insert(0, placeholder2)
    set_entry2.bind("<FocusIn>", lambda event: on_entry_click(event, set_entry2, placeholder2))
    set_entry2.bind("<FocusOut>", lambda event: on_focus_out(event, set_entry2, placeholder2))
    set_entry2.place(x=140, y=5)

    # Подсказка 1
    help1 = ttk.Button(settings, text="?")
    help1.place(x=175, y=5, width=20, height=20)
    help1.bind("<Enter>", lambda event: show_tooltip(200, 80, event,
                    "По умолчанию - от 3.2 до 5.8\n Для сгенерированных паролей\nи ключей рекомендуется - от 3.9"))
    help1.bind("<Leave>", lambda event: hide_tooltip(event))

    # Длина пароля/ключа от и до
    set_label3 = Label(settings, text="Длина пароля/ключа от")
    set_label3.place(x=5, y=35)
    set_entry3 = tk.Entry(settings, width=4, fg='gray')
    placeholder3 = str(input_text3)
    set_entry3.insert(0, placeholder3)
    set_entry3.bind("<FocusIn>", lambda event: on_entry_click(event, set_entry3, placeholder3))
    set_entry3.bind("<FocusOut>", lambda event: on_focus_out(event, set_entry3, placeholder3))
    set_entry3.place(x=150, y=35)

    set_label4 = Label(settings, text="до")
    set_label4.place(x=182, y=35)
    set_entry4 = tk.Entry(settings, width=4, fg='gray')
    placeholder4 = str(input_text4)
    set_entry4.insert(0, placeholder4)
    set_entry4.bind("<FocusIn>", lambda event: on_entry_click(event, set_entry4, placeholder4))
    set_entry4.bind("<FocusOut>", lambda event: on_focus_out(event, set_entry4, placeholder4))
    set_entry4.place(x=205, y=35)

    # Подсказка 2
    help2 = ttk.Button(settings, text="?")
    help2.place(x=240, y=35, width=20, height=20)
    help2.bind("<Enter>", lambda event: show_tooltip(185, 80, event,
                    "    По умолчанию - от 6 до 32\n         Для ключей и хэшей\n   рекомендуется - от 16 до 512"))
    help2.bind("<Leave>", lambda event: hide_tooltip(event))

    # Значение Passwordmeter от
    set_label5 = Label(settings, text="Значение Passwordmeter от")
    set_label5.place(x=5, y=65)
    set_entry5 = tk.Entry(settings, width=4, fg='gray')
    placeholder5 = str(input_text5)
    set_entry5.insert(0, placeholder5)
    set_entry5.bind("<FocusIn>", lambda event: on_entry_click(event, set_entry5, placeholder5))
    set_entry5.bind("<FocusOut>", lambda event: on_focus_out(event, set_entry5, placeholder5))
    set_entry5.place(x=165, y=65)

    # Подсказка 3
    help3 = ttk.Button(settings, text="?")
    help3.place(x=198, y=65, width=20, height=20)
    help3.bind("<Enter>", lambda event: show_tooltip(185, 80, event,
                "       По умолчанию - от 3\n       Для сложных паролей\n рекомендуется - от 7 (max 10)"))
    help3.bind("<Leave>", lambda event: hide_tooltip(event))

    # Значение вероятности для ИИ
    set_label6 = Label(settings, text="Значение вероятности для ИИ от")
    set_label6.place(x=5, y=95)
    set_entry6 = tk.Entry(settings, width=4, fg='gray')
    placeholder6 = str(input_text6)
    set_entry6.insert(0, placeholder6)
    set_entry6.bind("<FocusIn>", lambda event: on_entry_click(event, set_entry6, placeholder6))
    set_entry6.bind("<FocusOut>", lambda event: on_focus_out(event, set_entry6, placeholder6))
    set_entry6.place(x=195, y=95)

    # Подсказка 4
    help4 = ttk.Button(settings, text="?")
    help4.place(x=229, y=95, width=20, height=20)
    help4.bind("<Enter>", lambda event: show_tooltip(200, 120, event,
                "       По умолчанию - от 0.5\n   Значение задает вероятность,\nот которой ИИ будет определять\n"
                "            слово как пароль\n\n      Рекомендуется не менять"))
    help4.bind("<Leave>", lambda event: hide_tooltip(event))

    # Чекбоксы
    label = Label(settings, text="Искать в:")
    label.place(x=5, y=125)
    # Чекбокс "txt"
    check_var1 = BooleanVar()
    check_var1.set(check1)
    check_button = ttk.Checkbutton(settings, text=".txt", variable=check_var1, style="Custom.TCheckbutton")
    check_button.place(x=10, y=150)
    # Чекбокс "docx, doc"
    check_var2 = BooleanVar()
    check_var2.set(check2)
    check_button = ttk.Checkbutton(settings, text=".doc, .docx", variable=check_var2, style="Custom.TCheckbutton")
    check_button.place(x=75, y=150)
    # Чекбокс "xlsx', xls"
    check_var3 = BooleanVar()
    check_var3.set(check3)
    check_button = ttk.Checkbutton(settings, text=".xls, .xlsx", variable=check_var3, style="Custom.TCheckbutton")
    check_button.place(x=170, y=150)
    # Чекбокс "config, ini, xml, yaml, log"
    check_var4 = BooleanVar()
    check_var4.set(check4)
    check_button = ttk.Checkbutton(settings, text=".config, .ini, .xml, .yaml, .log", variable=check_var4, style="Custom.TCheckbutton")
    check_button.place(x=10, y=180)
    # Чекбокс - искать по ключевым словам
    check_var5 = BooleanVar()
    check_var5.set(check5)
    check_button = ttk.Checkbutton(settings, text="Искать по ключевым словам", variable=check_var5, style="Custom.TCheckbutton")
    check_button.place(x=10, y=220)
    # Чекбокс - искать по ключевым словам c частичным или полным совпадением
    check_var6 = BooleanVar()
    check_var6.set(check6)
    check_button = ttk.Checkbutton(settings, text="Искать даже с частичным совпадением", variable=check_var6, style="Custom.TCheckbutton")
    check_button.place(x=30, y=250)
    # Чекбокс - искать регулярному выражению
    check_var7 = BooleanVar()
    check_var7.set(check7)
    check_button = ttk.Checkbutton(settings, text="Искать по регулярному выражению", variable=check_var7, style="Custom.TCheckbutton")
    check_button.place(x=10, y=280)
    help5 = ttk.Button(settings, text="?")
    help5.place(x=237, y=283, width=20, height=20)
    help5.bind("<Enter>", lambda event: show_tooltip(225, 120, event,
                "Поиск слов, в которых присутствует\nобязательно хотя бы одна цифра,\nхотя бы одна латинская буква\n(в нижнем или верхнем регистре),\nхотя бы один специальный символ\nи длина строки от 7 до 32 символов"))
    help5.bind("<Leave>", lambda event: hide_tooltip(event))

    # Кнопка сохранить и отменить
    button = ttk.Button(settings, text="Сохранить", command=lambda: save())
    button.place(x=260, y=315)
    button = ttk.Button(settings, text="Отменить", command=lambda: settings.destroy())
    button.place(x=90, y=315)

    # Добавить слово в список ключевых слов
    def add_word():
        words = word_entry.get().split()
        if words:
            for word in words:
                word_list.insert(tk.END, word)  # добавляем слово в конец списка
                array.append(word)
        word_entry.delete(0, tk.END)  # очищаем поле ввода

    # Удалить слово в список ключевых слов
    def delete_selected_word():
        # получаем индекс выбранного элемента
        selected_indices = word_list.curselection()
        # удаляем выбранный элемент, если он есть
        for i in selected_indices[::-1]:
            selected_word = word_list.get(i)
            word_list.delete(i)
            if selected_word in array:
                array.remove(selected_word)
            if word_list.size() > i:
                word_list.selection_set(i)
            elif word_list.size() > 0:
                word_list.selection_set(word_list.size() - 1)

    # Список ключевых слов
    label = Label(settings, text="Ключевые слова")
    label.place(x=290, y=5)
    word_entry = ttk.Entry(settings)
    word_entry.place(x=280, y=25)
    word_list = tk.Listbox(settings)
    word_list.place(x=280, y=55)
    for word in array:
        word_list.insert(tk.END, word)
    add_button = ttk.Button(settings, text="Добавить", command=add_word)
    add_button.place(x=280, y=225)
    delete_button = ttk.Button(settings, text="Удалить", command=delete_selected_word)
    delete_button.place(x=350, y=225)

    def save():
        global input_text1, input_text2, input_text3, input_text4, input_text5, input_text6
        global check1, check2, check3, check4, check5, check6, check7
        end = True
        if float(set_entry1.get()) > 0 and float(set_entry2.get()) > 0 and int(set_entry3.get()) > 0 \
                    and int(set_entry4.get()) > 0 and int(set_entry5.get()) > 0 and float(set_entry6.get()) > 0:
            input_text1 = set_entry1.get()
            input_text2 = set_entry2.get()
            input_text3 = set_entry3.get()
            input_text4 = set_entry4.get()
        else:
            messagebox.showerror("Ошибка", "Значения не могут быть меньше 0")
            end = False
        if float(set_entry5.get()) <= 10:
            input_text5 = set_entry5.get()
        else:
            messagebox.showerror("Ошибка", "Значение passwordmeter не может быть\nменьше 0 или больше 10")
            end = False
        if float(set_entry6.get()) <= 1:
            input_text6 = float(set_entry6.get())
        else:
            messagebox.showerror("Ошибка", "Значение вероятности не может быть\nменьше 0 или больше 1")
            end = False

        check1 = check_var1.get()
        check2 = check_var2.get()
        check3 = check_var3.get()
        check4 = check_var4.get()
        check5 = check_var5.get()
        check6 = check_var6.get()
        check7 = check_var7.get()
        if end:
            settings.destroy()

    def show_tooltip(c_x, c_y, event, text):
        global tooltip
        tooltip = tk.Toplevel(root)
        ttk.Style().configure("Tooltip.TLabel", background="white")
        tooltip.wm_overrideredirect(True)  # Убираем рамку окна
        tooltip.geometry(f"{c_x}x{c_y}+{x}+{y}")
        tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root-40}")  # Позиционируем окно подсказки
        tooltip.configure(bg='white')

        label = ttk.Label(tooltip, text="Справка", style="Tooltip.TLabel")
        label.place(x=72, y=5)
        label = ttk.Label(tooltip, text=text, style="Tooltip.TLabel")
        label.place(x=10, y=25)

    def hide_tooltip(event):
        tooltip.destroy()