# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.


glossary = {'list': 'Conjunto de items organizados',
            'tuple': 'Lista imutável',
            'dictionary': 'Conjunto de informações sobre vários parâmetros',
            'if': 'Construção para verificação de caso',
            'else': 'Negativa caso o if não seja satisfeito',
            'for': 'Construção para realização de loop',
            }

for keys in glossary.keys():
    print(keys.title() + ": " + glossary[keys])