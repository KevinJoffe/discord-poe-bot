import requests


def get_exalted_price():
    response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Harvest&type=Currency')

    exalted_orb_id = "exalted-orb"

    if response.status_code == 200:
        print('Success!')
        lines = response.json()['lines']
        exalted_price = 'unknown'
        for currency in lines:
            if currency['detailsId'] == exalted_orb_id:
                print(currency["receive"]["value"])
                exalted_price = currency["receive"]["value"]
        return exalted_price
        # print(lines)
        # print(len(data.items()))
        # for key, value in data.items():
        #     print(key, ":", value)

    elif response.status_code == 404:
        print('Not Found.')
