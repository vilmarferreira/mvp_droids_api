from rest_framework import serializers

from contato.models import Contato
from contato.serializers import ContatoSerializer
from demanda.models import Demanda
from endereco.models import Endereco
from endereco.serializers import EnderecoSerializer


class DemandaSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    contato = ContatoSerializer()
    status = serializers.CharField(source='get_status_display',read_only=True)
    class Meta:
        model = Demanda
        fields = '__all__'
    def create(self, validated_data):
        try:
            endereco = Endereco.objects.create(**validated_data.pop('endereco'))
            contato = Contato.objects.create(**validated_data.pop('contato'))
            validated_data['endereco'] = endereco
            validated_data['contato'] = contato
        except Exception as e:
            raise ValueError(str(e))
        return super(DemandaSerializer, self).create(validated_data)

    # def update_contato(self,instance,data):
    #     serializer = ContatoSerializer(instance,data,partial=True)
    #     serializer.is_valid(raise_exception=False)
    #     serializer.save()
    # def update_endereco(self,instance,data):
    #     serializer = EnderecoSerializer(instance,data,partial=True)
    #     serializer.is_valid(raise_exception=False)
    #     serializer.save()
    def update(self, instance, validated_data):
        validated_data.pop('contato',None)
        validated_data.pop('endereco',None)
        return super(DemandaSerializer, self).update(instance, validated_data)