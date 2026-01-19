from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Hospital(models.Model):
	name = models.CharField(max_length=200)
	address = models.TextField()
	city = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Bed(models.Model):
	hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='beds')
	bed_type = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	is_available = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.bed_type} - {self.hospital.name}"

class BloodBank(models.Model):
	name = models.CharField(max_length=255)
	address = models.TextField()
	city = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=15)

	def __str__(self):
		return self.name

class BloodUnit(models.Model):
	BLOOD_GROUP_CHOICES = [
		("A+","A+"),
		("A-","A-"),
		("B+","B+"),
		("B-","B-"),
		("O+","O+"),
		("O-","O-"),
		("AB+","AB+"),
		("AB-","AB-"),
	]

	blood_bank = models.ForeignKey(
		BloodBank,
		on_delete=models.CASCADE,
		related_name="blood_units"
	)
	blood_group = models.CharField(
		max_length=3,
		choices=BLOOD_GROUP_CHOICES,
		default="O+"
	)
	units_available = models.PositiveIntegerField(default=0)
	price_per_unit = models.DecimalField(
		max_digits=10,
		decimal_places=2,
		null=True,
		blank=True
	)
	is_available = models.BooleanField(default=True)
	last_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.blood_group} - {self.blood_bank.name}"

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('hospital', 'Hospital'),
        ('bloodbank', 'Blood Bank'),
        ('user', 'User'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
