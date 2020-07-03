def minmax(a_list):
    if not a_list:
        raise ValueError
    else:
        return (min(a_list), max(a_list))


print(minmax([]))
