# Write a program to fill in a letter template given below with name and date.
    # letter = '''
    # Dear <|Name|>,
    # You are selected!
    # <|Date|>
    # '''

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Satyam").replace("<|Date|", "20 Feb 2025"))
