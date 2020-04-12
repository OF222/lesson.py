x=[2,4,6,8]
x[2]=7
print(x)

#要素の追加、削除、選択
x.append(9)
print(x)

del x[0:3]
print(x)

print(x[0:2])

x += [2,4,6]
print(x)
print(len(x))