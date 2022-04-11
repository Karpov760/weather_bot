import requests
from pprint import pprint
token ='9bdb588bbe6b4e7884a105739220804'

def get_weather(city):
    try:
        r = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={token}&q={city}"
        )
        data = r.json()
        #pprint(data)
        temp_c = data['current']['temp_c']
        feelslike_c = data['current']['feelslike_c']
        wind_s = round(int(data['current']['wind_kph']) / 3.6, 2)

        print(
              f"Температура: {temp_c}C°\n"
              f"Ощущается как: {temp_c}C°\n"
              f"Ветер: {wind_s} м/с"
              )

    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите город: ")
    get_weather(city)


if __name__ == '__main__':
    main()
