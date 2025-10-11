from django.db import models
from accounts.models import User


class Wait(models.Model):
    WAIT_STATUS = (
        ('در حال انتظار', 'در حال انتظار'),
        ('اتمام شد', 'اتمام شد'),
        ('لغو', 'لفو')
    )

    FACILITY_STATUS = (
        ('ساده', 'ساده'),
        ('با پریز', 'با پریز'),
    )
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(choices=WAIT_STATUS, max_length=20, default=WAIT_STATUS[0][0])
    facility = models.CharField(choices=FACILITY_STATUS, max_length=20, default=FACILITY_STATUS[0][0])

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
