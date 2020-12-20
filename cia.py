# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 13:52:30 2020

@author: konstnar
"""

from bs4 import BeautifulSoup as sp
import os,re

file = open('page.html', encoding='utf-8')
file = file.readline()

page = sp(file,'lxml')
qstn = page.findAll('div',class_ = 'freebirdFormviewerViewItemsItemItemTitle exportItemTitle freebirdCustomFont')
for q in qstn:
    print(re.sub("\s\*","",q.text))
    
#   if answer is in radio button
#   wrong answers will not be retrived  (have to add manually)
ans = page.findAll(['label','span'],class_ = 'docssharedWizToggleLabeledContainer freebirdFormviewerViewItemsRadioChoice freebirdLabeledControlDarkerDisabled isChecked freebirdFormviewerViewItemsRadioGraded freebirdFormviewerViewItemsRadioCorrect isDisabled')



#   if answers is in text box
#   wrong will be retrived  (change it)
ans = page.findAll(['label','span'],class_ = 'docssharedWizToggleLabeledContainer freebirdFormviewerViewItemsCheckboxContainer freebirdLabeledControlDarkerDisabled isChecked isDisabled')

for node in ans:
    print(node.find('span').text)
        
#"//label[contains(@class,'freebirdLabeledControlDarkerDisabled isChecked ')]//span"