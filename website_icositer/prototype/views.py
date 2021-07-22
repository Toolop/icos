from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from prototype.models import Prototype
from prototype.forms import PROTOTYPEForm

def create(request):
	akun_form = PROTOTYPEForm(request.POST or None)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('prototype:list')

	context = {
		"page_title":"Registrasi Perlombaan",
		"akun_form":akun_form,
	}

	return render(request,'prototype/form.html',context)

def list(request):
	semua_akun = Prototype.objects.all()

	context = {
		'page_title':'Pendaftaran Perlombaan Prototype',
		'semua_akun':semua_akun,
	}

	return render(request,'prototype/prototype.html',context)

import xlwt

def export_library_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Perpus.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('PerpustakAAn')
 
    # Sheet header, first row
    row_num = 1
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = ['id_library', 'name']
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
 
    rows = PerpustakaanForm.objects.all().values_list('id_library', 'name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
 
    wb.save(response)
    return response