from difflib import context_diff
from dis import dis
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.db.models import Q
from . models import Client, DispatchCargoChina, ReceivedCargoChina, ReceivedCargoKenya, Remark,Message,DispatchCargoKenya, SalesAgent,ReceivedCargoYiwu,DispatchCargoYiwu
from .forms import  SalesAgentForm,CargoFormKenya, ClientForm, RemarkForm,dispatchFormChina,CargoFormChina,dispatchFormKenya,CargoFormYiwu,DispatchCargoYiwu, dispatchFormYiwu


# login page.. .
def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User Doest exist')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Username or password not found or does not exist')

    context ={
        'page':page
    }
    return render(request,'dashboard/login_register.html',context)

# logging out user
def logoutUser(request):
    logout(request)
    return redirect('login')

# registration page.
def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'error occurred during registration')

    return render(request,'dashboard/login_register.html',{'form':form})
# remark
def remark(request,pk):
    remark = Remark.objects.get(id=pk)
    remarks = Remark.objects.all()
    remark_messages = remark.message_set.all().order_by('-created')
    participants = remark.participants.all()

    if request.method == 'POST':
        remark_messages = Message.objects.create(
            user=request.user,
            remark = remark,
            body = request.POST.get('body')
        )
        remark.participants.add(request.user)
        return redirect('remark',pk=remark.id)

    context = {
        'remark':remark, 'remark_messages':remark_messages,
        'participants':participants,'remarks':remarks
    }
    return render (request,'dashboard/remark.html',context)

# Create Rwmark.
def createRemark(request):
    form = RemarkForm()
    if request.method == 'POST':
        form = RemarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    
    context = {'form':form}
    return render(request,'dashboard/remark_form.html',context)
@login_required(login_url='login')
def index(request):
  
    clients = Client.objects.all()
    salespersons = SalesAgent.objects.all()
    context = {'clients':clients,'salespersons':salespersons}

    return render(request,'dashboard/index.html',context)

# def home(request):
#     return render(request,'dashboard/login_register.html')
def chart(request):
    # context= {

    # }
    return render(request,'dashboard/charts.html')

def client(request):
      # search all clients
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    clients = Client.objects.filter(
        Q(name__icontains = q)
        
    )
   
    # clients = Client.objects.get(id=pk)
    clients = Client.objects.all().order_by('-created')
    cargos = ReceivedCargoChina.objects.all().order_by('-created')
    count = Client.objects.count()
    salespersons = SalesAgent.objects.all()
    # Client.objects.filter(created=2022).order_by('-created')
    context = {'clients':clients,'count':count,'cargos':cargos,'salespersons':salespersons}
    # Client.objects.all().order_by('created')
    
    return render (request,'dashboard/clients.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            clients = Client.objects.order_by('-created').filter(
                Q(name__icontains=keyword) | Q(contact__icontains=keyword)
                ) 
            client_count = clients.count()
    context  = {
        'clients'      :clients,
        'client_count' :client_count,
        'keyword'       :keyword,
    }
    return render (request, 'dashboard/clients.html',context)


def searchAdd(request):
    page = 'searchadd'
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            clients = Client.objects.order_by('-created').filter(
                Q(name__icontains=keyword) | Q(contact__icontains=keyword)
                ) 
            client_count = clients.count()
    context  = {
        'page':page,
        'clients'      :clients,
        'client_count' :client_count,
        'keyword'       :keyword,
    }
    return render (request, 'dashboard/client_form.html',context)

@login_required(login_url='login')
def createClient(request):
    clients = Client.objects.all().order_by('-created')
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-client')

    context = {'form': form, 'clients':clients}
    return render (request,'dashboard/client_form.html',context)






def agent(request):
    clients = Client.objects.all().order_by('-created')
    cargos = ReceivedCargoChina.objects.all().order_by('-created')
    count = Client.objects.count()
    salespersons = SalesAgent.objects.all()
    # Client.objects.filter(created=2022).order_by('-created')
    context = {'clients':clients,'count':count,'cargos':cargos,'salespersons':salespersons}
    # Client.objects.all().order_by('created')
    return render (request,'dashboard/salesperson.html',context)

@login_required(login_url='login')
def createSalesAgent(request):
    clients = Client.objects.all().order_by('-created')
    salespersons = SalesAgent.objects.all()
    form = SalesAgentForm()
    if request.method == 'POST':
        form = SalesAgentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Sales Person Created Successfully!')
            return redirect('agent')
    context = {'form':form,'salespersons': salespersons,'clients':clients}
    return render (request,'dashboard/sales_agent.html',context)


# def cargo(request):

# ------------------------------------------China Warehouse Logic---------------------------------------------#
#-------------------------------------------separation of matters --------------------------------------#
# -------------------------------------------China cargo Operations--------------------------------------------#
def china(request):
    cargos = ReceivedCargoChina.objects.all().order_by('-created')
    count = ReceivedCargoChina.objects.count()
    cargos_d = DispatchCargoChina.objects.all()
    clients = Client.objects.all()
    count_clients = Client.objects.count()
    context = {'cargos': cargos,'count_clients':count_clients,'count':count,'clients':clients,'cargos_d':cargos_d}
    return render (request,'dashboard/china.html',context)


