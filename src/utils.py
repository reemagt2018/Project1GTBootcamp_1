import requests

def get_search_params(key):
    target_city = input("Target city: ")
    params = {
        "address":target_city,
        "key":key
    }
    return params


def get_search_radius_params(zip_code, key):
    search_radius = int(input("Search radius: "))
    params = {
        "zip":zip_code,
        "distance":search_radius,
        "key":key
    }
    return params


def get_units(size):
    power = 2**10
    n = 0
    dict_powerN = {0 : '', 1: 'K', 2: 'M', 3: 'B', 4: 'T'}
    while size > power:
        size /=  power
        n += 1
    return f"{'{:.2f}'.format(size)}{dict_powerN[n]+'B'}"


def fetch(url):
    res = requests.get(url)
    size = get_units(len(res.content))
    return {"response":res, "size":size}


def write_zipcodes(ziplist):
    with open("zipcodes.py", "w") as zipcodes:
        zipcodes.write(f"ziplist = {[zip for zip in ziplist]}")

