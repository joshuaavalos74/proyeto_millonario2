from django.shortcuts import render
from usuario.models import Perfil
# Create your views here.
def perfil_especifico(request):
	"""."""
	perfil = Perfil.objects.get()
	return render(request, 'lista_estudiantes.html',{'Perfil': perfil})


