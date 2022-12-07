data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

codes = []
designations = []

for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)
operators = {}

c = 0
while len(operators) != len(designations):
    operators[designations[c]] = {codes[c]}
    c += 1
del operators['Katel'],operators ['Fonex']
operators ['Megacom'].add('0555')
operators ['O!'].add('0700')
operators ['O!'].add('0500')
operators ['Megacom'].add('0999')
operators ['Beeline'].add('0222')
operators ['Beeline'].add('0777')
for key,values in operators.items():
    print(key ,'-' ,values )


