'''
Assignment #6

1. Add / modify code ONLY between the marked areas (i.e. "Place code below") 
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 06_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
7. Make sure your work is committed to your master branch


'''

import numpy as np, pandas as pd, matplotlib.pyplot as plt
import unittest
import requests

# ------ Place code below here \/ \/ \/ ------
# import plotly library and enter credential info here


# ------ Place code above here /\ /\ /\ ------

def exercise01():
    '''
    Create a DataFrame df with 4 columns and 3 rows of data in one line of code. The data can be arbitrary integers.
    For example
    
               0  1  2   3
            0  1  2  3   4
            1  5  6  7   8
            2  7  8  9  10

    '''

    # ------ Place code below here \/ \/ \/ ------
 

    # ------ Place code above here /\ /\ /\ ------

    return df

def exercise02(a):
    # The function exercise02() receives a Python list and converts it to an ndarray. Convert the list to a numpy ndarray called array.

    # ------ Place code below here \/ \/ \/ ------


    # ------ Place code above here /\ /\ /\ ------

    return array

def exercise03(a):
    # The function exercise03() receives an ndarray of integers. Return the sum of those integers using NumPy.

    # ------ Place code below here \/ \/ \/ ------


    # ------ Place code above here /\ /\ /\ ------
    return sum

def exercise04(a):
    # The function exercise04() receives an ndarray matrix (2D) of integers. Return the sum of the 2nd column using NumPy.

    # ------ Place code below here \/ \/ \/ ------


    # ------ Place code above here /\ /\ /\ ------
    return sum

def exercise05(n):
    # The function exercise05() receives an integer n. Return an ndarray filled with zeros of size n x n (n rows, n columns)

    # ------ Place code below here \/ \/ \/ ------


    # ------ Place code above here /\ /\ /\ ------
    return zeros

def exercise06(n):
    # The function exercise06() receives an integer n. Return an ndarray filled with ones of size n x n (n rows, n columns)

    # ------ Place code below here \/ \/ \/ ------



    # ------ Place code above here /\ /\ /\ ------
    return ones

def exercise07(sd,m,s):
    # The function exercise07() receives integers sd, m, s which are standard deviation, mean and size respectively. 
    # Return an ndarray filled with s random numbers conforming to a normal distribution of standard deviation = sd and mean = m

    # ------ Place code below here \/ \/ \/ ------


    # ------ Place code above here /\ /\ /\ ------
    return random_numbers

def exercise08():
    '''
    Load the CSV data from http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv into a DataFrame
    # Return the following items:
    - row_count - Total # of rows
    - avg_sq_ft - Average square feet across all transactions
    - df_zip_95670 - DataFrame containing all transactions in zip code 95670
    - df_zip_not_95610 - DataFrame containing all transactions not in zip code 95610
    '''

    # ------ Place code below here \/ \/ \/ ------


    # ------ Place code above here /\ /\ /\ ------

    return df, row_count, avg_sq_ft, df_zip_95670, df_zip_not_95610

def exercise09():
    '''
    Load historical Bitcoin prices that are in JSON format from https://api.coindesk.com/v1/bpi/historical/close.json using
    start date 9/1/2017 and end date 10/5/2018. Documentation on the API is here: https://www.coindesk.com/api/
    Note: You may need to use the requests library and header spoofing to grab the data and then giving it to a DataFrame 

    With the prices loaded into the DataFrame:

    - Drop the disclaimer column
    - Remove the bottom two rows
    - Plot a price timeseries and publish it to Plotly using the Plotly API and set the URL to the chart to the plotly_url variable.
    Publication to Plotly will occur programmtically via plotly API. You will need to import the library and create an API key from
    the plotly dashboard.
    - Print the head
    - Print the tail

    '''
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    # ------ Place code below here \/ \/ \/ ------



    # ------ Place code above here /\ /\ /\ ------    
    return df, plotly_url


def exercise10(n):
    # Create a numpy identity matrix of size n
    # ------ Place code below here \/ \/ \/ ------


    # ------ Place code above here /\ /\ /\ ------  
    return identity_matrix

def exercise11(n):
    '''
    Using NumPy, create a single dimension array, array_1d, of size n containing integers 0 to n-1
    Reshape the array. The reshaped array, array_reshaped, should be n/3 columns and 3 rows
    '''
    # ------ Place code below here \/ \/ \/ ------



    # ------ Place code above here /\ /\ /\ ------  
    return array_1d, array_reshaped

def exercise12(n):
    '''
    Create a checkerboard NumPy matrix of size 2n x 2n using one line of code
    A checkerboard matrix is a matrix with alternating 1s and 0s across rows and columns with the top left value equal to 1
    '''
    # ------ Place code below here \/ \/ \/ ------



    # ------ Place code above here /\ /\ /\ ------ 

    return checkerboard_matrix

def exercise13(n):
    '''
    Create a pandas Series, s, with n random integers between 0 and n, for n days starting from 1/1/2010 and plot the
    cumulative sum on a  chart. The data range should be an index.
    
    '''
    # ------ Place code below here \/ \/ \/ ------

   

    # ------ Place code above here /\ /\ /\ ------ 
    return s


