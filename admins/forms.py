from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError

from main.models import StandardSection
from user.models import User, Company, UserCompanyInfo


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-8',
                                      'placeholder': 'Введите никнейм'})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-8',
                                       'placeholder': 'Введите email'})
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput()
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите имя'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите фамилию'})
    )
    patronymic = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите Отчество'})
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control py-8',
                                      'placeholder': 'Введите номер телефона'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-8',
                                          'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-8',
                                          'placeholder': 'Повторите пароль'})
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'image', 'first_name',
            'last_name', 'patronymic', 'phone', 'password1', 'password2',
        )

# Временное решение
class UserEditForm(forms.ModelForm):
    username_validator = UnicodeUsernameValidator()
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-8',
                                      'placeholder': 'Введите никнейм'}),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        }
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-8',
                                       'placeholder': 'Введите email'})
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput()
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите имя'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите фамилию'})
    )
    patronymic = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите Отчество'})
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-8',
                                      'placeholder': 'Введите номер телефона'})
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'image', 'first_name',
            'last_name', 'patronymic', 'phone',
        )


class UserChangePasswordForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': ('The two password fields didn’t match.'),
    }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-8',
                                          'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-8',
                                          'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('password','password2',)

    def save(self, commit=True):
        if self.cleaned_data["password"] == self.cleaned_data["password2"]:
            user = super(UserChangePasswordForm, self).save(commit=True)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


class UserCompanyInfoForm(forms.ModelForm):
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control py-8',
                                   'placeholder': 'Введите название организации'})
    )
    department = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите название отдела'})
    )
    position = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите должность'})
    )
    expert = forms.BooleanField(
        required=False
    )
    chief_project_engineer = forms.BooleanField(
        required=False
    )
    assistant = forms.BooleanField(
        required=False
    )

    class Meta:
        model = UserCompanyInfo
        fields = ('company', 'department', 'position', 'expert', 'chief_project_engineer', 'assistant',)


class CompanyRegistrationFrom(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите название организации'})
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control py-8',
                                      'placeholder': 'Введите номер телефона'})
    )
    email = forms.CharField(
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control py-8',
                                       'placeholder': 'Введите email'})
    )
    manager = forms.ModelChoiceField(
        required=False,
        queryset=User.objects.select_related().exclude(
            id__in=(Company.objects.filter(manager__isnull=False).values('manager'))),
        empty_label='Выберете пользователя',
        widget=forms.Select(attrs={'class': 'form-control py-8',
                                   'placeholder': 'Выберите менеджера'})
    )

    class Meta:
        model = Company
        fields = ('name', 'phone', 'email', 'manager')


class CompanyEditForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите название организации'})
    )
    manager = forms.ModelChoiceField(
        queryset=User.objects.select_related().exclude(
            id__in=(Company.objects.filter(manager__isnull=False).values('manager'))),
        empty_label='Выберете пользователя',
        widget=forms.Select(attrs={'class': 'form-control py-8'})
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-8',
                                      'placeholder': 'Введите номер телефона'})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-8',
                                       'placeholder': 'Введите email'})
    )

    class Meta:
        model = Company
        fields = ('name', 'manager', 'phone', 'email',)



class StandardSectionCreateForm(forms.ModelForm):
    PROJECT_TYPE_CHOICES = {
        (1, 'Площадной'),
        (2, 'Линейный'),
    }
    abbreviation = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите аббревиатуру раздела'}),
        max_length=16
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control py-8',
                   'placeholder': 'Введите наименование раздела'}),
        max_length=256
    )
    project_type = forms.ChoiceField(
        choices=PROJECT_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control py-8'})
    )

    class Meta:
        model = StandardSection
        fields = ('abbreviation', 'name', 'project_type', )