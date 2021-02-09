from dotenv import load_dotenv
import speedtest
import requests
import json
import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
import ssl
import sys
ssl._create_default_https_context = ssl._create_unverified_context

sched = BlockingScheduler()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

load_dotenv()

key = os.environ.get("NETWORK_ID", False)
if not key:
    key = input("Enter the network key, obtained from the ISP Logger dashboard:\t")

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

@sched.scheduled_job('interval', minutes=60)
def test():
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

test()
if len(sys.argv) == 1 or sys.argv[1] != "--one-shot":
    sched.start()