backpack_m = 1300
list_of_things = {'cup': 350,
                  'sleeping_bag': 650,
                  'sweater': 430,
                  'slippers': 220,
                  'toothpaste': 550,
                  'Toothbrush': 50,
                  'blouse': 400,
                  'pants': 550,
                  'boots': 870,
                  'shampoo': 1200,
                  'soap': 440}

list_keys = list(list_of_things.keys())
result = []


def rec(all_perm, curr_weight, index):
    for i in range(index+1, len(list_of_things)):
        if curr_weight + list_of_things[list_keys[i]] <= backpack_m:
            new_curr_weight = curr_weight + list_of_things[list_keys[i]]
            new_all_perm = all_perm + [list_keys[i]]
            result.append(new_all_perm)
            rec(new_all_perm, new_curr_weight, i)


rec([], 0, 0)
print(result)
