K = int(input())
message = input()
for i in range(len(message)):
    shift = 3 * (i+1) + K
    code = (ord(message[i]) - ord('A') - shift) % 26 + ord('A')
    print(chr(code), end='')