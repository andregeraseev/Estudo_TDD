from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimalModelTestCase(TestCase):

    def setUp(self) -> None:
        self.animal = Animal.objects.create(
            nome_animal = 'Leao',
            predador = 'Sim',
            venenoso =' Nao',
            domestico = 'Nao'
        )
    def test_animal_cadastrado_com_caractersticas(self):
        """Teste que verifica se animal cadastrado com suas caracteristicas"""
        self.assertEquals(self.animal.nome_animal, 'Leao')
