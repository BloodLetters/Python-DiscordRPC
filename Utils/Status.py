import time
from pypresence import Presence
from JsonReader import *
from Utils.Time import *

useTimer = 1
    


def Run():
    client_id = getClientId()
    RPC = Presence(client_id)
    RPC.connect()
    start_time = time.time()
    RPC.update(state=getState(), details=getDetails(), start=start_time, large_image=getlargeIcon(),
               small_text=getSmallText(), small_image=getSmallIcon(), large_text=getLargeText(),
               buttons=[
                   {"label": getButton("1", False), "url": getButton("1", True)},
                   {"label": getButton("2", False), "url": getButton("2", True)}
               ])

    print("RPC -> Rich Presence Has Started!")
    i = 0
    while True:
        if useTimer == 1:
            print("[" + getHour() + ":" + getMinute() + ":" + getSecond() + "]" + " Rpc ReLoaded")
            time.sleep(reloadTime())
        else:
            i = i + 1
            print("[" + str(i) + "]" + " Rpc ReLoaded!")
            time.sleep(reloadTime())
