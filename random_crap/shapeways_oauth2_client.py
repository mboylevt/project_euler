import base64
import json
import requests

AUTH_URL = '/oauth2/token'
MATERIALS_URL = '/materials/v1'
MODEL_URL = '/model/v1'

class ShapewaysOauth2Client():
    """
    Shapeways API client, supporting Oauth2 Bearer Token
    """

    def __init__(self, api_url=None):
        self.access_token = None
        if not api_url:
            self.api_url = 'https://api.shapeways.com'

    def authenticate(self, client_id, client_secret):
        """
        Authenticate your application and retrieve a bearer token

        :type client_id: str
        :type client_secret: str
        :return: True for success, false for Failure
        :rtype: bool
        """
        auth_post_data = {
            'grant_type': 'client_credentials'
        }

        response = requests.post(url=self.api_url + AUTH_URL, data=auth_post_data, auth=(client_id, client_secret))
        if response.status_code == 200:
            self.access_token = response.json()['access_token']
            return True
        print("Error: status code " + str(response.status_code))
        print(response.content)
        return False

    def _execute_get(self, url, **params):
        response = requests.get(url=url, **params)
        content = response.json()
        try:
            if content['result'] == 'success':
                return content
            else:
                raise RuntimeError(content)
        except:
            raise RuntimeError(content)

    def get_materials(self):
        """
        Use your bearer token to retrieve our material list

        :return: list of materials
        :rtype: list()
        """

        if not self.access_token:
            raise RuntimeError("Access token not defined: be sure to call .authenticate() first!")

        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        content = self._execute_get(url=self.api_url + MATERIALS_URL, headers=headers)
        return content['materials']

    def get_models(self, page_count=1):
        """
        Use your bearer token to retrieve a list of your models

        :return: list of materials
        :rtype: list()
        """

        if not self.access_token:
            raise RuntimeError("Access token not defined: be sure to call .authenticate() first!")

        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        response = requests.get(url=self.api_url + MODEL_URL + '?page=' + str(page_count), headers=headers)
        content = response.json()
        if content['result'] == 'success':
            return response.json()['models']
        else:
            raise RuntimeError(content)