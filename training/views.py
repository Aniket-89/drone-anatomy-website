from django.shortcuts import render

# Create your views here.


def training_view(request):

    return render(request, "training/basic-training.html", context={})
