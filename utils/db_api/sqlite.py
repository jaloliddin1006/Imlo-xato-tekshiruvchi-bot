import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
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
            id int NOT NULL,
            Name varchar(95) NOT NULL,
            user_mintaqa varchar(95),
            user_mintaqa_nomi varchar(95),
            tabrik_ism varchar(95),
            tabrik_tr int,
            date_of_start date,
            check_sub int,
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, tabrik_ism: str = None, date_of_start: str = 'uz', check_sub: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, tabrik_ism) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, tabrik_ism, date_of_start, check_sub) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, tabrik_ism, date_of_start, check_sub), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_check_sub(self):
        sql = """
        SELECT id FROM Users WHERE check_sub = 1
        """
        return self.execute(sql, fetchall=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_mintaqa(self, user_mintaqa, user_mintaqa_nomi, id):
        # SQL_EXAMPLE = "UPDATE Users SET tabrik_ism=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET user_mintaqa=?, user_mintaqa_nomi = ? WHERE id=?
        """
        return self.execute(sql, parameters=(user_mintaqa, user_mintaqa_nomi, id), commit=True)

    def update_check_sub(self, check_sub, id):
        # SQL_EXAMPLE = "UPDATE Users SET tabrik_ism=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET check_sub=? WHERE id=?
        """
        return self.execute(sql, parameters=(check_sub, id), commit=True)

    def update_user_tabrik_ism(self, tabrik_ism, id):
        # SQL_EXAMPLE = "UPDATE Users SET tabrik_ism=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET tabrik_ism=? WHERE id=?
        """
        return self.execute(sql, parameters=(tabrik_ism, id), commit=True)

    def update_user_tabrik_tr(self, tabrik_tr, id):
        # SQL_EXAMPLE = "UPDATE Users SET tabrik_tr=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET tabrik_tr=? WHERE id=?
        """
        return self.execute(sql, parameters=(tabrik_tr, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    pass
#     print(f"""
# _____________________________________________________        
# Executing: 
# {statement}
# _____________________________________________________
# """)
