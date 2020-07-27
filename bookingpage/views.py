from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')
def booking(request):
    return render(request, 'booking.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')
    