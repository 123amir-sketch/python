from django.db import models

# Create your models here.
class ResultFile(models.Model):
    file = models.FileField(upload_to='result_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Result(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    marks = models.FloatField()
    uploaded_file = models.ForeignKey(ResultFile, on_delete=models.CASCADE)