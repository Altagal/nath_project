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
