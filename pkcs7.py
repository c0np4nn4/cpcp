m = "YELLOW SUBMARINE"
blockSize = 10

m = m.encode()

length = 0
while length < len(m):
    length += blockSize

count = length - len(m)

pad = bytes([count]) * count
result = m + pad

print(result)