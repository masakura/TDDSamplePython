import doctest


def include_tax(price):
    """消費税込み金額を返す
    >>> include_tax(100)
    108
    >>> include_tax(128)
    138
    """
    return int(price * 1.08)

if __name__ == "__main__":
    doctest.testmod()