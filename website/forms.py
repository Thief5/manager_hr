from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Utilizatori



NIVELURI_EXPERIENTA = [
    ('INCEPATOR', 'Începător'),
    ('INTERMEDIAR', 'Intermediar'),
    ('AVANSAT', 'Avansat'),
]


DEPARTAMENT_CHOICES = [
    ('Gradinarit', 'Gradinarit'),
    ('Vopsele', 'Vopsele'),
    ('Tinichigerie', 'Tinichigerie'),
    ('Unelte', 'Unelte')
]

class SignUp(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    first_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    phone = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'})
    )
    departament = forms.ChoiceField(
        label="", 
        choices=DEPARTAMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'departament', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUp, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small></small></span>'

        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['phone'].label = ''
        self.fields['phone'].help_text = '<span class="form-text text-muted"><small></small></span>'

        self.fields['departament'].widget.attrs['class'] = 'form-control'
        self.fields['departament'].label = ''
        self.fields['departament'].help_text = '<span class="form-text text-muted"><small></small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Parola ta nu poate fi similară cu informații personale</li><li>Parola trebuie să conțină minim 8 caractere</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmă Parola'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Rescrie parola pentru verificare</small></span>'

class AddUser(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Nume", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Prenume", "class": "form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email", "class": "form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Nr. Telefon", "class": "form-control"}), label="")
    departament = forms.ChoiceField(required=True, choices=DEPARTAMENT_CHOICES, widget=forms.Select(attrs={"class": "form-control"}), label="")
    nivel = forms.ChoiceField(required=True, choices=NIVELURI_EXPERIENTA, widget=forms.Select(attrs={"class": "form-control"}), label="")
    salariu = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Salariu", "class": "form-control"}), label="")

    class Meta:
        model = Utilizatori
        exclude = ("user", )