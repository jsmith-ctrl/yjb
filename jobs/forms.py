from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job

        fields = [
            'title',
            'company',
            'description',
            'commitment',
            'location',
            'salary',
            'experience',
            'requirements',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Junior Software Developer',
            }),

            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company name',
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Describe the position...',
            }),

            'commitment': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Full-time, Part-time, Contract',
            }),

            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. North Battleford, SK',
            }),

            'salary': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. $50,000 - $65,000 per year',
            }),

            'experience': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 2+ years',
            }),

            'requirements': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'List the requirements for this position...',
            }),
        }