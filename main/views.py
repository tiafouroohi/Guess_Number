from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'number' in request.session:
        pass
    else: 
        request.session['number']=8
        request.session['log']=[]
    return render(request, "index.html")

def process(request):
    print(request.session['number'])
    request.session['log']=[]
    request.session['user']= int(request.POST['guess_number'])
    
    
    if request.session['user'] > request.session['number']:
        
        request.session['log'].append("too high")
    
    if request.session['number'] > request.session['user']:
        request.session['log'].append("too low")
    else:
        request.session['log'].append("you got it")
    
    return redirect ("/")
    


# Create your views here.
# can check if something is not in session by using if key not in request.session
# make a third request.session key and use for message 