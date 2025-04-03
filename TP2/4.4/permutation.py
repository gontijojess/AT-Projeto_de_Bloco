def permute_string(string, prefix="", result=None):
    if result is None:
        result = set()
    if len(string) == 0:
        result.add(prefix)
    else:
        for i in range(len(string)):
            remainder = string[:i] + string[i+1:]
            permute_string(remainder, prefix + string[i], result)
    return result

string_teste = "ttp2"
permutation_list = permute_string(string_teste)
print(f"{len(permutation_list)} permutacoes únicas possíveis para a string '{string_teste}':")
for x in permutation_list:
    print(x)