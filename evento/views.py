from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import Evento
# Create your views here.
def inicio(request):
    html ="""<h1>Opções</h1>
        <ul>
            <li><a href='/eventos'>Eventos</a></li>
            <li><a href='/eventosCientificos'>EventoCientifico</a></li>
            <li><a href='/pessoas'>Pessoas</a></li>
            <li><a href='/pessoasFisicas'>Pessoas Fisicas</a></li>
            <li><a href='/pessoasJurudicas'>Pessoas Juridicas</a></li>
            <li><a href='/autores'>Autores</a></li>
            <li><a href='/artigos'>Artigos</a></li>
        </ul>
        """
    return HttpResponse(html)

def consulta_inscricao(request, id):
    inscricao = InscricaoEvento.objects.get(pk=id)
    return HttpResponse(inscricao.evento+"- "+inscricao.participantes +' - '+str(inscricao.data_inscricao) +' - '+inscricao.tipo_inscricao)
