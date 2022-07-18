from django.shortcuts import render,redirect
from .forms import ReceiveGoodsForm
from dashboard.models import Client,SalesAgent
# Create your views here.
def index(request):
    # every things that happens
    return render (request,'in_house/index.html')


def ofloadedCargo(request):
    # cargos = ReceivedCargo.objects.all().order_by('-created')
    # cargos = ReceivedCargoChina.objects.all()
    # cargos_d = DispatchCargoChina.objects.all()
    clients = Client.objects.all().order_by('-created')
    #count = ReceivedCargoChina.objects.count()
    salespersons = SalesAgent.objects.all()
    form = ReceiveGoodsForm()
    if request.method == 'POST':
        form = ReceiveGoodsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('in_house')

    context = {'form': form,'clients':clients,'salespersons':salespersons}
    return render (request,'in_house/receive_cargo.html',context)

