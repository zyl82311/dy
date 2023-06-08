"""
抖音自用版
by Pearson
开宝箱,宝箱广告,视频广告
6.2 修复签到
增加走路
暂时未写异常处理,bug提交https://t.me/+T8ozejX9rnkwZDE1
https://github.com/Pears0nLee/SnakeMelon
url#cookie#argus#ladon@
"""
import os
import time
import random
import base64
import requests
import json
import threading

cookies = "passport_csrf_token=23e02c6f14741421f529ada978c8c195; passport_csrf_token_default=23e02c6f14741421f529ada978c8c195; d_ticket=06f0f80f82bd38f442cd7c766f433a610f022; n_mh=Jbk5x1uAlVTr5ZD522hOIAC8cm6J9QTTKYcf6lMTuh8; odin_tt=eb2b31c36adcc7ec4d78b62ad3345c98fd05ed0dd87e6b323a7e54ccad13b91a229d11ca2f706a78e6a8dc2b8c47110cfc98403ae74c82a6502b1ed721437f4b038d593c079095433588bda75104c372; passport_assist_user=CkG7MrGIG-RbIgUMd57HA1DswTJU9nIwF3u5bvs_-PFLVmZhj7ksXcrmDCejUzpJya2p0dHowHQQ4LcILhwX-2YhzRpICjyK0HzUoPfoupGwAi2eUThYyptKwwoo0ShcXJbFhqTadIHyWPnf2aMV59phNMmWuApvgFAhAhImIL8cUPoQseCyDRiJr9ZUIgEDxPn30g%3D%3D; sessionid=91525c4f92daf9f864a0746a32e9e9be; sessionid_ss=91525c4f92daf9f864a0746a32e9e9be; sid_guard=91525c4f92daf9f864a0746a32e9e9be%7C1685671907%7C5184000%7CTue%2C+01-Aug-2023+02%3A11%3A47+GMT; sid_tt=91525c4f92daf9f864a0746a32e9e9be; uid_tt=85900d5315a75d4883de0f715f3509b5; uid_tt_ss=85900d5315a75d4883de0f715f3509b5; msToken=U1o2kTiMgOjnwBfkWPA9KMD1DhEPsNeCRZfm5v5zuOl_qx9BHylDg9TvB9WIwCdmXo8UBLk5nNXoLIoV3X2khqfgIA==; install_id=2799769091849603; ttreq=1$34883c976b83758f6bca163554b5dd8ea3d47197; store-region=cn-js; store-region-src=uid"
ua = "AwemeLite 14.9.0 rv:149005 (iPhone; iOS 14.2; zh_CN) Cronet"


