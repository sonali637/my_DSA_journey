def common_latter(s1,s2):
    common = set(s1) & set(s2)
    return ''.join(sorted(common))
s1 = "programming"
s2 = "language"
print(common_latter(s1,s2))



