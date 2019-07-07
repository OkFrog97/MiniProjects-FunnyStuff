import requests

def get_location ():
    return requests.get("http://www.freegeoip.net/json").json()

def main ():
    print (get_location())


if __name__ == "__main__":
    main ()