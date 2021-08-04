from django.db import models


# Create your models here.
class Once(models.Model):
    federal_tax = models.TextField(max_length=100, default='620')
    state_tax = models.TextField(max_length=100)
    sdi = models.TextField(max_length=100)
    work_comp = models.TextField(max_length=100)
    tdi = models.TextField(max_length=100)
    social_security = models.TextField(max_length=100, default='620')
    medicare = models.TextField(max_length=100, default='145')

    def __str__(self):
        return self.federal_tax + '....once'

class Daily(models.Model):
    federal_tax = models.TextField(max_length=100, default='1.72')
    state_tax = models.TextField(max_length=100)
    sdi = models.TextField(max_length=100)
    work_comp = models.TextField(max_length=100)
    tdi = models.TextField(max_length=100)
    social_security = models.TextField(max_length=100, default='1.72')
    medicare = models.TextField(max_length=100, default='0.40')

    def __str__(self):
        return self.federal_tax + '....Daily'

class Weekly(models.Model):
    federal_tax = models.TextField(max_length=100, default='11.92')
    state_tax = models.TextField(max_length=100)
    sdi = models.TextField(max_length=100)
    work_comp = models.TextField(max_length=100)
    tdi = models.TextField(max_length=100)
    social_security = models.TextField(max_length=100, default='11.92')
    medicare = models.TextField(max_length=100, default='2.79')

    def __str__(self):
        return self.federal_tax + '....Weekly'

class Bi_Weekly(models.Model):
    federal_tax = models.TextField(max_length=100, default='23.85')
    state_tax = models.TextField(max_length=100)
    sdi = models.TextField(max_length=100)
    work_comp = models.TextField(max_length=100)
    tdi = models.TextField(max_length=100)
    social_security = models.TextField(max_length=100, default='23.85')
    medicare = models.TextField(max_length=100, default='5.58')

    def __str__(self):
        return self.federal_tax + '....BI_Weekly'


class Semi_monthly(models.Model):
    federal_tax = models.TextField(max_length=100, default='25.83')
    state_tax = models.TextField(max_length=100)
    sdi = models.TextField(max_length=100)
    work_comp = models.TextField(max_length=100)
    tdi = models.TextField(max_length=100)
    social_security = models.TextField(max_length=100, default='25.83')
    medicare = models.TextField(max_length=100, default='6.04')

    def __str__(self):
        return self.federal_tax + '....Semi_Monthly'

class Monthly(models.Model):
    federal_tax = models.TextField(max_length=100, default='51.67')
    state_tax = models.TextField(max_length=100)
    sdi = models.TextField(max_length=100)
    work_comp = models.TextField(max_length=100)
    tdi = models.TextField(max_length=100)
    social_security = models.TextField(max_length=100, default='51.67')
    medicare = models.TextField(max_length=100, default='12.08')

    def __str__(self):
        return self.federal_tax + '....Monthly'


class Quartely(models.Model):
    federal_tax = models.TextField(max_length=100, default='155')
    state_tax = models.TextField(max_length=100)
    sdi = models.TextField(max_length=100)
    work_comp = models.TextField(max_length=100)
    tdi = models.TextField(max_length=100)
    social_security = models.TextField(max_length=100, default='155')
    medicare = models.TextField(max_length=100, default='36.25')

    def __str__(self):
        return self.federal_tax + '....Quartely'


class Semi_annually(models.Model):
    federal_tax = models.TextField(max_length=100, default='310')
    state_tax = models.TextField(max_length=100)
    sdi = models.TextField(max_length=100)
    work_comp = models.TextField(max_length=100)
    tdi = models.TextField(max_length=100)
    social_security = models.TextField(max_length=100, default='310')
    medicare = models.TextField(max_length=100, default='72.50')

    def __str__(self):
        return self.federal_tax + '....Semi-Annually'


class Annually(models.Model):
    federal_tax = models.TextField(max_length=100, default='620')
    state_tax = models.TextField(max_length=100)
    sdi = models.TextField(max_length=100)
    work_comp = models.TextField(max_length=100)
    tdi = models.TextField(max_length=100)
    social_security = models.TextField(max_length=100, default='620')
    medicare = models.TextField(max_length=100, default='145')

    def __str__(self):
        return self.federal_tax + '....Annually'

class image_upld(models.Model):
    logo = models.ImageField(blank=True)



class State(models.Model):
    state_name = models.TextField(max_length=100)
    once_tax = models.ForeignKey(Once, on_delete=models.CASCADE, default=None)
    daily_tax = models.ForeignKey(Daily, on_delete=models.CASCADE, default=None)
    weekly_tax = models.ForeignKey(Weekly, on_delete=models.CASCADE, default=None)
    Bi_Weekly_tax = models.ForeignKey(Bi_Weekly, on_delete=models.CASCADE, default=None)
    Semi_monthly_tax = models.ForeignKey(Semi_monthly, on_delete=models.CASCADE, default=None)
    monthly_tax = models.ForeignKey(Monthly, on_delete=models.CASCADE, default=None)
    quartely_tax = models.ForeignKey(Quartely, on_delete=models.CASCADE, default=None)
    semi_annually_tax = models.ForeignKey(Semi_annually, on_delete=models.CASCADE, default=None)
    annually = models.ForeignKey(Annually, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.state_name + "...."
