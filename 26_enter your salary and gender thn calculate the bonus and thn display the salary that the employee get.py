#A company decides to give bonus to its employee on this diwali.
#A 5% bonus on salary is given to the male workers and 10% bonus salary to the female workers.
#If salary of the employee is less than 15000 thn the employee get an extra  3% bonus on the salary
#WAP to enter your salary and gender thn calculate the bonus that has to given to the employee  and display the salary that the employee will get...
sal=int(input('Enter your salary')) 
gender=input('Enter your gender')

if gender=='male':
    bonus=0.05*sal
else:
    bonus=0.10*sal

if sal<15000:
    print('As ur salary is less than 15000 so u will get extra 3% bonus,And ur')
    bonus=bonus+0.03*sal

sal=bonus+sal
print('Salary is',sal)        
