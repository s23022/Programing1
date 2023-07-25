def concat_words(*args, separator="."):
    concat_words("a", "b", "c", "d", separator="_")
    return separator.join(args)
