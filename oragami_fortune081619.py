# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:41:15 2019

@author: Owner
"""

#replicate an oragami fortune teller

#ask individuals to pick a color on the outside of the fortune teller
color_pick=input("Pick one of these colors: red, blue, green, yellow, pink, purple, white, black. ")

#then ask what number they will pick based on their initial answer
if color_pick=="red" or color_pick=="green" or color_pick=="pink" or color_pick=="white":

  #this is indented because it falls under the if statement
  numb_pick=input("Pick from the following numbers: 1, 3, 5, and 7. ")

  #give fortune based on number
  if numb_pick=="1" or numb_pick=="3":
    #this is double indented
    print("You will be rich!")

  #this is unindented
  if numb_pick=="5" or numb_pick=="7":
    print("You will win the lottery soon.")

#this is unidented back to the margin
if color_pick=="blue" or color_pick=="yellow" or color_pick=="purple" or color_pick=="black":

  #this is indented
  numb_pick=input("Pick from the following numbers: 2, 4, 6, and 8. ")
  if numb_pick=="2" or numb_pick=="4":
    
   #this is double indented
    print("You will have your own TV show.")

  if numb_pick=="6" or numb_pick=="8":
    print("You will find a pot of gold.")
