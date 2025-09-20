# Representation of CFG rules
grammar = [
    ('E', ['E', '+', 'E']),
    ('E', ['E', '-', 'E']),
    ('E', ['E', '*', 'E']),
    ('E', ['E', '/', 'E']),
    ('E', ['E']),                       # or ('E', ['F']) if that's intended
    ('F', ['aF']),
    ('F', ['bF']),
    ('F', ['0F']),
    ('F', ['1F']),
    ('F', ['a']),
    ('F', ['b']),
    ('F', ['0']),
    ('F', ['1'])
]

print("CFG")
for rule in grammar:
    print(rule)
