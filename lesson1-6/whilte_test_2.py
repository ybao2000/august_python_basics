while True:   # while is similar to if, but the difference is if is not loop, while is a loop
  line = input("Enter a line (end to break): ")
  if line == "end":
    break  # this is a jump, get out of the loop
  if line == "#":
    continue  # this is another jump, go back to while
  print(line)

print()
print("End")


# program or code
# 3 basic structure
# 1. sequential
# 2. conditional (if, elif, else), could be skipped
# 3. loop (repeated, while -- conditional loop, for -- definite lop)