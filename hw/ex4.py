class MyDict(dict):
        """
        >>> x = MyDict([('one', 1), ('two', 2), ('three', 3)])
        >>> print(x['three'])
        3
        >>> print(x.get('two'))
        2
        >>> print(x.one)
        1
        >>> print(x.test)
        Traceback (most recent call last):
        ...
        AttributeError
        """
        def __getattr__(self, name):
            try:
                return self[name]
            except KeyError:
                raise AttributeError


if __name__ == "__main__":
    import doctest
    doctest.testmod()
