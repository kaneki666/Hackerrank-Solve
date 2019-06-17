import pyhash

bit_vector = [0] * 20

fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

fnv_pikachu = fnv("Pikachu") % 20
fnv_charmender = fnv("Charmender") %20
murmur_pikachu = murmur("Pikachu") % 20
murmur_charmender = murmur("Charmender") %20

print(fnv_pikachu)
print(fnv_charmender)
print(murmur_pikachu)
print(murmur_charmender)
