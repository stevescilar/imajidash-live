from django.shortcuts import render

# Create your views here.
def trackFinance(request):
    
    return render(request,'finance/track_finance.html')
