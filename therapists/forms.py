from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Schedule
        fields = [
            'user',
            'day',
            'hours',
        ]

    def __init__(self,request, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['value'] = request.user.email
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'