from django import forms
from first_app.models import Topic


class NewTopic(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
