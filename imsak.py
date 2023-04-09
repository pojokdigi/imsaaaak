import requests
import json
import datetime

url = "https://equran.id/api/v2/imsakiyah/provinsi"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.content)
    provinces = data['data']
    print("\nPilih Provinsi:\n")
    for i, province in enumerate(provinces):
        print(f"{i+1}. {province}")

    # choose province by number
    province_num = int(input("Choose a province by number: "))
    province = provinces[province_num-1]
    payload = {"provinsi": province}
    city_url = "https://equran.id/api/v2/imsakiyah/kabkota"
    city_response = requests.post(city_url, data=payload)
    if city_response.status_code == 200:
        city_data = json.loads(city_response.content)
        cities = city_data['data']
        print("\nPilih Kab/Kota:\n")
        for i, city in enumerate(cities):
            print(f"{i+1}. {city}")
        
        # choose city by number
        city_num = int(input("Choose a city by number: "))
        city = cities[city_num-1]
        payload = {"provinsi": province, "kabKota": city}
        jadwal_url = "https://equran.id/api/v2/imsakiyah/jadwal"
headers = {'Content-Type': 'application/json'}
jadwal_response = requests.post(jadwal_url, json=payload, headers=headers)

if jadwal_response.status_code == 200:
    jadwal_data = jadwal_response.json()
    provinsi = jadwal_data['data']['provinsi']
    kab_kota = jadwal_data['data']['kabKota']

    print(f"\nBerikut adalah Jadwal Untuk Wilayah:\nProvince: {provinsi}\nCity: {kab_kota}\n")
    today = datetime.date.today().strftime('%Y-%m-%d')
    if today in jadwal_data['data']['data']:
        today_data = jadwal_data['data']['data'][today]
        imsak = today_data['imsak']
        subuh = today_data['subuh']
        dzuhur = today_data['dzuhur']
        ashar = today_data['ashar']
        maghrib = today_data['maghrib']
        isya = today_data['isya']

        print(f"\nImsak: {imsak}\nSubuh: {subuh}\nDzuhur: {dzuhur}\nAshar: {ashar}\nMaghrib: {maghrib}\nIsya: {isya}")
    else:
        print("Jadwal tidak tersedia!")
else:
    print("Gagal mendapatkan Jadwal!")
