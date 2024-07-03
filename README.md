Документация для разработчиков

Описание:
Приложение "Журнал тренировок" - это графический интерфейс пользователя (GUI), разработанный с использованием библиотеки Tkinter в Python. Он позволяет пользователям вводить данные о своих тренировках, включая упражнение, вес и количество повторений, а также просматривать, экспортировать и импортировать эти данные.

Структура кода:

TrainingLogApp - основной класс, который создает и управляет интерфейсом приложения.
__init__(self, root): Инициализирует приложение, загружает данные из файла и создает виджеты.
load_data(self): Загружает данные о тренировках из файла "training_data.json".
save_data(self): Сохраняет данные о тренировках в файл "training_data.json".
create_widgets(self): Создает все виджеты интерфейса, включая поля ввода, кнопки и дерево для отображения записей.
add_entry(self): Обрабатывает добавление новой записи в журнал тренировок.
update_records_tree(self): Обновляет дерево отображения записей.
view_records(self): Открывает новое окно для просмотра всех записей.
export_to_csv(self): Экспортирует данные о тренировках в файл "training_data.csv".
import_from_csv(self): Импортирует данные о тренировках из файла "training_data.csv".
Зависимости:

tkinter: Библиотека для создания графического интерфейса пользователя.
json: Для чтения и записи данных в формате JSON.
datetime: Для получения текущей даты.
csv: Для экспорта и импорта данных в формате CSV.
Использование:

Запустите приложение, выполнив скрипт main.py.
Введите данные о тренировке (упражнение, вес, повторения) и нажмите "Добавить запись".
Просматривайте записи, нажав на кнопку "Просмотреть записи".
Экспортируйте данные в формат CSV, нажав на кнопку "Экспортировать в CSV".
Импортируйте данные из CSV-файла, нажав на кнопку "Импортировать из CSV".
Документация для пользователей

Описание:
Приложение "Журнал тренировок" позволяет вам вести учет ваших тренировок, включая упражнения, веса и количество повторений. Вы можете добавлять новые записи, просматривать все сохраненные записи, экспортировать данные в формат CSV и импортировать данные из CSV-файла.

Основные возможности:

Добавление записей: Введите информацию о вашей тренировке (упражнение, вес, количество повторений) и нажмите "Добавить запись". Ваша запись будет сохранена в журнале.
Просмотр записей: Нажмите на кнопку "Просмотреть записи", чтобы открыть окно, в котором вы можете видеть все сохраненные записи.
Экспорт в CSV: Нажмите на кнопку "Экспортировать в CSV", чтобы сохранить все ваши записи в файл "training_data.csv". Этот файл можно открыть в электронных таблицах, таких как Microsoft Excel или Google Sheets.
Импорт из CSV: Нажмите на кнопку "Импортировать из CSV", чтобы загрузить данные из файла "training_data.csv" в ваш журнал тренировок. Это может быть полезно, если вы хотите перенести данные из другого источника.
Начало работы:

Запустите приложение, дважды щелкнув по файлу main.py.
Введите информацию о вашей тренировке в соответствующие поля (упражнение, вес, количество повторений).
Нажмите кнопку "Добавить запись", чтобы сохранить вашу тренировку в журнале.
Используйте другие кнопки, чтобы просматривать, экспортировать или импортировать данные.
