from PIL import Image
import numpy as np
import pandas as pd



def pixel_df(DF_train, DF_test, L):
    for j in L:
        K = []
        Images = []
        for i in range(1,65):
#           if((j=="B01") and (i==1)):
#               f = "B01(0).pgm"
#           else:
            f = "Dataset/" + j + " (" + str(i) + ").pgm"
            im = Image.open(f)
            a = np.asarray(im)
            a = a.reshape(1,192*168)
            Images.append(a)
            a = list(a)
            K.append(sum(sum(a)))
        J = sorted(K,reverse=True)
        Index = []
        for i in range(64):
            Index.append(K.index(J[i]))
        a = len(J)//3
        b = 2*a
        c = len(J)
        for i in range(1,a+1):
            if(i<=(0.8*(a+1))):
                if(i==1):
                    df_train = pd.DataFrame(Images[Index[i-1]])
                else:
                    df_train = df_train.append(pd.DataFrame(Images[Index[i-1]]))
            else:
                if(i==18):
                    df_test = pd.DataFrame(Images[Index[i-1]])
                else:
                    df_test = df_test.append(pd.DataFrame(Images[Index[i-1]]))
        for i in range(a+1,b+1):
            if(i<=(0.8*(b+1-a) + a)):
                df_train = df_train.append(pd.DataFrame(Images[Index[i-1]]))
            else:
                df_test = df_test.append(pd.DataFrame(Images[Index[i-1]]))
        for i in range(b+1,c+1):
            if(i<=(0.8*(c+1-b) + b)):
                df_train = df_train.append(pd.DataFrame(Images[Index[i-1]]))
            else:
                df_test = df_test.append(pd.DataFrame(Images[Index[i-1]]))
        DF_train.append(df_train)
        DF_test.append(df_test)
        
        
        
L = ["B01","B02","B03","B04","B05","B06","B07","B08","B09","B10"]
DF_train = []
DF_test = []
pixel_df(DF_train,DF_test, L )



for i in range(len(DF_train)):
    if(i==0):
        A = DF_train[0]
    else:
        A = A.append(DF_train[i])
for i in range(len(DF_test)):
    if(i==0):
        Z = DF_test[0]
    else:
        Z = Z.append(DF_test[i])
        
        
Mean = A.mean()
A = (A-Mean)
Z = Z-Mean