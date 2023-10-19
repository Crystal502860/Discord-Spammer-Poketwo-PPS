from webserver import keep_alive
import requests

channelID = 1005686311836995594
headers = {
    "NjA0MzcwOTU4NTE3NjY1ODcz.G7Qms_.H4diW76GwpXYruU3LJj0DVlymeKhGSyyE2GjRI":
    "NjA0MzcwOTU4NTE3NjY1ODcz.G7Qms_.H4diW76GwpXYruU3LJj0DVlymeKhGSyyE2GjRI"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
