import requests
from boto3.session import Session
import boto3

class privat:
    def __init__(self):
        URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
        responce = requests.get(URL)
        data = responce.json()
        self.show_currencies(data)

    def show_currencies(self, data):
        f = open('currenc.txt', 'w')
        for item in data:
            print(item["ccy"] + " " + item["base_ccy"] +
                  " " + item["buy"] + " | " + item["sale"])
            f.write(item["ccy"] + " " + item["base_ccy"] +
                    " " + item["buy"] + " | " + item["sale"]+"\n")
        f.close


class weather:
    def __init__(self):
        URL = "https://samples.openweathermap.org/data/2.5/find?q=Dubno&units=metric&appid=439d4b804bc8187953eb36d2a8c26a02"
        responce = requests.get(URL)
        data = responce.json()
        self.show_weather(data)
        self.s3()

    def show_weather(self, data):
        temp = data['list']
        f = open('weather.txt', 'w', encoding='UTF8')
        for item in temp:
            min_t = item['main']['temp_min']
            max_t = item['main']['temp_max']
            print("Мінімальна температура: " + str(min_t) +
                  "\nМаксимальна температура: " + str(max_t))
            f.write("Мінімальна температура: " + str(min_t) +
                    "\nМаксимальна температура: " + str(max_t))
        f.close

    def s3(self):
        bucketname = "dubnobucket"
        file_name = "weather.txt"
        s3 = boto3.client('s3')
        s3.upload_file(file_name, bucketname, file_name)


if __name__ == "__main__":
    privat()
    weather()
