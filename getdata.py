import pandas as pd
from sodapy import Socrata

USER = "" # NYC Open Data username
PASS = "" # NYC Open Data password

def PullYear(client, year, fname):
    try:
        data = client.get("7ym2-wayt", where=f"boro='Manhattan' AND yr={year}", limit=4000000)
        df = pd.DataFrame.from_records(data)
        df.to_csv(fname)
        print(f"Success, length of pulled dataset: {len(data)}")
    except:
        print("Failed to contact server")

def PullSpeedLimits(client, fname):
    try:
        data = client.get("tyzs-7edu", select="street, postvz_sl", limit=4000000)
        df = pd.DataFrame.from_records(data)
        df.to_csv(fname)
        print(f"Success, length of pulled dataset: {len(data)}")
    except:
        print("Failed to contact server")
    

if __name__ == "__main__":
    # Attach client
    # Must have an account, otherwise download will be rate limited
    client = Socrata("data.cityofnewyork.us", "HTWuJPdtrL0DEPqucNNvJ1d68", USER, PASS)
    
    # https://data.cityofnewyork.us/resource/7ym2-wayt -> Date-Time by borough
    # https://data.cityofnewyork.us/resource/tyzs-7edu -> Speed limit by street
    PullYear(client, 2014, "2014-volumes.csv")
    PullYear(client, 2015, "2015-volumes.csv")
    PullYear(client, 2016, "2016-volumes.csv")
    PullSpeedLimits(client, "speeds.csv")