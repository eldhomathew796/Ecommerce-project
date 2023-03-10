from .models import Cart,CartItem
from .views import cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
          cart=Cart.objects.filter(cart_id=cart_id(request))
          cart_items=CartItem.objects.filter(cart=cart[:1])
          for cart_item in cart_items:
            item_count+=cart_item.quantity
        except CartItem.DoesNotExist:
            return dict(item_count=item_count) 
            
    return dict(item_count=item_count)        
            