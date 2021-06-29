import timeit
import logging
import Arithmetics
import Test_Arithmetics
import Test
import time

def PrintName():
   print("Hello, Payal here!!")
   print("End of PrintName Function execution ")

def LeapYear(year,four):
   return (year%four)

def test_example():
   assert LeapYear(2016,4) == 0

if __name__ == '__main__':
   test_example()
   Test_Arithmetics.Test_Arithmetics().run_test()
   Test.Testing().run_test()
   PrintName();
   start_time = timeit.default_timer()
   print(f'PrintName Function Time: {timeit.default_timer() - start_time}')
   start_time = timeit.default_timer()
   LeapYear(2016,4)
   print(f'LeapYear Function Time: {timeit.default_timer() - start_time}')
