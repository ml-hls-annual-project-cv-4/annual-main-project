# Тема проекта:  Детекция участников и регулирующих объектов дорожного движения

## Участники проекта

| Фамилия Имя | github |
| --- | --- |
| Анисимов Данил | ExLineP |
| Головкина Ольга | olga-golovkina |
| Коваленко Максим | max-kovalenko | 

## Checkpoints
1. [Этапы выполнения годового проекта](https://github.com/ml-hls-annual-project-cv-4/annual-main-project/wiki/%D0%AD%D1%82%D0%B0%D0%BF%D1%8B-%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B3%D0%BE%D0%B4%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
2. [Информация о датасетах](https://github.com/ml-hls-annual-project-cv-4/annual-main-project/blob/datasets-info/files/datasets_info.txt)

# Выступления
1. [Презентация для 4 чекпойнта](https://bimacademy-my.sharepoint.com/:p:/g/personal/golovkinaos_bimacad_ru/EU6Lj6l7R5xBmr2I-vM3GIUBWjoWsXzd6K_tYgKJkcnBeQ?e=hTzUwJ)

## О сайте
Сайт на React

Как запустить:
1) Клонировать данную ветку
2) Ввести команду установки всех зависимостей
```console
npm i
```
3) Ожидать установки всех зависимостей
4) Для запуска сайта в режиме разработчика ввести:
```console
npm run dev
```

Deploy версия на Vercel: https://cv-cars-4.vercel.app/

FastApi Api:
```console
cd ./api
pip install -r requirements.txt
uvicorn main:app --reload
```
