from django.shortcuts import render

# Create your views here.
def trackFinance(request):
    
    return render(request,'dashboard/track_finance.html')
