from django import forms

# Reordering Form and View


class TaskForm(forms.Form):
    position = forms.CharField()