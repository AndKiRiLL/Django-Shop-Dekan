from django import forms

class FormAdd(forms.Form):
    caption = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form__block__chapter__input', 'name': 'caption'}))
    price = forms.IntegerField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form__block__chapter__input', 'name': 'price'}))
    path_img = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form__block__chapter__input', 'name': 'path_img'}))
    select = forms.ChoiceField(choices=((1, 'Процессоры'), (2, 'Видеокарты'), (3, 'Оперативная память')), label='', widget=forms.Select(attrs={'class': 'form__block__chapter__input__radial', 'name': 'select'}))
