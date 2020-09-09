from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from contato.serializers import ContatoSerializer
from demanda.models import Demanda
from demanda.serializers import DemandaSerializer, DemandaSerializer
from endereco.serializers import EnderecoSerializer
from utils.decorators import assign_request_user
from rest_framework.exceptions import ValidationError

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
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationError(serializer.errors)
    def update_endereco(self,data):
        object = self.get_object()
        instance = object.endereco
        serializer = EnderecoSerializer(instance,data,partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationError(serializer.errors)

    @assign_request_user(user_field="anunciante")
    def update(self, request, *args, **kwargs):
        newcontato = request.data.get('contato',None)
        newendereco = request.data.get('endereco',None)
        if newcontato:
            self.update_contato(newcontato)
        if newendereco:
            self.update_endereco(newendereco)
        return super().update(request, *args, **kwargs)

    @action(methods=["put"], detail=True, url_path="finalizar")
    def finalizar_demanda(self, *_args, **_kwargs):
        instance = self.get_object()
        try:
            instance.finalizar()
            return Response(
                self.get_serializer(instance=instance).data, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(e,status=status.HTTP_400_BAD_REQUEST)