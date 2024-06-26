from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm
# Create your views here.


def about_me(request):
    """
    Renders latest info on site author plus allows user collab requests.

    Displays individual instance of :model:`about.About`.

    **For context**
    ``about``
        The latest instance of :model:`about.About`.
        ``collaborate_form``
            An instance of :form:`about.CollaborateForm`.

    **Template**
    :template:`about/about.html`
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Your collaboration request has been \
                                 successfully received. The usual response \
                                 time is around 3 working days.")

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form
         },
    )
