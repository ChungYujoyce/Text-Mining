## Text mining hw 6
### Simple Movies Recommend System 

1. We choose “encourage wise hope” to be the query text. 

2. Implement the information retrieval without feature selection and find out the top 10 movies. We can observe that the Eternal (2004) and Dangal (2016) are significantly similar with the query text. 

![](https://i.imgur.com/SdLMd2k.png)

3. Run the Information Retrieval code again with feature selection and find out the top 10 movies. The numbers of the features are set 1500. We can observe that only 50% of the top 10 movies are the same as the result without feature selection. Especially, the second highest movie was not included in the previous result. 

![](https://i.imgur.com/cgIeUwA.png)


 4. Refection and discussion:
     We also tried to do the feature selection with 5000 features and do the information retrieval code again to get the result. There are some comparison with the 2 results: 
     * Speed
      In feature selection case, it just spent 5.19sec to finish the procedure. But in without feature selection case, the procedure needs 37.44 sec to be done. Discuss in depth, if we choose more features, it spent more time. This process (1500 features selection) only takes 5 seconds, while the process (5000 features selection) needs to be increased to 15.42 seconds to complete. More time-consuming details are shown as below. 
      ![](https://i.imgur.com/G9jspyC.png)
      * The number of features 
      Roughly speaking, the first 8 movies with function selection are the same, although the similarity values are different. We can say that the results are not much different. We think as long as we do the feature selection, we can find important information, so the results will be similar. 
      ![](https://i.imgur.com/LeiYMQD.png)


