from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def portfolio_dashboard(request):
    return render(request,"portfolio_web/portfolio.html")