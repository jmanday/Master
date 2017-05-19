#Selecciono los variables numericas de iris
x=iris[,1:4]
# llamo a analisis factorial con un factor ( no ermite hacerlo con mas con solo 4 variables)
solu=factanal(x,factors=1,scores="regression")
solu
#compruebo como se comporta este factor en relación con las clases
y1=solu$scores
y2=iris$Species
h=data.frame(y1,y2)
str(h)
boxplot(h$Factor1 ~ h$y2,col=3)
#Otra funcion que hace analisis factorial (realmente componentes principales)
datos=x
sal=prcomp(datos,retX=TRUE)
sal
str(sal)
sal$x
#El numero de factores a seleccionar se ajusta mediante tol= umbral (ver descripcion de la función)
sal=prcomp(datos,retX=TRUE,tol=0.15)
sal
str(sal)
sal$x
#Como puede verse el criterios de selección no es muy claro.
 
