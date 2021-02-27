from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class contact(models.Model):
    name = models.CharField(_("Your Name"), max_length=150, blank=False,null=False)
    email = models.EmailField(_("Email Address"), max_length=254, blank=False,null=False)
    subject = models.CharField(_("subject"), max_length=150, blank=False,null=False)
    models =  models.TextField(_("Message"), blank=False,null=False)

    def __str__(self):
        return self.name
    

class location(models.Model):
    title = models.CharField(_("Name of Location"), max_length=150, blank=False,null=False)
    image = models.ImageField(_("Image"), upload_to="media/location", height_field=None, width_field=None, max_length=25600)
    subject = models.CharField(_("subject"), max_length=150, blank=False,null=False)
    short_describe =  models.CharField(_("Short describe"), max_length=150, blank=False,null=False)
    describtion = models.TextField(_("Details of place"))
    offer = models.BooleanField(_("Offer"),default=False)
    def __str__(self):
        return self.title
    

class Subcriber(models.Model):
    name = models.CharField(_("Fullname"), max_length=150)
    email_id = models.EmailField(_("Email ID"), max_length=254)

    def __str__(self):
        return self.name


class Setting(models.Model):
    company_name = models.CharField(_("Company name"), max_length=150)
    copyright = models.CharField(_("Copyright"), max_length=150)
    company_email = models.EmailField(_("Company register Email Address"), max_length=254)
    mobile_number = PhoneNumberField(_("Phone number"))
    office_address = models.CharField(_("Office Address"), max_length=250)

    def __str__(self):
        return self.company_name
    