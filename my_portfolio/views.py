from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio



# Create your views here.
portfolio = Portfolio.objects.all()
def home(request):
    return render(request, 'my_portfolio/home.html')
    #return render(request, 'my_portfolio/home.html', {'portfolio': Portfolio})

def portfolio(request):
    # Retrieve portfolio items from the database
    portfolio_items = Portfolio.objects.all()
    
    # Other context data can be added here
    context = {
        'page_title': 'Your Page Title',
        'portfolio_items': portfolio_items,
        # Add more context data as needed
    }
    return render(request, 'my_portfolio/portfolio.html', context)


def about(request):
    return render(request, 'my_portfolio/about.html')

def service(request):
    return render(request, 'my_portfolio/service.html')
