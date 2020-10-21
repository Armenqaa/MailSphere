import psycopg2 as pc
import prettytable


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
                               '(id BIGSERIAL NOT NULL PRIMARY KEY,' +
                               'name VARCHAR(50) NOT NULL,' +
                               'age INT NOT NULL,' +
                               'email VARCHAR(50));')
        print(f'Таблица {self.table_name} готова к использованию')
        self.db_connection.commit()

    def get_all(self):
        self.db_cursor.execute(f'SELECT * FROM {self.table_name};')
        description_list = []
        for index, _ in enumerate(self.db_cursor.description):
            description_list.append(self.db_cursor.description[index][0])
        table = prettytable.PrettyTable(description_list)
        for row in self.db_cursor:
            table.add_row(row)
        print(table)

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
a.get_all()
# a.drop()
