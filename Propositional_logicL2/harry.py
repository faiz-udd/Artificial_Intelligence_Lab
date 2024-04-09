#Note: It's Code writted From CS50 lectures
from logic import * 
rain = Symbol("rain") #its raining
hagrid = Symbol("hagrid") #Harry Visited Hagrid
dumbledore = Symbol("dubmbledore") #Harry Visited dumbledore

knowledge =And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)
print(model_check(knowledge, rain))