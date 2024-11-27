from django.shortcuts import render

def quienes_somos(request):
    return render(request, 'nosotros/nosotros.html')
