def join_with_separator(*words, separator="_"):
    return separator.join(words)


words_list = ("a", "b", "c", "d")
separator_str = "_"
result = join_with_separator(*words_list, separator=separator_str)
print(result)
