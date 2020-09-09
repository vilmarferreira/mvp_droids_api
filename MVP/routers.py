from rest_framework import routers
from demanda.views import DemandaViewSet
from endereco.views import EstadoViewSet

ROUTER = routers.SimpleRouter(trailing_slash=False)
ROUTER.register('demandas',DemandaViewSet)
ROUTER.register('estados',EstadoViewSet)