from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from myupload.views import Upload
from .forms import TestField

#
# def dataform(request):
#     return render(request,"field.html",{})


@login_required
def data(request):
    # form = TestField(request.POST or None)
    form = TestField
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            a = form.cleaned_data.get("first_interest")
            b = form.cleaned_data.get("first_principal")
            c = form.cleaned_data.get("other_rent")
            d = form.cleaned_data.get("other_tax")
            e = form.cleaned_data.get("other_interest")
            f = form.cleaned_data.get("other_principal")
            g = form.cleaned_data.get("save_acc")
            h = form.cleaned_data.get("fixed_deposit")
            i = form.cleaned_data.get("kvp_ivp")
            j = form.cleaned_data.get("nsc_1")
            k = form.cleaned_data.get("nsc_2")
            l = form.cleaned_data.get("nsc_3")
            m1 = form.cleaned_data.get("fd_1")
            m2 = form.cleaned_data.get("fd_2")
            m3 = form.cleaned_data.get("fd_3")
            n = form.cleaned_data.get("b_d")
            o = form.cleaned_data.get("i_property")
            p = form.cleaned_data.get("ppf")
            q = form.cleaned_data.get("pension")
            r = form.cleaned_data.get("lic")
            s = form.cleaned_data.get("fdr")
            t = form.cleaned_data.get("fees")
            u = form.cleaned_data.get("mf_uti")
            v = form.cleaned_data.get("n_pension")
            w = form.cleaned_data.get("edu_loan")
            x = form.cleaned_data.get("m_parent")
            y = form.cleaned_data.get("m_you")
            z = form.cleaned_data.get("d11")
            aa = form.cleaned_data.get("d12")
            bb = form.cleaned_data.get("d21")
            cc = form.cleaned_data.get("d22")
            dd = form.cleaned_data.get("d31")
            ee = form.cleaned_data.get("d32")
            ff1 = form.cleaned_data.get("d_1")
            ff2 = form.cleaned_data.get("d_2")
            ff3 = form.cleaned_data.get("d_3")

            gg = form.cleaned_data.get("section_1")
            hh = form.cleaned_data.get("section_2")
            ii = form.cleaned_data.get("other_deduct")
            jj = form.cleaned_data.get("interest_due")
            kk = form.cleaned_data.get("p_repayment")

            ll = form.cleaned_data.get("ifsc")
            mm = form.cleaned_data.get("acc")

            tt = form.cleaned_data.get("time")

            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, 'vamagithub@gmail.com']

            contact_message = "1.\t HOUSE PROPERTY\n" \
                              "1.1 .\t FIRST HOUSE\n" \
                              "\t1.1\t Interest:\t %s \n" \
                              "\t1.2\t Principal:\t %s \n" \
                              "1.2.\t OTHER HOUSE\n" \
                              "\t1.2.1.\t Rent Received:\t %s \n" \
                              "\t1.2.2.\t Municipal Tax:\t %s \n" \
                              "\t1.2.3.\t Interest:\t %s \n" \
                              "\t1.2.4.\t Principal:\t %s \n" \
                              "2.\t OTHER INCOME\n" \
                              "\t2.1\t Interest earned on Saving Bank Account:\t %s \n" \
                              "\t2.2\t Interest on Fixed Deposit:\t %s \n" \
                              "\t2.3\t Interest earned on KVP OR IVP:\t %s \n" \
                              "\t2.4.1\t Interest on NSC:\t %s -AMOUNT\t %s \n" \
                              "\t2.4.2\t Interest on NSC:\t %s -AMOUNT\t %s \n" \
                              "\t2.4.3\t Interest on NSC:\t %s -AMOUNT\t %s \n" \
                              "\t2.5\t Interest earned on Bonds & Debentures:\t %s \n" \
                              "\t2.6\t Purchase of Immovable Property:\t %s \n" \
                              "\t2.7\t Interest earned on PPF:\t %s \n" \
                              "\t2.8\t Pension Received:\t %s \n" \
                              "\t2.9\t Interest Due:\t %s \n" \
                              "\t2.10\t Principal Repayment:\t %s \n" \
                              "3.\t DEDUCTIONS\n" \
                              "\t3.1\t LIC Premium:\t %s \n" \
                              "\t3.2\t Tax Savor FDR:\t %s \n" \
                              "\t3.3\t Tuition Fees:\t %s \n" \
                              "\t3.4\t Investment in notified MF/UT:\t %s \n" \
                              "\t3.5\t Investment in National Pension Scheme:\t %s \n" \
                              "\t3.6\t Interest component of Education Loan:\t %s \n" \
                              "\t3.7\t Medical Insurance - OF PARENTS:\t %s \n" \
                              "\t3.8\t Medical Insurance - OF YOURSELF & INDEPENDENT:\t %s \n" \
                              "4.\t DONATIONS GIVEN\n" \
                              "\t4.1\t %s(DROPDOWN1):AMOUNT:\t%s \t AMOUNT:\t%s\n" \
                              "\t4.2\t %s(DROPDOWN2):AMOUNT:\t%s \t AMOUNT:\t%s\n" \
                              "\t4.3\t %s(DROPDOWN3):AMOUNT:\t%s \t AMOUNT:\t%s\n" \
                              "5.\t ROYALITY RECEIVED \n" \
                              "\t5.1\t Section 80 QQB(AMOUNT): \t %s \n" \
                              "\t5.2\t Section 80 QQB(AMOUNT): \t %s \n" \
                              "6.\t ANY OTHER DEDUCTIONS \n" \
                              "\t6.1\t Other Deductions: \t %s \n" \
                              "7.\t BANK DETAILS \n" \
                              "\t7.1\t IFSC Code: \t %s \n" \
                              "\t7.2\t Account Number: \t %s \n" \
                              "8.\t BEST TIME TO CALL ME \n" \
                              "\t8.1\t I will be free at around %s.\n" \
                              % (a, b, c, d, e, f, g, h, i, m1, j, m2, k, m3, l, n, o, p, q, jj, kk, r, s, t,
                                 u, v, w, x, y, ff1, z, aa, ff2, bb, cc, ff3, dd, ee,
                                 gg, hh, ii, ll, mm, tt)

            send_mail('Fields Data from a customer',
                      contact_message,
                      from_email,
                      to_email,
                      fail_silently=False)  # SEE THIS MAKE IT TRUE IT DOESNOT WORK
            # return HttpResponseRedirect('thanks')
            # return render(request, "field.html", {"form": form, })
            return render(request, "pay.html", {"form": form, })

    else:
        form = TestField()

    return render(request, "field.html", {"form": form, })
