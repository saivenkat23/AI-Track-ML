#Assignment-1

#A farmer has recently acquired a 110 hectares piece of land. He has decided to grow Wheat and barley on that land. Due to the quality of the sun and the region’s excellent climate, the entire production of Wheat and Barley can be sold. He wants to know how to plant each variety in the 110 hectares, given the costs, net profits and labor requirements according to the data shown below:
#Crop 	Cost (Rs/Hec) 	Profit (Price/Hec) 	Man-days/Hec
#Wheat 	7000 	50 	10
#Barley 	2000 	120 	30

#The farmer has a budget of Rs. 7,00,000 and availability of 1,200 man-days during the planning horizon. Find the optimal solution and the optimal value.

from scipy.optimize import linprog
obj  = [-50, -120]
left = [[10, 30], [7000, 2000], [1, 1]]
right = [1200, 700000, 110]
bound = [(0, float("inf")), (0, float("inf"))]
opt = linprog(c = obj, A_ub = left, b_ub = right, bounds = bound)
print(opt)

print(f'For getting Maximum Profit\nArea for growing Wheat: {opt.x[0]} in hectares\nArea for growing Barley: {opt.x[1]} in hectares')
output:
  con: array([], dtype=float64)
     fun: -5778.947342194284
 message: 'Optimization terminated successfully.'
     nit: 5
   slack: array([3.98570933e-06, 6.77887059e-03, 4.73684292e+00])
  status: 0
 success: True
       x: array([97.89473581,  7.36842126])
For getting Maximum Profit
Area for growing Wheat: 97.89473581371212 in hectares
Area for growing Barley: 7.368421262572312 in hectares
