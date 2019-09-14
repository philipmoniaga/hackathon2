import json
from models.customer import Customer


class CustomerDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)  # NOQA

    def object_hook(self, obj):
        key_error = ''
        if 'user_id' not in obj:
            key_error = 'user_id'
        if 'name' not in obj:
            key_error = 'name'
        if 'longitude' not in obj:
            key_error = 'longitude'
        if 'latitude' not in obj:
            key_error = 'latitude'
        if key_error != '':
            raise KeyError("Mandatory key: " + key_error)
        return Customer(obj['user_id'], obj['latitude'], obj['longitude'], obj['name'])  # NOQA
