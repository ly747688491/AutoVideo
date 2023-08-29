ADD_BUTTON_ICON = "resources/ButtonIcon/Add.png"
IMPORT_BUTTON_ICON = "resources/ButtonIcon/import.png"
DEFAULT_AVATAR = "resources/Avatar.png"
SYSTEM_LOGO = "resources/logo.png"
EXECUTABLE_PATH = "utils/chromedriver/chromedriver.exe"
AVATAR_PATH = "resources/AccountAvatar"
COOKIE_DELAY = 1000 * 30

ERROR_MESSAGE_DICT = {
    "unread_user_agree": {"title": "错误", "content": "请阅读并同意用户协议", "isClosable": False, "duration": 2000},
    "password_format_error": {"title": "密码格式错误",
                              "content": "必须包含大小写字母和数字的组合，可以使用特殊字符，长度在6-20之间",
                              "isClosable": False, "duration": 2000},
    "missing_username_or_password": {"title": "错误", "content": "请输入用户名和密码", "isClosable": False,
                                     "duration": 2000},
}

BaseURL = "http://127.0.0.1:8000/api/"
