import json

from random_crap.shapeways_oauth2_client import ShapewaysOauth2Client

client_id = 'ENPbso1i8tyUWX2tmMhHK5pm8pcHN9cauV96CVALkaIQUa3qQr'
client_secret = 'j7aEPlq83n9UtU0t3u1dg6Gk1Bw1CwU4TsTosKTjTSwl3GVQ0y'

sw_api = ShapewaysOauth2Client()
sw_api.authenticate(client_id, client_secret)
print(json.dumps(sw_api.get_cart(), indent=4, sort_keys=True))
print(json.dumps(sw_api.add_to_cart(model_id=7904178, material_id=6, quantity=5), indent=4, sort_keys=True))
print(json.dumps(sw_api.get_cart(), indent=4, sort_keys=True))

# print(json.dumps(sw_api.get_materials(), indent=4, sort_keys=True))
# print(json.dumps(sw_api.get_models(), indent=4, sort_keys=True))
# print(json.dumps(sw_api.upload_model('cube.stl'), indent=4, sort_keys=True))