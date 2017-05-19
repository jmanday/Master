
# Loading training and test data
set.seed(1)
train <- read.csv("train.csv")
test <- read.csv("test.csv")

# Load requires libraries
library(ggplot2)
library(randomForest)
library(rpart)
library(rpart.plot)
library(pander)
library(caTools)
library(rattle)
library(RColorBrewer)
library(plyr)

# Converting variables as factors
train2 <- train
train2$Survived <- as.factor(train2$Survived)
train2$Pclass <- as.factor(train2$Pclass)

# Splitting training data
set.seed(1446)
split <- sample.split(train2$Survived, SplitRatio = 0.75)
sub_training_data <- subset(train2, split == TRUE)
sub_testing_data <- subset(train2, split == FALSE)

# Visualizing Data
table(train2$Sex, train2$Survived)
prop.table(table(train$Sex, train$Survived), margin = 1)
k <- ggplot(train2, aes(Survived))
k + geom_bar(aes( fill = Sex), width=.85, colour="darkgreen") + scale_fill_brewer() +
  ylab("Survival Count (Genderwise)") +
  xlab("Survived: No = 0, Yes = 1") +
  ggtitle("Titanic Disaster: Gender Vs. Survival (Training Dataset")

# Build the decision tree model
formula <- Survived ~ Sex
dtree <- rpart(formula, data=sub_training_data, method="class")

# Performance on the Training Data
dtree_tr_predict <- predict(dtree, newdata=sub_training_data, type="class")
dtree_tr_predict.t <- table(sub_training_data$Survived, dtree_tr_predict)
dtree_tr_accuracy <- (dtree_tr_predict.t[1, 1] + dtree_tr_predict.t[2, 2]) / sum(dtree_tr_predict.t)
cat("Model Accuracy on Sub sample on training data: ", dtree_tr_accuracy)

# Performance on the Testing Data
dtree_te_predict <- predict(dtree, newdata=sub_testing_data, type="class")
dtree_te_predict.t <- table(sub_testing_data$Survived, dtree_te_predict)
dtree_testing_accuracy <- (dtree_te_predict.t[1, 1] + dtree_te_predict.t[2, 2]) / sum(dtree_te_predict.t)
cat("Model Accuracy in Prediction: ", dtree_testing_accuracy)

# Display the decision tree
fancyRpartPlot(dtree)

# Model Rebuilding
formula2 <- Survived ~ Sex + Pclass + Age
dtree2 <- rpart(formula2, data = sub_training_data, method="class")

# Performance on the Training Data
dtree_tr_predict2 <- predict(dtree2, newdata = sub_training_data, type="class")
dtree_tr_predict.t2 <- table(sub_training_data$Survived, dtree_tr_predict2)
dtree_tr_accuracy2 <- (dtree_tr_predict.t2[1, 1] + dtree_tr_predict.t2[2, 2]) / sum(dtree_tr_predict.t2)
cat("Model Accuracy on Sub sample on training data: ", dtree_tr_accuracy2)

# Performance on the Testing Data
dtree_te_predict2 <- predict(dtree2, newdata = sub_testing_data, type="class")
dtree_te_predict.t2 <- table(sub_testing_data$Survived, dtree_te_predict2)
dtree_testing_accuracy2 <- (dtree_te_predict.t2[1, 1] + dtree_te_predict.t2[2, 2]) / sum(dtree_te_predict.t2)
cat("Model Accuracy in Prediction: ", dtree_testing_accuracy2)

# Display the Decision Tree
fancyRpartPlot(dtree2)

# Building Model using randomForest package
# Finding NAs and Iputing/Removing the NAs
nmissing <- function(x) sum(is.na(x))
L <- colwise(nmissing)(train)
knitr::kable(L, digits = 2, caption = "Training Data: NA's")
names(train) # use all of these

predicted_age <- rpart(Age ~ Pclass + Sex + SibSp + Parch + Fare + Embarked + Survived, data = train[!is.na(train$Age), ], method = "anova")
train1 <- train
test1 <- test

summary(train1$Age)

train1$Age[is.na(train1$Age)] <- predict(predicted_age, train[is.na(train$Age), ])
summary(train1$Age)

k1 <- colwise(nmissing)(train1)
knitr::kable(k1, digits = 2, caption = "Training Data: NA's")

# Developing RF Model
train1$Survived <- as.factor(train1$Survived)
train1$Sex <- as.factor(train1$Sex)
train1$Embarked <- as.factor(train1$Embarked)
test1$Sex <- as.factor(test1$Sex)
test1$Embarked <- as.factor(test1$Embarked)

sapply(train1, class)
sapply(test1, class)

formula2 <- Survived ~ Pclass + Sex + Age
my_rf_model <- randomForest(formula2, data = train1, importance=TRUE, ntree=2000)

importance(my_rf_model)
varImpPlot(my_rf_model, main = "RF: Variable Importance")

my_RF_prediction <- predict(my_rf_model, test1)
options('digits'= 3)
conf_matrix <- my_rf_model$confusion
knitr::kable(conf_matrix, digits = 2, caption = "Prediciton Errors: ")

options('digits'= 3)
my_rf_model$confusion[, 'class.error']
my_rf_model

# Saving Result for Kaggle Submission
my_solution_rf <- data.frame(PassengerId = test1$PassengerId, Survived = my_RF_prediction)
write.csv(my_solution_rf, file = "my_solution_rf.csv" , row.names=FALSE)
