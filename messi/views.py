from django.shortcuts import render
from.models import*
# Create your views here.
def index(request):

    info = CompanyInformation.objects.all().first()
    product = Product.objects.all()
    
    

    data ={
    'info':info,
    'product':product
 } 
    return render(request, 'index.html',data)


def contact(request):
    return render(request, 'contact.html')
