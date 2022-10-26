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
Решение на этот кейс [тут](https://github.com/man780/django/blob/d3928526ba74371c29ea0383d95f6400b0018e24/api/serializers.py#L22). 
method:`to_internal_value()`  line: 22

Теперь [назад](https://github.com/man780/django)