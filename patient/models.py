from django.db import models

# Create your models here.
class Feature(models.Model):
    femaleres = models.BooleanField(default=False)
    age = models.IntegerField()
    married = models.BooleanField(default=False)
    children = models.IntegerField()
    hhsize = models.IntegerField()
    edu = models.IntegerField()
    hh_children = models.IntegerField()
    cons_social =  models.IntegerField()
    cons_allfood = models.IntegerField()
    cons_med_total = models.IntegerField()
    cons_ed = models.IntegerField()
    ent_wagelabor = models.BooleanField(default=False)
    ent_ownfarm = models.BooleanField(default=False)
    ent_business = models.BooleanField(default=False)
    ent_nonagbusiness = models.BooleanField(default=False)
    fs_meat  = models.IntegerField()
    fs_enoughtom =models.BooleanField(default=False)
    fs_sleephun = models.BooleanField(default=False)
    med_expenses_hh_ep = models.IntegerField()
    labor_primary = models.BooleanField(default=False)
