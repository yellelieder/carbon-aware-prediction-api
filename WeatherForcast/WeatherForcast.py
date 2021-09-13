import logging
import requests
import json
import logging
from datetime import datetime

WEATHER_DATA_API_KEY="89f83e40489b5e87c4cb16463dc68b42"

log=logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler=logging.FileHandler("logs.log")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(funcName)s:%(message)s"))
log.addHandler(handler)

def get_url(lat, lng):
    '''
    Turns geo-coordinates in weather api url.

        Parameters:
        ----------

        lat : str
            Lattitude of the place where energy is going to be consumed.

        lng : str
            Longitude of the place where energy is going to be consumed.

        Returns:
        ----------

        url : str
            Url with correct parameter for requesting weather data.yoy
    '''
    #starts at last full hour, if it is 7:30 now, first return is 6
    no_of_hours=12
    log.info(f"converting {lat} and {lng} to weather api url")
    return f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lng}&cnt={no_of_hours}&units=metric&appid={WEATHER_DATA_API_KEY}"


#https://openweathermap.org/api/one-call-api
def get_forcast(lat, lng, hours_from_now, hours_total):
    '''
    Turns geo-coordinates in weather forcast.

        Parameters:
        ----------

        lat : str
            Lattitude of the place where energy is going to be consumed.

        lng : str
            Longitude of the place where energy is going to be consumed.

        Returns:
        ----------

        response : str
            Weather forcast for wind and sun, for timeframe requested.
    '''
    #start und ende in unix
    log.info(f"request weather api")
    #response=requests.get(get_url(lat,lng)).json()
    return requests.get(get_url(lat,lng)).json()["list"][hours_from_now:hours_from_now+hours_total]

if __name__=="__main__":
    #nur wenn Anfrage in den nächsten 30 Tage
    #dann genau für den Zeitraum
    #print(json.dumps(get_forcast("51.4582235","7.0158171", 3,2), indent=1))
    forcast = get_forcast("51.4582235","7.0158171", 3,5)
    for i in forcast:
        print("\nTime: ",datetime.utcfromtimestamp(i["dt"]).strftime('%d.%m.%Y %H:%M'))
        print("Cloudiness: ",i["clouds"]["all"],"%")
        print("Wind: ",i["wind"]["speed"],"meters/second")
        

#sonnenstunden
#uv index
#windstärke