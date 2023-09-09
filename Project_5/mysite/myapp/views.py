from django.shortcuts import render
from myapp.models import Food,Consume

def index(request):
    if request.method == 'POST':
        # Get the value of 'food_consumed' from the POST data
        food_consumed = request.POST['food_consumed']
        
        # Attempt to retrieve a 'Food' object where the 'name' matches 'food_consumed'
        consume = Food.objects.get(name=food_consumed)
        
        # Get the currently logged-in user
        user = request.user
        
        # Create a 'Consume' object associating the user and the retrieved 'Food' object
        consume = Consume(user=user, food_consumed=consume)
        
        # Save the 'Consume' object to the database
        consume.save()
        
        # Retrieve all 'Food' objects from the database
        foods = Food.objects.all()
    else:
        # If the request method is not POST, retrieve all 'Food' objects
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    # Render the 'myapp/index.html' template with the 'foods' variable in the context
    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food':consumed_food})
