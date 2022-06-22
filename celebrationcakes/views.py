from django.shortcuts import render


def celebrationcakes(request):
    """ A view that renders the cart contents page """

    return render(request, 'celebrationcakes/celebrationcakes.html')