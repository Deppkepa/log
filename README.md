# Логирование

1. Загружаем на машину все файлы.py.
2. Запустить файл User-service командой: `python3 User-service.py`.
3. Командой запускаем файл-прослушку: `python3 subscriber.py`.
4. Запускаем генерацию случайных сообщений с помощью команды: `python3 publisher.py`.
   
# Результат:
Логи записываются в файл и выводятся в консоль логи по шаблону.

Если хотим проверить файл логов то запускаем файл для проверки правильности зауписанных логов: `python3 checker.py`.

Пример: `my_app-test.py`
