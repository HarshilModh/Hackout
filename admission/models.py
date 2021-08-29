from django.db import models
from django.db import connections
# Create your models here.
class collegedetails(models.Model):
    College_Name = models.CharField(max_length=150)
    Course_name = models.CharField(max_length=150)
    total_seat = models.CharField(max_length=150)
    Category = models.CharField(max_length=150)
    Opening = models.CharField(max_length=150)
    Closing = models.CharField(max_length=150)
    Fees_Anual = models.CharField(max_length=150)
    Hostel = models.CharField(max_length=150)
    Transportation = models.CharField(max_length=150)
    class Meta:
        db_table = "collegedata"
