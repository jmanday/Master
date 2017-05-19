# Leer datos
adult.training <- read.csv("adult.training.csv", header = TRUE, sep = ",")
adult.test <- read.csv("adult.test.csv", header = TRUE, sep = ",")

# Reemplazar valores '?' por NA
adult.training[adult.training == '?'] <- NA

# Reducir el tamaño del dataset
adult.training <- head(adult.training, n = 500)

# Listar número de valores perdidos, según combinaciones de variables
require(mice)
md.pattern(adult.training)

# Listar número de valores perdidos, por pares de variables
md.pairs(adult.training)

# Visualizar datasets con valores perdidos con paquete VIM
require(VIM)
aggr(adult.training, col=c('navyblue','red'), numbers=TRUE, sortVars=TRUE, labels=names(adult.training), cex.axis=.7, gap=3, ylab=c("Histogram of missing data", "Pattern"))
marginplot(adult.training[,c("Workclass","Native.country")], col=c("blue","red","orange"), cex=1.5, cex.lab=1.5, cex.numbers=1.3, pch=19)
pbox(adult.training, pos=1, int=FALSE, cex=1.2)

# Realizar imputación de valores perdidos, 
# Por defecto: predictive mean matching (pmm), m = 5 (número de imputaciones)
# En el dataset, hay valores perdidos en Native.country, Workclass, Occupation
# imp <- mice(adult.training)
imp <- mice(data = adult.training, method = c("", "polyreg", "", "", "", "", "cart", "", "", "", "", "", "", "sample", ""), m = 3)
str(imp)

# Analizar datasets con valores imputados
complete(imp)   # complete(imp, 2)
require(lattice)
plot(imp)
xyplot(imp, Workclass ~ Age + Marital.status)
stripplot(imp, pch = 20, cex = 1.2)

# Especificar predictores
pred <- imp$predictorMatrix
pred[,"Age"] <- 0
pred[2, 1] <- 0
# imp <- mice(adult.training, predictorMatrix = pred)

# Recomendaciones: reducir variables con muchas categorías, estudiar correlaciones
quickpred(adult.training)

# Usar datasets con conjuntos imputados
# -- usando un dataset con imputaciones cualquiera
require(caret)
training <- complete(imp)
rf_1 <- caret::train(Class ~ . , data = training, method = "rf")
training <- complete(imp, 2)
rf_2 <- caret::train(Class ~ . , data = training, method = "rf")
training <- complete(imp, 3)
rf_3 <- caret::train(Class ~ . , data = training, method = "rf")
training <- adult.training[apply(adult.training, 1, function(row) !any (row %in% c(NA))), ]
rf <- caret::train(Class ~ . , data = training, method = "rf")

predictions1 <- predict(rf1, newdata = adult.test)
predictions2 <- predict(rf2, newdata = adult.test)
predictions3 <- predict(rf3, newdata = adult.test)
predictions4 <- predict(rf4, newdata = adult.test)
write.csv(predictions1, file = "predictions1.csv")
write.csv(predictions2, file = "predictions2.csv")
write.csv(predictions3, file = "predictions3.csv")
write.csv(predictions4, file = "predictions4.csv")
write.csv(predictions, file = "predictions.csv")

