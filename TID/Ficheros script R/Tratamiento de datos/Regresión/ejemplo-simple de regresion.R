iris2=iris[,1:4]
library("stats", lib.loc="C:/Program Files/R/R-3.1.2/library")
pairs(iris2)
cor(iris2)
modelo=Petal.Length~Petal.Width
regre=lm(modelo,iris2)
summary(regre)
x=iris2$Petal.Width
y=iris2$Petal.Length
plot(x,y,xlab="Petal.Width",ylab="Petal.Length",col=2,main="Regresion Lineal")
abline(regre,col=3)
#Vamos ahora a predecir Sepal.width en funcion de las otras dos variables.
model= Sepal.Width~Petal.Length+Petal.Width
regr=lm(model,iris2)
summary(regr)
coef(regr)
x=iris2$Petal.Width
y=iris2$Sepal.Width
plot(x,y,xlab="Petal.Width",ylab="Sepal.Width",col=2,main="Regresion Lineal 2 variables")
abline(coef(regr)[1],coef(regr)[3],col=4)
x=iris2$Petal.Length
y=iris2$Sepal.Width
plot(x,y,xlab="Petal.Length",ylab="Sepal.Width",col=2,main="Regresion Lineal 2 variables")
abline(regr,col=4)
#Analicemos si predicen mejor por separado, probamos dos modelos independientes
model= Sepal.Width~Petal.Width
regr=lm(model,iris2)
summary(regr)
x=iris2$Petal.Width
y=iris2$Sepal.Width
plot(x,y,xlab="Petal.Width",ylab="Sepal.Width",col=2,main="Regresion Lineal 1 variable")
abline(regr,col=4)
model= Sepal.Width~Petal.Length
regr=lm(model,iris2)
summary(regr)
x=iris2$Petal.Length
y=iris2$Sepal.Width
plot(x,y,xlab="Petal.length",ylab="Sepal.Width",col=2,main="Regresion Lineal 1 variable")
abline(regr,col=4)
#Vemos que no van mejor
 
