from rest_framework import serializers
from testapp.models import Employee

#! validators 3rd method
def multiples_of_100(value):
    if value %1000 !=0:
        raise serializers.ValidationError('salary should be multiples of 1000')
 

# class EmployeeSerializer(serializers.Serializer):
#     ename=serializers.CharField(max_length=30)
#     enum=serializers.IntegerField()
#     esal=serializers.IntegerField(validators=[multiples_of_100])
#     eadres=serializers.CharField(max_length=30)
#     #! validations ---session 13 
#     def validate_esal(self,value):
#         if value < 5000:
#             raise serializers.ValidationError('employee salary should be >5000') 
#         return value
    
#     #object level 
#     def validate(self, data):
#         ename=data.get('ename')
#         esal=data.get('esal')
#         if ename.lower() == 'bhargav':
#             if esal <50000:
#                 raise serializers.ValidationError('bhargav salary should be >=50000')
#         return data
#     def create(self,validated_data):
#         return Employee.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.ename=validated_data.get('ename',instance.ename)
#         instance.enum=validated_data.get('enum',instance.enum)
#         instance.esal=validated_data.get('esal',instance.esal)
#         instance.eadres=validated_data.get('eadres',instance.eadres)
#         instance.save()
#         return instance
    
#----------------#!MODEL SERIALIZERS----------------------------------------------------------------#

class EmployeeSerializer(serializers.ModelSerializer):
    esal=serializers.IntegerField(validators=[multiples_of_100])
    
    class Meta:
        model = Employee
        fields='__all__'
        #fields=['ename','enum','eadres']
        #exclude=['esal'] if 999 fields dont include salary
    #by defining model serializer we perform all 4 operations  without writing extra code
    