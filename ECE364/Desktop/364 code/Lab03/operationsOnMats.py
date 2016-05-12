#! /usr/bin/env python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-02-04 11:17:55 -0500 (Wed, 04 Feb 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Lab03/operationsOnMats.py $: 
import os
import math
import sys

def checkIfMatrixIsValid(matrix):
    if type(matrix[0]) is not list:
        return False
    else:
        num_lists = len(matrix)
        if num_lists == 1:
            return True
        cmpr = len(matrix[0])
        for i in range(0, num_lists):
            if len(matrix[i]) != cmpr:
                return False
            else:
                cmpr = len(matrix[i])
    #if reaches here, then return true
    return True
                
def getMatrixSize(matrix):
    ret_list = []
    if checkIfMatrixIsValid(matrix) == True:
        rowCount = len(matrix)
        colCount = len(matrix[0])
        ret_list = [rowCount, colCount]
        return ret_list
    else:
        return ret_list

def getRow(matrix, rowIndex):
    ret_list = []
    if checkIfMatrixIsValid(matrix) == False:
        return ret_list
    else:
        size = len(matrix)
        if rowIndex in range(0, size):
            ret_list = matrix[rowIndex]
            return ret_list
        else:
            return ret_list

def getColumn(matrix, columnIndex):
    ret_list = []
    if checkIfMatrixIsValid(matrix) == False:
        return ret_list
    else:
        size = len(matrix[0]) #size no of columns
        if columnIndex in range(0, size):
            for i in range(0, len(matrix)):
                ret_list.append(matrix[i][columnIndex])
            return ret_list
        else:
            return ret_list

def transposeMatrix(matrix):
    if checkIfMatrixIsValid(matrix) == False:
        return None
    else:
        transpose = []
        num_cols = len(matrix[0])
        for i in range(0, num_cols):
            transpose.append(getColumn(matrix, i))
        return transpose

def dotProduct(row, column):
    if len(row) <= 0 or len(column) <= 0 or len(row) != len(column):
        return None
    else:
        size = len(row)
        sum_of_prod = 0
        for i in range(0, size):
            sum_of_prod = sum_of_prod + (row[i] * column[i])
        return sum_of_prod

def multiplyMatrices(matrix1, matrix2):
    if checkIfMatrixIsValid(matrix1) == False or checkIfMatrixIsValid(matrix1) == False:
        #print("1")
        return None
    elif len(matrix1[0]) != len(matrix2):
        #print("2")
        return None
    else:
        mul_mat = []
        for i in range(0, len(matrix1)):
            tmp = []
            for j in range(0, len(matrix2[0])):
                 tmp.append(dotProduct(getRow(matrix1, i), getColumn(matrix2, j)))
            mul_mat.append(tmp)
        
        return mul_mat
        

if __name__ == "__main__":
    mat1 = [[3,2,1],[4,5],[3,1,0]]
    c = checkIfMatrixIsValid(mat1)
    print c
    mat2 = [[9,1],[1,3],[3,1]]
    c = checkIfMatrixIsValid(mat2)
    print c
    mat3 = [[9,8,5,2]]
    c = checkIfMatrixIsValid(mat3)
    print c
    mat4 = [[9],[3],[1]]
    c = checkIfMatrixIsValid(mat4)
    print c
    mat5 = [9,8,5,2]
    c = checkIfMatrixIsValid(mat5)
    print c
    t = getMatrixSize(mat2)
    print t
    t = getMatrixSize(mat1)
    print t
    r = getRow(mat2,1)
    print r
    r = getRow(mat2,3)
    print r
    r = getRow(mat1,0)
    print r
    c = getColumn(mat2,0)
    print c
    c = getColumn(mat2,3)
    print c
    c = getColumn(mat1,0)
    print c
    t = transposeMatrix(mat2)
    print t
    t = transposeMatrix(mat1)
    print t
    row1 = [6,2,9,0]
    column1 = [1,3,2,1]
    d = dotProduct(row1,column1)
    print d
    row2 = [6,2,9,0]
    column2 = [3,2,1]
    d = dotProduct(row2,column2)
    print d
    m1 = [[7,8,-2],[4,2,5]]
    m2 = [[9,0],[3,7],[-2,10]]
    m3 = multiplyMatrices(m1,m2)
    print m3
    m1 = [[9,10],[6,3],[10,4]]
    m2 = [[7,0,4],[5,4,1]]
    m3 = multiplyMatrices(m1,m2)
    print m3
    m1 = [[3,2,8]]
    m2 = [[0,-1,-1],[4,-3,8],[-3,-3,2]]
    m3 = multiplyMatrices(m1,m2)
    print m3
