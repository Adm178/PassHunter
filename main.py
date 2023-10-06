from tkinter import ttk
import tkinter as tk
from tkinter import *
from wordbook import open_wordbok_window
from set_wind import open_settings_window
from func import get_directory, on_header_click, scan, export_to_txt, copy_to_clipboard, f_menu, state, get_directory2
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

root = ThemedTk(theme='scidblue')  # создание окна
root.title("PassHunter")  # установка заголовка окна
root.iconbitmap('images/icon.ico')  # изменение иконки окна
# получение размеров экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# расчет положения окна по центру экрана
x_position = (screen_width - 900) // 2  # ширина окна
y_position = (screen_height - 440) // 2  # высота окна
# установка размеров и положения окна
root.geometry(f"900x440+{x_position}+{y_position}")
# запрет изменения размеров окна
root.resizable(False, False)

# -------------------------------------------
# Адрес директории поиска
label = Label(root, text="Документы:")
label.place(x=449, y=13)
directory_entry = ttk.Entry(root, width=53)
directory_entry.place(x=522, y=10)
# Кнопка выбора директории
image = ImageTk.PhotoImage(Image.open("images/folder.png"))
address_button = ttk.Button(root, image=image, command=lambda: get_directory(directory_entry))
address_button.place(x=850, y=10)

# Радиокнопка
label = Label(root, text="Поиск с помощью:")
label.place(x=5, y=80)
selected_option = tk.StringVar(value="option1")
selected_option.trace("w", lambda *args: state(selected_option, address_button2))
option1 = tk.Radiobutton(root, text="Энтропии и\nPasswordmeter", variable=selected_option, value="option1")
option1.place(x=8, y=105)
option2 = tk.Radiobutton(root, text="Словаря", variable=selected_option, value="option2")
option2.place(x=8, y=145)
option3 = tk.Radiobutton(root, text="Нейросети", variable=selected_option, value="option3")
option3.place(x=8, y=175)

# Адрес словаря
label2 = Label(root, text="Словарь:")
label2.place(x=5, y=13)
directory_entry2 = ttk.Entry(root, width=53)
directory_entry2.place(x=60, y=10)
# Кнопка выбора директории
address_button2 = ttk.Button(root, image=image, command=lambda: get_directory2(directory_entry2))
address_button2.place(x=388, y=10)
state(selected_option, address_button2)

# Ползунки
scrollbar = ttk.Scrollbar(root)
scrollbar2 = ttk.Scrollbar(root, orient="horizontal")
# Таблица
tree = ttk.Treeview(root, show="headings", columns=("num", "passw", "path", "entropy", "Passwordmeter","Probability"),
                    yscrollcommand=scrollbar.set, xscrollcommand=scrollbar2.set)
scrollbar.config(command=tree.yview)
scrollbar2.config(command=tree.xview)
tree.bind('<Double-Button-1>', lambda event: on_header_click(event, tree))  # Сортировка двойным кликом ЛКМ
tree.heading("#1", text="№")
tree.heading("#2", text="Пароль/Ключ")
tree.heading("#3", text="Путь")
tree.heading("#4", text="Энтропия")
tree.heading("#5", text="Passwordmeter")
tree.heading("#6", text="Вероятность по ИИ")
tree.column("#0", width=0, stretch=NO)
tree.column("#1", width=35, stretch=NO)
tree.column("#2", width=140, stretch=NO)
tree.column("#3", width=300, stretch=NO)
tree.column("#4", width=60, stretch=NO)
tree.column("#5", width=90, stretch=NO)
tree.column("#6", width=120)
tree.place(x=123, y=45, height=330)  # Измените высоту таблицы здесь
scrollbar.place(x=885, y=58, height=310)  # Измените высоту полосы прокрутки здесь
scrollbar2.place(x=150, y=380, width=690)  # Измените положение полосы прокрутки горизонтальной прокрутки здесь

# Создание контекстного меню для копирования
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Скопировать", command=lambda: copy_to_clipboard(tree, root))
    # Вызов контекстного меню при нажатии на правую кнопку мыши
tree.bind("<Button-3>", lambda event: f_menu(event, menu))

# Кнопка генератора словаря
button = ttk.Button(root, text="Генератор словаря", command=lambda: open_wordbok_window(root), style='Button2.TButton')
button.place(x=520, y=400)

# Кнопка настроек
button = ttk.Button(root, text="Настройки", command=lambda: open_settings_window(root), style='Button2.TButton')
button.place(x=680, y=400)

# Кнопка для запуска сканирования
style = ttk.Style().configure('Button2.TButton', font=('Segoe UI Semibold', 11))  # Установка размера шрифта
ttk_button = ttk.Button(root, text="Сканировать", command=lambda: scan(tree, selected_option), style='Button2.TButton')
ttk_button.place(x=780, y=400)

# Кнопка для экспорта данных
ttk_button = ttk.Button(root, text="Экспорт", command=lambda: export_to_txt(tree), style='Button2.TButton')
ttk_button.place(x=10, y=400)

if __name__ == '__main__':
    root.mainloop()  # Запуск главного цикла программы