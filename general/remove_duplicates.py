"""
remove duplicates from a string - python way :)

"""

def remove_duplicates(string):
    if string is None or len(string) < 1:
        return False
    array = [e for e in string]
    return ''.join(set(array))


print remove_duplicates("sssddre")
