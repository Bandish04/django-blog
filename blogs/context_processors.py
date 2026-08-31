from.models import Category
from assignments.models import Sociallink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    social_links = Sociallink.objects.all()
    return dict(social_links=social_links)