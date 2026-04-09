from django import forms
from .models import Autor, Editora, Livro, Publica


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']
        labels = {'nome': 'Nome do Autor'}
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Digite o nome do autor'}),
        }


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']
        labels = {'nome': 'Nome da Editora'}
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Digite o nome da editora'}),
        }


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['isbn', 'titulo', 'publicacao', 'preco', 'estoque', 'editora']
        labels = {
            'isbn': 'ISBN',
            'titulo': 'Título',
            'publicacao': 'Data de Publicação',
            'preco': 'Preço (R$)',
            'estoque': 'Estoque',
            'editora': 'Editora',
        }
        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: 9788575227608'}),
            'titulo': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Título do livro'}),
            'publicacao': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'preco': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01', 'min': '0'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-input', 'min': '0'}),
            'editora': forms.Select(attrs={'class': 'form-input'}),
        }


class PublicaForm(forms.ModelForm):
    class Meta:
        model = Publica
        fields = ['livro', 'autor']
        labels = {
            'livro': 'Livro',
            'autor': 'Autor',
        }
        widgets = {
            'livro': forms.Select(attrs={'class': 'form-input'}),
            'autor': forms.Select(attrs={'class': 'form-input'}),
        }
