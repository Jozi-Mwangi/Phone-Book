from django.shortcuts import render
from .models import Contact, Person
from django.db.models import Q

# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def contacts_view(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts}
    # print(contacts)
    return render (request, 'contacts.html', context)

def search_view (request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')

        if query is not None:
            lookup = Q(name__icontains=query)
            results = Contact.objects.filter(lookup)
            context = {'results':results, 'submitbutton':submitbutton}
            return render (request, 'search.html', context)
        else:
            return render (request, 'search.html')
            
    return render (request, 'search.html')
        
    