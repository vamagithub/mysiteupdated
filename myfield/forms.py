from django import forms


class TestField(forms.Form):
    NSC = (
        ('Financial Year 2015-16', 'Financial Year 2015-16'),
        ('Financial Year 2014-15', 'Financial Year 2014-15'),
        ('Financial Year 2013-14', 'Financial Year 2013-14'),
        ('Financial Year 2012-13', 'Financial Year 2012-13'),
        ('Financial Year 2011-12', 'Financial Year 2011-12'),

    )

    DONATIONS = (
        ('Item1', 'Item1'),
        ('Item2', 'Item2'),
        ('Item3', 'Item3'),
        ('Item4', 'Item4'),
        ('Item5', 'Item5'),
        ('Item6', 'Item6'),
        ('Item7', 'Item7'),
        ('Item8', 'Item8'),
        ('Item9', 'Item9'),
        ('Item10', 'Item10'),
        ('Item11', 'Item11'),
        ('Item12', 'Item12'),
        ('Item13', 'Item13'),
        ('Item14', 'Item14'),
        ('Item15', 'Item15'),

    )

    TIME = (
        ('8 am - 9 am', '8 am - 9 am'),
        ('9 am - 10 am', '9 am - 10 am'),
        ('10 am - 11 am', '10 am - 11 am'),
        ('11 am - 12 pm', '11 am - 12 pm'),
        ('12 pm - 1 pm', '12 pm - 1 pm'),
        ('1 pm - 2 pm', '1 pm - 2 pm'),
        ('2 pm - 3 pm', '2 pm - 3 pm'),
        ('3 pm - 4 pm', '3 pm - 4 pm'),
        ('4 pm - 5 pm', '4 pm - 5 pm'),
        ('5 pm - 6 pm', '5 pm - 6 pm'),
        ('7 pm - 8 pm', '7 pm - 8 pm'),
        ('8 pm - 9 pm', '8 pm - 9 pm'),
        ('9 pm - 10 pm', '9 pm - 10 pm'),


    )

    # detail = forms.CharField(max_length=100)
    first_interest = forms.CharField(max_length=100)
    first_principal = forms.CharField(max_length=100)

    other_rent = forms.CharField(max_length=100)
    other_tax = forms.CharField(max_length=100)
    other_interest = forms.CharField(max_length=100)
    other_principal = forms.CharField(max_length=100)

    interest_due = forms.CharField(max_length=100)
    p_repayment = forms.CharField(max_length=100)

    save_acc = forms.CharField(max_length=100)
    fixed_deposit = forms.CharField(max_length=100)
    kvp_ivp = forms.CharField(max_length=100)
    nsc_1 = forms.CharField(max_length=100)
    nsc_2 = forms.CharField(max_length=100)
    nsc_3 = forms.CharField(max_length=100)
    b_d = forms.CharField(max_length=100)
    i_property = forms.CharField(max_length=100)
    ppf = forms.CharField(max_length=100)
    pension = forms.CharField(max_length=100)
    lic = forms.CharField(max_length=100)
    fdr = forms.CharField(max_length=100)
    fees = forms.CharField(max_length=100)
    mf_uti = forms.CharField(max_length=100)
    n_pension = forms.CharField(max_length=100)
    edu_loan = forms.CharField(max_length=100)

    m_parent = forms.CharField(max_length=100)
    m_you = forms.CharField(max_length=100)

    d11 = forms.CharField(max_length=100)
    d12 = forms.CharField(max_length=100)
    d21 = forms.CharField(max_length=100)
    d22 = forms.CharField(max_length=100)
    d31 = forms.CharField(max_length=100)
    d32 = forms.CharField(max_length=100)

    section_1 = forms.CharField(max_length=100)
    section_2 = forms.CharField(max_length=100)

    other_deduct = forms.CharField(widget=forms.Textarea)

    fd_1 = forms.ChoiceField(choices=NSC)
    fd_2 = forms.ChoiceField(choices=NSC)
    fd_3 = forms.ChoiceField(choices=NSC)

    d_1 = forms.ChoiceField(choices=DONATIONS)
    d_2 = forms.ChoiceField(choices=DONATIONS)
    d_3 = forms.ChoiceField(choices=DONATIONS)

    acc = forms.CharField(max_length=100)
    ifsc = forms.CharField(max_length=100)

    time = forms.ChoiceField(choices=TIME)

