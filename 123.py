from itertools import combinations

def quine_mccluskey(variables, minterms):
    # Step 1: Group minterms by the number of 1s in their binary representation
    groups = {}
    for minterm in minterms:
        num_ones = bin(minterm).count('1')
        if num_ones not in groups:
            groups[num_ones] = [minterm]
        else:
            groups[num_ones].append(minterm)
    
    # Step 2: Generate prime implicants
    prime_implicants = []
    for i in range(variables + 1):
        if i not in groups or i + 1 not in groups:
            continue
        next_group = groups[i + 1]
        current_group = groups[i]
        new_group = {}
        for m1 in current_group:
            for m2 in next_group:
                # Find minterms differing by only one bit
                if bin(m1 ^ m2).count('1') == 1:
                    combined = m1 | m2
                    if combined not in new_group:
                        new_group[combined] = [m1, m2]
                    else:
                        new_group[combined].extend([m1, m2])
        prime_implicants.extend(new_group.values())
        groups[i + 1] = [m for m in next_group if m not in new_group.keys()]
    
    # Step 3: Convert prime implicants to strings
    prime_implicants_strings = []
    for implicant in prime_implicants:
        implicant_str = ''
        for i in range(variables):
            if implicant & (1 << (variables - 1 - i)):
                implicant_str += '1'
            elif implicant & (1 << (variables - 1 - i)) == 0:
                implicant_str += '0'
            else:
                implicant_str += '-'
        prime_implicants_strings.append(implicant_str)
    
    # Step 4: Sort and return prime implicants
    sorted_implicants = sorted(prime_implicants_strings, key=lambda implicant: implicant.replace('-', '2'))
    return sorted_implicants

# Example usage:
variables = 3
minterms = [0, 1, 2, 5, 6, 7]
result = quine_mccluskey(variables, minterms)
print(result)  # ["00-", "0-0", "11-", "1-1", "-01", "-10"]