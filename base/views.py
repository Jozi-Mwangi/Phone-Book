from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from .models import Contact, Person
from .forms import ContactForm

# Create your views here.
def main_view(request):
    contacts = Contact.objects.all()
    context={'contacts':contacts}
    return render(request, 'main.html', context)


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
        name=request.POST['name']
        phone_number=request.POST['phone_number']
        email=request.POST['email']

        if form.is_valid():
            contact = Contact(name=name, phone_number=phone_number, email=email)
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
        new_name=request.POST['name']
        new_phone_num=request.POST['phone_number']
        new_email=request.POST['email']


        if form.is_valid():
            contact.name=new_name
            contact.phone_number=new_phone_num
            contact.email=new_email
            contact.save()
            form.save()
            return redirect ('main')
        else:
            print (form.errors)

    # if request.method == 'DELETE':
    #     form = ContactForm(request.POST, instance=contact)
    #     form.delete()
    #     return redirect ('main')
    
    context = { 'contact':contact,'form':form}
    return render(request, 'update_contact.html', context)
        
def delete_contact(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return (request, reverse('main'))

def contact_view(request,pk):
    contact=Contact.objects.get(id=pk)

    name = contact.name
    phone_num = contact.phone_number
    email = contact.email

    context={
        'contact':contact,
        'name':name,
        'phone_num':phone_num,
        'email':email,
    }
    return render (request, 'contacts.html', context)