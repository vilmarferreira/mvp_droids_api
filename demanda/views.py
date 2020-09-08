from rest_framework.viewsets import ModelViewSet

from contato.serializers import ContatoSerializer
from demanda.models import Demanda
from demanda.serializers import DemandaSerializer, DemandaSerializer
from endereco.serializers import EnderecoSerializer
from utils.decorators import assign_request_user

class DemandaViewSet(ModelViewSet):
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer

    def get_queryset(self):
        return self.request.user.demandas_anunciantes.all()

    @assign_request_user(user_field="anunciante")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update_contato(self,data):
        object = self.get_object()
        instance = object.contato
        serializer = ContatoSerializer(instance,data,partial=True)
        serializer.is_valid()
        serializer.save()
    def update_endereco(self,data):
        object = self.get_object()
        instance = object.endereco
        serializer = EnderecoSerializer(instance,data,partial=True)
        serializer.is_valid()
        serializer.save()
    @assign_request_user(user_field="anunciante")
    def update(self, request, *args, **kwargs):
        newcontato = request.data.pop('contato',None)
        newendereco = request.data.pop('endereco',None)
        if newcontato:
            self.update_contato(newcontato)
        if newendereco:
            self.update_endereco(newendereco)
        return super().update(request, *args, **kwargs)

