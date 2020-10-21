import psycopg2 as pc
import prettytable


def basis_function(user_id, name, age, email):
    """
    Функция по изменённому значению выбирает параметр для дальнейшей обработки
    """
    selection_parameter = [None, None]
    if user_id is not None:
        selection_parameter[0] = 'id'
        selection_parameter[1] = user_id
    elif name is not None:
        selection_parameter[0] = 'name'
        selection_parameter[1] = name
    elif age is not None:
        selection_parameter[0] = 'age'
        selection_parameter[1] = age
    else:
        selection_parameter[0] = 'email'
        selection_parameter[1] = email
    return selection_parameter


# main class
class Worker:

    def __init__(self, table_name='Worker'):
        self.table_name = table_name
        self.db_cursor = None
        self.db_connection = None

    def print(self, record_tracker=0):
        """
        Метод печатает часть таблицы, на которую падает курсор
        """
        count = 0
        description_list = [self.db_cursor.description[index][0] for index, _ in enumerate(self.db_cursor.description)]
        table = prettytable.PrettyTable(description_list)
        for row in self.db_cursor:
            table.add_row(row)
            count += 1
        print(table)
        if record_tracker == 1:
            print(f'{count} совпадений')
        print()

    def connection(self):
        # подключение к дб
        if self.db_connection is None:
            self.db_connection = pc.connect(database="python",
                                            user="postgres",
                                            password="69420A1X")
        # курсор
        if self.db_cursor is None:
            self.db_cursor = self.db_connection.cursor()

    def create_table(self):
        """
        Создание таблицы
        """
        self.connection()
        self.db_cursor.execute(f'CREATE TABLE IF NOT EXISTS {self.table_name}' +
                               '(id BIGSERIAL NOT NULL PRIMARY KEY,' +
                               'name VARCHAR(50) NOT NULL,' +
                               'age INT NOT NULL,' +
                               'email VARCHAR(50));')
        print(f'Таблица {self.table_name} готова к использованию')
        self.db_connection.commit()

    def insert(self, name, age, email=None):
        """
        Вставка новой строки в таблицу с возможностью не писать поле email
        """
        default_sense = [None, None]
        default_sense[0] = 'email, '
        if email is not None:
            default_sense[1] = email
        self.db_cursor.execute(f"INSERT INTO {self.table_name} ({default_sense[0]}name, age) VALUES ('{default_sense[1]}', '{name}', {age})")
        self.db_connection.commit()
        print('Вставка завершена')
        self.get_all()

    def update(self, object_to_change, name=None, age=None, email=None):
        """
        Изменение полей по параметру object_to_change (Должно быть передано имя объекта, например: id/name/age/email)
        """
        selection_parameter = basis_function(None, name, age, email)
        self.db_cursor.execute(f"UPDATE {self.table_name} SET {selection_parameter[0]} = '{selection_parameter[1]}' WHERE "
                               f"{object_to_change[0]} = '{object_to_change[1]}';")
        self.db_connection.commit()
        print('Обноление завершено')
        self.get_all()

    def delete(self, user_id=None, name=None, age=None, email=None):
        """
        Удаление строк по id/имени/возрасту/почтовому адресу
        """
        try:
            selection_parameter = basis_function(user_id, name, age, email)
            self.db_cursor.execute(f"DELETE FROM {self.table_name} WHERE "
                                   f"{selection_parameter[0]} = '{selection_parameter[1]}';")
            self.db_connection.commit()
            print('Удаление завершено')
            self.get_all()
        except(Exception, pc.errors.InvalidTextRepresentation):
            print('Неправильный ввод')

    def get(self, user_id=None, name=None, age=None, email=None):
        """
        Получение строк с входными параметрами id/имени/возраста/почтового адреса
        """
        try:
            selection_parameter = basis_function(user_id, name, age, email)
            self.db_cursor.execute(f"SELECT * FROM {self.table_name} WHERE "
                                   f"{selection_parameter[0]} = '{selection_parameter[1]}';")
            self.print(record_tracker=1)
        except(Exception, pc.errors.InvalidTextRepresentation):
            print('Неправильный ввод')

    def get_all(self):
        """
        Получение и вывод всех элементов таблицы
        """
        self.db_cursor.execute(f'SELECT * FROM {self.table_name} ORDER BY id;')
        self.print()

    def drop(self):
        """
        Удаление таблицы
        """
        self.db_cursor.execute(f'DROP TABLE {self.table_name};')
        self.db_connection.commit()
        print('Таблица удалена')

    def close(self):
        """
        Отключение от курсора и сервера
        """
        if not self.db_cursor.closed:
            self.db_cursor.close()
        if not self.db_connection.closed:
            self.db_connection.close()

    def __del__(self):
        self.close()
        print('\n/////////////////////////////\n')
        print('Курсор закрыт')
        print('Соединение завершено')


a = Worker()
a.create_table()
a.get_all()
a.insert(name='Armen', age=20)
a.insert(name='Maria', age=19, email='qwerty@mail.ru')
a.insert(name='Oleg', age=21)
a.insert(name='Dmitriy', age=23, email='dmitriy99@yandex.ru')
a.insert(name='Olga', age=18)
a.insert(name='Artem', age=25)
a.insert(name='Olga', age=19)
a.get(age=19)
a.update(['email', None], email='emailisnone')
a.update(['id', 5], age=19)
a.drop()
