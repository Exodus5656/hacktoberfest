'''Future Value function that I was working on.'''

def main():
    
	#Variables for the formula that can be found here
        #(http://financeformulas.net/Future_Value_of_Annuity.html)

	P = float(input("Enter your monthly investment into the account"))
	yearly_rate = float(input("Enter the percent of return. '10% = 10'"))
	r = ((yearly_rate / 100) / 12)
	length_of_input = float(input("Enter how many years to invest"))
	n = length_of_input * 12
    
    
    	#Break the formula down into this code to calculate the 
	fv = P * (((1 + r) ** n -1) / (r))
    
	print( "Return is $%8.2f" % (fv))
    
    
    
    
    
    
main()
