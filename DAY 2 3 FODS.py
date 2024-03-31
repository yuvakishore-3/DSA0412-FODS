import numpy as np
fuel_efficiency = np.array([25, 30, 28, 32, 27])
average_fuel_efficiency = np.mean(fuel_efficiency)
model1_index = 0  
model2_index = 2  
model1_fuel_efficiency = fuel_efficiency[model1_index]
model2_fuel_efficiency = fuel_efficiency[model2_index]
percentage_improvement = ((model1_fuel_efficiency - model2_fuel_efficiency) / model2_fuel_efficiency) * 100
print("Average Fuel Efficiency:", average_fuel_efficiency)
print("Percentage Improvement between Model 1 and Model 2:", percentage_improvement)
