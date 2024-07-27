from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUp, AddUser
from .models import Utilizatori

def home(request):
    utilizatori = Utilizatori.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Te-ai logat cu succes")
                return redirect('home')
            else:
                messages.error(request, "Verifica daca datele sunt corecte")
        else:
            messages.error(request, "Trebuie sa completezi toate campurile")

    return render(request, 'home.html', {'utilizatori': utilizatori})

def logout_user(request):
    logout(request)
    messages.success(request, "Te-ai delogat cu succes")
    return redirect('home')

def send_confirmation_email(user):
    subject = 'Confirmare crearii contului'
    message = f'Buna {user.username},\n\nContul tau a fost creat cu succes!'
    email_from = 'your_email@gmail.com'
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)

def register_user(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)

                Utilizatori.objects.create(
                    user=user,
                    first_name=form.cleaned_data.get('first_name', ''),
                    last_name=form.cleaned_data.get('last_name', ''),
                    email=form.cleaned_data.get('email', ''),
                    phone=form.cleaned_data.get('phone', ''),
                    departament=form.cleaned_data.get('departament', ''),
                    nivel='INCEPATOR',
                    salariu=0.00
                )

                # Trimitere mail de confirmare
                send_confirmation_email(user)
                messages.success(request, "Contul tau a fost creat cu succes")
                return redirect('home')
            else:
                messages.error(request, "A aparut o eroare in crearea contului")
                return redirect('register')
    else:
        form = SignUp()
    return render(request, 'register.html', {'form': form})

def utilizator_detalii(request, pk):
    if request.user.is_authenticated:
        try:
            utilizator_detalii = Utilizatori.objects.get(id=pk)
            return render(request, 'detalii.html', {'utilizator_detalii': utilizator_detalii})
        except Utilizatori.DoesNotExist:
            messages.error(request, "Utilizatorul nu a fost gasit")
            return redirect('home')
    else:
        messages.error(request, "Trebuie sa fii logat")
        return redirect('home')

def sterge_utilizator(request, pk):
    if request.user.is_authenticated:
        try:
            sterge_c = Utilizatori.objects.get(id=pk)
            sterge_c.delete()
            messages.success(request, "Utilizator sters")
        except Utilizatori.DoesNotExist:
            messages.error(request, "Utilizatorul nu a fost gasit")
        return redirect('home')
    else:
        messages.error(request, "Trebuie sa fii logat")
        return redirect('home')

def adauga_user(request):
    form = AddUser(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Utilizator adaugat")
                return redirect('home')
        return render(request, 'adauga_user.html', {'form': form})
    else:
        messages.error(request, "Trebuie sa fii logat")
        return redirect('home')

def modifica_utilizator(request, pk):
    if request.user.is_authenticated:
        try:
            utilizator_curent = Utilizatori.objects.get(id=pk)
        except Utilizatori.DoesNotExist:
            messages.error(request, "Utilizatorul nu a fost gasit")
            return redirect('home')

        if request.method == "POST":
            form = AddUser(request.POST, instance=utilizator_curent)
            if form.is_valid():
                form.save()
                messages.success(request, "Datele utilizatorului au fost modificate cu succes")
                return redirect('home')
        else:
            form = AddUser(instance=utilizator_curent)
        return render(request, 'modifica_utilizator.html', {'form': form})
    else:
        messages.error(request, "Trebuie sa fii logat")
        return redirect('home')
