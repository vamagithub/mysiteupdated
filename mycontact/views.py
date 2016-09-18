# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    title_align_center = "True "
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_name = form.cleaned_data.get("name")
        subject = form.cleaned_data.get("subject")
        form_message = form.cleaned_data.get("message")
        str= 'EasyReturn Query:'
        from_email = 'Your Website<hi@easyreturns.tax>'
        to_email = [from_email, 'vamagithub@gmail.com']

        contact_message = "This is a Query Contact Message from \n\t Name:\t\t%s\n\t Message:\t%s ...\tfrom: %s" % (
            form_name,
            form_message,
            form_email)

        send_mail(str+subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)  # SEE THIS MAKE IT TRUE IT DOESNOT WORK

    context = {
        "form": form,
        "title_align_center": title_align_center,
    }

    return render(request, "index.html", context)
