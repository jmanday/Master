#Vamos a tratar de predecir la variable impago de bankloan a trav?s de regrrsi?n logistica.
#utilizaremos los datos finanacieros, es decir ingresos y deudas.
#Puesto que se trata de predecir una clase genero entrenamiento y test
library("dplyr", lib.loc="C:/Program Files/R/R-3.1.2/library")
dato=filter(bankloan,is.na(bankloan$impago)==FALSE)
# Genero conjunto de entrenamiento y conjunto de test.
#Hago muestreo aleatorio mediante la generaci?n de dos particiones al 70% y 30% de los datos
ind=sample(2,nrow(dato),replace=TRUE,prob=c(0.7,0.3))
entrena=dato[ind==1,]
test=dato[ind==2,]
modelo=impago~ingresos+deudaingr+deudacred+deudaotro
#modelo=impago~ingresos+deudacred
resul=glm(modelo,family=binomial(link="logit"),entrena)
summary(resul)
factsl=factor(cut(predict(resul,type="response"),breaks=c(0,0.50,1.0)))
table(factsl,entrena$impago)
#Ver que pasa con los test 
testpred=factor(cut(predict(resul,test,type="response"),breaks=c(0,0.50,1.0)))
tt=table(testpred,test$impago)
tt
#calculo de las medidas de calidad para prediccion
#Porcentaje de bien clasificados y de error
#Genero el vector diagonal y lo sumo
dd=diag(tt)
bien=sum(dd)
bien_clasificados=(bien/nrow(test))*100
#Bien y mal clasificados
bien_clasificados
100-bien_clasificados
#Precision, Recall y F-measure
ft=0 
m=c(1:nrow(tt))
n=m
prec=n
rec=m
fmes=m
for(i in 1:nrow(tt)){m[i]=sum(tt[i,])}
for(i in 1:nrow(tt)){n[i]=sum(tt[,i])}
for(i in 1:nrow(tt)){prec[i]=dd[i]/m[i]}
for(i in 1:nrow(tt)){rec[i]=dd[i]/n[i]} 
for(i in 1:nrow(tt)){fmes[i]=2*dd[i]/(m[i]+n[i])}
ft=0
for(i in 1:nrow(tt)){ft=ft+(fmes[i]/nrow(tt))}
#Precision
prec

#Recall
rec
#F-measure
fmes
#F-measure total
ft
#Calculo de loas curvas ROC
library("ROCR", lib.loc="C:/Program Files/R/R-3.1.2/library")
m=predict(resul,newdata=test,type="response")
pred=prediction(m,test$impago)
perf=performance(pred,"tpr","fpr")
plot(perf, main="Regresion Logistica") 
