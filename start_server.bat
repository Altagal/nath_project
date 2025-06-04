@echo off
REM Ativa o ambiente virtual (ajuste o caminho se necessário)
call venv\Scripts\activate

cd nath

REM Roda o servidor Django
python manage.py runserver

REM Mantém o terminal aberto após a execução (opcional)
pause