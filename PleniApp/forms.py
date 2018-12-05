from django import forms

class UserSignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CreateLectureForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    unit_index = forms.CharField()
    lecture_type_index =  forms.CharField()
    lecture_index_number = forms.CharField()
