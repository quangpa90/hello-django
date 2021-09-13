import requests
class MockApi:
    __url = 'https://611ba73022020a00175a4615.mockapi.io'

    def get_products_by_category(self, category):
        url = f'{self.__url}/category/{category}/product'
        response = requests.get(url)
        return response.json()