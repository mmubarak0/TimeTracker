#!/usr/bin/python3

import time
import os
import shelve
import datetime

# TODO > start counting the time when I start this program (start_time) $START
# TODO > pause counting the time when I press P (pause_time)
# TODO > continue counting the time when I press n (continue_time)
# TODO > stop counting the time when I press q (stop_time) $STOP
# TODO > save the time spent after pressing q in status.txt
# file in days > hours > minute>second format (save_time) $TIME
# TODO > calculate the total time spent in the same format
# by all time (save_time_total) $ALL_TIME

# allTimeStart == tstart
allTimeStart = []
# allTimeStop == tstop
allTimeStop = []

etimstat = time.strftime("%I:%M:%S")
tume = datetime.datetime.now()

shelfFile = shelve.open("./db/db")
shelfFileDay = shelve.open("./db/db%s" % tume.day)


def start_time():
    startTime = time.time()
    allTimeStart.append(startTime)
    return allTimeStart


def stop_time():
    stopTime = time.time()
    allTimeStop.append(stopTime)
    return allTimeStop


# list pause time
listPauseTime = []


def addPauseTime():
    n = 0
    for i in listPauseTime:
        n = n + i
    return n


start_time()


# Old --------------------------------
def oldcode():
    # x = input("enter ")
    # if x == "p":
    #     pauseTimeStart = time.time()
    # x = input("enter ")
    # if x == "n":
    #     pauseTimeEnd = time.time()
    #     pauseTime = (pauseTimeEnd) - (pauseTimeStart)
    # pause = []
    # for i in str(pauseTime):
    #     if i == ".":
    #         break
    #     else:
    #         pause.append(i)
    # print("".join(pause))

    # x = input("enter ")
    # if x == "q":
    #     stop_time()
    #     save_time = allTimeStop[0] - allTimeStart[0] - pauseTime

    # alltime = []
    # for i in str(save_time):
    #     if i == ".":
    #         break
    #     else:
    #         alltime.append(i)
    # # print("".join(alltime))

    # START = allTimeStart[0]
    # STOP = allTimeStop[0]
    # TIME = "".join(alltime)
    # ALL_TIME = save_time

    # # print START
    # starSTART = []
    # for i in str(START):
    #     if i == ".":
    #         break
    #     else:
    #         starSTART.append(i)
    # print("".join(starSTART))
    # # print STOP
    # starSTOP = []
    # for i in str(STOP):
    #     if i == ".":
    #         break
    #     else:
    #         starSTOP.append(i)
    # print("".join(starSTOP))
    # # # print TIME
    # # starTIME = []
    # # for i in str(TIME):
    # #     if i == ".":
    # #         break
    # #     else:
    # #         starTIME.append(i)
    # # print("".join(starTIME))
    # print(TIME)
    # # print ALL_TIME
    # starALL_TIME = []
    # for i in str(ALL_TIME):
    #     if i == ".":
    #         break
    #     else:
    #         starALL_TIME.append(i)
    # print("".join(starALL_TIME))
    # addPauseTime()
    pass
# Old code --------------------------------


# Redefined code --------------------------------

print("""
the counter has been started since you see this message ...
[1] type (p) to pause the time counter, (n) to continue .
[2] type (q) to save status and quite .
[3] type (show) to show status .
[4] type (l) to make loop .
[5] type (h) to show this help message .
""")

n = True

while n:
    x = input("Press ")
    # help message
    if x == "h":
        print("""
the counter has been started since you see this message ...
[1] type (p) to pause the time counter, (n) to continue .
[2] type (q) to save status and quite .
[4] type (l) to make loop .
[5] type (h) to show this help message .
""")
    # reset the counter
    if x == "l":
        start_time()
    # pause the time counter
    if x == "p":
        pauseTimeStart = time.time()
        print("the counter has been paused press (n) to continue ....")
    # continue the time counter , save the pause time
    if x == "n":
        print("counter is now working ...")
        pauseTimeEnd = time.time()
        try:
            pauseTime = (pauseTimeEnd) - (pauseTimeStart)
        except Exception:
            pass
        # adding pause times
        try:
            listPauseTime.append(pauseTime)
        except Exception:
            pass
    # save status and quite
    if x == "q":
        stop_time()
        save_time = allTimeStop[0] - allTimeStart[0] - addPauseTime()
        seconds = round(save_time)
        minutes = round(round(save_time)/60)
        hours = round(round(save_time)/(60*60), 2)
        days = round(round(save_time)/(60*60*24), 2)

        if round(round(save_time)/(60*60), 2) >= 15:
            print(f"\ntime {seconds} seconds >> \
{minutes} minute >> \
{hours} hours >> \
{days} days  ⚠️")

        elif round(round(save_time)/(60)) < 15:
            print(f"\ntime {round(save_time)} seconds >> \
{round(round(save_time)/60, 2)} minute")

        else:
            print(f"\ntime {seconds} seconds >> \
{minutes} minute >> \
{hours} hours >> \
{days} days")
        n = False

print("\nstarted at", etimstat)
print("Ended at ", time.strftime("%I:%M:%S"))

try:
    shelfFile["cats"] += allTimeStart
    shelfFile["dogs"] += allTimeStop
    # for day
    shelfFileDay["cats"] += allTimeStart
    shelfFileDay["dogs"] += allTimeStop
except Exception:
    shelfFile["cats"] = allTimeStart
    shelfFile["dogs"] = allTimeStop
    # for day
    shelfFileDay["cats"] = allTimeStart
    shelfFileDay["dogs"] = allTimeStop

ss = shelfFile["cats"]
sp = shelfFile["dogs"]
ssday = shelfFileDay["cats"]
spday = shelfFileDay["dogs"]

TimeTakenAtThisSession = round(sp[-1] - ss[-1])
HistoryOfProgram = round((sp[-1] - ss[0]))


def total_time_today_for_this_program():
    day = []
    for i in range(len(ssday)):
        try:
            day.append(spday[-i] - ssday[-i])
        except Exception:
            break
    zday = 0
    for i in day:
        zday += i
    return zday


def total_time_from_creating_this_program():
    x = []
    for i in range(len(ss)):
        try:
            x.append(sp[-i] - ss[-i])
        except Exception:
            break
    zx = 0
    for i in x:
        zx += i
    print("total time this program was running since first launch is :")
    return zx


TOTAL = total_time_from_creating_this_program()
TOTALDAY = total_time_today_for_this_program()
shelfFile.close()

final = ('"'+str(round(TOTAL))+' seconds >> \
'+str(round(TOTAL/60, 2))+' minute >> \
'+str(round(TOTAL/60/60, 2))+' hours >> \
'+str(round(TOTAL/60/60/24, 2))+' days 💙️"')

finalday = ('"'+str(round(TOTALDAY))+' seconds >> \
'+str(round(TOTALDAY/60, 2))+' minute >> \
'+str(round(TOTALDAY/60/60, 2))+' hours >> \
'+str(round(TOTALDAY/60/60/24, 2))+' days 💙️"')

print(final)
# os.system("echo %s >> ./status.txt" % str(final))
tumme = f"{tume.day}_{tume.month}_{tume.year}"
os.system("echo %s >> ./statusdb/status%s.txt" % (str(final), tumme))
os.system("echo %s >> ./statusdb/bydays/status%s.txt" % (str(finalday), tumme))

# while True:
#     print(finalday, end="\r")
#     time.sleep(1)
#     print(final, end="\r")
#     time.sleep(1)
