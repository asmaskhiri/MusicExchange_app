from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import BandForm, ContactUsForm, ListingForm
from django.http import Http404

def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})


def band_detail(request, id):  # notez le paramètre id supplémentaire

    try:
        band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
    except Band.DoesNotExist:
        raise Http404("this id does not exist")
    return render(request,
                 'listings/band_detail.html',
                 {'band': band})  # nous mettons à jour cette ligne pour passer le groupe au gabarit


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
    else:

        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})


def listings(request):
    lists = Listing.objects.all()
    return render(request,
    'listings/listings.html',
    {'liste':lists})


def listing_detail(request, id):  # notez le paramètre id supplémentaire
    try:
        ad = Listing.objects.get(id=id)  # nous insérons cette ligne pour obtenir l' annonce avec cet id
    except Listing.DoesNotExist:
        raise Http404("this id does not exist")

    return render(request,
                 'listings/listing_detail.html',
                 {'ad': ad})  # nous mettons à jour cette ligne pour passer le groupe au gabarit

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            list = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('ad-detail', list.id)
    else:

        form = ListingForm()

    return render(request,
            'listings/Create_new_listing.html',
            {'form': form})



def about(request):
    return render(request, 'listings/about.html')


def contact(request):
    # ajoutez ces instructions d'impression afin que nous puissions jeter un coup d'oeil à « request.method » et à « request.POST »
    # print('La méthode de requête est : ', request.method)
    #print('Les données POST sont : ', request.POST)
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent') # ajoutez cette instruction de retour

    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
                'listings/contact.html',
                {'form': form})
def redirectPage(request):
    return render(request, 'listings/redirect.html')


