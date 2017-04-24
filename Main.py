# coding: utf-8
# # Machine learn from more than one input using decision trees
# Machine Learning using clothes and cushions.

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [('100 dress green', 'like'),('50 shirt blue','dislike')]
cl = NaiveBayesClassifier(train)
print(cl.classify("green"))  

# As it's naive bayes it's not connecting the pieces together. It's taking everything individually.For example you may only dislike the dress because it's green, not because it's £100 or because it's a dress. 

#Decision tree 
import pandas as pd
data = pd.DataFrame()
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(['dress','skirt','shirt','multi word sentance'])
data['Type'] = le.transform(['dress','skirt','dress','multi word sentance']) 
test = le.transform(['skirt']) 
preference = le.fit(['like', 'dislike'])
data['Result'] = le.transform(['like', 'dislike','like','dislike']) 

# This doesn't handle paragraphs of words very well. 

from sklearn import tree
#X = [[100, 'dress'], [50, 'skirt']]
data['Cost'] = [100 , 50, 75, 35]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(data[['Cost','Type']],data['Result'])

result = clf.predict([[100, test]])

#need to do a little more to handle categorical data. Need to convert the categorical data into
#so the algorith can still work. 

list(le.inverse_transform([result]))

#Now do something similar for Cushions. Look how to get data from the internet to do this.
    
from lxml import html
import requests

#input variable is the webpage

webpage_choice = ['https://www.johnlewis.com/scion-sula-cushion/p3204660?colour=Multi#media-overlay_show',
                 'https://www.johnlewis.com/sanderson-dandelion-clocks-cushion/p1966026?colour=Natural',
                 'https://www.johnlewis.com/scion-mr-fox-cushion/p1966025?colour=Steel',
                 'https://www.johnlewis.com/voyage-blue-whale-cushion/p3086238',
                 'https://www.johnlewis.com/voyage-expressive-thistle-cushion/p2539753',
                 'https://www.johnlewis.com/john-lewis-plain-velvet-cushion/p2799405?colour=Gold'
                 ]
for i in range (0, len(webpage_choice)):
    webpage = (webpage_choice[i])
    page = requests.get(webpage)
    tree = html.fromstring(page.content)

    Name = tree.xpath('//*[@id="prod-title"]/span/text()')
    print(Name)    
    Description = tree.xpath('//*[@id="tabinfo-care-info"]/span/p/text()') 
    if not Description:
        Description = tree.xpath('//*[@id="tabinfo-care-info"]/span/text()') 
        if not Description:
            Description = tree.xpath('//*[@id="tabinfo-care-info"]/span/div[1]/text()') 
          
    print(Description)    
    Price= tree.xpath('//*[@id="prod-add-to-basket"]/div[2]/div/ul/li/strong[2]/text()')    
    #print(Price)    

#Now extract the number and use  to get the image
webpage_num = int(filter(str.isdigit, webpage_choice[3]))
print(webpage_num)

#Get image - unfortunaltly the numbers are different so i can't get  the right one image from the main page link. 

import urllib
urllib.urlretrieve("https://johnlewis.scene7.com/is/image/JohnLewis/000271594?$prod_main$" , "Cushion.jpg")
from IPython.display import Image
Image("Cushion.jpg")

# developed what I wanted from this exercise. Worth moving to something else. 
