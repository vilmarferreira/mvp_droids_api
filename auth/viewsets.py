from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from auth.serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken



# class RegisterView(APIView):
#     """View para registro"""
#     serializer_class = RegisterSerializer
#     authentication_classes = None
#
#     @transaction.atomic
#     def post(self, request, *args, **kwargs):
#         """
#         Args:
#             request:
#             *args:
#             **kwargs:
#         """
#         sid = transaction.savepoint()
#         serializer = self.get_serializer(data=request.data)
#
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             data = {
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                 }
#             response = Response(data,status.HTTP_201_CREATED)
#             transaction.savepoint_commit(sid)
#             return response
#         transaction.savepoint_rollback(sid)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RegisterView(TokenObtainPairView):
    # """View para registro"""
    # serializer_class = RegisterSerializer
    # authentication_classes = None

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        """
        Args:
            request:
            *args:
            **kwargs:
        """
        sid = transaction.savepoint()
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return super().post(request, *args, **kwargs)
        transaction.savepoint_rollback(sid)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)