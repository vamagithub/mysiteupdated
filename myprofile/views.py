from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Thing
from .forms import ThingForm
from django.template.defaultfilters import slugify


# Create your views here.

def settings(request):

    if hasattr(request.user, 'thing'):
        things = Thing.objects.all()
        return render(request, 'settings.html', {'things': things, })
    else:
        return render(request, 'settings1.html')


@login_required
def thing_detail(request, slug):
    # grab the object
    thing = Thing.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'things/thing_detail.html', {'thing': thing, })


@login_required
def edit_thing(request, slug):
    # grab the object
    thing = Thing.objects.get(slug=slug)

    if (thing.user != request.user):
        raise Http404
    # set the form we are using
    form_class = ThingForm

    # if we're coming to this view from a sbmitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('thing_detail', slug=thing.slug)
            # otherwise just create the form
    else:
        form = form_class(instance=thing)

        # and render the template
        return render(request, 'things/edit_thing.html', {'thing': thing, 'form': form, })

@login_required
def create_thing(request):
    form_class = ThingForm
    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(request.POST)

        if form.is_valid():

            # create an instance but dont save yet
            thing = form.save(commit=False)
            # set the additional details
            thing.user = request.user
            thing.slug = slugify(thing.pan)

            # save the object
            thing.save()

            # redirect to our newly created thing
            return redirect('thing_detail', slug=thing.slug)

            # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'things/create_thing.html', {'form': form, })
