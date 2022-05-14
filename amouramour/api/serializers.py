from django.contrib.auth.models import User, Group
from rest_framework import serializers

from amouramour.api.models import Cliente, FormaPagto, Pedido, Produto, Status, Transportadora


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TransportadoraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transportadora
        fields = '__all__'

class FormaPagtoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormaPagto
        fields = '__all__'

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
