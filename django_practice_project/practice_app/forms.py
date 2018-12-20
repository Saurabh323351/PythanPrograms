from django import forms
from practice_app.models import Student


class StudentForm(forms.ModelForm):
    st_name = forms.CharField(widget=forms.TextInput(), required=True, max_length=25)
    st_rollno = forms.IntegerField(widget=forms.NumberInput, required=True)
    st_address = forms.CharField(widget=forms.Textarea, required=True, max_length=100)
    st_qualification = forms.CharField(max_length=10)

    class Meta:
        model = Student
        fields = ['st_name', 'st_rollno', 'st_address', 'st_qualification']


