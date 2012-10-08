from django import forms
from django.contrib.formtools.wizard.views import SessionWizardView
from django.template import RequestContext
from django.shortcuts import render_to_response

from eve_db.models import InvType, InvBlueprintType

class SelectBlueprintForm(forms.Form):
    """
    Form to select the blueprint the user wants to manufacture.
    """
    blueprint = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'class' : 'input-large required' }))
    
    def clean_blueprint(self):
        blueprint_name = self.cleaned_data['blueprint']
        
        if len(blueprint_name) < 3:
            raise forms.ValidationError("Blueprint name '%s' is too short!" % blueprint_name)
        
        # Look if there is at least one blueprint that goes by the name given by the user
        blueprints = InvBlueprintType.objects.filter(blueprint_type__name__icontains=blueprint_name)
            
        # If there are no items at all in the result then raise an ValidationError
        if len(blueprints) == 0:
            raise forms.ValidationError("Could not find blueprint '%s'" % blueprint_name)
    
        return blueprint_name
        
class ManufacturingCalculatorForm(forms.Form):
    """
    This is the form where the user types in the information for the manufacturing job. Based
    on those information the calculations will be made.
    """
    
    SKILL_INDUSTRY_CHOICES = (
        (0, 0), 
        (1, 1), 
        (2, 2),
        (3, 3),
        (4, 4), 
        (5, 5)
    )
    
    SKILL_PRODUCTION_EFFICIENCY_CHOICES = (
        (0, 0), 
        (1, 1), 
        (2, 2),
        (3, 3),
        (4, 4), 
        (5, 5)
    )
    
    # (typeID, typeName)
    HARDWIRING_CHOICES = (
        (0, "No Hardwiring"),
        (27170, "Zainou 'Beancounter' Industry BX-801"),
        (27167, "Zainou 'Beancounter' Industry BX-802"),
        (27171, "Zainou 'Beancounter' Industry BX-804")
    )
    
    # blueprint related fields
    blueprint_material_efficiency = forms.IntegerField(min_value=-4, max_value=1000, initial=0, widget=forms.TextInput(attrs={'class': 'input-mini required'}))
    blueprint_production_efficiency = forms.IntegerField(min_value=-4, max_value=1000, initial=0, widget=forms.TextInput(attrs={'class': 'input-mini required'}))
    blueprint_runs = forms.IntegerField(min_value=0, max_value=10000, initial=1, widget=forms.TextInput(attrs={'class': 'input-mini required'}))
    blueprint_price = forms.DecimalField(min_value=0, max_digits=32, decimal_places=2, initial=0, required=False)
    
    # player skill and item related fields
    skill_industry = forms.ChoiceField(choices=SKILL_INDUSTRY_CHOICES, initial=5, widget=forms.Select(attrs={'class': 'input-mini required'}))
    skill_production_efficiency = forms.ChoiceField(choices=SKILL_PRODUCTION_EFFICIENCY_CHOICES, initial=5, widget=forms.Select(attrs={'class': 'input-mini required'}))
    hardwiring = forms.ChoiceField(choices=HARDWIRING_CHOICES, widget=forms.Select(attrs={'class': 'input-xlarge required'}))
    
    # production slot fields
    slot_production_time_modifier = forms.FloatField(min_value=0, max_value=10, initial="1.00", widget=forms.TextInput(attrs={'class': 'input-mini required'}))
    slot_material_modifier = forms.FloatField(min_value=0, max_value=10, initial="1.00", widget=forms.TextInput(attrs={'class': 'input-mini required'}))
    
    # fields for calculating profit
    target_sell_price = forms.DecimalField(min_value=0, max_digits=32, decimal_places=2, initial="0", required=False)