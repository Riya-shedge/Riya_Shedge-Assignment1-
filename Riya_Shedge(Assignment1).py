#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RIYA SHEDGE
#
# Created:     03-03-2023
# Copyright:   (c) RIYA SHEDGE 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#to calculate simple interest
P=int(input("Enter principle amount:"))
T=int(input("Enter time:"))
R=int(input("Enter Rate:"))
simple_interest=P*T*R/100
print("The Simple Interest is:",simple_interest)