# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    awda = models.TextField(max_length=255, null=True, blank=True)
    awdawd = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Test(models.Model):

    #__Test_FIELDS__
    abc = models.TextField(max_length=255, null=True, blank=True)

    #__Test_FIELDS__END

    class Meta:
        verbose_name        = _("Test")
        verbose_name_plural = _("Test")


class Ddd(models.Model):

    #__Ddd_FIELDS__
    awdawd = models.TextField(max_length=255, null=True, blank=True)
    awdaw = models.BooleanField()
    awd = models.CharField(max_length=255, null=True, blank=True)

    #__Ddd_FIELDS__END

    class Meta:
        verbose_name        = _("Ddd")
        verbose_name_plural = _("Ddd")



#__MODELS__END
