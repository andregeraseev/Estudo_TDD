from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViewTestCase(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'calopsita',
            predador = 'Nao',
            venenoso = 'Nao',
            domestico= 'Sim'
        )

    def test_index_retorna_caracteristicas_do_animal(self):
        """verifica se a index retorna as caracteristicas do animal"""
        response= self.client.get('/',
                                  {'buscar':'calopsita'})
        caracteristica_animal_pesquisado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']),QuerySet)
        self.assertEquals(caracteristica_animal_pesquisado[0].nome_animal, 'calopsita')