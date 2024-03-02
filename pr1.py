fruits = ["apple","banana","cherry","kiwi"]

element_to_remove = "banana"
i=0

while i < len(fruits):
  if fruits[i] == element_to_remove:
    fruits.remove(fruits[i])
    break
  else:
    i += 1
print(fruits)
