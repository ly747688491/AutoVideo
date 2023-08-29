from config.setting import BaseURL
from models.Platform import PlatformCurd
from utils.Request import get_request


def GetPlatform():
    platform = PlatformCurd()
    plat_list = platform.find_info()
    dict_list = []
    for item in plat_list:
        item_dict = {
            "platform_title": item[0],
            "platform_icon": item[1],
            "platform_type": item[2],
            "login_url": item[3],
            "home_url": item[4],
            "avatar_selector": item[5],
            "name_selector": item[6],
            "platform_name": item[7]
        }
        dict_list.append(item_dict)
    return dict_list


def GetPlatformById(token, id):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{BaseURL}account/platform/{id}/"
    if response := get_request(url, headers=headers):
        return response.get("data")
