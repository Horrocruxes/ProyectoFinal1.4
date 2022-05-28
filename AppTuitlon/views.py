from django.shortcuts import render
from AppTuitlon.models import Tuitl, Avatar
from AppTuitlon.forms import TuitlForm, RegisterForm, AvatarForm, TuitlForm2
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

#Vista para registrarse
def register(request):

    if request.method == 'POST':   

        form = RegisterForm(request.POST)  

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "AppTuitlon/inicio.html", {'mensaje':"Usuario Creado"})
    
    else:

        form = RegisterForm()   
    
    
    return render(request, "AppTuitlon/registrarse.html", {'form':form})

#Vusta para logearse
def login_request(request):

    if request.method == 'POST': 

        form = AuthenticationForm(request, data = request.POST) 

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')   
            contra=form.cleaned_data.get('password')    

            user=authenticate(username=usuario, password=contra)    

            if user:    

                login(request, user)   #hacemos login

                
                return render(request, "AppTuitlon/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:   
    
            return render(request, "AppTuitlon/inicio.html", {'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() #mostrar el formulario

    return render(request, "AppTuitlon/login.html", {'form':form})   


#Vista para ir al inicio
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request,'AppTuitlon/inicio.html')

#Vista para poder tuitlear

@login_required
def tuitlear(request):

    if request.method == 'POST':

        miForm = TuitlForm2(request.POST, request.FILES)

        print(miForm)

        if miForm.is_valid:

            info = miForm.cleaned_data
          
            tuitl_a = Tuitl(contenido = info['contenido'], 
             imagen=info['imagen'])
    
            
            tuitl_a.save()
            
            return render(request, 'AppTuitlon/inicio.html')
    else:
        
        miForm = TuitlForm2()
    try:
        tuitl_a = Tuitl.objects.all()
    except:
        tuitl_a = None
    return render(request, 'AppTuitlon/tuitls.html', {'miForm':miForm})


#Class para ver todos los tuitls
class TuitlList(ListView):

      model = Tuitl 
      template_name = "AppTuitlon/tuitls_list.html"

#Class para ver tuitl particular
class TuitlDetalle(DetailView):

      model = Tuitl
      template_name = "AppTuitlon/tuitl_detalle.html"


#Class para borrar tuitls; quedó armada pero no se utilizará para no romper la estética simil Twitter
class TuitlDelete(DeleteView):

    model = Tuitl
    success_url = "/AppTuitlon/tuitl/list"




#Vista para subir avatares
@login_required
def addImg(request):

    if request.method == 'POST': 

        miForm = AvatarForm(request.POST, request.FILES) 

        if miForm.is_valid():

            info= miForm.cleaned_data

            avatar = Avatar(user=request.user, imagen=info['imagen'])

            avatar.save()

            return render(request, "AppTuitlon/inicio.html")

    else:

        miForm = AvatarForm()
    
    return render(request, "AppTuitlon/addImg.html", {'form':miForm})

#Vista para editar Usuarios
@login_required
def editUser(request):

    usuario = request.user 

    if request.method == "POST":   

        miForm = RegisterForm(request.POST) 

        if miForm.is_valid():

            info = miForm.cleaned_data     

           
            usuario.username = info['username']
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.save()

            return render(request, "AppTuitlon/inicio.html")

    else:

        miForm= RegisterForm(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "AppTuitlon/editUser.html",{'miForm':miForm, 'usuario':usuario.username})
