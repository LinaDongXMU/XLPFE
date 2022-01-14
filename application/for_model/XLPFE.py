import pandas as pd

data_train=pd.read_csv("./train.csv")
x_train=data_train[["VDW","HB","HP","HM","HS","RT","q","C","N","O","H","F","P","S","Cl","Br","I","1","2","3","am","ar","his","arg","lys","ile","phe","leu","trp","ala","met","pro","val","cys","asn","gly","ser","gln","tyr","thr","asp","glu","hoh","phis","parg","plys","pile","pphe","pleu","ptrp","pala","pmet","ppro","pval","pcys","pasn","pgly","pser","pgln","ptyr","pthr","pasp","pglu"]]
y_train=data_train["exp"]

data_test=pd.read_csv("./test.csv")
x_test=data_test[["VDW","HB","HP","HM","HS","RT","q","C","N","O","H","F","P","S","Cl","Br","I","1","2","3","am","ar","his","arg","lys","ile","phe","leu","trp","ala","met","pro","val","cys","asn","gly","ser","gln","tyr","thr","asp","glu","hoh","phis","parg","plys","pile","pphe","pleu","ptrp","pala","pmet","ppro","pval","pcys","pasn","pgly","pser","pgln","ptyr","pthr","pasp","pglu"]]

from sklearn.preprocessing import StandardScaler

transfer=StandardScaler()
x_trains=transfer.fit_transform(x_train)
x_tests=transfer.fit_transform(x_test)

import numpy as np
from sklearn.metrics import mean_squared_error
from scipy.stats import pearsonr
from sklearn.model_selection import GridSearchCV

from sklearn.ensemble import ExtraTreesRegressor

et=ExtraTreesRegressor()
# param={"n_estimators":[50,100,150,200,250,300,350,400,450,500,550,600],"random_state":[np.random.RandomState(1)]}
# estimator2=GridSearchCV(et,param_grid=param,cv=5)

# estimator2.fit(x_trains,y_train)
# y_pre22=estimator2.predict(x_trains)
# MSE22=mean_squared_error(y_train,y_pre22)
# print("MSE:\n",MSE22)
# Rp22=pearsonr(y_train,y_pre22)
# print("Rp:\n",Rp22)

import joblib
# joblib.dump(estimator2,"./XLPFE.pkl")
estimator2=joblib.load("./XLPFE.pkl")

y_pre2222=estimator2.predict(x_tests)
data_test["Pre"]=y_pre2222
data_test.to_csv("./results.csv")