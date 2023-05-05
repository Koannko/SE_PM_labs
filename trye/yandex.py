def configure(left, right):
    return 0.5**(left + 1) * (1 - 0.5 ** 9) / 0.5

def main():
    sum = 0
    for right in range(1, 12):
        left = 3
        result = configure(left, right)
        sum += result
        print("Running left = {left}, right = {right}, sum = {sum}".format(left=left, right=right, sum=sum))
        left += 1

main()