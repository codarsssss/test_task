from django.shortcuts import render, get_object_or_404
from django.apps import apps
from .models import *
from .forms import ModelAddForm


def display_model(request, model_pk=1):
    my_model = get_object_or_404(MyModels, pk=model_pk)
    model = apps.get_model('home_app', my_model.name)
    model_data = model.objects.all()
    fields = model._meta.get_fields()[1:]
    fields = fields[model_pk - 1:] + fields[:model_pk - 1]

    if request.method == 'POST':
        form = ModelAddForm(request.POST)
        if form.is_valid():
            f = [name.name for name in fields]
            v = form.cleaned_data.values()

            model.objects.create(**dict(zip(f, v)))
    else:
        form = ModelAddForm()

    return render(request, 'home_app/index.html', {
        'model_data': model_data,
        'model_title': my_model.name,
        'fields': fields,
        'pk':model_pk,
        'max_pk': len(MyModels.objects.all()),
        'form': form
    })
