import datetime
import pytz

def get_current_utc0():
  now = datetime.datetime.now(pytz.utc)
  return now

def timestamp2utc0(unix_timestamp):
  gmt_datetime = datetime.datetime.utcfromtimestamp(unix_timestamp)
  print(f"UTC datetime: {gmt_datetime}")
  return gmt_datetime

if __name__ == "__main__":
  # now = get_current_utc0()
  # print(f"The current utc0 is {now}.")

  timestamp2utc0(1679815620)
