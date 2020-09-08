from rest_framework import routers
from demanda.views import DemandaViewSet


ROUTER = routers.SimpleRouter(trailing_slash=False)
ROUTER.register('demandas',DemandaViewSet)