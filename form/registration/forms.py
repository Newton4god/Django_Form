from django import forms
from .models import Student


class RegistrationForm(forms.ModelForm):
    SKILL_CHOICES = [
        ("SEO", "SEO"),
        ("Software development", "Software development"),
        ("Branding", "Branding"),
        ("Digital strategy", "Digital strategy"),
        ("Design engineering", "Design engineering"),
        ("UI/UX", "UI/UX"),
        ("Data analysis", "Data analysis"),
    ]

    skill = forms.ChoiceField(choices=SKILL_CHOICES)

    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email",
            "school_id",
            "skill",
            "phone_number",
        ]

    def clean_skill(self):
        skill = self.cleaned_data["skill"]
        if Student.objects.filter(skill=skill).count() >= 30:
            raise forms.ValidationError(
                f"The maximum number of students for {skill} has been reached."
            )
        return skill


# from django import forms
# from .models import Student


# class RegistrationForm(forms.ModelForm):
#     SKILL_CHOICES = [
#         ("SEO", "SEO"),
#         ("Software development", "Software development"),
#         ("Branding", "Branding"),
#         ("Digital strategy", "Digital strategy"),
#         ("Design engineering", "Design engineering"),
#         ("UI/UX", "UI/UX"),
#         ("Data analysis", "Data analysis"),
#     ]

#     skill = forms.ChoiceField(choices=SKILL_CHOICES)

#     class Meta:
#         model = Student
#         fields = ["first_name", "last_name", "email", "school_id", "skill"]


# # from django import forms
# # from .models import Student


# # class RegistrationForm(forms.ModelForm):
# #     class Meta:
# #         model = Student
# #         fields = ["first_name", "last_name", "email", "school_id", "course_code"]
