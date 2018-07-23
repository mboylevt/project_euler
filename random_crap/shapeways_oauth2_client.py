import base64
import json
import requests

AUTH_URL = '/oauth2/token'
MATERIALS_URL = '/materials/v1'
SINGLE_MATERIAL_URL = '/materials/{material_id}/v1'
MODEL_URL = '/model/v1'
SINGLE_MODEL_URL = '/model/{model_id}/v1'
ORDER_URL = '/orders/v1'
CART_URL = '/orders/cart/v1'


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

    def _validate_response(self, content):
        """
        Internal function - validate results
        :rtype: list()
        """
        try:
            if content['result'] == 'success':
                return content
            else:
                raise RuntimeError(content)
        except:
            raise RuntimeError(content)

    def _execute_get(self, url, **params):
        """
        Internal function - execute get request and validate
        :param url:
        :param params:
        :rtype: list()
        """
        if not self.access_token:
            raise RuntimeError("Access token not defined: be sure to call .authenticate() first!")

        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        response = requests.get(url=url, headers=headers, **params)
        return self._validate_response(response.json())

    def _execute_post(self, url, **params):
        """
        Internal function - execute get request and validate
        :param url:
        :param params:
        :rtype: list()
        """
        if not self.access_token:
            raise RuntimeError("Access token not defined: be sure to call .authenticate() first!")

        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        response = requests.post(url=url, headers=headers, **params)
        return self._validate_response(response.json())

    def get_materials(self):
        """
        Get our material list

        :return: list of materials
        :rtype: list()
        """
        content = self._execute_get(url=self.api_url + MATERIALS_URL)
        return content['materials']

    def get_single_material(self, material_id):
        """
        Get information on a single material.

        :param material_id: material to query
        :type material_id: int
        :return:
        """
        material_url = SINGLE_MATERIAL_URL.format(material_id=material_id)
        content = self._execute_get(self.api_url + material_url)
        return content

    def get_models(self, page_count=1):
        """
        Use your bearer token to retrieve a list of your models

        :return: list of materials
        :rtype: list()
        """
        content = self._execute_get(url=self.api_url + MODEL_URL + '?page=' + str(page_count))
        return content['models']

    def get_single_model(self, model_id):
        """
        Get information for a single model

        :type model_id: int

        :return: model information for a single model
        """
        model_url = MODEL_URL.format(model_id=model_id)
        content = self._execute_get(self.api_url + model_url)
        return content

    def upload_model(self, path_to_model):
        """
        Upload a model to Shapeways

        :param path_to_model: path to model on your local filesystem
        :type path_to_model: str
        :return:
        """

        with open(path_to_model, 'rb') as model_file:
            model_file_data = model_file.read()

        model_upload_post_data = {
            'fileName': 'cube.stl',
            'file': base64.b64encode(model_file_data).decode('utf-8'),
            'description': 'Someone call a doctor, because this cube is SIIIICK.',
            'hasRightsToModel': 1,
            'acceptTermsAndConditions': 1
        }

        content = self._execute_post(url=self.api_url + MODEL_URL, data=json.dumps(model_upload_post_data))
        return content

    def get_cart(self):
        """
        Get the current contents of a cart

        :return:
        """
        content = self._execute_get(self.api_url + CART_URL)
        return content

    def add_to_cart(self, model_id, material_id, quantity=1):
        """
        Add a model to the cart.

        :param model_id:
        :return:
        """
        add_to_cart_data = {
            'modelId': model_id,
            'materialId': material_id,
            'quantity': quantity
        }
        content = self._execute_post(self.api_url + CART_URL, data=json.dumps(add_to_cart_data))
        return content

    def order_model(self, model_id, material_id, payment_verification_id, first_name, last_name, country, city,
                    address1, address2, zip_code, phone_number, state=None):
        """
        Order a model.

        :type model_id: int
        :type material_id: int
        :type payment_verification_id: str
        :return:
        """
        items = [{
            'materialId': material_id,
            'modelId': model_id,
            'quantity': 1
        }]

        order_data = {
            'items': items,
            'firstName': first_name,
            'lastName': last_name,
            'country': country,
            'state': state,
            'city': city,
            'address1': address1,
            'address2': address2,
            'zipCode': zip_code,
            'phoneNumber': phone_number,
            'paymentVerificationId': payment_verification_id,
            'paymentMethod': 'credit_card',
            'shippingOption': 'Cheapest'
        }

        content = self._execute_post(url=self.api_url + ORDER_URL, data=json.dumps(order_data))
        return content