def receiveChina(request):
    # cargos = ReceivedCargo.objects.all().order_by('-created')
    cargos = ReceivedCargoChina.objects.all()
    cargos_d = DispatchCargoChina.objects.all()
    clients = Client.objects.all().order_by('-created')
    count = ReceivedCargoChina.objects.count()
    salespersons = SalesAgent.objects.all()
    form = CargoFormChina()
    if request.method == 'POST':
        form = CargoFormChina(request.POST)
        if form.is_valid():
            form.save()
            return redirect('china')

    context = {'form': form,'clients':clients,'count':count,'cargos_d':cargos_d,'cargos':cargos,'salespersons':salespersons}
    return render (request,'dashboard/china/receive_cargo.html',context)
    # bulk sms
#Yiwu Operations 
def yiwu(request):
    cargos = ReceivedCargoYiwu.objects.all().order_by('-created')
    count = ReceivedCargoYiwu.objects.count()
    cargos_d = DispatchCargoYiwu.objects.all()
    clients = Client.objects.all()
    count_clients = Client.objects.count()
    context = {'cargos': cargos,'count_clients':count_clients,'count':count,'clients':clients,'cargos_d':cargos_d}
    return render (request,'dashboard/yiwu.html',context)


def receiveYiwu(request):
    # cargos = ReceivedCargo.objects.all().order_by('-created')
    cargos = ReceivedCargoYiwu.objects.all()
    cargos_d = DispatchCargoYiwu.objects.all()
    clients = Client.objects.all().order_by('-created')
    count = ReceivedCargoYiwu.objects.count()
    salespersons = SalesAgent.objects.all()
    form = CargoFormYiwu()
    if request.method == 'POST':
        form = CargoFormYiwu(request.POST)
        if form.is_valid():
            form.save()
            return redirect('yiwu')

    context = {'form': form,'clients':clients,'count':count,'cargos_d':cargos_d,'cargos':cargos,'salespersons':salespersons}
    return render (request,'dashboard/yiwu/receive_cargo.html',context)

@login_required(login_url='login')
def dispatchYiwu(request):
    clients = Client.objects.all().order_by('-created')
    cargos = ReceivedCargoYiwu.objects.all()
    cargos_d = DispatchCargoYiwu.objects.all()
    form = dispatchFormYiwu()
    if request.method == 'POST':
        form = dispatchFormYiwu(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dispatch-yiwu')
    context ={'form':form,'cargos':cargos,'cargos_d':cargos_d,'clients':clients}
    return render (request,'dashboard/yiwu/dispatch_cargo.html',context)

def dispatchedYiwu(request):
    cargos = ReceivedCargoYiwu.objects.all()
    cargos_d = DispatchCargoYiwu.objects.all()
    context = {'cargos_d':cargos_d,'cargos':cargos}
    return render(request, 'dashboard/yiwu/dispatched_china.html',context)



@login_required(login_url='login')
def dispatchChina(request):
    clients = Client.objects.all().order_by('-created')
    cargos = ReceivedCargoChina.objects.all()
    cargos_d = DispatchCargoChina.objects.all()
    form = dispatchFormChina()
    if request.method == 'POST':
        form = dispatchFormChina(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dispatch-china')
    context ={'form':form,'cargos':cargos,'cargos_d':cargos_d,'clients':clients}
    return render (request,'dashboard/china/dispatch_cargo.html',context)

def dispatchedChina(request):
    cargos = ReceivedCargoChina.objects.all()
    cargos_d = DispatchCargoChina.objects.all()
    context = {'cargos_d':cargos_d,'cargos':cargos}
    return render(request, 'dashboard/china/dispatched_china.html',context)


# ---------------------------------------------------------------------------------------------------------#
#----------------------------------------End of China Ops _______-------------------------------------------#


# ------------------------------------------Kenya Warehouse Logic---------------------------------------------#
#-------------------------------------------separation of matters --------------------------------------#
# -------------------------------------------Kenya cargo Operations--------------------------------------------#


def kenya(request):
    cargos = ReceivedCargoKenya.objects.all().order_by('created')
    count = ReceivedCargoKenya.objects.count()
    cargos_d = DispatchCargoKenya.objects.all()
    # clients = Client.objects.all()
    # count_clients = Client.objects.count()
    clients = Client.objects.all().order_by('-created')
    count = Client.objects.count()
    context = {'count':count,'clients':clients,'cargos':cargos,'cargos_d':  cargos_d}
    return render(request,'dashboard/kenya.html',context)

def receiveKenya(request):
    # cargos = ReceivedCargo.objects.all().order_by('-created')
    clients = Client.objects.all().order_by('-created')
    cargos = DispatchCargoKenya.objects.all().order_by('-created')
    cargos_d = DispatchCargoChina.objects.all()
    form = CargoFormKenya()
    if request.method == 'POST':
        form = CargoFormKenya(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kenya')

    context = {'form': form,'clients':clients,'cargos':cargos,'cargos_d':cargos_d }
    return render (request,'dashboard/kenya/receive_cargo.html',context)

@login_required(login_url='login')
def dispatchKenya(request):
    clients = Client.objects.all().order_by('-created')
    cargos = ReceivedCargoKenya.objects.all()
    cargos_d = DispatchCargoKenya.objects.all()
    form = dispatchFormKenya()
    if request.method == 'POST':
        form = dispatchFormKenya(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dispatch-kenya')
    context ={'form':form,'cargos':cargos,'cargos_d':cargos_d,'clients':clients}
    return render (request,'dashboard/kenya/dispatch_cargo.html',context)

def dispatchedKenya(request):
    clients = Client.objects.all().order_by('-created')
    cargos = ReceivedCargoKenya.objects.all()
    cargos_d = DispatchCargoKenya.objects.all()
    context = {'cargos_d':cargos_d,'cargos':cargos,'clients':clients}
    return render(request, 'dashboard/kenya/dispatched_kenya.html',context)