from django import forms
from .models import Todo


class TodoSerializer(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter task...",
            }
        ),
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Description...",
                'rows': '5'
            }
        ),
    )

    is_completed = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(
            attrs={"class": "form-check-input"}),
    )