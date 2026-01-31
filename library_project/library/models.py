from django.db import models

# Create your models here.
class AddBook(models.Model):
    book_name=models.CharField(max_length=200)
    book_edition=models.CharField(max_length=100)
    book_writer=models.CharField(max_length=500)

    def __str__(self):
        return self.book_name
    

class AddStudent(models.Model):
    name=models.CharField(max_length=200)
    faculty=models.CharField(max_length=100)
    gender=models.CharField(max_length=1)

    def __str__(self):
        return self.name
    

class WithdrawBook(models.Model):
    student_name=models.CharField(max_length=200)
    book_name=models.CharField(max_length=200)
    faculty=models.CharField(max_length=100)
    gender=models.CharField(max_length=1)
    date=models.CharField()
    is_returned=models.BooleanField(default=False)
    teacher_or_student=models.TextField()
    def __str__(self):
        return self.student_name
    


        