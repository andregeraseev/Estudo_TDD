from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(r'C:\Users\agera\OneDrive\Área de Trabalho\Alura\tdd\chromedriver.exe')

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
        pass