from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.apps import apps
from .models import *


def display_model(request, model_pk=1):
    my_model = get_object_or_404(MyModels, pk=model_pk)

    model = apps.get_model(app_label='home_app', model_name=my_model.name)

    model_data = model.objects.all()
    print(model_data)

    fields_and_values = []

    for item in model_data:
        field_data = {}

        for field in item._meta.fields:
            field_data[field.name] = getattr(item, field.name)

            fields_and_values.append(field_data)
    return render(request, 'home_app/index.html', {
        'model_data': model_data,
        'model_title': my_model.name,
        'fields_and_values': fields_and_values,
    })

