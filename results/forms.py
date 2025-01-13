from django import forms
class_choices = [
    ('', 'Select Class'),
    ('math', 'math'),
    ('english', 'english'),
    ('comouter', 'comouter'),
]
class resultform(forms.Form):
    roll_no = forms.IntegerField(label="ROLL NO", widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Roll No'}))
    student_class = forms.ChoiceField(label='class', choices=class_choices, required=True, widget=forms.Select(attrs={'class':'form-control'}))