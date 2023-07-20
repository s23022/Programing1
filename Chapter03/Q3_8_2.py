import pickle

with open("test1.pk1", "rd") as f:
    result = pickle.load(f)
    print(result)
