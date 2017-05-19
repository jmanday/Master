# We get the vector white the count occurances each value than the variable can take 
table(train$Sex)

# We get the proportion of male and female that survived 
prop.table(table(train$Sex, train$Survived))

# It's give us the proportion each row (divides each row by the total number of passengers) 
prop.table(table(train$Sex, train$Survived),1)

# We altered the column with 1’s for the subset of passengers where the variable “Sex” is equal to “female”
test$Survived <- 0
test$Survived[test$Sex == 'female'] <- 1

# We add a new variable
train$Child <- 0
train$Child[train$Age < 18] <- 1


# With the function aggregate we create a table with both gender and age to see the survival proportions for different subsets
aggregate(Survived ~ Child + Sex, data=train, FUN=sum)