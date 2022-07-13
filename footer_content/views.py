from django.shortcuts import render
from .models import Returns, Postage, Privacy, About


def ReturnsContent(request):
    """ A view that renders the returns and refunds page """

    returns = Returns.objects.all()

    context = {
        'returns': returns,
    }

    return render(request, 'footer_content/returns.html', context)


def PostageContent(request):
    """ A view that renders the postage and packaging page """

    postage = Postage.objects.all()

    context = {
        'postage': postage,
    }

    return render(request, 'footer_content/postage.html', context)


def PrivacyContent(request):
    """ A view that renders the privacy content page """

    privacy = Privacy.objects.all()

    context = {
        'privacy': privacy,
    }

    return render(request, 'footer_content/privacy.html', context)


def AboutContent(request):
    """ A view that renders the about us content page """

    about = About.objects.all()

    context = {
        'about': about,
    }

    return render(request, 'footer_content/about.html', context)
