import json
import time

from Controllers.PlatformController import GetPlatformById
from Controllers.UserController import GetLoginUser, GetUserInfo
from config.setting import BaseURL
from models.Account import AccountCurd
from utils.Request import get_request


def SaveAccount(account_name, avatar_path, cookie):
    account = AccountCurd()
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user = GetLoginUser()
    cookie_str = json.dumps(cookie)
    user_account = {
        "account_name": account_name,
        "account_avatar": avatar_path,
        "cookie": cookie_str,
        "operator": user.get("user_id"),
        "user_group": "",
        "status": 1,
        "create_time": create_time,
        "update_time": update_time,
        "create_user": user.get("user_id"),
        "update_user": user.get("user_id"),
    }
    account.create_account(user_account, user.get("user_id"))


def GetAccount():
    access_token = GetLoginUser().get("access_token")
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"{BaseURL}account/account/"
    user = GetUserInfo(access_token)
    if response := get_request(url, headers=headers):
        account_list = response.get("data")
        accounts = []
        for account in account_list:
            platform = account.get("from_platform")
            platform = GetPlatformById(access_token, platform)
            if account.get('create_time') == account.get('update_time'):
                update_time = account.get('create_time')
            else:
                update_time = account.get('update_time')
            new_account = {
                'username': account.get('username'),
                'account_avatar': account.get('account_avatar'),
                'account_status': account.get('account_status'),
                'update_time': update_time,
                'account_operator': user['nickname'],
                'platform_name': platform.get("platform_name"),
                'platform_avatar': platform.get("platform_icon")
            }
            accounts.append(new_account)
        return accounts


GetAccount()
