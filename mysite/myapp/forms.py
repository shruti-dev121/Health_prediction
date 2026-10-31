from django import forms
from .models import Details
from datetime import date

class Detailform(forms.ModelForm):

    class Meta:
        model = Details

        fields = [
            "full_name",
            "date_of_birth",
            "email_address",
            "glucose",
            "haemoglobin",
            "cholesterol"
        ]

        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={"type": "date"}
            )

        }
        def clean_date_of_birth(self):
            dob = self.cleaned_data["date_of_birth"]
            if dob > date.today():
                raise forms.ValidationError("date cant be in future")
            return dob
        def clean_glucose(self):
            value = self.cleaned_data['glucose']
            if value <= 0:
               raise forms.ValidationError("Glucose must be positive")

            return value  
        def clean_haemoglobin(self):
            value = self.cleaned_data['haemoglobin']

            if value <= 0:
               raise forms.ValidationError("Haemoglobin must be positive")

            return value
        def clean_cholesterol(self):
            value = self.cleaned_data['cholesterol']

            if value <= 0:
              raise forms.ValidationError("Cholesterol must be positive")

            return value