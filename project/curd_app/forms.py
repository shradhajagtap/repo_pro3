from django import forms
from .models import OnlineFood


class OnlineFoodForm(forms.ModelForm):
    class Meta:
        model = OnlineFood
        fields = "__all__"

        widgets = {
            "customer_first_name": forms.TextInput(attrs={"class": "form-control"}),
            "customer_last_name": forms.TextInput(attrs={"class": "form-control"}),
            "customer_address": forms.TextInput(attrs={"class": "form-control", "rows": 5, "col": 5}),
            "customer_mobile_no": forms.NumberInput(attrs={"class": "form-control"}),
            "food_mode": forms.Select(attrs={"class": "form-control"}),
        }
