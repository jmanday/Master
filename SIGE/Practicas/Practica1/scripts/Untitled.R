# Leer datos
adult.training.full <- read.csv("adult.training.csv", header = TRUE, sep = ",")
adult.test <- read.csv("adult.test.csv", header = TRUE, sep = ",")
adult.training <- head(adult.training.full, n = 5000)

# Pre-procesamiento
# -- valores perdidos
adult.training[adult.training == '?'] <- NA
library(mice)
imp <- mice(data = adult.training, method = c("", "polyreg", "", "", "", "", "cart", "", "", "", "", "", "", "sample", ""), m = 3)

# -- ruido de clase, se aplica la función ENN indicando que columna se cree que tiene ruido y que columnas se utilizan para detectarlo
library(NoiseFiltersR)
training_withNoise <- complete(imp)
noise_filter <- ENN(Class ~ ., data = training_withNoise, k = 5)
training_withoutNoise <- noise_filter$cleanData

# -- create subgrupos para entrenamiento, crea 5 subconjuntos con los valores por defecto de cross-validation aunque solo cojo uno
library(caret)
folds <- createFolds(training_withoutNoise$Class, 5)
training_fold <- training_withoutNoise[folds[[1]],]

# Árbol de decisión con rpart (usaremos training_withoutNoise, en lugar de folds), lo empleamos para conocer las variables que serán mas representativas para la clasificacion
training <- training_withoutNoise
library(rpart)
rpart1 <- rpart(Class ~ ., data = training, control = rpart.control(maxdepth = 3))
library(partykit)
rpart1a <- as.party(rpart1)
plot(rpart1a)
rpartFull <- rpart(Class ~ ., data = adult.training.full)
rpartFulla <- as.party(rpartFull)
plot(rpartFulla)
rpartPred <- predict(rpartFull, adult.test, type = "class")
confusionMatrix(rpartPred, adult.test$Class)

# Árbol de decisión con caret
cvCtrl <- trainControl(method = "repeatedcv", repeats = 3,
                       summaryFunction = twoClassSummary,
                       classProbs = TRUE)
set.seed(1)

# -- cambiar nombres de columns (caracteres >, <= son problemáticos)
training$Class <- as.character(training$Class)
training$Class[training$Class == ">50K"] <- "More50K"
training$Class[training$Class == "<=50K"] <- "Less50K"
training$Class <- as.factor(training$Class)

adult.test$Class <- as.character(adult.test$Class)
adult.test$Class[adult.test$Class == ">50K"] <- "More50K"
adult.test$Class[adult.test$Class == "<=50K"] <- "Less50K"
adult.test$Class <- as.factor(adult.test$Class)

rpartTune <- train(Class ~ ., 
                   data = training, 
                   method = "rpart",
                   tuneLength = 30,
                   metric = "ROC",
                   trControl = cvCtrl)
plot.train(rpartTune, scales = list(x = list(log = 10)))
plot(rpartTune$finalModel)
library(rattle)
fancyRpartPlot(rpartTune$finalModel)

rpartTune_pred1 <- predict.train(rpartTune, adult.test, type = "raw")
confusionMatrix(rpartTune_pred1, adult.test$Class)

rpartTune_pred2 <- predict.train(rpartTune, adult.test, type = "prob")
library(pROC)
rpartROC <- roc(adult.test$Class, rpartTune_pred2[, "Less50K"], levels = unique(adult.test$Class))
plot(rpartROC, type = "S" , print.thres = 0.9) # formato: http://web.expasy.org/pROC/

# Sub-sampling
down_train <- downSample(training, training$Class)
table(down_train$Class)

up_train <- upSample(training, training$Class)
table(up_train$Class)

library(DMwR)
smote_train <- SMOTE(Class ~ ., data  = training)  
table(smote_train$Class) 

ctrl <- trainControl(method = "repeatedcv", repeats = 5,
                     classProbs = TRUE,
                     summaryFunction = twoClassSummary)

set.seed(1)
orig_fit <- train(Class ~ ., data = training, 
                  method = "treebag",
                  nbagg = 50,
                  metric = "ROC",
                  trControl = ctrl)

# continuar probando modelos con diferentes métodos para balancer clases
# (ver ejemplo: http://topepo.github.io/caret/subsampling-for-class-imbalances.html)
# (para Titanic con regresión logística: https://www.r-bloggers.com/illustrated-guide-to-roc-and-auc/)
