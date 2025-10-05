from random import randrange


def get_random_item(query):
    """
    Возвращает случайный элемент из запроса
    :param query: SQLAlchemy запрос
    :return: случайный объект или None
    """
    quantity = query.count()
    if quantity:
        offset_value = randrange(quantity)
        return query.offset(offset_value).first()
    return None
