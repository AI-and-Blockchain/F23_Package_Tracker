import pandas as pd
from sodapy import Socrata

if __name__ == "__main__":
    # Attach client
    client = Socrata("data.cityofnewyork.us", "HTWuJPdtrL0DEPqucNNvJ1d68", "grajec@rpi.edu", "ChaseBlake!2001") 
    
    # Graph test query
    # Query: All segment ids for boro=Manhattan AND year>=2015
    # Total points: 6127170
    # https://data.cityofnewyork.us/resource/7ym2-wayt -> Date-Time by borough
    # https://data.cityofnewyork.us/resource/btm5-ppia -> Smaller date-time
    # https://data.cityofnewyork.us/resource/tyzs-7edu -> Speed limit by street
    print("Collecting data...")
    data = client.get("7ym2-wayt", where="boro='Manhattan' AND yr=2014", limit=4000000)
    print(f"Length of full dataset: {len(data)}")
    
    df = pd.DataFrame.from_records(data)
    df.to_csv("out.csv")
    print("Completed")