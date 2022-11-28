import pandas as pd

def loadData(path: str) -> pd.DataFrame:
    data = pd.read_csv(path, dtype = {'Code':int,
                                       'Cause':str,
                                       'ISO3':str,
                                       'Year':int,
                                       'Sex':str,
                                       'Age Group.2':str,
                                       'Population':int,
                                       'Deaths':float,
                                       'Death rate per 100 000 population':float,
                                       'DALY':float,
                                       'DALY rate per 100 000 population':float})
    return data