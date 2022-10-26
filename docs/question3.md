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

Теперь [назад](https://github.com/man780/django)