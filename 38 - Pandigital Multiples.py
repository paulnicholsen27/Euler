'''Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
 We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 
1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the 
concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed 
as the concatenated product of an integer with (1,2, ... , n) where n  1?'''

def pandigital_check( number ):
	digits = str( number )
	return len( digits ) == 9 and set( digits ) == set( "123456789" )

def pandigitals( ):
	pandigital_products = [ ]
	for x in range( 10000 ):
		product_string = ""
		multiplier = 1
		while len( product_string ) < 9:
			product_string += str( x * multiplier )
			multiplier += 1
		if pandigital_check( product_string ): 
			pandigital_products.append( int( product_string ) )
	return max( pandigital_products )

print pandigitals( )