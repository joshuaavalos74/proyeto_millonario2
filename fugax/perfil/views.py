from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from usuario.models import Perfil
# Create your views here.

@login_required
def perfil_especifico(request, profile_pk):
	"""."""
	perfil = Perfil.objects.get(pk=profile_pk)
	return render(request, 'profile.html',{'Perfil': perfil})

@login_required
def perfil(request):
	p = Perfil.objects.get(pk=user.pk)
	""" redirect codigo aqui  """
	