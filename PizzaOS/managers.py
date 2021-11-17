class UsersDBManager:
    def __init__(self, con):
        self.con = con
        self.cursor = con.cursor()

    def create_table(self):
        with open('create_users_table.sql', 'r') as f:
            self.cursor.execute(f.read())
            self.con.commit()

    def drop_table(self):
        query = """DROP TABLE USERS;"""
        self.cursor.execute(query)

    def list(self, range_id: tuple):
        query = f"""SELECT * FROM users WHERE ID BETWEEN {range_id[0]} AND {range_id[1]};"""
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        print("Результат", record)


    def create(self, request):
        username = request.get('username', 'отсутствует')
        phone = request.get('phone', 'отсутствует')
        name = request.get('name', 'отсутствует')
        query = f"""INSERT INTO users(username, phone, name) VALUES('{username}','{phone}','{name}');"""
        self.cursor.execute(query)
        self.con.commit()

    def retrieve(self, pk):
        query = f"""SELECT * FROM USERS WHERE ID={pk}"""
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        print("Результат", record)

    def update(self, request, pk):
        query = f"""UPDATE USERS SET """
        for key, item in request.items():
            query += f"""{key}='{item}',"""
        query = query[:-1]
        query += f""" WHERE ID={pk};"""
        self.cursor.execute(query)
        self.con.commit()

    def partial_update(self, request, pk):
        query = f"""UPDATE USERS SET """
        for key, item in request.items():
            query += f"""{key}='{item}',"""
        query = query[:-1]
        query += f""" WHERE ID={pk};"""
        self.cursor.execute(query)
        self.con.commit()

    def destroy(self, pk):
        query = f"""DELETE FROM USERS WHERE ID={pk};"""
        self.cursor.execute(query)
        self.con.commit()

    def __del__(self):
        self.cursor.close()
