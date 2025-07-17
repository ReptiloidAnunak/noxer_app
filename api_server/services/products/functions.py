import requests

def get_api_dict(source: str) -> dict:
        response = requests.get(source)
        return response.json()


def get_prods_lst_from_api(source: str) -> list:
    json_data = get_api_dict(source)
    products = json_data.get("products", [])
    return products

