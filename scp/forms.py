from django import forms
from django.forms import TextInput, DateInput, Textarea
from .models import Task, Profile, Project
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomeCreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Адрес электронной почты")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','code','language','status','start_date','end_date']
        widgets = {
            'title': TextInput(attrs={
                'class': 'title-project',
                'placeholder': 'Введите название задачи',
                'style': 'resize: none;',
                'required': True,
            }),
            'description': Textarea(attrs={
                'class': 'desc-project',                     # Класс для CSS-стилей
                'placeholder': 'Введите описание',          # Подсказка внутри поля
                'rows': 5,                                  # Количество строк
                'cols': 50,                                 # Количество символов в строке
                'maxlength': 500,                           # Максимальная длина текста
                'required': True,                           # Поле обязательно для заполнения
                'style': 'resize: vertical;', # Inline-стили (запрет изменения размера и цвет границы)
            }),
            'code': Textarea(attrs={
                'class': 'desc-project',                     
                'placeholder': 'Введите код проекта',         
                'rows': 35,                                  
                'cols': 50,                                  
                'required': False,                           
                'style': 'resize: vertical;',
            }),
            'start_date': DateInput(attrs={
                'class': 'desc-project', 
                'type':'date',
                'required': False,
            }),
            'end_date': DateInput(attrs={
                'class': 'desc-project', 
                'type':'date',
                'required': False,
            })

        }

class EditProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','code','language','status','start_date','end_date']
        widgets = {
            'title': TextInput(attrs={
                'class': 'title-project',
                'placeholder': 'Введите название задачи',
                'style': 'resize: none;',
                'required': True,
            }),
            'description': Textarea(attrs={
                'class': 'desc-project',                     # Класс для CSS-стилей
                'placeholder': 'Введите описание',          # Подсказка внутри поля
                'rows': 5,                                  # Количество строк
                'cols': 50,                                 # Количество символов в строке
                'maxlength': 500,                           # Максимальная длина текста
                'required': True,                           # Поле обязательно для заполнения
                'style': 'resize: vertical;', # Inline-стили (запрет изменения размера и цвет границы)
            }),
            'code': Textarea(attrs={
                'class': 'desc-project',                     
                'placeholder': 'Введите код проекта',         
                'rows': 35,                                  
                'cols': 50,                                  
                'required': False,                           
                'style': 'resize: vertical;',
            }),
            'start_date': DateInput(attrs={
                'class': 'desc-project', 
                'type':'date',
                'required': False,
            }),
            'end_date': DateInput(attrs={
                'class': 'desc-project', 
                'type':'date',
                'required': False,
            })

        }

class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','status','priority']
        widgets = {
            'title': TextInput(attrs={
                'class': 'title-project',
                'placeholder': 'Введите название задачи',
                'style': 'resize: none;',
                'required': True,
            }),
            'description': Textarea(attrs={
                'class': 'desc-project',                     # Класс для CSS-стилей
                'placeholder': 'Введите описание',          # Подсказка внутри поля
                'rows': 5,                                  # Количество строк
                'cols': 50,                                 # Количество символов в строке
                'maxlength': 500,                           # Максимальная длина текста
                'required': True,                           # Поле обязательно для заполнения
                'style': 'resize: vertical;', # Inline-стили (запрет изменения размера и цвет границы)
            }),

        }

class EditTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','status','priority']
        widgets = {
            'title': TextInput(attrs={
                'class': 'title-project',
                'placeholder': 'Введите название задачи',
                'style': 'resize: none;',
                'required': True,
            }),
            'description': Textarea(attrs={
                'class': 'desc-project',                     # Класс для CSS-стилей
                'placeholder': 'Введите описание',          # Подсказка внутри поля
                'rows': 5,                                  # Количество строк
                'cols': 50,                                 # Количество символов в строке
                'maxlength': 500,                           # Максимальная длина текста
                'required': True,                           # Поле обязательно для заполнения
                'style': 'resize: vertical;', # Inline-стили (запрет изменения размера и цвет границы)
            }),

        }

class ProjectFilterForm(forms.ModelForm):
    model = Project
    fields = ['created_at']
    created_at =forms.DateField(
        widget = forms.DateInput(attrs={'type':'created_at'}),
        required=False,
        label = 'Срок выполнения'
    )

class ProfileSettings(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'style': 'display: none; text-decoration: none;' , 'class': 'id_avatar'}),
            'bio': forms.Textarea(attrs={'class': 'bio-profile', 'rows': 5, 'style': 'resize: vertical'}),
        }
 