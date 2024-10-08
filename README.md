# GitHub Status Checker

## Описание

Этот проект представляет собой веб-приложение, которое проверяет текущий статус различных компонентов GitHub, таких как Git операции, API запросы, PRs и другие. Приложение использует API GitHub Status для получения информации о текущем состоянии системы и отображает ее на веб-странице.

## Функциональность

- Отображение статуса GitHub компонентов в виде списка.
- Кнопка "Get Status" для обновления данных о статусе.
- Компоненты, которые не находятся в состоянии 'Operational', выделены цветом для легкости восприятия.

## Технологии

- **Python** — Backend
- **Flask** — Веб-фреймворк для Python
- **HTML/CSS** — Веб-разметка и стилизация
- **JavaScript** — Для динамического обновления страницы

## Установка и запуск

### Клонирование репозитория

```bash
git clone https://github.com/your-username/github-status-checker.git
cd github-status-checker
