import sqlite3
import pandas as pd

class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            user_id int NOT NULL,
            full_name varchar(255) NOT NULL,
            language varchar(3) NOT NULL,
            PRIMARY KEY (user_id)
            );
"""
        self.execute(sql, commit=True)

    def create_table_kirim(self):
        sql = """
        CREATE TABLE Kirim (
            type varchar(255) NOT NULL,
            name varchar(255) NOT NULL,
            value varchar(31) NOT NULL,
            date varchar(31) NOT NULL, 
            user_id int NOT NULL
            );
"""
        self.execute(sql, commit=True)

    def create_table_chiqim(self):
        sql = """
        CREATE TABLE Chiqim (
            type varchar(255) NOT NULL,
            name varchar(255) NOT NULL,
            value varchar(31) NOT NULL,
            date varchar(31) NOT NULL, 
            user_id int NOT NULL
            );
"""
        self.execute(sql, commit=True)
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, user_id: int, full_name: str,  language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(user_id, full_name, language) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(user_id, full_name, language), commit=True)

    def add_kirim(self, type: str, name: str, value: str, date: str,  user_id: int):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Kirim(type, name, value, date, user_id) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(type, name, value, date, user_id), commit=True)

    def add_chiqim(self, type: str, name: str, value: str, date: str,  user_id: int):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Chiqim(type, name, value, date, user_id) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(type, name, value, date, user_id), commit=True)
    def select_all_users(self):
        sql = """
        SELECT user_id FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_language(self, user_id, language):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET language=? WHERE user_id=?
        """
        return self.execute(sql, parameters=(language, user_id), commit=True)


    # total time
    def get_kirim(self, user_id):
        sql = "SELECT type, name, value, date FROM Kirim WHERE user_id == ? "
        data = self.execute(sql, parameters=(user_id,), fetchall=True)
        return pd.DataFrame(data, columns=['Turi', 'Izoh', 'Qiymati', 'Sana'])
    ##################
    def get_chiqim(self, **kwargs):
        sql = "SELECT type, name, value, date FROM Chiqim WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        data = self.execute(sql, parameters=parameters, fetchall=True)
        return pd.DataFrame(data, columns=['Turi', 'Izoh', 'Qiymati', 'Sana'])
    # last 30 days
    def get_kirim_30(self, date, user_id):
        sql = f"""
                SELECT type, name, value, date FROM Kirim 
                WHERE date >= ? AND user_id = ?
                """
        data = self.execute(sql, parameters=(date, user_id), fetchall=True)
        return pd.DataFrame(data, columns=['Turi', 'Izoh', 'Qiymati', 'Sana'])
    ##################
    def get_chiqim_30(self, date, user_id):
        sql = f"""
                SELECT type, name, value, date FROM Chiqim 
                WHERE datetime(date) >= ? and user_id == ?
                """
        data = self.execute(sql, parameters=(date, user_id), fetchall=True)
        return pd.DataFrame(data, columns=['Turi', 'Izoh', 'Qiymati', 'Sana'])
    # starts month
    def get_kirim_month(self, date, user_id):

        sql = f"""
                SELECT type, name, value, date FROM Kirim 
                WHERE date >= ? AND user_id = ?
                """
        data = self.execute(sql, parameters=(date, user_id), fetchall=True)

        return pd.DataFrame(data, columns=['type', 'name', 'value', 'date'])

    ##################
    def get_chiqim_month(self, date, user_id):
        sql = f"""
                SELECT type, name, value, date FROM Chiqim 
                WHERE datetime(date) >= ? and user_id == ?
                """
        data = self.execute(sql, parameters=(date, user_id), fetchall=True)
        return pd.DataFrame(data, columns=['type', 'name', 'value', 'date'])
def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")