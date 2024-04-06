from django import forms


class ContactForm(forms.Form):
    
    first_name = forms.CharField(max_length=40)
    user_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    title = forms.CharField(max_length=100)
    message_content = forms.CharField(widget=forms.Textarea, max_length=300)
    class Meta:
        fields = ['first_name','user_name','email','title','message_content']