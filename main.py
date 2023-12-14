import requests


url = f"https://wttr.in/{input('Введите ваш город: ')}"

params = {
    "nm": "",
    "lang": "ru"
}

response = requests.get(url, params=params)
response.raise_for_status()
print(response.text)
    


    