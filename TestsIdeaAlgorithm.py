from algorithm.IdeaAlgorithm import IdeaAlgorithm

key = 0x40000000330000000000000440000055
inputText = 0x677367736467

print('key\t\t', hex(key))
print('plaintext\t', hex(inputText))


ideaAlgorithm = IdeaAlgorithm(key)
encrypted = ideaAlgorithm.encrypt(inputText)
decrypted = ideaAlgorithm.decrypt(encrypted)

print('encrypted\t', hex(encrypted))
print('decrypted\t', hex(decrypted))

assert inputText == decrypted






print()
key = 0x49955880331112256788765441234555
inputText = 0x56856556858756

print('key\t\t', hex(key))
print('plaintext\t', hex(inputText))


ideaAlgorithm = IdeaAlgorithm(key)
encrypted = ideaAlgorithm.encrypt(inputText)
decrypted = ideaAlgorithm.decrypt(encrypted)

print('encrypted\t', hex(encrypted))
print('decrypted\t', hex(decrypted))

assert inputText == decrypted
