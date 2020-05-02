def groupAnagrams(strs):
    if not strs:
        return []
    dictionary = {}
    for item in strs:
        newItem = ''.join(sorted(item))
        if newItem not in dictionary.keys():
            dictionary[newItem] = [item]
        else:
            dictionary[newItem].append(item)

    return dictionary.values()


if __name__ == "__main__":
    strs = ["tan", "ant", "nat", "ate", "eat", "tae"]
    print(groupAnagrams(strs))
