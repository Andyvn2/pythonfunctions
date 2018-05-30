def draw_stars(x):

	for counter in range(0,len(x)):
		print x[counter]*"*"



x = [4, 6, 1, 3, 5, 7, 25]

draw_stars(x)


def draw_stars(x):

	for counter in range(0,len(x)):
		if type(x[counter])==int:
			print x[counter]*"*"
		else:
			y=x[counter]

			y= y.lower()

			
			print x[counter].count("")* y[0]



x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)


