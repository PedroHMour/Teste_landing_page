import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    # Setup do WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # Teardown (executa após o teste)
    driver.quit()

@pytest.mark.cadastro
def test_formulario(driver):
    driver.get("file:///C:/Users/henri/OneDrive/Desktop/Teste_landing_page/pages/landing_page.html")

    # Preenche o formulário
    driver.find_element(By.ID, "nome").send_keys("João Silva")
    driver.find_element(By.ID, "email").send_keys("joao.silva@gmail.com")
    driver.find_element(By.ID, "senha").send_keys("senha123")
    driver.find_element(By.ID, "senha").send_keys(Keys.RETURN)

    time.sleep(2)

    # Verifica se a mensagem de sucesso está na página
    assert "Cadastro realizado com sucesso" in driver.page_source
