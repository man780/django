# Вопросы
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

## 2. Для создания Entity на вход POST API подаётся json вида

```json
{
  "data[value]": 10
}
```

Как исправить сериализатор так, чтобы он мог принять поле `"data[value]"` и сохранить его в поле `value`?

_**Пояснение:**_ Python не позволит написать в сериализаторе `ata[value] = IntegerField(...),` но есть другое решение 

_**Подсказка:**_ Модели остаются неизменными

## *Ответ на 2 - вопрос*
`{"data[value]": 10}` тут ключ `data[value]` не соответствует JSON format key.
Тут будет несколько ответов:
1. `{data_value: 10}`
Решение на этот кейс [тут](https://github.com/man780/django/commit/e33ee34d99628696770ce31b0a4f5bb2d6acc081)
2. `{data: {value: 10}}`
Решение на этот кейс [тут](https://github.com/man780/django/blob/d3928526ba74371c29ea0383d95f6400b0018e24/api/serializers.py#L22) method:`to_internal_value()`  line: 22

## 3. Как вывести properties в формате `{key:value, ...}`, если мы заранее не знаем сколько и каких key может быть?
_**Пояснение:**_ Иногда нужно вывести данные, когда имена полей заранее неизвестны. 
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

## *Ответ на 3 - вопрос*
Тут думаю вы имели в виду что надо список `Entity` с `value`, `properties`

Только в списке выше: `{"value": "type: str"}`, а наш model `Entity` field `value`: `type: int`

Для этого я не стал менять model value type и оставил как есть
Тут сделал 2 решения 
1. Стандартный `/api/entity/full/` Но JSON чуть по другому выводит данные
2. И не стандартный `/api/entity/full2/` `Response json` выводит именно так как вы написали в задание
