from django import forms

from .models import Webinar

class WEBINARForm(forms.ModelForm):
	class Meta:
		model = Webinar
		fields =[
			'email',
			'nama',
			'jurusan',
			'nim',
			'instansi',
			'negara_kota',
			'lomba',
			'alasan',
			'no_wa'
		]