from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    nome_da_empresa = "CLINICA PET"
    descricao_da_empresa = "A nossa rede de clínicas está no mercado a mais de 20 anos. São mais de 50 profissionais trabalhando conosco."

    contato_empresa = {
        "endereco": "Avenida Brigadeiro Faria Lima, 1987 - Itaim Bibi - São Paulo - SP",
        "telefone": "+55 11 97674-1514",
        "email": "clinicapet@clinicasp.com.br",
    }

    return render(request, 'empresa/index.html', {'nome_da_empresa': nome_da_empresa, 'descricao_da_empresa': descricao_da_empresa, 'contato_empresa': contato_empresa})



def sobre(request):
    return HttpResponse("Página sobre")


def servicos(request):
    return HttpResponse("Página de Serviços")