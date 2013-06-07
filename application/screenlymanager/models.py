from django.db import models
from django.core.urlresolvers import reverse
import datetime
import os


class Client(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    last_ip = models.IPAddressField(blank=True)
    port = models.PositiveIntegerField(default='8080')
    last_active = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(max_length=1024, blank=True, null=True)

    def __unicode__(self):
        return u"%s [%s:%s]" % (self.name, self.last_ip, self.port)

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk': self.pk})

    def screenshot_url(self):
        if self.last_ip and self.port:
            url = 'http://%s:%s/static/img/screenshot.png' % (self.last_ip, self.port)
            return url
        return None

    def is_online(self):
        response = os.system("ping -c 1 " + self.last_ip)
        if response == 0:
            self.last_active = datetime.datetime.now()
            self.save()
            return True
        return False
