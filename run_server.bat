@echo off
title My Book Library - Django Server
cd /d "%~dp0"
echo Activating Virtual Environment...
call venv\Scripts\activate
echo Starting Django Server on http://127.0.0.1:8000/ ...
python manage.py runserver 127.0.0.1:8000
pause
