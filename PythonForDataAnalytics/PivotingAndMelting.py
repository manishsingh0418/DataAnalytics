import pandas as pd

#Pivoting

# dict ={"keys":["k1","k2","k1","k2"],
#        "Names":["John","Ben","David","Pater"],
#        "Houses":["red","blue","green","red"],
#        "Grades":["3rd","8th","9th","8th"]}
#
# df=pd.DataFrame(dict)
# print(df)
# print(df.pivot(index="keys",columns="Names",values=["Houses","Grades" ]))

#Melting

dict ={"keys":["k1","k2","k1","k2"],
       "Names":["John","Ben","David","Pater"],
       "Houses":["red","blue","green","red"],
       "Grades":["3rd","8th","9th","8th"]}

df=pd.DataFrame(dict)
print(df)
print(pd.melt(df,id_vars=["Names"],value_vars=["Houses"]))