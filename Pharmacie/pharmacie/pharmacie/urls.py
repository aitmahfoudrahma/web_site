from django.urls import path
from pharmacieapp.views import *



urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_user, name='register_user'),
    path('homepage/', homepage, name='homepage'),
    path('', login_view, name='login'),
    path('medicaments/', medicament_list, name='medicament_list'),
    path('fournisseurs/', fournisseur_list, name='fournisseur_list'),
    path('clients/', clients_list, name='clients_list'),
    path('assurances/', assurances_list, name='assurances_list'),
    path('ventes/', ventes_list, name='ventes_list'),
    path('commandes/', commandes_list, name='commandes_list'),
    path('medicaments/create/', create_medicament, name='create_medicament'),
    path('fournisseur/create/', create_fournisseur, name='create_fournisseur'),
    path('client/create/', create_client, name='create_client'),
    path('commande/create/', make_order, name='make_order'),
    path('vente/create/', make_vente, name='make_vente'),
    path('contact/', contact, name='contact'),
    path('promotion/', promotion, name='promotion'),
    path('autre_page/', autre_page, name='autre_page'),

]
