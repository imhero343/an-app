from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin
from django.contrib import admin
from .models import Person
from import_export import resources


# @admin.register(Person)
# class RecordsAdmin(ImportExportModelAdmin):

#     def get_export_headers(self):
#         headers = super().get_export_headers()
#         for i, h in enumerate(headers):
#             if h == 'id':
#                 headers[i] = "lastname"
#             if h == 'First Name':
#                 headers[i] = "firstname"
#         return headers
class BookResource(resources.ModelResource):

    def get_export_headers(self):
        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            if h == 'id':
                headers[i] = "التسلسل"
            if h == 'name':
                headers[i] = "الاسم"
            if h == 'direction':
                headers[i] = "التوجه"
            if h == 'represent':
                headers[i] = "الموقعية"
            if h == 'gov':
                headers[i] = "المحافظة"
            if h == 'area':
                headers[i] = "المنطقة"
            if h == 'phone':
                headers[i] = "رقم الهاتف"
            if h == 'nkown_person':
                headers[i] = "الشخص المعروف"
            if h == 'nkown_person_phone':
                headers[i] = "رقم الشخص المعروف"
            if h == 'nkown_person_relation':
                headers[i] = "مقدار علاقة الشخص بالمعرف"
            if h == 'notes':
                headers[i] = "الملاحظات"
            if h == 'age':
                headers[i] = "العمر"
        return headers

    class Meta:
        model = Person


class BookAdmin(ImportExportModelAdmin):
    resource_classes = [BookResource]


admin.site.register(Person, BookAdmin)
# class BookResource(resources.ModelResource):

#     class Meta:
#         model = Person
#         fields = ('id', 'name', 'price',)
