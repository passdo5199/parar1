#!/bin/bash

set -e

echo "Текущая папка:"
pwd

echo "Содержимое папки:"
ls -la

echo "Получение обновлений:"
git pull

echo "Запуск программы:"
python main.py

echo "Скрипт выполнен успешно"
