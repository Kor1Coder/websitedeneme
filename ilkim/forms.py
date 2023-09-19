from django import forms
class nameform(forms.Form):
        name = forms.CharField(label='name', max_length=80,required=False)
        surname = forms.CharField(label='surname',max_length=80,required=False)
        email = forms.EmailField(label='email',required=False)
        textarea = forms.CharField(required=False)
        inlineRadioOptions=forms.CharField(required=False)

    # Create your models here.