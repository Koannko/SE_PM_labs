def add_chars(w1, w2):
    """
    Необязательное задание.
    Возвращает строку, содержащую символы, недостающие для получения w2 из w1.
    Подразумевается, что w1 - это подпоследовательность w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # запрещено использовать циклы и множества!
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp'])
    True
    """
    if len(w1) == 0:
        return ''
    if w1[0] == w2[0]:
        return add_chars(w1[1:], w2[1:])
    return w2[0] + add_chars(w1, w2[1:])
print(add_chars("coy", "cacophony"))