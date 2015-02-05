def Tj(fs = 1370, a = 0.28, sigma = 5.67E-8, f = 0.77):
	return float(fs*(1-a)/(4*sigma*(1-(f/2))))

def main():
	print(" %5d" % (Tj()))

if __name__ == "__main__":
	main()
