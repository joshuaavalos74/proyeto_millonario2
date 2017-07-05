from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from usuario.models import Perfil
# Create your views here.

@login_required
def perfil_especifico(request, profile_pk):
	"""."""
	perfil = Perfil.objects.get(pk=profile_pk)
	print("cacacacacacacac", perfil.usuario)
	return render(request, 'profile.html',{'perfil': perfil})

@login_required
def perfil(request):
	p = Perfil.objects.get(usuario__pk=request.user.pk)
	return redirect('/perfil/%s' % p.pk)
	""" redirect codigo aqui  """
	