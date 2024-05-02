@echo off
CALL .\venv\Scripts\activate
py -m unittest -v
:: py -m unittest discover -s tests -t . -v
cmd /k