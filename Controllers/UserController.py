from config.setting import BaseURL
from models.User import UserTemp
from utils.Request import post_request, get_request


def UsernameLogin(user, password):
    form_data = {
        "username": user,
        "password": password,
    }
    login_url = f"{BaseURL}token/"
    if response := post_request(login_url, form_data):
        access_token = response.get("data").get("access")
        refresh_token = response.get("data").get("refresh")
        user_info = GetUserInfo(access_token)
        user_id = user_info.get("id")
        user_name = user_info.get("username")
        nick_name = user_info.get("nickname")
        user_temp = UserTemp()
        if login_user := user_temp.get_user(user_id):
            print(login_user)
            try:
                user_temp.update_token(user_id, access_token, refresh_token)
                return True
            except Exception:
                return None
        else:
            try:
                user_temp.insert_user(access_token, refresh_token, user_id, user_name, nick_name)
                return True
            except Exception:
                return None
    return False


def PhoneLogin(phone, captcha):
    print(type(phone), type(captcha))


def GetUserInfo(access_token):
    """
    获取用户信息
    :return:
    """
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"{BaseURL}system/Info/get_UserInfo/"
    if response := get_request(url, headers=headers):
        return response.get("data")
    return None


def get_username(user_id):
    """
    获取用户名等信息
    """
    user = UserTemp()
    user_info = user.get_user(user_id)
    print(user_id)
    user = {
        "username": user_info[-2],
        "nickname": user_info[-1],
    }
    return user


def GetLoginUser():
    """
    获取登录用户信息
    :return:
    """
    user = UserTemp()
    login_user = user.get_login(status=1)
    if login_user is not None:
        return {
            "access_token": login_user[1],
            "refresh_token": login_user[2],
            "status": login_user[3],
            "create_time": login_user[4],
            "update_time": login_user[5],
            "user_id": login_user[6],
            "user_name": login_user[7],
            "nick_name": login_user[8],
        }


def logoutUser(user_id):
    user = UserTemp()
    user.logout_user(user_id)
