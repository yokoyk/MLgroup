def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    retArray = ones((shape(dataMatrix)[0],1))

    if threshIneq == 'lt':
        retArray[dataMatrix[:,dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:,dimen] > threshVal] = 1.0
    return retArray


def buildStump(dataArr, classLabels,D):
    dataMatrix = mat(dataArr)
    labelMat = mat(classLabels).T
    m,n = shape(dataMatrix)
    numSteps = 10.0
    bestStump = {}
    bestClassEst = mat(zeros((m,1)))
    minError = inf
    for i in range(n):
        rangeMin = dataMatrix[:,i].min
        rangeMax = dataMatrix[:,i].max()
        stepSize = (rangeM - rangeMin)/numSteps
        for j in range(-1,int(numSteps)+1):
            for inequal in ['lt','gt']:
                threshVal = (rangeMin + float(j)*stepSize)
                predictedVals =  stumpClassify(dataMatrix,i,threshVal, inequal)
                errArr = mat(ones(m,1))
                errArr[predictedVals == labelMat] = 0
                wieghtedError = D.T*errArr
                print "split: dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f," %(i,threshVal,inequal,weightedError)
                if wieghtedError < minError:
                    minError =  wieghtedError
                    bestClassEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClassEst
