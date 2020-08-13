def add(*matrices):
  l = len(matrices[0][0])
  con1 = False in [len(a) == l for m in zip(*matrices) for a in m]
  con2 = False in [len(a) == len(matrices[0]) for a in matrices]
  if con1 or con2:
    raise ValueError("Given matrices are not the same size.")
  return [
    [sum(values) for values in zip(*rows)]
    for rows in zip(*matrices)
  ]

a = [[1,2,3], [2,3,4]]
b = [[3,4,5], [4,5,6]]
c = [[4,5,6], [5,6,7]]

print(add(a,b,c))