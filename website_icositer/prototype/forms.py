from django import forms

from prototype.models import Prototype

class PROTOTYPEForm(forms.ModelForm):
	class Meta:
		model = Prototype
		fields =[
			'nama_ketua',
			'email',
			'no_telepon',
			'instansi',
			'prodi_ketua',
			'nama_anggota1',
			'prodi_anggota1',
			'nama_anggota2',
			'prodi_anggota2',
			'subtema',
			'file_pdf',
		]