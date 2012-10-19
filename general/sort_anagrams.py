"""
sort words from dictionary so that anagram appear near each other

read english dictionary /usr/share/dict/words
"""

anagrams = {}

with open('/usr/share/dict/words') as f:
	for word in f:
		key = sorted(word.strip())
		key = ''.join(key)
		if anagrams.has_key(key):
			anagrams[key].append(word.strip())
		else:
			anagrams[key] = [word.strip()]

print anagrams
