ans = []
for N in range(0,40+1):
    if bin(N)[-4:] == "1011":
        ans.append(N)
print(max(ans))