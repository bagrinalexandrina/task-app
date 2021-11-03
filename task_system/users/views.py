
from users.models import User
from drf_util.decorators import serialize_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.serializers import UserListSerializer, UserSerializer



class RegisterUserView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
    

    def get(self, request):
        user = User.objects.all()

        return Response(UserListSerializer(user, many=True).data)

    @serialize_decorator(UserSerializer)
    def post(self,request):
        validated_data=request.serializer.validated_data

        user = User.objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            username = validated_data['username'],
            is_superuser = True,
            is_staff = True,
            is_active=True
        )
        user.set_password(validated_data['password'])
        user.save()
       
        return Response(UserSerializer(user).data)


