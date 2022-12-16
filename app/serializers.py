from rest_framework import serializers
from .models import Apicrud


# class serializers_Apicrud(serializers.ModelSerializer):
#     class Meta:
#         model = Apicrud
#         # fields = ['id','first', 'second','third']
#         fields = '__all__'
        
class serializers_Apicrud(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apicrud
        # fields = ['id','url','first', 'second','third','fourth','fifth','sixth','seventh','eight','nine']
        fields = '__all__'