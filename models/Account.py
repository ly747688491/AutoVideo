from db.Database import Connect


class AccountCurd:
    def __init__(self):
        self.conn = Connect().__enter__()

    def create_account(self, account, user_id):
        try:
            query = """INSERT INTO account (account_name, account_avatar, cookie, operator, user_group, status,
             create_time, update_time, create_user, update_user,user_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)"""
            with self.conn as c:
                c.cur.execute(
                    query,
                    (
                        account["account_name"],
                        account["account_avatar"],
                        account["cookie"],
                        account["operator"],
                        account["user_group"],
                        account["status"],
                        account["create_time"],
                        account["update_time"],
                        account["create_user"],
                        account["update_user"],
                        user_id
                    ),
                )
                c.conn.commit()
                return c.cur.lastrowid
        except Exception as e:
            print(e)

    def read_account(self, user_id):
        with self.conn as c:
            c.cur.execute("SELECT * FROM account WHERE user_id = ?", (user_id,))
            account = c.cur.fetchall()
        return account

    def update_account(self, account_id, account):
        with self.conn as c:
            c.cur.execute(
                """
                UPDATE account
                SET account_name = ?, account_avatar = ?, cookie = ?, operator = ?, user_group = ?, status = ?, 
                create_time = ?, update_time = ?, create_user = ?, update_user = ?
                WHERE id = ?
            """,
                (
                    account["account_name"],
                    account["account_avatar"],
                    account["cookie"],
                    account["operator"],
                    account["user_group"],
                    account["status"],
                    account["create_time"],
                    account["update_time"],
                    account["create_user"],
                    account["update_user"],
                    account_id,
                ),
            )
            c.conn.commit()

    def delete_account(self, account_id):
        with self.conn as c:
            c.cur.execute("DELETE FROM account WHERE id = ?", (account_id,))
            c.conn.commit()
