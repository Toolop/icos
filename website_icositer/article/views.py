from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

from article.models import Article
from article.forms import ARTICLEForm

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def regist(request):
    berhasil = False
    if request.method == "POST":
        form = ARTICLEForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email_peserta = form.cleaned_data.get("email")
            subject = 'Written Idea Registration Confirmation'
            html_message = render_to_string('regisformconfir/confirmation.html', {'pendaftar': form.cleaned_data, 'lomba':'Written Idea'})
            plain_message = strip_tags(html_message)
            from_email = 'confirmation@icositer2021.com'
            to = email_peserta
            send_mail(subject, plain_message, from_email, [to], html_message=html_message)
            return HttpResponseRedirect("/writtenidea/registration?success")     
    else:
        if 'success' in request.GET:
            berhasil=True
    context = {
    'Article':Article,
    'berhasil':berhasil
    }
    return render(request,'article/form.html',context)

import xlwt

def export_article_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="science article.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('ARTICLE')
 
    # Sheet header, first row
    row_num = 1
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = ['Nama Ketua',
    		   'Email',
    		   'No Telepon',
    		   'Instansi',
    		   'Prodi Ketua',
    		   'Nama Anggota 1',
    		   'Prodi Anggota 1',
    		   'Nama Anggota 2',
    		   'Prodi Anggota 2',
    		   'Subtema']
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
 
    rows = Article.objects.all().values_list('nama_ketua',
    										   'email',
    										   'no_telepon',
    										   'instansi',
    										   'prodi_ketua',
    										   'nama_anggota1',
    										   'prodi_anggota1',
    										   'nama_anggota2',
    										   'prodi_anggota2',
    										   'subtema')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
 
    wb.save(response)
    return response