from datetime import datetime

from db.Database import Connect


class UserTemp:
    def __init__(self):
        self.conn = Connect().__enter__()

    def insert_user(self, access_token, refresh_token, user_id, user_name, nick_name):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        SQL = """INSERT INTO user (access_token,refresh_token,status,create_time,update_time,UserId,UserName,NickName) VALUES (?,?,?,?,?,?,?,?)"""
        try:
            with self.conn as cursor:
                cursor.cur.execute(SQL, (access_token, refresh_token, 1, now, now, user_id, user_name, nick_name))
                cursor.conn.commit()
                return cursor.cur.lastrowid
        except Exception as e:
            print(e)
            return None

    def update_token(self, user_id, access_token, refresh_token):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        SQL = """UPDATE user SET access_token=?,refresh_token=?,update_time=?,status=? WHERE UserId = ?"""
        try:
            with self.conn as cursor:
                cursor.cur.execute(SQL, (access_token, refresh_token, now, 1, user_id))
                cursor.conn.commit()
        except Exception as e:
            print(e)
            return None

    def get_user(self, user_id):
        SQL = """SELECT * FROM user WHERE UserId=?"""
        try:
            with self.conn as cursor:
                cursor.cur.execute(SQL, (user_id,))
                return cursor.cur.fetchone()
        except Exception as e:
            print(e)
            return None

    def get_login(self, status):
        SQL = """SELECT * FROM user WHERE status=?"""
        try:
            with self.conn as cursor:
                cursor.cur.execute(SQL, (status,))
                return cursor.cur.fetchone()
        except Exception as e:
            print(e)
            return None

    def logout_user(self, user_id):
        SQL = """UPDATE user SET status = ? WHERE id = ?"""
        try:
            with self.conn as cursor:
                cursor.cur.execute(SQL, (0, user_id))
                cursor.conn.commit()
        except Exception as e:
            print(e)
            return None
