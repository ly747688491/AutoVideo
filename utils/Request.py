import requests
from qfluentwidgets import InfoBar


def post_request(url, data):
    """
    发送post请求
    :param url: 请求地址
    :param data: 请求数据
    :return: 返回响应数据
    """
    try:
        response = requests.post(url, data)
        return response.json()
    except Exception:
        InfoBar.error(
            title="登录失败",
            content="服务器请求错误",
            duration=6000
        )


def get_request(url, data=None, headers=None):
    """
    发送get请求
    :param url: 请求地址
    :return: 返回响应数据
    """
    try:
        response = requests.get(url, data=data, headers=headers)
        return response.json()
    except Exception as e:
        InfoBar.error(
            title="登录失败",
            content=e,
            duration=6000
        )


def put_request(url, data):
    """
    发送put请求
    :param url: 请求地址
    :param data: 请求数据
    :return: 返回响应数据
    """
    response = requests.put(url, data)
    return response.text


def delete_request(url, data):
    """
    发送delete请求
    :param url: 请求地址
    :param data: 请求数据
    :return: 返回响应数据
    """
    response = requests.delete(url, data)
    return response.text


def patch_request(url, data):
    """
    发送patch请求
    :param url: 请求地址
    :param data: 请求数据
    :return: 返回响应数据
    """
    response = requests.patch(url, data)
    return response.text
