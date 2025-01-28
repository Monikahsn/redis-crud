import json
from django.core.cache import cache

def create_item(key, data):
    cache.set(key, json.dumps(data))

def read_item(key):
    data = cache.get(key)
    return json.loads(data) if data else None

def update_item(key, data):
    if cache.get(key):
        cache.set(key, json.dumps(data))
    else:
        return "Key not found"

def delete_item(key):
    cache.delete(key)
