import os, requests, msal, webbrowser, json
import nath.settings as settings
from datetime import datetime
import xlsxwriter

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from gestao.models import (
    Laboratorio,
    Projeto,
    Especie,
    Amostra,
    SolicitacaoAmostra,
)
from gestao.forms import (
    LaboratorioForm,
    ProjetoForm,
    EspecieForm,
    AmostraForm,
    AmostraCompartilhadaForm,
)
from django.contrib import messages
from django.http import HttpResponse
from dotenv import load_dotenv

load_dotenv()


# Laboratorio
@login_required
def laboratorio_list(request):
    pre_context = {
        "card_title": "Laboratórios",
    }

    context = {
        "laboratorio_list": Laboratorio.objects.all(),
    }
    return render(request, "gestao/laboratorio_list.html", {**pre_context, **context})


@login_required
def laboratorio_create(request):

    pre_context = {
        "card_title": "Laboratorio",
    }

    if request.method == "GET":
        context = {
            "form": LaboratorioForm(),
        }

    if request.method == "POST":
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_save(request)
            return redirect("laboratorio_list")
        else:
            context = {
                "form": form,
            }

    return render(request, "gestao/laboratorio.html", {**pre_context, **context})

@login_required
def laboratorio_update(request, pk):
    obj = get_object_or_404(Laboratorio, id=pk)

    pre_context = {
        "card_title": "Laboratorio",
    }

    if request.method == 'GET':
        context = {
            "form": LaboratorioForm(instance=obj),
        }

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect('laboratorio_list')
        else:
            context = {
                "form": form,
            }

    return render(request, 'gestao/laboratorio.html', {**pre_context, **context})


@login_required
def laboratorio_delete(request, pk):
    obj = get_object_or_404(Laboratorio, id=pk)
    if obj.custom_delete(request):
        return redirect('laboratorio_list')
    return redirect('laboratorio_update', pk)


# Projeto
@login_required
def projeto_list(request):
    pre_context = {
        "card_title": "projetos",
    }

    context = {
        "projeto_list": Projeto.objects.all(),
    }
    return render(request, "gestao/projeto_list.html", {**pre_context, **context})


@login_required
def projeto_create(request):

    pre_context = {
        "card_title": "Projeto",
    }

    if request.method == "GET":
        context = {
            "form": ProjetoForm(),
        }

    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_save(request)
            return redirect("projeto_list")
        else:
            context = {
                "form": form,
            }

    return render(request, "gestao/projeto.html", {**pre_context, **context})


@login_required
def projeto_update(request, pk):
    obj = get_object_or_404(Projeto, id=pk)

    pre_context = {
        "card_title": "Projeto",
    }

    if request.method == 'GET':
        context = {
            "form": ProjetoForm(instance=obj),
        }

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect('projeto_list')
        else:
            context = {
                "form": form,
            }

    return render(request, 'gestao/projeto.html', {**pre_context, **context})


@login_required
def projeto_delete(request, pk):
    obj = get_object_or_404(Projeto, id=pk)
    if obj.custom_delete(request):
        return redirect('projeto_list')
    return redirect('projeto_update', pk)


# Especie
@login_required
def especie_list(request):
    pre_context = {
        "card_title": "Especies",
    }

    context = {
        "especie_list": Especie.objects.all(),
    }
    return render(request, "gestao/especie_list.html", {**pre_context, **context})


@login_required
def especie_create(request):

    pre_context = {
        "card_title": "Especie",
    }

    if request.method == "GET":
        context = {
            "form": EspecieForm(),
        }

    if request.method == "POST":
        form = EspecieForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_save(request)
            return redirect("especie_list")
        else:
            context = {
                "form": form,
            }

    return render(request, "gestao/especie.html", {**pre_context, **context})



@login_required
def especie_update(request, pk):
    obj = get_object_or_404(Especie, id=pk)

    pre_context = {
        "card_title": "Especie",
    }

    if request.method == 'GET':
        context = {
            "form": EspecieForm(instance=obj),
        }

    if request.method == 'POST':
        form = EspecieForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect('especie_list')
        else:
            context = {
                "form": form,
            }

    return render(request, 'gestao/especie.html', {**pre_context, **context})


