from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    username=forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    name=forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email=forms.EmailField(label='',required=True, widget=forms.TextInput(attrs={'placeholder':'Email'}))
    phoneNumber=forms.IntegerField(max_value=9999999999,min_value=999999999,label='',required=True, widget=forms.TextInput(attrs={'placeholder':'Phone Number'}))

    age=forms.IntegerField(label='',required=True, widget=forms.TextInput(attrs={'placeholder':'Age'}))
    department=forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'placeholder':'Department'}))
    role=forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'placeholder':'Role'}))
    salary=forms.FloatField(label='',required=True, widget=forms.TextInput(attrs={'placeholder':'Salary'}))
    leaves=forms.IntegerField(label='',required=True, widget=forms.TextInput(attrs={'placeholder':'Leave'}))
    joinDate=forms.DateField(label='',required=True, widget=forms.TextInput(attrs={'placeholder':'Join Date'}))
    status=forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'placeholder':'Status'}))

    class Meta:
        model = Employee
        fields=[
            'username',
            'name',
            'email',
            'phoneNumber',
            'age',
            'department',
            'role',
            'salary',
            'leaves',
            'joinDate',
            'status',
        ]
