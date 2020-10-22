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

    EDA of anon.ipynb (Incomplete - currently uses anon1)

        -small amount of EDA on bank dataset
  
        -mostly looking at balance, days past due, and credit risk code

    Merge.ipynb (Incomplete)
        -merge of metrics with anon
        -errors
        
    national.xlsx
    
        -Sheet 1 of Metrics.xlsx with modifications:
            1) Took out dates past Q4 2021
            2) Inserted real data in for Q1,Q2 2020 (some are missing)
