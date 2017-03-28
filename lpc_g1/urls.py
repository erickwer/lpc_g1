"""lpc_g1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from evento.views import inicio,consulta_inscricao
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', inicio, name='inicio'),

    url(r'^consultaInscricao/([0-9]{1})/',consulta_inscricao, name='consultaInscricao'),

    url(r'^eventos/', evento, name='evento'),
    url(r'^evento/([0-9]{1})/',eventoId, name='eventoId'),

    url(r'^eventosCientificos/', eventoCientifico, name='eventosCientificos'),
    url(r'^eventoCientifico/([0-9]{1})/',eventoCientificoId, name='eventoCientificoId'),

    url(r'^pessoas/', pessoa, name='pessoas'),
    url(r'^pessoa/([0-9]{1})/',pessoaId, name='pessoaId'),

    url(r'^pessoasFisicas/', pessoaFisica, name='pessoasFisicas'),
    url(r'^pessoaFisica/([0-9]{1})/',PessoaFisicaId, name='pessoaFisicaId'),

    url(r'^pessoasJuridicas/', pessoaJuridica, name='pessoasJurudicas'),
    url(r'^pessoaFisica/([0-9]{1})/',pessoaJuridicaId, name='pessoaJuridicaId'),

    url(r'^autores/', autor, name='autores'),
    url(r'^autor/([0-9]{1})/',autorId, name='autorId'),

    url(r'^artigos/', artigo, name='artigo'),
    url(r'^artigo/([0-9]{1})/',artigoId, name='artigoId'),

]
