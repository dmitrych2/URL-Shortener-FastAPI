class ShortenerBaseError(Exception):
    pass

class NoLongUrlFoundError(ShortenerBaseError):
    pass

class SlugAlreadyExists(ShortenerBaseError):
    pass