## 1. Как правильно сохранять `modified_at`?
_**Пояснение:**_ при создании записи в запросе приходит только `value`, но в БД нужно записать не только `value`, но и того 
пользователя, который сделал POST-запрос.

_**Подсказка:**_ Модели и сериализаторы остаются неизменными

## *Ответ на 1 - вопрос*
во `views.py` добавим код
```python
def perform_create(self, serializer):
    serializer.save(modified_by=self.request.user) # Тут self.request.user выводит текущего user по request
```

Теперь [назад](https://github.com/man780/django)