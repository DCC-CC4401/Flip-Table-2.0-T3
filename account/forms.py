from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Client, Peddler, Established
from django.views.generic.edit import UpdateView
from django.contrib.admin import widgets
from django.db import models


class ClientCreateForm(UserCreationForm):
    CHOICES = (
        ('1', 'AvatarEstudiante1.png',),
        ('2', 'AvatarEstudiante2.png',),
        ('3', 'AvatarEstudiante3.png',),
        ('4', 'AvatarEstudiante4.png',))
    choices = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(ClientCreateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['choices'].widget.attrs.update({'class': 'with-gap'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Profile without database save")
        user = super(ClientCreateForm, self).save(commit=True)
        image = "default/" + dict(self.fields['choices'].choices)[self.cleaned_data['choices']]
        profile = Client(user=user, image=image)
        profile.save()
        return user, profile


class PeddlerCreateForm(UserCreationForm):
    cash = forms.BooleanField(initial=True, required=False)
    credit = forms.BooleanField(initial=False, required=False)
    debit = forms.BooleanField(initial=False, required=False)
    social = forms.BooleanField(initial=False, required=False)

    CHOICES = (
        ('1', 'AvatarVendedor1.png',),
        ('2', 'AvatarVendedor2.png',),
        ('3', 'AvatarVendedor3.png',),
        ('4', 'AvatarVendedor4.png',))
    choices = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(PeddlerCreateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['cash'].widget.attrs.update({'class': 'filled-in'})
        self.fields['credit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['debit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['social'].widget.attrs.update({'class': 'filled-in'})
        self.fields['choices'].widget.attrs.update({'class': 'with-gap'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Profile without database save")
        user = super(PeddlerCreateForm, self).save(commit=True)
        image = "default/" + dict(self.fields['choices'].choices)[self.cleaned_data['choices']]
        profile = Peddler(user=user, image=image, cash=self.cleaned_data['cash'], credit=self.cleaned_data['credit'],
                          debit=self.cleaned_data['debit'], social=self.cleaned_data['social'])
        profile.save()
        return user, profile


class EstablishedCreateForm(UserCreationForm):
    cash = forms.BooleanField(initial=True, required=False)
    credit = forms.BooleanField(initial=False, required=False)
    debit = forms.BooleanField(initial=False, required=False)
    social = forms.BooleanField(initial=False, required=False)
    start = forms.TimeField()
    end = forms.TimeField()

    CHOICES = (
        ('1', 'AvatarVendedor1.png',),
        ('2', 'AvatarVendedor2.png',),
        ('3', 'AvatarVendedor3.png',),
        ('4', 'AvatarVendedor4.png',))
    choices = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(EstablishedCreateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['cash'].widget.attrs.update({'class': 'filled-in'})
        self.fields['credit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['debit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['social'].widget.attrs.update({'class': 'filled-in'})
        self.fields['choices'].widget.attrs.update({'class': 'with-gap'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Profile without database save")
        user = super(EstablishedCreateForm, self).save(commit=True)
        image = "default/" + dict(self.fields['choices'].choices)[self.cleaned_data['choices']]
        profile = Established(user=user, image=image, cash=self.cleaned_data['cash'],
                              credit=self.cleaned_data['credit'],
                              debit=self.cleaned_data['debit'], social=self.cleaned_data['social'],
                              start=self.cleaned_data['start'], end=self.cleaned_data['end'])
        profile.save()
        return user, profile


class ClientUpdateForm(forms.ModelForm):
    CHOICES = (
        ('1', 'AvatarEstudiante1.png',),
        ('2', 'AvatarEstudiante2.png',),
        ('3', 'AvatarEstudiante3.png',),
        ('4', 'AvatarEstudiante4.png',))
    choices = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(ClientUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['choices'].widget.attrs.update({'class': 'with-gap'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Profile without database save")
        self.instance.first_name = self.cleaned_data['first_name']
        self.instance.last_name = self.cleaned_data['last_name']
        self.instance.email = self.cleaned_data['email']
        self.instance.save()
        profile = Client.objects.get(user=self.instance)
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.email = self.cleaned_data['email']
        print(profile)
        profile.image = "default/" + dict(self.fields['choices'].choices)[self.cleaned_data['choices']]
        profile.save()
        return profile


class EstablishedUpdateForm(forms.ModelForm):
    cash = forms.BooleanField(initial=True, required=False)
    credit = forms.BooleanField(initial=False, required=False)
    debit = forms.BooleanField(initial=False, required=False)
    social = forms.BooleanField(initial=False, required=False)
    start = forms.TimeField()
    end = forms.TimeField()

    CHOICES = (
        ('1', 'AvatarVendedor1.png',),
        ('2', 'AvatarVendedor2.png',),
        ('3', 'AvatarVendedor3.png',),
        ('4', 'AvatarVendedor4.png',))
    choices = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(EstablishedUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['cash'].widget.attrs.update({'class': 'filled-in'})
        self.fields['credit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['debit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['social'].widget.attrs.update({'class': 'filled-in'})
        self.fields['choices'].widget.attrs.update({'class': 'with-gap'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Profile without database save")
        self.instance.first_name = self.cleaned_data['first_name']
        self.instance.last_name = self.cleaned_data['last_name']
        self.instance.email = self.cleaned_data['email']
        self.instance.save()
        profile = Established.objects.get(user=self.instance)
        profile.image = "default/" + dict(self.fields['choices'].choices)[self.cleaned_data['choices']]
        profile.cash = self.cleaned_data['cash']
        profile.credit = self.cleaned_data['credit']
        profile.debit = self.cleaned_data['debit']
        profile.social = self.cleaned_data['social']
        profile.start = self.cleaned_data['start']
        profile.end = self.cleaned_data['end']
        profile.save()
        return profile


class PeddlerUpdateForm(forms.ModelForm):
    cash = forms.BooleanField(initial=True, required=False)
    credit = forms.BooleanField(initial=False, required=False)
    debit = forms.BooleanField(initial=False, required=False)
    social = forms.BooleanField(initial=False, required=False)

    CHOICES = (
        ('1', 'AvatarVendedor1.png',),
        ('2', 'AvatarVendedor2.png',),
        ('3', 'AvatarVendedor3.png',),
        ('4', 'AvatarVendedor4.png',))
    choices = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(PeddlerUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['cash'].widget.attrs.update({'class': 'filled-in'})
        self.fields['credit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['debit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['social'].widget.attrs.update({'class': 'filled-in'})
        self.fields['choices'].widget.attrs.update({'class': 'with-gap'})

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Profile without database save")
        self.instance.first_name = self.cleaned_data['first_name']
        self.instance.last_name = self.cleaned_data['last_name']
        self.instance.email = self.cleaned_data['email']
        self.instance.save()
        profile = Peddler.objects.get(user=self.instance)
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.email = self.cleaned_data['email']
        profile.image = "default/" + dict(self.fields['choices'].choices)[self.cleaned_data['choices']]
        profile.cash = self.cleaned_data['cash']
        profile.credit = self.cleaned_data['credit']
        profile.debit = self.cleaned_data['debit']
        profile.social = self.cleaned_data['social']
        profile.save()
        return profile

