from django.shortcuts import render

def listado_inmuebles(request):
    return render(request, 'inmuebles/listado.html')
