# You have been contacted by Boeing airplane manufacturing company. You are to develop an algorithm  
# that will calculate the specific impulse, 𝐼𝑠𝑝 of a jet engine given the following constant parameters. 
# 𝑔 = 9.8, 𝛾 = 1.4, 𝑅 = 270𝐾 
# However, the Mach number, Me and combustion chamber temperature, T will be provided by the  
# technicians. Use the formulae below: 
# 𝐼𝑠𝑝 = 
# 1 
# 𝑔 
# [ 𝑀𝑒 × √𝛾𝑅𝑇 × ( 
# 1 
# 1 + 
# 𝛾 − 1 
# 2 
# × (𝑀𝑒) 
# 2 
# ) ]
import math
g = 9.8
y = 1.4
R = 270

#divide the calculations into several sections to make it easier then combining them at the end


#calculates 1 over g
first_calc = 1 / g

#input the values of Me & T
Me = float(input('Enter Mack number: '))
T = float(input('Enter the combustion chamber temperature: '))

#calculates yRT
second_calc = ( y * R * T)

#claculates 1 over 1 plus y -1 over 2 divided by the square of Me
third_calc = ( (1) / ((1) + ((y-1)/(2)) * (Me * Me)))

#creates a variable to store the value of the calculation between the second_calc and third_calc
solution_1 = (second_calc * third_calc)

#finding the square of the solution_1
root_of_solution_1 = math.sqrt(solution_1)

#multiply Me by root_of_solution_1
solution_2 = (Me * root_of_solution_1)

#multiply first_calc by solution_2
solution_3 = (first_calc * solution_2)

# final solution
Specific_impulse = round(solution_3, 2) 

#print out Specific impulse
print(f'The Specific impulse is {Specific_impulse}')








