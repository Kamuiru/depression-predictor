from django.shortcuts import render, redirect
from .forms import FeatureForm
import joblib
from django.conf import settings
import os
from .models import Feature

# Create your views here.
def index(request):
    feature_form = FeatureForm(request.POST or None)
    if feature_form.is_valid():
        feature_form.save()
        return redirect('results')
    return render(request, 'patient/index.html', {'feature_form':feature_form})

def clinic(request):
    path = 'model/model.joblib'
    absolute_path = os.path.join(settings.STATIC_ROOT, path)
    model = joblib.load(absolute_path)

    features = Feature.objects.latest('id')
    predictions = model.predict([[features.femaleres, features.age, features.married, features.children, features.hhsize, features.edu, features.hh_children, features.cons_allfood, features.cons_med_total, features.cons_ed, features.cons_social, features.ent_wagelabor, features.ent_ownfarm, features.ent_business, features.ent_nonagbusiness, features.fs_meat, features.fs_enoughtom,features.fs_sleephun, features.med_expenses_hh_ep, features.labor_primary]])
    return render(request, 'patient/clinic.html', {'predictions':predictions})


