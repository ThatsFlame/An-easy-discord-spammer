import requests

chan_id = "insert channel id"

payload = {
    "content" : "insert what u want"
}

header = {
    'authorization' : "token"
}
while True:
    r = requests.post(f"https://discord.com/api/v9/channels/{chan_id}/messages",
                   data=payload, headers=header)

                  
