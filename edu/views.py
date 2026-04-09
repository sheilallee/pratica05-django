from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Autor, Editora, Livro, Publica
from .forms import AutorForm, EditoraForm, LivroForm, PublicaForm


# ─── Index ─────────────────────────────────────────────────────────────────────

def index(request):
    context = {
        'total_autores': Autor.objects.count(),
        'total_editoras': Editora.objects.count(),
        'total_livros': Livro.objects.count(),
        'total_publicacoes': Publica.objects.count(),
    }
    return render(request, 'edu/index.html', context)


# ─── Autor ──────────────────────────────────────────────────────────────────────

def autor_list(request):
    autores = Autor.objects.all().order_by('nome')
    return render(request, 'edu/autor_list.html', {'autores': autores})


def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor cadastrado com sucesso!')
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'edu/autor_form.html', {'form': form, 'titulo': 'Novo Autor'})


def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor atualizado com sucesso!')
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'edu/autor_form.html', {'form': form, 'titulo': f'Editar Autor: {autor.nome}'})


def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, 'Autor excluído com sucesso!')
        return redirect('autor_list')
    return render(request, 'edu/confirm_delete.html', {
        'objeto': autor,
        'tipo': 'Autor',
        'cancel_url': 'autor_list',
    })


# ─── Editora ─────────────────────────────────────────────────────────────────────

def editora_list(request):
    editoras = Editora.objects.all().order_by('nome')
    return render(request, 'edu/editora_list.html', {'editoras': editoras})


def editora_create(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editora cadastrada com sucesso!')
            return redirect('editora_list')
    else:
        form = EditoraForm()
    return render(request, 'edu/editora_form.html', {'form': form, 'titulo': 'Nova Editora'})


def editora_update(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editora atualizada com sucesso!')
            return redirect('editora_list')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'edu/editora_form.html', {'form': form, 'titulo': f'Editar Editora: {editora.nome}'})


def editora_delete(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        editora.delete()
        messages.success(request, 'Editora excluída com sucesso!')
        return redirect('editora_list')
    return render(request, 'edu/confirm_delete.html', {
        'objeto': editora,
        'tipo': 'Editora',
        'cancel_url': 'editora_list',
    })


# ─── Livro ────────────────────────────────────────────────────────────────────────

def livro_list(request):
    livros = Livro.objects.select_related('editora').all().order_by('titulo')
    return render(request, 'edu/livro_list.html', {'livros': livros})


def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('livro_list')
    else:
        form = LivroForm()
    return render(request, 'edu/livro_form.html', {'form': form, 'titulo': 'Novo Livro'})


def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso!')
            return redirect('livro_list')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'edu/livro_form.html', {'form': form, 'titulo': f'Editar Livro: {livro.titulo}'})


def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('livro_list')
    return render(request, 'edu/confirm_delete.html', {
        'objeto': livro,
        'tipo': 'Livro',
        'cancel_url': 'livro_list',
    })


# ─── Publica ───────────────────────────────────────────────────────────────────────

def publica_list(request):
    publicacoes = Publica.objects.select_related('livro', 'autor').all().order_by('livro__titulo')
    return render(request, 'edu/publica_list.html', {'publicacoes': publicacoes})


def publica_create(request):
    if request.method == 'POST':
        form = PublicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicação cadastrada com sucesso!')
            return redirect('publica_list')
    else:
        form = PublicaForm()
    return render(request, 'edu/publica_form.html', {'form': form, 'titulo': 'Nova Publicação'})


def publica_update(request, pk):
    publica = get_object_or_404(Publica, pk=pk)
    if request.method == 'POST':
        form = PublicaForm(request.POST, instance=publica)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicação atualizada com sucesso!')
            return redirect('publica_list')
    else:
        form = PublicaForm(instance=publica)
    return render(request, 'edu/publica_form.html', {
        'form': form,
        'titulo': f'Editar Publicação: {publica}',
    })


def publica_delete(request, pk):
    publica = get_object_or_404(Publica, pk=pk)
    if request.method == 'POST':
        publica.delete()
        messages.success(request, 'Publicação excluída com sucesso!')
        return redirect('publica_list')
    return render(request, 'edu/confirm_delete.html', {
        'objeto': publica,
        'tipo': 'Publicação',
        'cancel_url': 'publica_list',
    })
