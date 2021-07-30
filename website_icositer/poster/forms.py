from django import forms

from poster.models import Poster

class POSTERForm(forms.ModelForm):
	class Meta:
		model = Poster
		fields = [
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