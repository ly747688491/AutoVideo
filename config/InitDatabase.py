DATABASE_NAME = "UserData.db"
CREATE_PLATFORM = """
CREATE TABLE IF NOT EXISTS `platform` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `platform_name` TEXT NOT NULL,
  `platform_icon` TEXT NOT NULL,
  `platform_type` TEXT DEFAULT 1,
  `login_url` TEXT NOT NULL ,
  `home_url` TEXT NOT NULL ,
  `create_time` TEXT NOT NULL,
  `update_time` TEXT NOT NULL,
  `create_user` INTEGER,
  `update_user` INTEGER,
  `index` TEXT NOT NULL,
  UNIQUE(`index`) ON CONFLICT REPLACE
);
"""
CREATE_ACCOUNT = """
CREATE TABLE IF NOT EXISTS `account` (
  `id` INTEGER PRIMARY KEY,
  `account_name` TEXT NOT NULL,
  `account_avatar` TEXT NOT NULL,
  `cookie` TEXT NOT NULL,
  `operator` INTEGER NOT NULL,
  `user_group` INTEGER,
  `status` INTEGER NOT NULL,
  `create_time` TEXT NOT NULL,
  `update_time` TEXT NOT NULL,
  `create_user` INTEGER,
  `update_user` INTEGER
);
"""
CREATE_USER = """
CREATE TABLE IF NOT EXISTS `user` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `access_token` TEXT NOT NULL,
  `refresh_token` TEXT NOT NULL,
  `status` INTEGER NOT NULL,
  `create_time` TEXT NOT NULL,
  `update_time` TEXT NOT NULL
  )
"""
TABLE_DATA = [
    {
        "name": "Platform",
        "comment": "平台表",
        "create_sql": CREATE_PLATFORM,
        "default_value": ""
    },
    {
        "name": "account",
        "comment": "账户表",
        "create_sql": CREATE_ACCOUNT,
        "default_value": ""
    },
]
