from db.Database import Connect


class PlatformCurd:

    def find_by_id(self, id):
        with Connect() as conn:
            query = "SELECT * FROM platform WHERE id = ?"
            conn.cur.execute(query, (id,))
            return conn.cur.fetchone()

    def find_by_create_user(self, create_user):
        with Connect() as conn:
            query = "SELECT * FROM platform WHERE create_user = ?"
            conn.cur.execute(query, (create_user,))
            return conn.cur.fetchall()

    def find_info(self):
        with Connect() as conn:
            query = "SELECT platform_name, platform_icon, platform_type, login_url, home_url, " \
                    " avatar_selector,name_selector,platform_title FROM platform"
            conn.cur.execute(query)
            return conn.cur.fetchall()

    def insert_all_fields(self, platform_name, platform_icon, platform_type, login_url, home_url, create_time,
                          update_time,
                          create_user, update_user, avatar_xpath, username_xpath, platform_title):
        with Connect() as conn:
            query = "INSERT INTO platform " \
                    "(platform_name, platform_icon, platform_type, login_url, home_url, create_time, " \
                    "update_time, create_user, update_user,avatar_selector,name_selector,platform_title)" \
                    " VALUES (?,?,?, ?, ?, ?,  ?, ?, ?, ?, ?,?)"
            conn.cur.execute(query, (platform_name, platform_icon, platform_type, login_url, home_url, create_time,
                                     update_time, create_user, update_user, avatar_xpath,
                                     username_xpath, platform_title))
            conn.conn.commit()
            return True

    def insert_non_null_fields(self, platform_name, platform_icon, login_url, home_url, create_time, update_time,
                               create_user,
                               additional_index, avatar_xpath, username_xpath, platform_title):
        with Connect() as conn:
            query = "INSERT INTO platform (platform_name, platform_icon, login_url, home_url, create_time, " \
                    "update_time, " \
                    "create_user,avatar_selector,name_selector,platform_title) " \
                    "VALUES (?, ?, ?, ?, ?, ?, ?,?,?,?)"
            conn.cur.execute(
                query, (platform_name, platform_icon, login_url, home_url, create_time, update_time, create_user,
                        additional_index, avatar_xpath, username_xpath, platform_title))
            conn.conn.commit()
            return True
