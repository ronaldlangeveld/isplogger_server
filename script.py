from dotenv import load_dotenv
import speedtest
import requests
import json
import datetime
import time
import os
import logging
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

load_dotenv()

key = os.environ.get("NETWORK_ID", False)
interval = int(os.environ.get("INTERVAL", 60)) * 60
server = "https://api.isplogger.com"

def initSpeedtest():
    print("Speedtest in Progress")
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    data = {
            "status": "success",
            "upload": int(res["upload"]),
            "download": int(res["download"]),
            "ping": res["ping"],
            "isp": res["client"]["isp"],
            "ip": res["client"]["ip"],
            "country": res["client"]["country"],
            "sent": res["bytes_sent"],
            "received": res["bytes_received"]
        }

    return data

def test(key):
    attempts = 10
    for i in range(attempts):

        try:

            tst = initSpeedtest()
            req = requests.post(server + "/api/speedtest/"+key, data=tst)
            print("Test complete")
            return "OK"

        except Exception as e:
            print(e)
            if i < attempts - 1:
                pass
                return "error"
            else:
                raise
        break

if key is False:
    key = input("Enter the network key, obtained from the ISP Logger dashboard:  ")
    # print(key)

while (1):
    test(key)
    time.sleep(interval)
    