@login_required
def especie_delete(request, pk):
    obj = get_object_or_404(Especie, id=pk)
    if obj.custom_delete(request):
        return redirect('especie_list')
    return redirect('especie_update', pk)


# Amostra
@login_required
def amostra_list(request):
    pre_context = {
        "card_title": "Minhas Amostras",
    }

    context = {
        "amostra_list": Amostra.objects.filter(created_by=request.user).all(),
    }
    return render(
        request,
        "gestao/amostra_list.html",
        {**pre_context, **context},
    )


@login_required
def amostra_create(request):

    pre_context = {
        "card_title": "Cadastro de Amostras",
    }

    if request.method == "GET":
        context = {
            "form": AmostraForm(),
        }

    if request.method == "POST":
        form = AmostraForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.custom_save(request)
            return redirect("amostra_list")
        else:
            context = {
                "form": form,
            }

    return render(request, "gestao/amostra.html", {**pre_context, **context})


@login_required
def amostra_read(request, pk):
    obj = get_object_or_404(Amostra, id=pk)

    pre_context = {
        "card_title": "Amostra",
    }

    if request.method == "GET":
        context = {
            "is_view": True,
            "form": AmostraForm(instance=obj, readonly=True),
            "amostra_obj": obj,
        }

    if request.method == "POST":
        form = AmostraForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect("amostra_list")
        else:
            context = {
                "form": form,
            }

    return render(request, "gestao/amostra.html", {**pre_context, **context})


@login_required
def amostra_update(request, pk):
    obj = get_object_or_404(Amostra, id=pk)

    pre_context = {
        "card_title": "Amostra",
    }

    if request.method == "GET":
        context = {
            "form": AmostraForm(instance=obj),
            "amostra_obj": obj,
        }

    if request.method == "POST":
        form = AmostraForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect("amostra_list")
        else:
            context = {
                "form": form,
            }

    return render(request, "gestao/amostra.html", {**pre_context, **context})


@login_required
def amostra_share_toogle(request, pk):

    obj = get_object_or_404(Amostra, id=pk)
    if not obj.is_compartilhavel:
        obj.is_compartilhavel = True
    else:
        obj.is_compartilhavel = False

    obj.custom_update(request, "Compartilhamento alterado.")

    return redirect("amostra_read", pk=pk)


@login_required
def amostra_compartilhada_list(request):
    pre_context = {
        "card_title": "Amostras Compatilhadas",
    }

    context = {
        "amostra_list": Amostra.objects.filter(is_compartilhavel=True).exclude(
            created_by_id=request.user.id
        ),
    }
    return render(
        request, "gestao/amostra_compartilhada_list.html", {**pre_context, **context}
    )


@login_required
def amostra_compartilhada_read(request, pk):
    obj = get_object_or_404(Amostra, id=pk)

    pre_context = {
        "card_title": "Amostra",
    }

    if request.method == "GET":
        context = {
            "is_view": True,
            "form": AmostraCompartilhadaForm(instance=obj, readonly=True),
            "solicitacao": SolicitacaoAmostra.objects.filter(
                amostra_pk=obj, usuario_solicitante_pk=request.user
            ).first(),
        }

    if request.method == "POST":
        form = AmostraForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_update(request)
            return redirect("amostra_list")
        else:
            context = {
                "form": form,
            }

    return render(
        request, "gestao/amostra_compartilhada.html", {**pre_context, **context}
    )


