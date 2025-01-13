from django import forms
from main.models import Example


class AddExampleForm(forms.ModelForm):
    
    class Meta:
        model = Example
        fields = ['first_name', 'last_name', 'email', 'age']
        
        labels = {
            'first_name': 'Enter Your First name ',
            'last_name': 'Write the Text ',
            'email': 'Write Email ',
            'age': 'Enter Your Age '
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.Textarea(attrs={'cols':50, 'rows': 5})

        }
