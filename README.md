# Loan-Project
    DSC 592 Final Project

Here is where we decsribe all of the files and its contents.

    anon.xlsx

        -original anonomyzed bank dataset
        -added column which converts date to quarter year string
  
    metrics.xlsx
  
        -original dataset containing values regarding global economy status
        -updated: according to https://www.federalreserve.gov/publications/2020-september-supervisory-scenarios.htm
            - 2020 Q1&Q2 now Historical 
            -New values for future projections 
            -updated 26Oct20

    EDA of anon.ipynb (Incomplete - currently uses anon1)

        -small amount of EDA on bank dataset
  
        -mostly looking at balance, days past due, and credit risk code

    Merge.ipynb ()
        -merge of metrics with anon (bank data)
        -results in final.csv
    
        
    national.xlsx
    
        -Sheet 1 of Metrics.xlsx with modifications:
            1) Took out dates past Q4 2021
            2) Inserted real data in for Q1,Q2 2020 (some are missing)
    final.csv
        - Fails to upload due to size
        
    Train Test Split Using Function.ipynb
    
        - Creates a train-test-split on final.csv
        - Scales numeric data
        - One-hot encodes columns of choice
        - Uses ttss.py (Have ttss.py in the same directory as this notebook)
         
    logistic regression
            -addition to train test split notebook
            -runs logistic regression
    logistic regression Risk Rating
            -runs logistic regression with Risk Rating (binned) as target
    helpers.py
            - Script with helper functions
            - Currently has:
                - tts_scale
                    - Does a train-test-split
                    - Scales numeric data
                    - One hot encodes columns, if columns are given
                    - Returns a finalized x_train, x_test, y_train, and y_test
          
    Decision Tree has: 
        - Decision Tree
        - Decision Tree with Bagging 
        - Random Forest
        - Random Forest AdaBoost
        - Linear Discriminant Analysis 
    
    Clustering of Credit Risk Code.ipynb
        - Our version of calculating risk code using unsupervised methods
        - Segments 10 risk code classes to 3
        - KMeans model suggests significant updates