@login_required
def amostra_solicitar(request, pk):
    amostra_obj = get_object_or_404(Amostra, id=pk)

    # SE  USUARIO JA REALIZOU A SOLICITACAO DA AMOSTRA, NAO PERMITE NOVA SOLICITACAO
    if SolicitacaoAmostra.objects.filter(
        amostra_pk=amostra_obj, usuario_solicitante_pk=request.user
    ):
        return redirect("amostra_compartilhada_read", pk=pk)

    solicitacao_obj = SolicitacaoAmostra(
        amostra_pk=amostra_obj,
        usuario_solicitante_pk=request.user,
    )

    solicitacao_obj.custom_discrete_save(request)
    messages.success(
        request,
        "Solicitação realizada com sucesso. Aguarde a resposta do responsável pela amostra.",
    )

    context = {}
    return redirect("amostra_compartilhada_read", pk=pk)


def solicitacao_read(request, pk):
    solicitacao_obj = get_object_or_404(SolicitacaoAmostra, id=pk)

    pre_context = {
        "card_title": "Solicitação",
    }

    if request.method == "GET":
        context = {
            "is_view": True,
            "form": AmostraCompartilhadaForm(instance=solicitacao_obj, readonly=True),
        }

    return render(
        request, "gestao/amostra_compartilhada.html", {**pre_context, **context}
    )


def atender_solicitacao(request, pk):
    solicitacao_obj = get_object_or_404(SolicitacaoAmostra, id=pk)

    # nao aceita se solicitação ja estiver recusada, cancelada ou entregue
    if solicitacao_obj.status != "P" and solicitacao_obj.status != "A":
        return redirect("amostra_read", pk=solicitacao_obj.amostra_pk.id)

    # Se solicitação ja foi atendida, agora ela sera entregue
    if solicitacao_obj.status == "A":
        solicitacao_obj.status = "E"
        solicitacao_obj.custom_discrete_save(request)
        return redirect("amostra_read", pk=solicitacao_obj.amostra_pk.id)

    # Aceita a solicitação selecionada e recusa as outras
    for solicitacao in solicitacao_obj.amostra_pk.solicitacoes.all():
        if solicitacao.status == "P":
            solicitacao.status = "R"
            solicitacao.custom_discrete_save(request)

    solicitacao_obj.status = "A"  # Aceita
    solicitacao_obj.custom_update(request, "Solicitação realizada.")

    return redirect("amostra_read", pk=solicitacao_obj.amostra_pk.id)


@login_required
def minhas_solicitacoes_list(request):
    pre_context = {
        "card_title": "Minhas Solicitações",
    }

    context = {
        "minhas_solicitacoes_list": SolicitacaoAmostra.objects.filter(
            usuario_solicitante_pk=request.user.id
        ),
    }
    return render(
        request, "gestao/minhas_solicitacoes_list.html", {**pre_context, **context}
    )


def auth_with_code(request):
    client_instance = msal.ConfidentialClientApplication(
        client_id=os.getenv("USER_ID"),
        client_credential=os.getenv("CLIENT_SECRET"),
        authority=settings.AUTHORITY_URL,
    )

    authorization_request_url = client_instance.get_authorization_request_url(
        settings.SCOPES
    )

    webbrowser.open(authorization_request_url, new=True)

    authorization_code = "M.C554_SN1.2.U.c0bd6bdd-430f-6957-6ba0-6ba0f9e07eb4"

    access_token = client_instance.acquire_token_by_authorization_code(
        code=authorization_code,
        scopes=settings.SCOPES,
    )

    access_token_id = access_token["access_token"]
    headers = {"Authorization": "Bearer " + access_token_id}

    response = requests.get(settings.GRAPH_API_ENDPOINT, headers=headers)

    return redirect("home")


def login_to_get_acess_token(request):

    app = msal.PublicClientApplication(
        client_id=os.getenv("APPLICATION_ID"),
        authority=settings.AUTHORITY_URL,
    )

    accounts = app.get_accounts()
    if accounts:
        app.acquire_token_silent(scopes=settings.SCOPES, account=accounts[0])
    flow = app.initiate_device_flow(scopes=settings.SCOPES)
    app_code = flow["message"]
    webbrowser.open(flow["verification_uri"])
    result = app.acquire_token_by_device_flow(flow)

    access_token_id = result["access_token"]
    headers = {"Authorization": "Bearer " + access_token_id}

    response = requests.get(settings.GRAPH_API_ENDPOINT, headers=headers)

    print(response.json())

    return redirect("home")


