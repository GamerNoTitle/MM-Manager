import requests as r

Logged = False


def __init__():
    global session
    session = r.session()


def Login(email, password):
    response = session.get('https://mox.moe/login.php')     # 获得未登录状态下的cookie
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': response.cookies,     # 设置未登录状态下的cookie
        'DNT': 1,
        'Host': 'mox.moe',
        'Referer': 'https://mox.moe/my.php',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
    }
    payload = {     # 构造登录使用的Payload
        'email': email,
        'passwd': password,
        'keepalive': 'on'
    }
    response = session.post('https://mox.moe/login_do.php',
                            params=payload, headers=headers)    # 登录
    if response.status_code == 200:
        global Logged
        Logged = True       # 设置为已登录状态
        return session
    else:
        return False


def GetPersonInfo(sessions):
    data = {
        'id': 0,
        'email': '',
        'name': '',
        'avatar': '',
        'level': 0,
        'default_format': '',
        'target_email': '',
        'push_email': '',
        'validate_time': ''
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': sessions.cookies,
        'DNT': 1,
        'Host': 'mox.moe',
        'Referer': 'https://mox.moe/my.php',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
    }

    My = sessions.get('https://mox.moe/my.php', headers=headers)


def Logout(sessions):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': sessions.cookies,
        'DNT': 1,
        'Host': 'mox.moe',
        'Referer': 'https://mox.moe/my.php',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
    }
    session.get('https://mox.moe/logout.php', headers=headers)      # 登出
    global Logged
    Logged = False      # 设置为未登录


if __name__ == '__main__':
    email = input('请输入邮箱：')
    password = input('请输入密码：')
    LocalSession = Login(email, password)
