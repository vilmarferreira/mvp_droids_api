from rest_framework.serializers import ModelSerializer
from endereco.models import Endereco, Estado


class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado 
        fields = '__all__'
class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
    def to_representation(self, instance):
        self.fields['estado'] = EstadoSerializer(read_only=True)
        return super(EnderecoSerializer, self).to_representation(instance)