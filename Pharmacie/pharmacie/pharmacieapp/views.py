from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


from .forms import UserLoginForm

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')  # Rediriger vers la page d'accueil après la connexion
            else:
                # Gérer le cas où l'authentification échoue
                # Peut-être afficher un message d'erreur dans le formulaire
                pass
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def register_user(request):
    # Votre logique pour récupérer les données du formulaire d'inscription
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    # Création d'un nouvel utilisateur
    user = User.objects.create_user(username=username, email=email, password=password)

    # Vous pouvez également ajouter d'autres informations à l'utilisateur si nécessaire
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()

    # Rediriger vers une page de succès ou effectuer d'autres actions après l'inscription
    return render(request, 'registration/success.html')


def homepage(request):
    return  render(request, 'homepage.html')
def medicament_list(request):
    medicaments = Medicament.objects.all()
    return render(request, 'medicament_list.html', {'medicaments': medicaments})

def fournisseur_list(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'fournisseur_list.html', {'fournisseurs': fournisseurs})

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'clients_list.html', {'clients': clients})
def assurances_list(request):
    assurances = Assurance.objects.all()
    return render(request, 'assurances_list.html', {'assurances': assurances})
def ventes_list(request):
    ventes = Vente.objects.all()
    return render(request, 'ventes_list.html', {'ventes': ventes})
def commandes_list(request):
    commandes = Commande.objects.all()
    return render(request, 'commandes_list.html', {'commandes': commandes})
def contact(request):
    # Logique de la vue de contact
    return render(request, 'contact.html')
def promotion(request):
    # logique pour la vue promotion
    return render(request, 'promotion.html')
def autre_page(request):
    # Logique pour la vue de l'autre page
    return render(request, 'autre_page.html')

def create_medicament(request):
    if request.method == 'POST':
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MedicamentForm()
    return render(request, 'medicament_form.html', {'form': form})

def create_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FournisseurForm()
    return render(request, 'fournisseur_form.html', {'form': form})

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            type_assurance = form.cleaned_data.get('Type_assurance')
            assurance = Assurance(ID_client=client, Type_assurance=type_assurance)
            assurance.save()
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def make_order(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommandeForm()
    return render(request, 'commande_form.html', {'form': form})
def make_vente(request):
    total_price = 0
    medicaments = []
    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            medicament = form.cleaned_data['ID_medic']
            quantity = form.cleaned_data['Quantite_vendue']
            unit_price = medicament.Prix_médic
            total_price = quantity * unit_price
            medicaments.append({
                'name': medicament.Nom_medic,
                'quantity': quantity,
                'unit_price': unit_price,
                'total_price': total_price
            })

            form.save()
    else:
        form = VenteForm()
    context = {
        'form': form,
        'selected_medicaments': medicaments,
        'total_price': total_price
    }
    return render(request, 'vente_form.html', context)

