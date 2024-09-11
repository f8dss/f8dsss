import requests
import time

def claim_daily_points():
    
    access_token = 'ISIEN_REFRESH_TOKENMU'

    
    url = 'https://api.assisterr.ai/incentive/users/me/daily_points'

    # Header dengan token otentikasi
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }

    # Melakukan request ke API untuk klaim daily points
    response = requests.post(url, headers=headers)

    # Memeriksa respons dari server
    if response.status_code == 200:
        print("Daily points berhasil di-claim!")
        print("Respons dari server:", response.json())
    else:
        print(f"Gagal klaim daily points. Status code: {response.status_code}")
        print("Respons dari server:", response.text)

def main():
    while True:
        claim_daily_points()
        # Tunggu selama 12 jam (43200 detik)
        time.sleep(43200)

if __name__ == "__main__":
    main()