class DY:
    def __init__(self, cookie):
        self.url = cookie.split("#")[0]
        self.cookie = cookie.split("#")[1]
        self.argus = cookie.split("#")[2]
        self.ladon = cookie.split("#")[3]
        self.nickname = self.get_nickname()

    def run(self):
        self.get_info()

        self.sign_in()
        time.sleep(1.5)
        self.read()
        time.sleep(1.5)
        self.open_box()
        print(f"准备看广告,假装看15s")
        time.sleep(random.randint(20, 30))
        self.box_ad()
        self.detail_info()
        time.sleep(random.randint(20, 30))
        self.detail_ad()
        step = self.get_step()
        time.sleep(0.5)
        self.read()
        time.sleep(1.5)
        self.upload_step(step)
        self.step_reward()

    def sign_in(self):
        try:
            url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/done/sign_in?{self.url}"
            headers = {
                'Host': 'api5-normal-c-lf.amemv.com',
                'Connection': 'keep-alive',
                'Content-Length': '22',
                'Accept': 'application/json',
                'Cookie': self.cookie,
                'User-Agent': ua,
                'passport-sdk-version': '5.12.1',
                'X-Argus': self.argus,
                'X-Ladon': self.ladon,
                'Content-Type': 'text/plain'}
            payload = base64.b64decode("ewogICJpbl9zcF90aW1lIiA6IDAKfQ==")
            response = requests.request("POST", url=url, headers=headers, data=payload)
            print(f"[{self.nickname}]签到成功,获取音符{response.json().get('data').get('amount')}")
        except:
            print("签到失败,可能今日已签到")

    def get_info(self):
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/page?{self.url}"
        headers = {'Host': 'api5-normal-c-lq.amemv.com',
                   'Accept': 'application/json',
                   'Cookie': self.cookie,
                   'User-Agent': ua}
        response = requests.request("GET", url=url, headers=headers)
        if response.json().get("data").get("is_login"):
            print(f"[{self.nickname}]登录成功\n"
                  f"[{self.nickname}]今日金币{response.json().get('data').get('income_data').get('amount1')}")

    def get_nickname(self):
        now = str(time.time()).replace(".", "")[:10]
        url = f"https://api5-core-c-lf.amemv.com/aweme/v1/user/profile/self/?{self.url}"
        headers = {'Host': 'api5-normal-c-lq.amemv.com',
                   'Content-Type': 'application/json; encoding=utf-8',
                   'Accept': 'application/json',
                   'tt-request-time': now,
                   'X-Argus': self.argus,
                   'X-Ladon': self.ladon,
                   'Cookie': self.cookie,
                   'User-Agent': ua}
        payload = None
        try:
            response = requests.request("GET", url=url, headers=headers, data=payload)
            nickname = response.json().get("user").get("nickname")
            return nickname
        except:
            print("获取用户名失败")

    def read(self):
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/done/read?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Content-Length': '22',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon,
            'Content-Type': 'text/plain'}
        payload = base64.b64decode("ewogICJpbl9zcF90aW1lIiA6IDAsCiAgInRhc2tfa2V5IiA6ICJyZWFkIgp9")
        response = requests.request("POST", url=url, headers=headers, data=payload)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]刷视频奖励--{response.json().get('data').get('score_amount')}")

    def open_box(self):
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/done/treasure_task?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Content-Length': '22',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon,
            'Content-Type': 'text/plain'}
        payload = base64.b64decode("ewogICJpbl9zcF90aW1lIiA6IDAKfQ==")
        response = requests.request("POST", url=url, headers=headers, data=payload)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]开宝箱奖励音符--{response.json().get('data').get('amount')}")

    def box_ad(self):
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/done/excitation_ad_treasure_box?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'X-Argus': self.argus,
            'X-Ladon': self.ladon}
        response = requests.request("POST", url=url, headers=headers)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]看宝箱广告--{response.json().get('data').get('amount')}")

    def detail_info(self):
        now = str(time.time()).replace(".", "")[:13]
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/sign_in/detail?{self.url}"
        headers = {'Host': 'api5-normal-c-lq.amemv.com',
                   'Content-Type': 'application/json; encoding=utf-8',
                   'Accept': 'application/json',
                   'tt-request-time': now,
                   'X-Argus': self.argus,
                   'X-Ladon': self.ladon,
                   'Cookie': self.cookie,
                   'User-Agent': ua}
        response = requests.request("GET", url=url, headers=headers)
        req_i = response.json().get("data").get("excitation_ad_info").get("req_id")
        ad_id = response.json().get("data").get("excitation_ad_info").get("ad_id")
        score_amount = response.json().get("data").get("excitation_ad_info").get("score_amount")
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]获取广告视频成功,预计获得{score_amount},假装看15秒")

    def detail_ad(self):
        now = str(time.time()).replace(".", "")[:13]
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/done/excitation_ad?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon}
        response = requests.request("POST", url=url, headers=headers)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]看视频奖励音符成功--{response.json().get('data').get('amount')}")

    def get_step(self):
        now = str(time.time()).replace(".", "")[:13]
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/walk/page?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon}
        response = requests.request("GET", url=url, headers=headers)
        if response.json().get("err_tips") == "成功":
            step = response.json().get("data").get("today_step")
            print(f"[{self.nickname}]当前步数{step}")
            return step
        else:
            print("走路出错")

    def upload_step(self, steps):
        now = str(time.time()).replace(".", "")[:10]
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/walk/step_submit?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon}
        step = random.randint(steps, steps + 1200)
        payload = {"step": step,
                   "submit_time": int(now),
                   "in_sp_time": 0}
        payload = json.dumps(payload)
        response = requests.request("POST", url=url, headers=headers, data=payload)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]上传步数成功,当前步数--{response.json().get('data').get('today_step')}")

    def step_reward(self):
        now = str(time.time()).replace(".", "")[:13]
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/walk/receive_step_reward?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon}
        payload = base64.b64decode("ewogICJpbl9zcF90aW1lIiA6IDAKfQ==")
        response = requests.request("POST", url=url, headers=headers, data=payload)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]领取步数奖励成功--{response.json().get('data').get('reward_amount')}")


if __name__ == "__main__":
    cookies = cookies.split("@")
    print(f"抖音激素版共获取到{len(cookies)}个账号by Pearson")
    print("bug提交https://t.me/+T8ozejX9rnkwZDE1")
    print("R18黄群不是我的,是内鬼外传改的")
    print("仓库地址,感谢点赞")
    print("https://github.com/Pears0nLee/SnakeMelon")
    i = 1
    for cookie in cookies:
        print(f"---开始第{i}个账号---")
        i += 1
        DY(cookie).run()
        time.sleep(random.randint(60, 200))
