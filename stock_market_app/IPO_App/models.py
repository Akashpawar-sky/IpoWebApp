from django.db import models

class IPO(models.Model):
    company_logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    company_name = models.CharField(max_length=100)
    price_band = models.DecimalField(max_digits=10, decimal_places=2)
    open_date = models.DateField()
    close_date = models.DateField()
    issue_size = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=50)
    listing_date = models.DateField()
    status = models.CharField(max_length=50)
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_gain = models.DecimalField(max_digits=10, decimal_places=2)
    cmp = models.DecimalField(max_digits=10, decimal_places=2)
    current_return = models.DecimalField(max_digits=10, decimal_places=2)
    rhp_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    drhp_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.company_name
