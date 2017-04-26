
import numpy 
import matplotlib.pyplot as plt 
import scipy.integrate

filename = "droptower_vdata.txt"


def main():

	pLineWidth = 2
	dataArr = numpy.loadtxt(filename) #ONLY loads float numbers from a file

	tVals = []
	vyVals = []

	for i in range(0, len(dataArr)):
		t = dataArr[i][0]
		tVals.append(t)
		vy = dataArr[i][1]
		vyVals.append(vy)


	#print(dataArr)
	#print(tVals)
	#print(vyVals)

	accelerations = differentiate(tVals, vyVals)
	print (accelerations)

	positions = integrate(vyVals)
	print(positions)

	plt.plot(tVals, positions, 'r-', lw = pLineWidth)
	plt.scatter(tVals, positions, color = 'r', marker = 'o')

	plt.xlabel("time")
	plt.ylabel("position")
	plt.show()

	plt.plot(tVals, vyVals, 'b:', lw = pLineWidth + 1)
	plt.scatter(tVals, vyVals, color = 'b', marker = 'v')

	plt.xlabel("time")
	plt.ylabel("velocity")
	plt.show()

	plt.plot(tVals[:-1], accelerations, 'm--', lw = pLineWidth - 0.5 ) 
	plt.scatter(tVals[:-1], accelerations, color = 'm', marker = 'o')
	plt.xlabel("time")
	plt.ylabel("acceleration")
	#the first argument of plt.plot takes the elements of the array fromt the first to the n-1th element
	plt.show()

	avgUpAcc = giveUpwardAcc(accelerations)
	print("Average upward acceleration = ", numpy.sum(avgUpAcc)/len(avgUpAcc))

	plt.plot(tVals, positions, 'r-', tVals, vyVals, 'b:', tVals[:-1], accelerations, 'm--')
	plt.scatter(tVals, positions, color = 'r', marker = 'o', label="position")
	plt.scatter(tVals, vyVals, color = 'b', marker = 'v', label = "velocity")
	plt.scatter(tVals[:-1], accelerations, color = 'm', marker = 'o', label = "acceleration")
	plt.xlabel("time")
	plt.ylabel("position/velocity/acceleration")
	plt.legend()
	plt.show()

	f, axarr = plt.subplots(3, sharex=True)
	axarr[0].plot(tVals, positions, 'r-')
	axarr[0].set_ylabel("position")
	axarr[0].set_xlim([0,10])
	axarr[1].plot(tVals, vyVals, 'b:')
	axarr[1].set_ylabel("velocity")
	axarr[2].plot(tVals[:-1], accelerations, 'm--')
	axarr[2].set_ylabel("acceleration")
	axarr[2].set_xlabel("time")
	axarr[0].set_title('sharing the x axis')
	plt.show()


def differentiate(xs, ys):
	diffYs = numpy.diff(ys)
	diffXs = numpy.diff(xs)

	diffs = diffYs / diffXs
	return diffs

def integrate(ys):
	integrals = scipy.integrate.cumtrapz(ys, dx = 1.0, initial = 0)
	return integrals

def giveUpwardAcc(accs):
	upAcc = []
	for i in range(0, len(accs)):
		if accs[i] > 0:
			upAcc.append(accs[i])
	return numpy.array(upAcc)

main()	

