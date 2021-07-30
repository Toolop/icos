from django import forms

from article.models import Article

class ARTICLEForm(forms.ModelForm):
	class Meta:
		model = Article
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