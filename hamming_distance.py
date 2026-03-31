def hamming_distance(text1, text2):
  distancia = 0
  for x,y in zip(text1, text2):
    xor = x ^ y
    distancia += bin(xor).count("1")
  return distancia

print(hamming_distance("git", "hub")
