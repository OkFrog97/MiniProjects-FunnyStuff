import requests

r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/699991.txt")

while "We" not in r.text:
    print (r.text)
    r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/{}".format(r.text))

with open ("last_file_words.txt", "w") as out:
        out.write(r.text)

print("End of the script")
input()