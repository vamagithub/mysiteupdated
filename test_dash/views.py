# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import UploadForms
from django.http import HttpResponse
# Create your views here.
from mysite import settings


@login_required
def Form(request):
    form = UploadForms
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            y = form.cleaned_data.get("yr")
            return render(request, "dash.html", {"form": form, })
    else:
        form = UploadForms()

    if hasattr(request.user, 'thing'):
        return render(request, "dash.html", {"form": form, })
    else:
        return render(request, 'settings1.html')


@login_required
def Upload(request):
    form = UploadForms(request.POST or None)
    y = form['yr'].value()
    from_email = request.user
    to_email = [from_email, 'vamagithub@gmail.com']
    subject = "EasyReturn Form-16 Submission"
    mail = EmailMessage(subject, y, from_email, to_email)
    for count, x in enumerate(request.FILES.getlist("files")):
        mail.attach(x.name, x.read().decode("ISO-8859-1"),
                    x.content_type)  # change ur type in unix system use only x.read()
    mail.send()

    # return HttpResponse("Files Sent !")
    return render(request, "display.html", {})
