from django import forms


class UploadForms(forms.Form):

    YEAR = (
        ('Financial Year 2015-16', 'Financial Year 2015-16'),
        ('Financial Year 2014-15', 'Financial Year 2014-15'),
        ('Financial Year 2013-14', 'Financial Year 2013-14'),
        ('Financial Year 2012-13', 'Financial Year 2012-13'),
        ('Financial Year 2011-12', 'Financial Year 2011-12'),

    )

    yr = forms.ChoiceField(choices=YEAR)
