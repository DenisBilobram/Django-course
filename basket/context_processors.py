from .models import Basket

def basket(request):
    basket = None
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).first()

    return {'basket': basket}
