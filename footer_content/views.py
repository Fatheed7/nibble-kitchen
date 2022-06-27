from django.shortcuts import render
from .models import Returns, Postage, Privacy


def ReturnsContent(request):
    """ A view that renders the cart contents page """

    returns = Returns.objects.all()

    context = {
        'returns': returns,
    }

    return render(request, 'footer_content/returns.html', context)

def PostageContent(request):
    """ A view that renders the cart contents page """

    postage = Postage.objects.all()

    context = {
        'postage': postage,
    }

    return render(request, 'footer_content/postage.html', context)

def PrivacyContent(request):
    """ A view that renders the cart contents page """

    privacy = Privacy.objects.all()

    context = {
        'privacy': privacy,
    }

    return render(request, 'footer_content/privacy.html', context)