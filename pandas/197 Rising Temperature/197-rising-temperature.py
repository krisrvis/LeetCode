import pandas as pd
import datetime as dt

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    w = weather.sort_values(by="recordDate", ascending=True)
    w["tempdiff"] = w["temperature"].diff()
    w["datediff"] = w["recordDate"].diff().dt.days
    return w[(w["tempdiff"] > 0) & (w["datediff"] == 1)]