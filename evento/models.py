from django.db import models
from django.utils import timezone

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.CharField('email', max_length=200)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()

        super(Pessoa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

class ArtigoCientifico(models.Model):
    titulo = models.CharField('titulo',max_length=300)
    autores = models.ManyToManyField('Autor')
    evento = models.ForeignKey('EventoCientifico')

    def save(self, *args, **kwargs):
        self.titulo = self.titulo.upper()

        super(ArtigoCientifico, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nome = models.ForeignKey('Pessoa')
    curriculo = models.CharField('curriculo',max_length=200)
    artigos = models.ManyToManyField('ArtigoCientifico')

    def save(self, *args, **kwargs):
        self.curriculo = self.curriculo.upper()

        super(Autor, self).save(*args, **kwargs)


    def __str__(self):
        return self.curriculo

class PessoaJuridica(models.Model):
    nome = models.ForeignKey('Pessoa')
    cnpj = models.CharField('cnpj',max_length=20)
    razao_social = models.CharField('razao social',max_length=50)

    def save(self, *args, **kwargs):
        self.cnpj = self.cnpj.upper()

        super(PessoaJuridica, self).save(*args, **kwargs)


    def __str__(self):
        return self.cnpj


class PessoaFisica(models.Model):
    nome = models.ForeignKey('Pessoa')
    cpf = models.CharField('cpf',max_length=15)

    def save(self, *args, **kwargs):
        self.cpf = self.cpf.upper()

        super(PessoaFisica, self).save(*args, **kwargs)

    def __str__(self):
        return self.cpf





class Evento(models.Model):
    nome = models.CharField('nome', max_length=200)
    evento_pricipal = models.CharField('evento principal', max_length=200)
    sigla= models.CharField('Sigla', max_length=20)
    data_hora_inicio = models.DateTimeField('data e hora do inicio do evento',default=timezone.now)
    palavras_chave = models.CharField('encerramento do evento', max_length=200)
    logotipo = models.CharField('logotipo',max_length=40)
    realizador = models.ForeignKey('Pessoa')
    cidade = models.CharField('cidade', max_length=80)
    uf = models.CharField('uf',max_length=2)
    endereco = models.CharField('endereco',max_length=200)
    cep =  models.CharField('cep',max_length=15)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()

        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nome)

class EventoCientifico(models.Model):
    evento = models.ForeignKey('Evento')
    issn = models.CharField('issn',max_length=40)
    artigo_cientifico = models.ManyToManyField('ArtigoCientifico')

    def save(self, *args, **kwargs):
        self.issn = self.issn.upper()

        super(EventoCientifico, self).save(*args, **kwargs)

    def __str__(self):
        return self.issn

class InscricaoEvento(models.Model):
    evento = models.ForeignKey('Evento')
    participantes = models.ManyToManyField('PessoaFisica')
    data_inscricao = models.DateTimeField('data e hora da inscrica',default=timezone.now)
    TIPO_PESSOA = (
        (u'Professor', u'Professor'),
        (u'Aluno', u'Aluno'),
        (u'Profissional', u'Profissional'),
    )
    tipo_inscricao = models.CharField(max_length=20,choices=TIPO_PESSOA)

    def save(self, *args, **kwargs):
        self.tipo_inscricao = self.tipo_inscricao.upper()

        super(InscricaoEvento, self).save(*args, **kwargs)

    def __str__(self):
        return self.tipo_inscricao
