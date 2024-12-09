#!/bin/bash
set -e

# Django migratsiyalarini bajarish
python3 manage.py migrate

# Django serverini ishga tushurish
python3 manage.py runserver 0.0.0.0:8000 &

# Botni ishga tushurish
python3 bot.py

# Skriptni to'liq bajarish uchun
wait $!
