def max_candies_on_path(isles):
    n = len(isles)
    
    if n == 1:
        return isles[0]
    
    # Initialize a list to store the maximum candies collected at each isle
    dp = [0] * n
    
    # Base case
    dp[0] = isles[0]
    dp[1] = max(isles[0], isles[1])
    
    # Dynamic programming to compute the maximum candies
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + isles[i])
    
    # The answer is the maximum of the last two isles
    return max(dp[-1], dp[-2])

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
li=[]
for _ in range(num_test_cases):
    isles = list(map(int, input().split()))
    result = max_candies_on_path(isles)
    li.append(result)
for i in li:
    print(i,end=' ')