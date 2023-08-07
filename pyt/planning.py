import schedule
import time
import work

from joef2t.utils.terminal import clearTerminal
# ---------------------------------------

# 20-min

dayTimes = [
    "01:25",
    "02:59",
    "03:59",
    ]

hourTimes = [
    ":17",
    ":37",
    ":57",
]
# ----------------------------

# 3/4-minute

minuteTimes = [
    ":01",
    ":04",
    ":08",
    ":12",
    ":15",    # -----
    ":21",
    ":24",
    ":28",
    ":32",
    ":35",    # -----
    ":41",
    ":44",
    ":48",
    ":52",
    ":55",    # -----
]
# --------------------
moreTimes = [
    "11:46",
    "11:50",
    "11:54",
    "12:06",
    "12:19",
    "12:26",
    "12:30",
    "12:39",    # -----
    "17:46",
    "17:50",
    "17:54",
    "18:06",
    "18:19",
    "18:26",
    "18:30",
    "18:39",    # -----
]

# ---------------------------------------
# for mt in minuteTimes + moreTimes:
#     schedule.every().hour.at(mt).do( work.minutely )

for ht in hourTimes:
    schedule.every().hour.at(ht).do( work.hourly )


for dt in dayTimes:
    schedule.every().day.at(dt).do( work.daily )

# ---------------------------------------

# clear termimal every hour
schedule.every().hour.at(":20").do( clearTerminal )
schedule.every().hour.at(":47").do( clearTerminal )
# --------------------------------------------------
while True:
    schedule.run_pending()
    time.sleep(1)
