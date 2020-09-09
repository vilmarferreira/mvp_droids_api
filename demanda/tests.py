from django.contrib.auth.models import User
from django.test import TestCase,Client

from contato.models import Contato
from .models import Demanda
from endereco.models import Estado, Endereco
from rest_framework import status
import json
client = Client()

class DemandaTest(TestCase):
    def setUp(self):
        user = User(username='darth_vader')
        user.set_password('password1234')
        user.is_active = True
        user.save()

        user2 = User(username='luke',is_active=True)
        user2.set_password('password1234')
        user2.save()

        estado,create = Estado.objects.get_or_create(nome='Tocantins',UF='TO')

        response = client.post(
            '/api-token-auth/',
            data=json.dumps({'username': 'darth_vader', 'password': 'password1234'}),
            content_type='application/json',
        )
        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access'],
        }

        self.payload_valid = {
            "endereco": {
                "rua": "Rua das Oliveiras",
                "numero": "s/n",
                "complemento": "Complemento",
                "bairro": "Bairro",
                "cep": "77.000-000",
                "cidade": "Palmas",
                "estado": estado.id
            },
            "contato": {
                "celular": "6398100000",
                "email": "email@email.com"
            },
            "descricao": "Braço esquerdo para doird R2D2"
        }

        self.payload_invalid = {
            "endereco": {
                "rua": "Rua das Oliveiras",
                "numero": "s/n",
                "complemento": "Complemento",
                "bairro": "Bairro",
                "cep": "77.000-000",
                "cidade": "Palmas",
                "estado": estado.id
            }
        }

        self.payload_valid_update = {
            "endereco": {
                "rua": "Novo endereço",
                "numero": "s/n",
                "complemento": "Estrela da morte",
                "bairro": "hemisfério norte",
                "cep": "77.000-000",
                "cidade": "Palmas",
                "estado": estado.id
            },
            "contato": {
                "celular": "6398100000",
                "email": "darthizinho@imperio.com"
            },
            "descricao": "Braço direito para doird R2D2"
        }

        ##criando objectos para testes de delete e update
        data_endereco = self.payload_valid['endereco'].copy()
        data_endereco['estado'] = estado
        data_contato = self.payload_valid['contato']
        endereco = Endereco.objects.create(**data_endereco)
        contato = Contato.objects.create(**data_contato)
        self.demanda = Demanda.objects.create(endereco = endereco,contato = contato,descricao = 'Braço para droid C3PO', anunciante=user)
        data_endereco['rua'] = 'Nova rua'
        data_contato['celular'] = '00000000000'
        endereco = Endereco.objects.create(**data_endereco)
        contato = Contato.objects.create(**data_contato)
        self.demanda2 = Demanda.objects.create(endereco = endereco,contato = contato,descricao = 'Perna para droid C3P1', anunciante=user2)

    def test_create_demanda(self):
        response = client.post(
            '/api/v1/demandas',
            content_type='application/json',
            data=json.dumps(self.payload_valid),
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_demanda_invalid(self):
        response = client.post(
            '/api/v1/demandas',
            content_type='application/json',
            data=json.dumps(self.payload_invalid),
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_unauthorized(self):
        response = client.post(
            '/api/v1/demandas',
            content_type='application/json',
            data=json.dumps(self.payload_valid),
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update(self):
        response = client.put(
            '/api/v1/demandas/{0}'.format(self.demanda.id),
            content_type='application/json',
            data=json.dumps(self.payload_valid_update),
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_update_partial(self):
        response = client.patch(
            '/api/v1/demandas/{0}'.format(self.demanda.id),
            content_type='application/json',
            data=json.dumps({'descricao':'Nova descricao'}),
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid(self):
        response = client.patch(
            '/api/v1/demandas/{0}'.format(self.demanda.id),
            content_type='application/json',
            data=json.dumps({'descricao': ''}),
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        response = client.delete(
            '/api/v1/demandas/{0}'.format(self.demanda.id),
            content_type='application/json',
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_demanda_other_user(self):
        response = client.delete(
            '/api/v1/demandas/{0}'.format(self.demanda2.id),
            content_type='application/json',
            **self.auth_headers
        )
        ##retorno 404 pois não é encontrado para aquele usuário, impossibilitando saber se o id existe na base de dados ou não.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_other_user(self):
        response = client.patch(
            '/api/v1/demandas/{0}'.format(self.demanda2.id),
            content_type='application/json',
            data=json.dumps({'descricao': 'Nova descricao'}),
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



