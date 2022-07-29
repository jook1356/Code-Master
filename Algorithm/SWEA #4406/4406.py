def count_blood(x):
    counted_blood = {type : 0 for type in x}
    for i in x:
        counted_blood[i] += 1
    return counted_blood

print(count_blood([
'A', 'B', 'A', 'O', 'AB', 'AB',
'O', 'A', 'B', 'O', 'B', 'AB',
])) # => {'A': 3, 'B': 3, 'O': 3, 'AB': 3}