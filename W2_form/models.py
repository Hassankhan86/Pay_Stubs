from django.db import models

# Create your models here.


class Employee1(models.Model):
    year_choice = (
        ('2010', '2010'),('2011', '2011'),('2012', '2012'),('2013', '2013'),('2014', '2014'),('2015', '2015'),
        ('2016', '2016'),('2017', '2017'),('2018', '2018'),('2019', '2019'),('2020', '2020'),('2021', '2021'),
    )
    tax_year = models.CharField(max_length=100, choices=year_choice)


    def __str__(self):
        return self.tax_year







