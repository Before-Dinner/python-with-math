for n in range(2, 31):
  for m in range(2, n + 1):
    if n % m == 0 :
      break
  if m == n :
    print(n)

