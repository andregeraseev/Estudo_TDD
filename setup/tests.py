from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from animais.models import Animal
import time


class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(r'C:\Users\agera\OneDrive\Área de Trabalho\Alura\tdd\chromedriver.exe')
        self.animal = Animal.objects.create(
            nome_animal = 'leao',
            predador = 'Sim',
            venenoso = 'Nao',
            domestico = 'Nao')


    def tearDown(self):
        self.browser.quit()

    # def test_para_verificar_se_a_janela_do_chrome(self):
    #     self.browser.get(self.live_server_url)



    def test_buscando_um_novo_animal(self):
        """Teste se um usuario encontra um animal pesquisando"""

        # Vini, deseja encontrar um novo animal,
        # para adotar.

        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')
        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEquals('Busca Animal', brand_element.text)

        # Ele vê um campo para pesquisar animais pelo nome.
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEquals(buscar_animal_input.get_attribute('placeholder'), 'Exemplo:leao')



        # Ele pesquisa por Leão e clica no botão pesquisar.
        buscar_animal_input.send_keys('leao')
        # time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        # O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.results-description')
        self.assertGreater(len(caracteristicas),3)
        # Ele desiste de adotar um leão.
        pass