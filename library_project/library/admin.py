from django.contrib import admin
from library.models import *

# Register your models here.
@admin.register(AddBook)
class AddBook(admin.ModelAdmin):
    list_display=['book_name','book_edition','book_writer']
    


@admin.register(AddStudent)
class AddBook(admin.ModelAdmin):
    list_display=['name','faculty','gender']



@admin.register(WithdrawBook)
class AddBook(admin.ModelAdmin):
    list_display=['student_name','book_name','faculty','gender','date','is_returned','teacher_or_student']




