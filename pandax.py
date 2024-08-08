import pandas as pd
import sys



# df = pd.read_csv('survey.csv')




# print (df.shape)
# print (df.info())

# print (df.head())


people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)

print (df["email"])
print (df[["first","last"]])


print(df.columns)

print (df.iloc[[0,1]])























