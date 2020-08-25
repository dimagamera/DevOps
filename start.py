import requests


class privat:
    def __init__(self):
        URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
        responce = requests.get(URL)
        data = responce.json()
        self.show_currencies(data)

    def show_currencies(self, data):
        for item in data:
            print(item["ccy"] + " " + item["base_ccy"] +
                  " " + item["buy"] + " | " + item["sale"])


class weather:
    def __init__(self):
        URL = "https://samples.openweathermap.org/data/2.5/find?q=Dubno&units=metric&appid=439d4b804bc8187953eb36d2a8c26a02"
        responce = requests.get(URL)
        data = responce.json()
        temp = data['list']
        for item in temp:
            min_t = item['main']['temp_min']
            max_t = item['main']['temp_max']
        print("Мінімальна температура: ", min_t,
              "\nМаксимальна температура:", max_t)


if __name__ == "__main__":
    a = privat()
    a.show_currencies('')
    weather()
