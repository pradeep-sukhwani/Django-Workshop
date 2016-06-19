from django import forms

class TodoForm(forms.Form):

    name = forms.CharField(max_length=255, min_length=4, required=True)
    is_completed = forms.BooleanField(required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    due_date = forms.DateField(required=False)


class TodoDeleteForm(forms.Form):
    pass