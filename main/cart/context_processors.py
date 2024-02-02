from .models import Cartpage

def count(request):
    count=0
    try:
        user_id=request.session['user']
        items = Cartpage.objects.all().filter(user_id=user_id)
        count=items.count()
    except:
        count=0       
    return dict(count=count)