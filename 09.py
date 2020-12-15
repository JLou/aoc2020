preambule_size = 25

with open('inputs/09.txt', 'r') as f:
    numbers = [int(x) for x in f.readlines()]

preambule = set(numbers[:preambule_size])

i=preambule_size
weak_number = 0
for number in numbers[preambule_size:]:
    found = False
    for diff in preambule:
        if diff < number and (number - diff) in preambule:
            found = True
            break
    if found:
        pass #print(f"number {number} is ok")
    else:
        print(f"guilty number {number}")
        weak_number = number
        break
    
    i += 1
    preambule.remove(numbers[i-preambule_size-1])
    preambule.add(number)

sum = numbers[0]
curr_start = curr_end = 0
while sum != weak_number:
    if sum < weak_number:
        curr_end += 1
        sum += numbers[curr_end]
    elif sum > weak_number:
        sum -= numbers[curr_start]
        curr_start +=1

print(numbers[curr_start:curr_end+1])
min_number, max_number=  min(numbers[curr_start:curr_end+1]), max(numbers[curr_start:curr_end+1])
print(f'{min_number} + {max_number} = {min_number + max_number}')