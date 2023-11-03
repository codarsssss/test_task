from django.shortcuts import render, get_object_or_404
from django.apps import apps
from .models import MyModels
from .forms import ModelAddForm


def display_model(request, model_pk=1):
    my_model = get_object_or_404(MyModels, pk=model_pk)
    model = apps.get_model('home_app', my_model.name)
    model_data = model.objects.all()
    fields = model._meta.get_fields()[1:]
    fields_after_shift = fields[model_pk - 1:] + fields[:model_pk - 1]

    if request.method == 'POST':
        form = ModelAddForm(request.POST)
        if form.is_valid():
            model_field_names = [name.name for name in fields]
            args_for_add = form.cleaned_data.values()

            model.objects.create(**dict(zip(model_field_names, args_for_add)))
    else:
        form = ModelAddForm()

    return render(request, 'home_app/index.html', {
        'model_data': model_data,
        'model_title': my_model.name,
        'fields': fields_after_shift,
        'pk': model_pk,
        'max_pk': len(MyModels.objects.all()),
        'form': form
    })