def exercise14(words):
    '''
    Exercise14() receives a Python list of words. Create and return a pandas DataFrame or Series that tabulates the length of 
    each word i.e. a list of the words hello, car, bye would produce a DataFrame with 3 rows and a column with the numbers 5,3,3
    Using Series.map() and lambdas may help.
    '''
    # ------ Place code below here \/ \/ \/ ------

   

    # ------ Place code above here /\ /\ /\ ------ 
    return df


def exercise15():
    '''
    Use the real estate transaction DataFrame from Exercise 8 and extract into a new DataFrame every 5th row using iloc 
    and just the street address and zip code columns. This can be done with one line of code.
    '''
    # ------ Place code below here \/ \/ \/ ------



    # ------ Place code above here /\ /\ /\ ------ 
    return df


class TestAssignment6(unittest.TestCase):
    def test_exercise15(self):
        print('Skipping exercise 15')
        df = exercise15()
        print(df)
    
    def test_exercise14(self):
        print('Skipping exercise 14')
        df = exercise14(['cat','frog','walrus','antelope'])
        print(df)

    def test_exercise13(self):
        print('Testing exercise 13')
        s= exercise13(1000)
        self.assertEqual(s.index[0],pd.Timestamp('2010-01-01 00:00:00'))
        self.assertEqual(len(s.index),1000)

    def test_exercise12(self):
        print('Testing exercise 12')
        cm = exercise12(10)
        self.assertEqual(cm.shape[0],20)
        self.assertEqual(cm[0,0],1)
        self.assertEqual(cm[0,1],0)
        cm = exercise12(5)
        self.assertEqual(cm.shape[0],10)
        self.assertEqual(cm[0,0],1)
        self.assertEqual(cm[0,1],0)        


    def test_exercise11(self):
        print('Testing exercise 11')
        a1d, ar = exercise11(15)
        self.assertEqual(a1d.shape[0],15)
        self.assertEqual(ar.shape[0],3)
        self.assertEqual(ar.shape[1],5)

    def test_exercise10(self):
        print('Testing exercise 10')
        im = exercise10(10)
        self.assertEqual(im.shape[0],10)
        self.assertEqual(im.shape[1],10)

    def test_exercise09(self):
        print('Skipping exercise 9')
        exercise09()
        

    def test_exercise08(self):
        print('Testing exercise 8')
        df, row_count, avg_sq_ft, df_zip_95670, df_zip_not_95610 = exercise08()
        self.assertEqual(df.shape[0],985)
        self.assertEqual(df.shape[1],12)
        self.assertEqual(row_count,985)
        self.assertAlmostEqual(avg_sq_ft,1314.91675127,2)
        self.assertEqual(df_zip_95670.shape[0],21)
        self.assertEqual(df_zip_not_95610.shape[0],978)
 
    
    def test_exercise07(self):
        print('Testing exercise 7')
        z = exercise07(10,5,100000)
        self.assertEqual(z.shape[0], 100000)
        self.assertLessEqual(np.average(z), 5.2)
        self.assertGreaterEqual(np.average(z), 4.7)
        z = exercise07(5,10,100000)
        self.assertEqual(z.shape[0], 100000)
        self.assertLessEqual(np.average(z), 10.2)
        self.assertGreaterEqual(np.average(z), 9.7)


    def test_exercise06(self):
        print('Testing exercise 6')
        z = exercise06(7).shape
        self.assertEqual(z[0], 7)
        self.assertEqual(z[1], 7)
        z = exercise05(70).shape
        self.assertEqual(z[0], 70)
        self.assertEqual(z[1], 70)
        

    def test_exercise05(self):
        print('Testing exercise 5')
        z = exercise05(7).shape
        self.assertEqual(z[0], 7)
        self.assertEqual(z[1], 7)
        z = exercise05(70).shape
        self.assertEqual(z[0], 70)
        self.assertEqual(z[1], 70)

    def test_exercise04(self):
        print('Testing exercise 4')
        array = np.array([[1,1,1,1,1],[0,2,0,0,1]])
        sum = exercise04(array)
        self.assertEqual(sum, 3)
        array = np.array([[1,6,1,1,1],[0,2,0,0,1]])
        sum = exercise04(array)
        self.assertEqual(sum, 8)

    def test_exercise03(self):
        print('Testing exercise 3')
        array = np.array([1,1,1,1,1])
        sum = exercise03(array)
        self.assertEqual(sum, 5)
        array = np.array([2,4])
        sum = exercise03(array)
        self.assertEqual(sum, 6)

    def test_exercise01(self):
        print('Testing exercise 1')
        m = exercise01().shape
        self.assertEqual(m[0], 3)
        self.assertEqual(m[1], 4)

    def test_exercise02(self):
        print('Testing exercise 2')
        m = exercise02([1,2,3,4,5,6])
        self.assertTrue(type(m) is np.ndarray)
        self.assertEqual(m.shape[0], 6)

if __name__ == '__main__':
    unittest.main()

