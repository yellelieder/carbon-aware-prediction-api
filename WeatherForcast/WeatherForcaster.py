import logging
import requests
import json
import logging

WEATHER_DATA_API_KEY="89f83e40489b5e87c4cb16463dc68b42"

log=logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler=logging.FileHandler("weatherdata.log")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(funcName)s:%(message)s"))
log.addHandler(handler)

def getUrl(lat, lng):
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
            Url with correct parameter for requesting weather data.
    '''
    log.info(f"converting {lat} and {lng} to weather api url")
    return f"https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lng}&units=metric&appid={WEATHER_DATA_API_KEY}"


#https://openweathermap.org/api/one-call-api
def getForcast(lat, lng):
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
    """Converts geo coordinates in wind and sun prediction."""
    #start und ende in unix
    log.info(f"request weather api")
    response=requests.get(getUrl(lat,lng)).json()
    return response

if __name__=="__main__":
    #nur wenn Anfrage in den nächsten 30 Tage
    #dann genau für den Zeitraum
    print(json.dumps(getForcast("51.4582235","7.0158171"), indent=1))

#sonnenstunden
#uv index
#windstärke