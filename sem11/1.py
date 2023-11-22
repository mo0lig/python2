import pandas as pd
def show_db(db):
    print(db)
def var_zero(db):
    df = pd.DataFrame(db, columns=["years", "Age"])
    print(df)
def function(db):
    df=len(db)
    print(df)#rows
    print(db.shape)#columns
    print(db.head)#You can have a look at the first five rows with .head()
    print(db.tail)#last five rows
def info(db):
    print(db.info())
    print(db.describe())#analyzes numeric columns by default
    print(db.describe(include=object))#analyzes cloumns which type is object
def counts(db):
    print(db["player"].value_counts())
    print(db.loc[db["player"] == "Lionel Messi", "Match played"])
    print(db.loc[db["player"] == "Lionel Messi", "Goal"].max())
    print(db.loc[db["player"] == "Lionel Messi", "Goal"].min())
    print(db.loc[db["player"] == "Lionel Messi", "Goal"].agg(("min","max")))
def new(db):
    new=db[db["years"]>1999]
    print(new)
    nn=db[db["Team"].str.endswith("Milan")]
    print(nn)
    nnew=db[(db["years"]>1999) & (db["Age"]>25)]
    print(nnew)
def nn(db):
    # print(db.isnull())
    # print(db.isna())
    db["id"].fillna("No", inplace = True)
    print(db)
db=pd.read_excel(r"C:\\Users\\Админ\\OneDrive\\Документы\\python2\\python2\\sem11\\balon.xlsx")
nn(db)