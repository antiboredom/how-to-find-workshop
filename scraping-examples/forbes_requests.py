import requests
import time
import json

cookies = {
    "notice_behavior": "implied,us",
    "fbs-session-promo-modal-shown": "true",
    "_pc_meter_expiration": "expired",
    "VWO": "36.300",
    "client_id": "520d093e38ed24fa9e6d10f129c6c5e2b89",
    "AWSALB": "5FuUNnxYl/0kXHuNlIVmvdsrkFxsjXeF/U8CtEnB5zHQMuPFXgRkVRY5UR4vaevOjQa/+b4tFxitnoVw3sycyE63K4fkGQ1hM8YUtKFMNANzZjvIB/kOLa/MGU0r",
    "AWSALBCORS": "5FuUNnxYl/0kXHuNlIVmvdsrkFxsjXeF/U8CtEnB5zHQMuPFXgRkVRY5UR4vaevOjQa/+b4tFxitnoVw3sycyE63K4fkGQ1hM8YUtKFMNANzZjvIB/kOLa/MGU0r",
    "blaize_session": "107e4aac-7a84-4dff-bb00-6c0fde9d9be5",
    "blaize_tracking_id": "af77d655-5bdf-4488-a770-906b9c662906",
    "_swb": "9e7c1ef7-cb53-41fe-a790-3a58691e9a71",
    "_swb_consent_": "eyJjb2xsZWN0ZWRBdCI6MTc3NDQ1MTI3MCwiY29udGV4dCI6eyJjb25maWd1cmF0aW9uSWQiOiJabTl5WW1WekwzZGxZbk5wZEdWZmMyMWhjblJmZEdGbkwzQnliMlIxWTNScGIyNHZkWE5mWjJWdVpYSmhiQzlsYmk4eE56YzBNemMxTXpBNCIsInNvdXJjZSI6ImxlZ2FsQmFzaXNEZWZhdWx0In0sImVudmlyb25tZW50Q29kZSI6InByb2R1Y3Rpb24iLCJpZGVudGl0aWVzIjp7InN3Yl93ZWJzaXRlX3NtYXJ0X3RhZyI6IjllN2MxZWY3LWNiNTMtNDFmZS1hNzkwLTNhNTg2OTFlOWE3MSJ9LCJqdXJpc2RpY3Rpb25Db2RlIjoidXNfZ2VuZXJhbCIsInByb3BlcnR5Q29kZSI6IndlYnNpdGVfc21hcnRfdGFnIiwicHVycG9zZXMiOnsiYW5hbHl0aWNzIjp7ImFsbG93ZWQiOiJ0cnVlIiwibGVnYWxCYXNpc0NvZGUiOiJkaXNjbG9zdXJlIn0sImJlaGF2aW9yYWxfYWR2ZXJ0aXNpbmciOnsiYWxsb3dlZCI6InRydWUiLCJsZWdhbEJhc2lzQ29kZSI6ImRpc2Nsb3N1cmUifSwiZnVuY3Rpb25hbCI6eyJhbGxvd2VkIjoidHJ1ZSIsImxlZ2FsQmFzaXNDb2RlIjoiZGlzY2xvc3VyZSJ9LCJyZXF1aXJlZCI6eyJhbGxvd2VkIjoidHJ1ZSIsImxlZ2FsQmFzaXNDb2RlIjoiZGlzY2xvc3VyZSJ9fX0%3D",
    "_ketch_consent_v1_": "eyJiZWhhdmlvcmFsX2FkdmVydGlzaW5nIjp7InN0YXR1cyI6ImdyYW50ZWQiLCJjYW5vbmljYWxQdXJwb3NlcyI6WyJkYXRhX2Jyb2tpbmciLCJiZWhhdmlvcmFsX2FkdmVydGlzaW5nIl19LCJhbmFseXRpY3MiOnsic3RhdHVzIjoiZ3JhbnRlZCIsImNhbm9uaWNhbFB1cnBvc2VzIjpbImFuYWx5dGljcyJdfSwiZnVuY3Rpb25hbCI6eyJzdGF0dXMiOiJncmFudGVkIiwiY2Fub25pY2FsUHVycG9zZXMiOlsicHJvZF9lbmhhbmNlbWVudCIsInBlcnNvbmFsaXphdGlvbiJdfSwicmVxdWlyZWQiOnsic3RhdHVzIjoiZ3JhbnRlZCIsImNhbm9uaWNhbFB1cnBvc2VzIjpbImVzc2VudGlhbF9zZXJ2aWNlcyJdfX0%3D",
    "usprivacy": "1---",
    "us_privacy": "1---",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:148.0) Gecko/20100101 Firefox/148.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "Referer": "https://www.forbes.com/billionaires/",
    "Alt-Used": "www.forbes.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0",
}

start = 0
limit = 50
total = 3428

results = []

while start + limit < total:
    print("scraping from", start, start + limit)
    response = requests.get(
        f"https://www.forbes.com/forbesapi/person/billionaires/2026/rank/true.json?fields=uri,finalWorth,age,countryOfCitizenship,source,qas,rank,status,category,person,personName,industries,organization,gender,firstName,lastName,squareImage,bios&limit={limit}&start={start}",
        cookies=cookies,
        headers=headers,
    )

    people = response.json()["personList"]["personsLists"]
    results += people

    with open("forbes_people.json", "w") as outfile:
        json.dump(results, outfile, indent=2)

    time.sleep(1)
    start += limit
