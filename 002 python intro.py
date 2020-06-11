#!/usr/bin/env python
# coding: utf-8

# # Variables 

# In[131]:


myAge = 22


# In[132]:


print(myAge)


# In[133]:


myAge = myAge + 1


# In[134]:


print (myAge)


# In[135]:


#challenge 
# 1) create a variable called 'restauran Bill' and set its value to 36.17
# 2) create a variable called 'serviceCharge' and set its value to 0.125
# 3) print out the amount of tip


# In[136]:


restaurantBill = 36.17
serviceCharge = 0.125
print(restaurantBill * serviceCharge)


# In[137]:


primeNumbers = [3, 7, 61, 29, 199]
type(primeNumbers)


# In[138]:


name = [1, "hello", 2, "me"]


# In[139]:


print (name[1])


# In[140]:


import pandas as pd
data = pd.read_csv('lsd_math_score.csv')


# In[141]:


print(data)


# In[142]:


type(data)


# In[143]:


onlyMathScores=data['Avg_Math_Test_Score']


# In[144]:


print(onlyMathScores)


# In[145]:


data["Test_subject"] = "jennifer Lopez"


# In[146]:


data


# In[147]:


data['High_Score'] =100


# In[148]:


data['High_Score'] = data['High_Score'] + data['Avg_Math_Test_Score']


# In[149]:


print (data)


# In[150]:


data['High_Score'] = data['High_Score'] * data['High_Score']


# In[151]:


print(data)


# In[152]:


print(onlyMathScores)


# In[153]:


type(onlyMathScores)


# In[154]:


columnList = data[['LSD_ppm', 'Avg_Math_Test_Score']]


# In[155]:


print(columnList)


# In[156]:


cleanData = columnList
print(cleanData)


# In[157]:


type(cleanData)


# In[158]:


y = data[['Avg_Math_Test_Score']]

X = data[['LSD_ppm']]


# In[159]:


type(y)


# In[160]:


type(X)


# In[161]:


del data['Test_subject']


# In[162]:


print(data)


# In[163]:


del data['High_Score']


# In[164]:


print (data)


# In[172]:


from sklearn.linear_model import LinearRegression


import life as hitchhikersGuide
import math


# In[173]:


type(hitchhikersGuide)


# In[174]:


hitchhikersGuide.theAnswer


# In[175]:


math.pi


# 

# In[176]:


math.e


# In[177]:


import matplotlib.pyplot as plt

from sklearn.liear_mode import linearRegression


# #  Function

# In[178]:


def get_milk():
    print('open door')
    print('walk to the store')
    print('Buy milk on the ground floor')
    print('Return with milk galore')


# In[179]:


get_milk()


# In[180]:


def fill_the_fridge(amount):
    print('open door')
    print('walk to the store')
    print('Buy ' + amount +' cartons on the ground floor')
    print('Return with milk galore')


# In[181]:


fill_the_fridge('five')


# In[182]:


fill_the_fridge('one thousand')


# In[183]:


def get_milk(money):
    litres = money / 1.5


# In[184]:


get_milk(200)


# In[185]:


def milk_mission(amount, destination):
    print('open door')
    print('walk to the ' + destination)
    print('Buy ' + amount +' cartons on the ground floor')
    print('Return with milk galore')


# In[186]:


milk_mission(amount='twenty', destination='department store')


# In[187]:


def get_milk(money):
    litres = money / 2
    return litres


# In[188]:


amount = get_milk(200)


# In[189]:


print(amount)


# In[190]:


def multiply(a, b):
    return a * b
#     return multiply


def addition(a, b):
    addition = a + b
    return addition


# In[191]:


test = multiply(3.14, 5.09)

print(test)


# In[192]:


addition(2, 1)


# In[193]:


import this


# In[194]:


hitchhikersGuide.quote_marvin()


# In[195]:


results = hitchhikersGuide.square_root(63.14)
print(results)


# In[196]:


def multiply(a, b):
    return a * b

multiply(h1)
# In[202]:


time = data[['Time_Delay_in_Minutes']]
LSD = data[['LSD_ppm']]
score = data[['Avg_Math_Test_Score']]


# In[203]:


get_ipython().run_line_magic('matplotlib', 'inline')

plt.plot(time, LSD, color='g', linewidth = 3)
plt.title('Tissue concetration of LSD over time', fontsize=17)
plt.xlabel('Time in minutes', fontsize=14)
plt.ylabel('Tissue LSD ppm', fontsize=14)
plt.text(x=0, y=-1, s='Wagener et al. (1968)', fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.style.use('classic')

plt.ylim(1, 8)
plt.xlim(0, 500)

plt.show()


# In[240]:


regr = LinearRegression()
regr.fit(LSD, score)
print ('Theta1:', regr.coef_[0][0])
print( 'Intercept', regr.intercept_[0])

print('R-square:',regr.score(LSD, score))

predicted_score = regr.predict(LSD)


# In[243]:


get_ipython().run_line_magic('matplotlib', 'inline')

plt.scatter(LSD, score, color='blue', s=100, alpha=0.7)
plt.title('Arithmetic vs LSD-25', fontsize=17)
plt.xlabel('Tissue LSD ppm', fontsize=14)
plt.ylabel('Performance score', fontsize=14)
plt.ylim(25,85)
plt.xlim(1,6.5)
plt.style.use('fivethirtyeight')
plt.plot(LSD, predicted_score, color='red', linewidth=3)

plt.show()



# In[ ]:




