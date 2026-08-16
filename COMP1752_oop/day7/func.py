def add(a, b):
	c = a + b
	return c
def rank(grade):
	if grade < 0 or grade > 100:
		x = "invalid"
	elif grade < 40:
		x = "failed"
	elif grade < 60:
		x = "passed"
	elif grade < 80:
		x = "merit"
	else:
		x = "distinction"
	return x
