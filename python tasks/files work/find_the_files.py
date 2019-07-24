import requests

r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/699991.txt")

while "We" not in r.text:
    print (r.text)
    r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/{}".format(r.text))

with open ("decode_data.txt", "w") as out:
        out.write(decoding_data)

print("End of the script")
input()