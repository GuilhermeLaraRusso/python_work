# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.

# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.

# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {'list': 'Conjunto de items organizados',
            'tuple': 'Lista imutável',
            'dictionary': 'Conjunto de informações sobre vários parâmetros',
            'if': 'Construção para verificação de caso',
            'else': 'Negativa caso o if não seja satisfeito',
            'for': 'Construção para realização de loop',
            }

print("List: " + glossary['list'] + '\n\nTuple: ' + glossary['tuple'] + '\n\nDictionary:' + glossary['dictionary'] +
      '\n\nIf: ' + glossary['if'] + '\n\nElse: ' + glossary['else'] + '\n\nFor: ' + glossary['for'] + '\n')