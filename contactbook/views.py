from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Contact

# Create your views here.

def home(request):
    contacts=Contact.objects.all()
    search_input=request.GET.get('search')
    if search_input:
        contacts=Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts=Contact.objects.all()
        search_input=''


    return render(request, 'home.html', {'contacts':contacts, 'search_input':search_input})

def addContact(request):
    if request.method=='POST':
        new_contact=Contact(
            full_name=request.POST['full_name'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            address=request.POST['address'],
            phone_number=request.POST['phone_number']
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'addcontact.html')

def Profile(request, pk):
    contact=Contact.objects.get(id=pk)
    return render(request, 'profile.html', {'contact': contact})

     
def Edit(request, pk):
    contact=Contact.objects.get(id=pk)

    if request.method=='POST':
        contact.full_name=request.POST['full_name'],
        contact.relationship=request.POST['relationship'],
        contact.email=request.POST['email'],
        contact.address=request.POST['address'],
        contact.phone_number=request.POST['phone_number'],

        contact.save()

        return redirect ('/profile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})

def Delete(request, pk):
    contact=Contact.objects.get(id=pk)

    if request.method=='POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact':contact})