def generate_access_token(app_id, scopes):
    # Save Session Token as a token file
    access_token_cache = msal.SerializableTokenCache()

    # read the token file
    if os.path.exists("ms_graph_api_token.json"):
        access_token_cache.deserialize(open("ms_graph_api_token.json", "r").read())
        token_detail = json.load(
            open(
                "ms_graph_api_token.json",
            )
        )

        token_detail_key = list(token_detail["access_token"].keys())[0]
        token_expiration = datetime.fromtimestamp(
            int(token_detail["AccessToken"][token_detail_key]["expires_on"])
        )
        if datetime.now() > token_expiration:
            os.remove("ms_graph_api_token.json")
            access_token_cache = msal.SerializableTokenCache()

    # assign a SerializableTokenCache object to the client instance
    client = msal.PublicClientApplication(
        client_id=app_id, token_cache=access_token_cache
    )

    accounts = client.get_accounts()
    if accounts:
        # load the session
        token_response = client.acquire_token_silent(scopes, accounts[0])
    else:
        # authetnicate your accoutn as usual
        flow = client.initiate_device_flow(scopes=scopes)
        print("user_code: " + flow["user_code"])
        webbrowser.open("https://microsoft.com/devicelogin")
        token_response = client.acquire_token_by_device_flow(flow)

    with open("ms_graph_api_token.json", "w") as _f:
        _f.write(access_token_cache.serialize())

    return token_response


def upload_to_onedrive(request):
    access_token = generate_access_token(
        app_id=os.getenv("APPLICATION_ID"),
        scopes=settings.SCOPES,
    )

    headers = {
        "Authorization": "Bearer " + access_token["access_token"],
    }

    file_path = "nath_project\nath\nath\artifacts\exemplo1.one"
    file_name = os.path.basename(file_path)

    with open(file_path, "rb") as upload:
        media_content = upload.read()

    response = request.put(
        settings.GRAPH_API_ENDPOINT
        + f"drive/itens/root:/Amostras/{file_name}:/content",
        headers=headers,
        data=media_content,
    )

    print(response.json())


def download_from_onedrive(request):
    pass


def graph_gab_callback(request):
    code = "Não recebido."
    if request.method == "GET":
        code = request.GET.get("code")
    return HttpResponse("Codigo: " + code)


def excel(request):
    if request.method == "GET":

        rowIndex = 2
        artifact_path = "nath/artifacts/Amostras.xlsx"

        workbook = xlsxwriter.Workbook(artifact_path)
        cell_format = workbook.add_format()
        cell_format.set_text_wrap()
        cell_format.set_align("top")
        cell_format.set_align("left")
        

        worksheet = workbook.add_worksheet()

        worksheet.write("A1", "Tipo da Amostra")
        worksheet.write("B1", "Data da Coleta")
        worksheet.write("C1", "Meio de Acondicionamento")
        worksheet.write("D1", "Condição de Armazenamento")
        worksheet.write("E1", "Especie")
        worksheet.write("F1", "Sexo Animal")
        worksheet.write("G1", "Identificacao Interna(IDI)")
        worksheet.write("H1", "Local da Amostra")

        for amostra in Amostra.objects.all():

            worksheet.write("A" + str(rowIndex), amostra.data_coleta)
            worksheet.write("C" + str(rowIndex), amostra.data_coleta)
            worksheet.write("B" + str(rowIndex), amostra.data_coleta)
            worksheet.write("D" + str(rowIndex), amostra.data_coleta)
            worksheet.write("E" + str(rowIndex), amostra.data_coleta)
            worksheet.write("F" + str(rowIndex), amostra.data_coleta)
            worksheet.write("G" + str(rowIndex), amostra.data_coleta)
            worksheet.write("H" + str(rowIndex), amostra.data_coleta)

            rowIndex += 1

        workbook.close()
    return HttpResponse()
