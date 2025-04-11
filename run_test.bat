@echo off
call venv\Scripts\activate
pytest --alluredir=report
allure serve report
