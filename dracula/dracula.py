novel = open('dracula.txt', 'r')
vampyTimes = open('vampytimes.txt', 'w')

count = 0
for line in novel:
    if "vampire" in line.lower():
        print(line)
        count += 1
        vampyTimes.write(line)

print(count)
