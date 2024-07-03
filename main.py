import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import csv

class TrainingLogApp:
    def __init__(self, root):
        self.root = root
        root.title("Журнал тренировок")

        self.data = self.load_data()
        self.create_widgets()

    def load_data(self):
        try:
            with open("training_data.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        with open("training_data.json", "w") as file:
            json.dump(self.data, file, indent=4)

    def create_widgets(self):
        # Виджеты для ввода данных
        self.exercise_label = ttk.Label(self.root, text="Упражнение:")
        self.weight_label = ttk.Label(self.root, text="Вес:")
        self.reps_label = ttk.Label(self.root, text="Повторения:")

        self.exercise_entry = ttk.Entry(self.root)
        self.weight_entry = ttk.Entry(self.root)
        self.weight_unit = tk.StringVar(value="кг")
        self.weight_unit_dropdown = ttk.Combobox(self.root, textvariable=self.weight_unit, values=["кг", "фунты"], state="readonly")
        self.reps_entry = ttk.Entry(self.root)

        self.exercise_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")
        self.weight_label.grid(row=0, column=2, padx=10, pady=10, sticky="E")
        self.weight_unit_dropdown.grid(row=0, column=4, padx=10, pady=10)
        self.reps_label.grid(row=0, column=6, padx=10, pady=10, sticky="E")

        self.exercise_entry.grid(row=0, column=1, padx=10, pady=10)
        self.weight_entry.grid(row=0, column=3, padx=10, pady=10)
        self.reps_entry.grid(row=0, column=7, padx=10, pady=10)

        # Кнопки
        self.add_button = ttk.Button(self.root, text="Добавить запись", command=self.add_entry)
        self.view_button = ttk.Button(self.root, text="Просмотреть записи", command=self.view_records)
        self.export_button = ttk.Button(self.root, text="Экспортировать в CSV", command=self.export_to_csv)


        self.add_button.grid(row=1, column=0, padx=10, pady=10)
        self.view_button.grid(row=1, column=1, padx=10, pady=10)
        self.export_button.grid(row=1, column=2, padx=10, pady=10)
        self.export_button.grid(row=1, column=3, padx=10, pady=10)


        # Виджет для просмотра записей
        self.records_tree = ttk.Treeview(self.root)
        self.records_tree["columns"] = ("Дата", "Упражнение", "Вес", "Повторения")
        self.records_tree.heading("#0", text="ID")
        self.records_tree.heading("Дата", text="Дата")
        self.records_tree.heading("Упражнение", text="Упражнение")
        self.records_tree.heading("Вес", text="Вес")
        self.records_tree.heading("Повторения", text="Повторения")
        self.records_tree.grid(row=2, column=0, columnspan=8, padx=10, pady=10)

        self.update_records_tree()

    def add_entry(self):
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
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)

        for i, entry in enumerate(self.data):
            self.records_tree.insert("", "end", text=str(i+1), values=(
                entry["date"], entry["exercise"], entry["weight"], entry["reps"]))

    def view_records(self):
        top = tk.Toplevel(self.root)
        top.title("Записи тренировок")

        view_tree = ttk.Treeview(top)
        view_tree["columns"] = ("Дата", "Упражнение", "Вес", "Повторения")
        view_tree.heading("#0", text="ID")
        view_tree.heading("Дата", text="Дата")
        view_tree.heading("Упражнение", text="Упражнение")
        view_tree.heading("Вес", text="Вес")
        view_tree.heading("Повторения", text="Повторения")
        view_tree.pack(fill=tk.BOTH, expand=True)

        for i, entry in enumerate(self.data):
            view_tree.insert("", "end", text=str(i+1), values=(
                entry["date"], entry["exercise"], entry["weight"], entry["reps"]))

    def export_to_csv(self):
        try:
            with open("training_data.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Дата", "Упражнение", "Вес", "Повторения"])
                for entry in self.data:
                    writer.writerow([entry["date"], entry["exercise"], entry["weight"], entry["reps"]])
            messagebox.showinfo("Экспорт данных", "Данные успешно экспортированы в training_data.csv")
        except Exception as e:
            messagebox.showerror("Ошибка экспорта", f"Произошла ошибка при экспорте данных: {e}")

        def import_from_csv(self):
            try:
                with open("training_data.csv", "r") as file:
                    reader = csv.DictReader(file)
                    new_data = []
                    for row in reader:
                        weight = float(row["Вес"])
                        reps = int(row["Повторения"])
                        new_data.append({
                            "date": row["Дата"],
                            "exercise": row["Упражнение"],
                            "weight": weight,
                            "reps": reps
                        })
                    self.data = new_data
                    self.save_data()
                    self.update_records_tree()
                    messagebox.showinfo("Импорт данных", "Данные успешно импортированы из training_data.csv")
            except FileNotFoundError:
                messagebox.showerror("Ошибка импорта", "Файл training_data.csv не найден.")
            except Exception as e:
                messagebox.showerror("Ошибка импорта", f"Произошла ошибка при импорте данных: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TrainingLogApp(root)
    root.mainloop()
