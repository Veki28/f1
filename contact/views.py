from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
# Create your views here.


def contact_me(request):
    """
    Renders latest info on site author and allows users to contact author.

    Displays individual instance of :model:`contact.Contact`.

    **For context**
    ``contact``
        The latest instance of :model:`contact.Contact`.
        ``contact_form``
            An instance of :form:`contact.ContactForm`.

    **Template**
    :template:`contact/contact.html`
    """

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Your message has been recieved.")

    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {"contact_form": contact_form
         },
    )
