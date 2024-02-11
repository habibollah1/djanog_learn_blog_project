from django.shortcuts import render
from .models import KalaList
from django.shortcuts import get_object_or_404


def kala_view_func(request):
    kala_list = KalaList.objects.filter(status='pub')

    return render(request, 'kala/kala_list.html', {'kala_list': kala_list})


def kala_types_func(request, pk):
    kala_type = get_object_or_404(KalaList, pk=pk)

    return render(request, 'kala/types_kala.html', {'kala_type': kala_type})


def new_kala_func(request):

    return render(request, 'kala/new_kala_create.html',)
