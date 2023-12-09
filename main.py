from datetime import datetime
from dateutil import tz

utc_dt = datetime.now(timezone.utc)  # UTC time
ch_dt = utc_dt.astimezone(tz.gettz("Europe/Zurich"))

with open("timestamps.txt", "a") as f:
    f.write(ch_dt.isoformat() + "\n")
