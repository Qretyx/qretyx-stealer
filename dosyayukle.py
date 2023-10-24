import requests

def yukle(dosya):
    file_path = dosya


    url = "https://file.io"

    # Dosya yükleme isteği için parametreler
    params = {
        "expires": "1w"  # Dosya linkinin ne kadar süre aktif olacağı (1 hafta)
    }

    # Dosya yükleme isteği gönderin
    with open(file_path, "rb") as f:
        response = requests.post(url, params=params, files={"file": f})

    # İsteğin başarılı olduğunu kontrol edin
    if response.status_code == 200:
        return response.json()["link"]
    else:
        # İsteğin başarısız olduğunu bildirin
        return "Dosya yukleme islemi basarisiz oldu."
