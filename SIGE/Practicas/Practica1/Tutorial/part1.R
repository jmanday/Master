# Set working directory and import datafiles
setwd("~/Desktop/Master/SIGE/Practicas/Practica1/dataset")
library(readr)
train <- read_csv("~/Desktop/Master/SIGE/Practicas/Practica1/dataset/train.csv")
View(train)

# To look at the structure of the dataframe
str(train)

# This avoid that the text string will be changed to factors
train <- read.csv("train.csv", stringsAsFactors=FALSE)

# To give the occurrences od each value
table(train$Survived)

# The function prop.table() shows the percentage
prop.table(table(train$Survived))

# Add the colum "Survived" if no exist or overwrite the values putting 418 times 0
test$Survived <- rep(0, 418)

# We create a new container with tow columns had been extracted the test dataframe to submit a csv file
submit <- data.frame(PassengerId = test$PassengerId, Survived = test$Survived)
write.csv(submit, file = "Alldied-p1.csv", row.names = FALSE)
