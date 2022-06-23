from django import forms


class RequestGameForm(forms.Form):
    username = forms.CharField(max_length=100, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))

    gametitle = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter title of the game'}))

    officialsite = forms.URLField(required=False,
                                  widget=forms.TextInput(attrs={'placeholder': 'Enter url for' + 'official site of the game'}))
