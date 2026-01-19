from rest_framework import serializers
from .models import Hospital, Bed, BloodBank, BloodUnit

class HospitalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hospital
		fields = "__all__"

class BedSerializer(serializers.ModelSerializer):
	hospital_name = serializers.CharField(
		source="hospital.name",
		read_only=True
	)

	class Meta:
		model = Bed
		fields = "__all__"

class BloodBankSerializer(serializers.ModelSerializer):
	class Meta:
		model = BloodBank
		fields = "__all__"

class BloodUnitSerializer(serializers.ModelSerializer):
	class Meta:
		model = BloodUnit
		fields = "__all__"
