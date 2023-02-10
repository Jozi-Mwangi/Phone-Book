from django.shortcuts import render, redirect
from .models import Contact, Person
from django.db.models import Q
from .forms import ContactForm

# Create your views here.
def main_view(request):
    return render(request, 'main.html')


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

def create_contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect ('main')
        else:
            print (form.errors)
    
    context ={'form':form}

    return render (request, 'create_form.html', context)

def update_contact(request, pk):
    contact = Contact.objects.get(id=pk)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect ('main')
        else:
            print (form.errors)

    # if request.method == 'DELETE':
    #     form = ContactForm(request.POST, instance=contact)
    #     form.delete()
    #     return redirect ('main')
    
    context = {'contact':contact, 'form':form}
    return render(request, 'update_contact.html', context)
        
    