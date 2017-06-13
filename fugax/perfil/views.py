from django.shortcuts import render
from usuario.models import Perfil
# Create your views here.
def perfil_especifico(request, profile_pk):
	"""."""
	perfil = Perfil.objects.get(pk=profile_pk)
	return render(request, 'profile.html',{'Perfil': perfil})


