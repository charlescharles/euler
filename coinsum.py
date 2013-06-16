def ways(s, vals):
	if s < 0 or not vals: return 0
	dp = [0]*(s+1)
	dp[0] = 1
	for i in range(len(vals)):
		for j in range(vals[i], s+1):
			dp[j] += dp[j-vals[i]]
	return dp[s]

coins = [1,2,5,10,20,50,100,200]
print ways(200, coins) 
