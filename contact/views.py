from django.shortcuts import render
from .forms import ContactForm

def ContactPage(request):
    """ A view that renders the contact us page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)