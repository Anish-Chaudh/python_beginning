ep1={345:23, 234:48,845:58,343:94,444:23}
ep2={344:22,585:94,485:94,948:44}
ep1.update(ep2)
# ep1.clear()
ep1.pop(345)
ep1.popitem()
del ep1[234]
print(ep1)