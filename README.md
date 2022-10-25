# Вопросы
## 1. Как правильно сохранять modified_at?
*Пояснение:* при создании записи в запросе приходит только value, но в БД нужно записать не только value, но и того пользователя, который сделал POST-запрос.

*Подсказка:* Модели и сериализаторы остаются неизменными

## *Ответ*
во ```views.py``` добавим код
```python
def perform_create(self, serializer):
    serializer.save(modified_by=self.request.user) # Тут self.request.user выводит текущего user по request
```

## 2. Для создания Entity на вход POST API подаётся json вида

```json
{
  "data[value]": 10
}
```

Как исправить сериализатор так, чтобы он мог принять поле ```"data[value]"``` и сохранить его в поле ```value```?

*Пояснение:* Python не позволит написать в сериализаторе ```data[value] = IntegerField(...),``` но есть другое решение 

*Подсказка:* Модели остаются неизменными

## *Ответ*
```{"data[value]": 10}``` тут ключ ```data[value]``` не соответствует JSON format key.
Тут будет несколько ответов:
1. ```{data_value: 10}```
2. ```{data: {value: 10}}```

## 3. Как вывести properties в формате ```{key:value, ...}```, если мы заранее не знаем сколько и каких key может быть?
*Пояснение:* Иногда нужно вывести данные, когда имена полей заранее неизвестны. 
Например
```json
[ 
  {
    "value": "circle",
    "properties": {
      "center": "100, 100",
      "radius": "50"
    }
  },
  {
    "value": "line",
    "properties": {
      "start": "150, 50",
      "end": "50, 150"
    }
  },
  {
    "value": "Медведь",
    "properties": {
      "класс": "Млекопитающие"
    }
  },
  {
    "value": "rectangle",
    "properties": {
      "corner_1": "50, 50",
      "corner_2": "150, 150"
    }
  }
]
```

## *Ответ*
