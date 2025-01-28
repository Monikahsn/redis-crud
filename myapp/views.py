from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .redis_client import create_item, read_item, update_item, delete_item

@csrf_exempt
def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        key = data.get('id')
        create_item(key, data)
        return JsonResponse({'message': 'Item created successfully!'})

@csrf_exempt
def read(request, key):
    data = read_item(key)
    if data:
        return JsonResponse(data)
    return JsonResponse({'error': 'Item not found'}, status=404)

@csrf_exempt
def update(request, key):
    if request.method == "PUT":
        data = json.loads(request.body)
        update_item(key, data)
        return JsonResponse({'message': 'Item updated successfully!'})

@csrf_exempt
def delete(request, key):
    delete_item(key)
    return JsonResponse({'message': 'Item deleted successfully!'})
