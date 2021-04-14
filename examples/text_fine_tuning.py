from quickai import TextFineTuning

TextFineTuning("./aclImdb", "./FUNCTIONTESTCLASSIFICATION", "classification", ["pos", "neg"], epochs=1)  # Text classification

TextFineTuning("./wnut17train.conll", "./FUNCTIONTESTTOKENCLASSIFICATION", "token_classification",
               epochs=1)  # Token Classification