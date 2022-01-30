## Описание

Приложение агрегирует данные из разынх источников по урлу http://localhost:9090/gather

## Устанвока зависимостей
```bash
make -f Makefile create-venv
source ./.venv/bin/activate
```
## Запуск

- Запуск источников данных
```bash
make -f Makefile start-transmitters
```
- Запуск приемника этих данных
```bash
make -f Makefile start-receiver
```

## Остановка

-Остановка источников данных
```bash
make -f Makefile stop-transmitters
```