from django import forms
from .models import Feature

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = [
                 'femaleres', 'age', 'married', 'children', 'hhsize','edu', 'hh_children', 'cons_social',
           'cons_allfood', 'cons_med_total', 'cons_ed', 'ent_wagelabor', 'ent_ownfarm','ent_business',
                           'ent_nonagbusiness', 'fs_meat','fs_enoughtom', 'fs_sleephun','med_expenses_hh_ep', 'labor_primary'
        ]

    # def __init__(self, *args, **kwargs):
    #     super(FeatureForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'

    def __init__(self, *args, **kwargs):
        super(FeatureForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, forms.CheckboxInput):
                self.fields[field].widget.attrs['class'] = 'form-check-input'
            else:
                self.fields[field].widget.attrs['class'] = 'form-control'