a = {x for x in "abcabcabc" if x not in "ab"}
b = {y for y in "abcabcabc" if y not in "ab"}
a | b
# 出力結果{'a','c'}
