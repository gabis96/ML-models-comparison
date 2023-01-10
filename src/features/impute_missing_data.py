import pandas as pd
from sklearn.impute import KNNImputer

def impute_poc(df):
    '''Imputes Perception of Corruption one missing data'''
    m = df[df.Country=='United Arab Emirates'].mean()
    df[df['Perceptions of corruption'].isna()] = m

def impute_with_knn(df):
    '''Imputes dataset in 'Social support' & 'Dystopia Residual' using KNN imputer '''
    # Apply label encoding for column Country with .cat.codes
    df_le = df.copy()
    df_le['Country'] = df_le['Country'].astype('category').cat.codes
    
    knn = KNNImputer()
    df[['Social support', 'Dystopia Residual']] = pd.DataFrame(knn.fit_transform(df_le)[:, [9,10]], columns=['Social support', 'Dystopia Residual'])

