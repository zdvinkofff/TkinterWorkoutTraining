import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import csv

class TrainingLogApp:
    """
    Основной класс приложения "Журнал тренировок".
    Отвечает за создание и управление графическим интерфейсом пользователя (GUI).
    """

    def __init__(self, root):
        """
        Инициализирует приложение.
        Загружает данные о тренировках из файла "training_data.json" и создает виджеты интерфейса.

        Args:
            root (tkinter.Tk): Корневое окно приложения.
        """
        self.root = root
        self.root.title("Журнал тренировок")

        # Загрузка данных о тренировках из файла
        self.data = self.load_data()

        # Создание виджетов интерфейса
        self.create_widgets()

    def load_data(self):
        """
        Загружает данные о тренировках из файла "training_data.json".
        Если файл не найден или содержит некорректные данные, возвращает пустой список.

        Returns:
            list: Список словарей, представляющих данные о тренировках.
        """
        try:
            with open("training_data.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        """
        Сохраняет данные о тренировках в файл "training_data.json".
        """
        with open("training_data.json", "w") as file:
            json.dump(self.data, file, indent=4)

    def create_widgets(self):
        """
        Создает все виджеты интерфейса, включая поля ввода, кнопки и дерево для отображения записей.
        """
        # Создание рамки для ввода данных
        input_frame = ttk.Frame(self.root)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Создание полей ввода
        ttk.Label(input_frame, text="Упражнение:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.exercise_entry = ttk.Entry(input_frame)
        self.exercise_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(input_frame, text="Вес:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.weight_entry = ttk.Entry(input_frame)
        self.weight_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.weight_unit = tk.StringVar(value="килограммы")
        self.weight_unit_menu = ttk.Combobox(input_frame, textvariable=self.weight_unit, values=["килограммы", "фунты"])
        self.weight_unit_menu.grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(input_frame, text="Повторения:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.reps_entry = ttk.Entry(input_frame)
        self.reps_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Создание кнопки для добавления записи
        self.add_button = ttk.Button(input_frame, text="Добавить запись", command=self.add_entry)
        self.add_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # Создание кнопки для экспорта в CSV
        self.export_button = ttk.Button(self.root, text="Экспортировать в CSV", command=self.export_to_csv)
        self.export_button.grid(row=1, column=0, padx=10, pady=10)

        # Создание кнопки для импорта из CSV
        self.import_button = ttk.Button(self.root, text="Импортировать из CSV", command=self.import_from_csv)
        self.import_button.grid(row=1, column=1, padx=10, pady=10)

        # Создание дерева для отображения записей
        self.records_tree = ttk.Treeview(self.root, columns=("Дата", "Упражнение", "Вес", "Повторения"))
        self.records_tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.records_tree.heading("#0", text="ID")
        self.records_tree.heading("Дата", text="Дата")
        self.records_tree.heading("Упражнение", text="Упражнение")
        self.records_tree.heading("Вес", text="Вес")
        self.records_tree.heading("Повторения", text="Повторения")

        # Создание кнопки для просмотра записей
        self.view_button = ttk.Button(self.root, text="Просмотреть записи", command=self.view_records)
        self.view_button.grid(row=1, column=2, padx=10, pady=10)

        # Заполнение дерева записями
        self.update_records_tree()

    def add_entry(self):
        """
        Обрабатывает добавление новой записи в журнал тренировок.
        Считывает данные из полей ввода, создает новую запись и добавляет ее в список данных.
        Сохраняет данные в файл и обновляет дерево записей.
        """
        exercise = self.exercise_entry.get()
        weight = float(self.weight_entry.get())
        if self.weight_unit.get() == "фунты":
            weight = weight * 0.453592  # Конвертируем фунты в килограммы
        reps = int(self.reps_entry.get())
        date = datetime.now().strftime("%Y-%m-%d")

        new_entry = {
            "date": date,
            "exercise": exercise,
            "weight": weight,
            "reps": reps
        }

        self.data.append(new_entry)
        self.save_data()
        self.update_records_tree()

        # Очистка полей ввода
        self.exercise_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.reps_entry.delete(0, tk.END)

    def update_records_tree(self):
        """
        Обновляет дерево отображения записей.
        Очищает дерево и заполняет его данными из списка self.data.
        """
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)

        for i, entry in enumerate(self.data):
            self.records_tree.insert("", "end", text=str(i + 1), values=(
                entry["date"],
                entry["exercise"],
                f"{entry['weight']:.2f}",
                entry["reps"]
            ))

    def view_records(self):
        """
        Открывает новое окно для просмотра всех записей.
        Создает дополнительное окно с деревом записей.
        """
        view_window = tk.Toplevel(self.root)
        view_window.title("Все записи")

        records_tree = ttk.Treeview(view_window, columns=("Дата", "Упражнение", "Вес", "Повторения"))
        records_tree.pack(padx=10, pady=10, fill="both", expand=True)
        records_tree.heading("#0", text="ID")
        records_tree.heading("Дата", text="Дата")
        records_tree.heading("Упражнение", text="Упражнение")
        records_tree.heading("Вес", text="Вес")
        records_tree.heading("Повторения", text="Повторения")

        for i, entry in enumerate(self.data):
            records_tree.insert("", "end", text=str(i + 1), values=(
                entry["date"],
                entry["exercise"],
                f"{entry['weight']:.2f}",
                entry["reps"]
            ))

    def export_to_csv(self):
        """
        Экспортирует данные о тренировках в файл "training_data.csv".
        Сохраняет все записи в формате CSV.
        """
        try:
            with open("training_data.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Дата", "Упражнение", "Вес", "Повторения"])
                for entry in self.data:
                    writer.writerow([
                        entry["date"],
                        entry["exercise"],
                        entry["weight"],
                        entry["reps"]
                    ])
            messagebox.showinfo("Экспорт успешен", "Данные успешно экспортированы в файл training_data.csv.")
        except Exception as e:
            messagebox.showerror("Ошибка экспорта", f"Произошла ошибка при экспорте данных: {e}")

    def import_from_csv(self):
        """
        Импортирует данные о тренировках из файла "training_data.csv".
        Загружает записи из CSV-файла и добавляет их в список self.data.
        Сохраняет обновленные данные в файл "training_data.json".
        """
        try:
            with open("training_data.csv", "r") as file:
                reader = csv.DictReader(file)
                new_data = []
                for row in reader:
                    new_entry = {
                        "date": row["Дата"],
                        "exercise": row["Упражнение"],
                        "weight": float(row["Вес"]),
                        "reps": int(row["Повторения"])
                    }
                    new_data.append(new_entry)
            self.data = new_data
            self.save_data()
            self.update_records_tree()
            messagebox.showinfo("Импорт успешен", "Данные успешно импортированы из файла training_data.csv.")
        except FileNotFoundError:
            messagebox.showerror("Ошибка импорта", "Файл training_data.csv не найден.")
        except Exception as e:
            messagebox.showerror("Ошибка импорта", f"Произошла ошибка при импорте данных: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TrainingLogApp(root)
    root.mainloop()
