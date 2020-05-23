# Text mining hw 7
## Text Classification  

We us the spacy package to lemmatize and select token based on POS. Then, we have 2 data frames to do some analysis: 

(a) The original one: amazon_reviewDF 
(b) The data after lemmatization, pos: amazon_reviewDF_lem_pos 

**1. Test 1: Does using lemmatization and POS selection give a better result?**

Yes, as Table 1 shows, even though the improvement is less, which still results in a relative gain of 0.9% and 1% for accuracy and F-score. There are 9 data correctly classified. It is convincing that using lemmatization and POS selection gives a better result. 
![](https://i.imgur.com/vV9SBWg.png)

**2. Test 2: if we limit the max_fetaure, does it affect the model performance?**

The data with Lemmatization & POS performs better, so we are going to use this model for the Test 2 experiments. The results list in Table 2. When the max_feature is set 4300, it achieves the best accuracy of 72.9%. We also observe that the positive category in max_feature = 5000 performs well. 

![](https://i.imgur.com/mclQaY9.png)

**3. Text 3: use different classification algorithm:**
We continuously follow the setting in Test 1 and Test 2 that the max_feature setting of the data with lemmatization and POS is 4300. And we chose some different classification algorithm to implement. The Table 3 summarizes our experimental results. 
![](https://i.imgur.com/z1Zpl4Z.png)

**4. Conclusion**
As Table 3 shows, the Neural Network with our setting outperforms all comparison models. Several notable observations can be made. First, the performance ranks are: 
* a. Neural Network Multi-Layer Perceptron with parameters tuning. 
* b. Logistic 
* c. Adaboost 
* d. Random Forest 
* e. Neural Network Multi-Layer Perceptron original 
* f. Decision Tree 

Second, we further inspect the setting of the best model – Neural Network Multi-Layer Perceptron with parameters tuning. There are several parameters: the activation is Relu, and the size of neurons in the hidden layers are [50, 50]. The max iteration is set 10. Learning rate is 0.001. The result shows that the loss decreases from 0.694 to 0.335. This also demonstrates our model can outperform other comparison methods. 
 