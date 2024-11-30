import pandas as pd
from itertools import combinations

#calculate the combinations list
def calculate_combinations(itemset, num_combinations):
    list_of_combination = []
    for comb in combinations(itemset, num_combinations):
        list_of_combination.append(comb)
    return list_of_combination

#calculate the value of bound
def calc_value(st, itemset, dictionary, n):
    # building W
    value = 0.0
    for num in range(n - 1, 0, -1):
        subsets = calculate_combinations(itemset, num)
        for comb in subsets:
            ck = all(item in comb for item in st)
            if ck :
                i = int(dictionary[comb]) * pow(-1.0, (n + 1) - num)
                value += i
    if st == ():
        empty = 0
        for dict_value in dictionary.values():
            empty += int(dict_value)
        value += empty * pow(-1.0, (n + 1))
        
    return value

#determin if itemset is drivable or not
def evaluate_bounds(itemset, dictionary):    
    upper_bounds = []
    lower_bounds = []
    lower_bound = 0
    upper_bound = 0
    n = len(itemset)
    for index in range(len(itemset)):
        subsets = calculate_combinations(itemset, index)
        # checking odd or even
        boolean_Odd = (n - len(subsets[0])) % 2
        for comb in subsets:
            # if the length is odd, update upper bound list
            if boolean_Odd:
                upper_bounds.append(calc_value(comb, itemset, dictionary, n))
            # if length is even, update lower bound list
            else:
                lower_bounds.append(calc_value(comb, itemset, dictionary, n))

    if max(lower_bounds) < 0:
        lower_bound = 0
    else:
        lower_bound = max(lower_bounds)

    upper_bound = min(upper_bounds)

    #  condition for upper and lower bound
    if lower_bound == upper_bound:
        bound = ' derivable'
    else:
        bound = ' non-derivable'

    return '{}: [{}, {}] {}'.format(itemset, lower_bound, upper_bound, bound)

#preprocessing for data
def main():
    itemset_df = pd.read_csv('itemsets.txt', header=None)
    ndi_df = pd.read_csv('ndi.txt', header=None)

    # converting itemsets to dictionary
    itemset_dict = {}
    for i, itemset_support in enumerate(itemset_df[0]):
        set_support_list = []
        for val in itemset_support.split(' '):
            if val == '-':
                continue
            else:
                set_support_list.append(val)
        itemset_dict[tuple(set_support_list[:-1])] = set_support_list[-1]
        # processing ndi 
    ndi_dict = {}
    for i, itemset in enumerate(ndi_df[0]):
        ndi_dict[i] = itemset.split(' ')
    for itemset in ndi_dict.values():
        # printing values
        print(evaluate_bounds(itemset, itemset_dict))


if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print('exception')
        traceback.print_exc()
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));
   
