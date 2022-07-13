from django.shortcuts import render
from .models import Gallery


def celebrationcakes(request):
    """ A view that renders the cart contents page """

    gallery = Gallery.objects.all()

    context = {
        'gallery': gallery,
    }

    return render(request, 'celebrationcakes/celebrationcakes.html', context)
