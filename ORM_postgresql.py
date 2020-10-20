import psycopg2 as pc


# validation
class PositiveInteger:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('Нужно целое число')
        elif value < 0:
            raise ValueError('Нужно положительное число')
        instance.__dict__[self.name] = value


# main class
class Worker:
    id = PositiveInteger()
    age = PositiveInteger()

    def __init__(self, table_name='Worker'):
        self.table_name = table_name
        self.db_cursor = None
        self.db_connection = None

    def connection(self):
        # connect to the db
        self.db_connection = pc.connect(database="python",
                                        user="postgres",
                                        password="69420A1X")

        # cursor
        self.db_cursor = self.db_connection.cursor()

    def create_table(self):
        self.connection()
        self.db_cursor.execute(f'CREATE TABLE IF NOT EXISTS {self.table_name}' +
                               '(id INT PRIMARY KEY NOT NULL,' +
                               'name VARCHAR(50) NOT NULL,' +
                               'age INT NOT NULL,' +
                               'email VARCHAR(50));')
        print(f'Таблица {self.table_name} создана')
        self.db_connection.commit()

    def drop(self):
        self.db_cursor.execute(f'DROP TABLE {self.table_name};')
        self.db_connection.commit()
        print('Таблица удалена')

    def close(self):
        self.db_cursor.close()
        self.db_connection.close()

    def __del__(self):
        self.close()
        print('Курсор закрыт')
        print('Соединение завершено')


a = Worker()
a.create_table()
a.drop()
