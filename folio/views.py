from django.shortcuts import render
from folio.models import *
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import redirect, render
from .form_enskripsyon import EnkripsyonForm
from .forms import NewProjectForm, UpdateProfileForm


# Create your views here.
def home(request):
    otantifye=request.user.is_authenticated
    
    project = Project.objects.select_related('user').order_by('user')
    profile = None
    profile1 =Profile.objects.all()
    if otantifye:
        profile, created = Profile.objects.get_or_create(user = request.user)
        
        
    
    context ={
        'project' : project,
        'otantifye': otantifye,
        'profile' : profile,
        'profile1' : profile1,
        

    }
    return render(request, 'home.html',context)



def showProfile(request, user):
    projet = Project.objects.select_related('user').filter(user = user)
    profile = Profile.objects.select_related('user').filter(user = user)
    projet0=None
    

    for el in profile:    
        profile0=el.user


    profile1 = Profile.objects.get(user = user)
    modify = ""
    if request.method == 'POST':
        modify = request.POST.get('modify')

 
    if modify:
        if request.user == profile0:
            return redirect(modifyProfile, user = user)
    context ={

        'projet' : projet,
        'profile': profile,
        'profile1': profile1,
        'profile0' : profile0,
 
    }
    return render(request, 'showProfile.html',context)


def redirProfile(request):
    if request.method == 'POST':
        value = request.POST.get('profile')
        projet = Project.objects.all()

        print(value)
        if Project.objects.filter(user = value):
            return redirect(showProfile, user = value)
        else:
            print("Pa gen profil")
    context = {

    }
    return render(request, 'showProfile.html', context)

def modifyProfile(request, user):
    profile = Profile.objects.get(user = user)

    if request.method == "POST":
        form =UpdateProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if form.is_valid:
            profile=form.save(commit=False)
            print(form)
            profile.user=request.user
            profile.save()
            return redirect(home)
    else:
        form=UpdateProfileForm(instance=request.user.profile)

        context = {
            'profile':profile,
            'form' : form

        }
    return render(request, 'modifyProfile.html', context)



def inscrire(request):
    otantifye=request.user.is_authenticated
    context={}
    if not otantifye:
        form = EnkripsyonForm()
        error_message = None
        if request.method == 'POST':
            data=request.POST
            form = EnkripsyonForm(data=data)
            email=request.POST.get('username')
            modpas=request.POST.get('password')
            cmodpas= request.POST.get('confirm_password')

            if modpas != cmodpas:
                error_message = "Password isn't the same"
            elif len(modpas) < 6:
                error_message = "Password too short"
            else:
                User.objects.create_user(username=email, password=modpas)
                return redirect(home)
        else:
            form=EnkripsyonForm()
        
        context={
            'form': form,
            'otantifye': otantifye,
            'error_message' : error_message
        }
    else:
        return redirect(home)
    return render(request, 'enskripsyon.html', context)

def koneksyon(request):
    context = {}
    otantifye=request.user.is_authenticated
    error_message = None
    if not otantifye:
        if request.method == 'POST':
            non=request.POST.get('non')
            modpas=request.POST.get('modpas')

        
            user = authenticate(username = non, password = modpas)
            if user is None:
                error_message = "user doesn't exist try again"
                print(error_message)
            else:
                login(request, user)
                return redirect(home)

    
            context={
                'error_message' : error_message
            }
    else:
        return redirect(home)
    return render(request, 'koneksyon.html',context)


def newProject(request):
    print("new project")
    otantifye=request.user.is_authenticated
    if not otantifye:
        return redirect(koneksyon)
    if  otantifye:
        if request.method == "POST": 
            form =NewProjectForm(data=request.POST, files=request.FILES)
            if form.is_valid(): 
                projet=form.save(commit=False)
                print(form)
                projet.user=request.user
                projet.save()

                for el in form.cleaned_data['categorys']:
                    selection = Category.objects.get(non = el)
                    selection.save()
                    projet.categorys.add(selection)
                return redirect(home)

        else:
            form=NewProjectForm()

        context={
            'form':form,
            'otantifye':otantifye
            }
    else :
        return redirect(inscrire)
    return render(request, 'new_project.html',context)

def showProject(request, slug, prouser =None):
    projet = Project.objects.select_related('user').prefetch_related('categorys').filter(slug = slug)
    otantifye=request.user.is_authenticated


    if request.method == 'POST':
        value = request.POST.get('delete')
        value1=request.POST.get('new')
        if value:
            if otantifye:
                user = request.user.id
                if prouser:
                    user = int(user)
                    prouser =int(prouser)
                if user == prouser:
                    Project.objects.filter(slug = slug).delete()
                    return redirect(home)
        if value1:
            return redirect(newProject)
    context = {
        'projet' : projet

    }
    return render(request, 'show_project.html', context)

def newProfile(request):
    otantifye=request.user.is_authenticated
    if not otantifye:
        return redirect(koneksyon)
    if  otantifye:
        if request.method == "POST":
            form =NewProfileForm(data=request.POST, files=request.FILES)
            if form.is_valid():
              profile=form.save(commit=False)
              profile.user=request.user
              profile.save()
            else:
                print("fomile a gen ere")

        else:
            form=NewProfileForm()

        context={
            'form':form,
            'otantifye':otantifye
            }
    else :
        return redirect(inscrire)
    return render(request, 'new_profile.html',context)

def dekonekte(request):
    logout(request)
    return redirect(home)



def navbar(request):
    otantifye=request.user.is_authenticated
 

    context={
        'otantifye' : otantifye
    }
    return render(request, 'navbar.html',context)
