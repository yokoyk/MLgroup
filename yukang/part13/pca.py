from numpy import *

def loadDataSet(filename,delim='\t'):
    fr = open(filename)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    dataArr = [map(float,line) for line in stringArr]
    return mat(dataArr)

def pca(dataMat, topNfeat=99999):
    meanVals = mean(dataMat,axis = 0)
    meanRemoved = dataMat - meanVals
    covMat = cov(meanRemoved,rowvar = 0)
    eigVals,eigVects = linalg.eig(mat(covMat))
    eigValInd = argsort(eigVals)
    eigValInd = eigValInd[:-(topNfeat+1):-1]
    redEigVects = eigVects[:eigValInd]
    lowDDataMat = meanRemoved*redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat

def replaceNanWithMean():
    dataMat = loadDataSet('secom.data','')
    numFeat = shpape(dataMat)[1]
    for i in range(numFeat):
        meanVal = mean(dataMat[nonzero(~isnan(dataMat[:,i].A))[0],i])
        dataMat[nonzero(isnan(dataMat[:,i].A))[0],i] = meanVal
    return dataMat