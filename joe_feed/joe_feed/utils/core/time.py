import datetime
import pytz

def get_current_utc0():
  now = datetime.datetime.now(pytz.utc)
  return now

if __name__ == "__main__":
  now = get_current_utc0()
  print(f"The current utc0 is {now}.")
