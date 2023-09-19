# In your Django views.py file
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def webhook_receiver(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Process the data from WordPress as needed
            # You can access the data using data['key'] where 'key' is the key in the JSON sent by WordPress
            # Perform actions, update models, etc.
            # Example: You could save data to a Django model
            # YourModel.objects.create(field1=data['field1'], field2=data['field2'
            print(data)
            return JsonResponse({'message': 'Webhook data received successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data received'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
