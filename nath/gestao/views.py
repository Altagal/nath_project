from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gestao.models import Laboratorio, Projeto, Especie, MaterialBiologico
from gestao.forms import LaboratorioForm, ProjetoForm, EspecieForm, MaterialBiologicoForm

# Laboratorio
@login_required
def laboratorio_list(request):
    pre_context = {
        "card_title": "Laboratórios",
    }

    context = {
        "laboratorio_list": Laboratorio.objects.all(),
    }
    return render(
        request, "gestao/laboratorio_list.html", {**pre_context, **context}
    )


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
    return render(
        request, "gestao/projeto_list.html", {**pre_context, **context}
    )


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
    return render(
        request, "gestao/especie_list.html", {**pre_context, **context}
    )


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


# MaterialBiologico
@login_required
def material_biologico_proprio_list(request):
    pre_context = {
        "card_title": "Minhas Amostras",
    }

    context = {
        "meus_material_list": MaterialBiologico.objects.filter(
            created_by=request.user
        ).all(),
    }
    return render(
        request, "gestao/material_biologico_list.html", {**pre_context, **context}
    )

@login_required
def material_biologico_compartilhados_list(request):
    pre_context = {
        "card_title": "Minhas Amostras",
    }

    context = {
        "material_biologico_list": MaterialBiologico.objects.filter(
            
        ).all(),
    }
    return render(
        request, "gestao/material_biologico_list.html", {**pre_context, **context}
    )


@login_required
def material_biologico_create(request):

    pre_context = {
        "card_title": "Cadastro de Amostras",
    }

    if request.method == "GET":
        context = {
            "form": MaterialBiologicoForm(),
        }

    if request.method == "POST":
        form = MaterialBiologicoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.custom_save(request)
            return redirect("material_biologico_proprio_list")
        else:
            context = {
                "form": form,
            }

    return render(request, "gestao/material_biologico.html", {**pre_context, **context})

