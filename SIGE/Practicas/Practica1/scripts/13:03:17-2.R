require(plyr)
require(ggplot2)
require(reshape2)

# Cargar datos
adult.training <- read.table(file = "/Users/jesusgarciamanday/Downloads/adult-dataset/adult.training.csv", sep = ',', header = TRUE)
head(adult.training)
str(adult.training)

adult.test <- read.table(file = "/Users/jesusgarciamanday/Downloads/adult-dataset/adult.test.csv", sep = ',', header = TRUE)
head(adult.test)
str(adult.test)

adult <- rbind(adult.training, adult.test)

# Selección de datos
adult.reduced <- head(adult, n = 500)
adult[adult$Workclass == "Private",]
adult[adult$Age > 45,]
unique(adult.reduced["Marital.status"])

# Combinacion de datos (para transformar valores)
status.eng <- c(unique(adult.reduced["Marital.status"]))
status.sp  <- c(Marital.status.sp = "Casado/a", "No casado/a", "Divorciado/a", "Separado/a", "Viudo/a", "Casado/a, conyuge ausente")
status.transl <- data.frame(status.eng, status.sp)
adult.transl <- join(x = adult, y = status.transl, by = c("Marital.status"))

# Cálculo de campos derivados
adult.transl$birthYear <- with(adult.transl, 2017-Age)

# Agrupar datos
adult.count.byage <- ddply(adult, c("Age"), function(x) {count(x$Class)})
adult.avgage.byclass <- ddply(adult, c("Class"), function(x) {mean(x$Age)})

# 1) histogramas
qplot(data = adult, x = Age)

ggplot(data = adult, aes(x = Age, fill = Class)) +
  geom_histogram(binwidth = 1) +
  facet_wrap(~Race)

ggplot(data = adult, aes(x = Age, colour = Class)) +
  geom_freqpoly(binwidth = 1)    

# 2) diagramas de barras
ggplot(data = adult, aes(x = Class, fill = Class)) +
  geom_bar() 

adult.count.byrace <- ddply(adult, c("Race"), function(x) {count(x$Class)}) # cuantos elementos hay para cada raza
colnames(adult.count.byrace) <- c("Race", "Salary", "Count") # 
adult.count.byrace.twocol <- dcast(adult.count.byrace, Race ~ Salary)
adult.count.byrace.twocol$Total <- adult.count.byrace.twocol$`<=50K` + adult.count.byrace.twocol$`>50K`
adult.count.byrace.twocol$`<=50K` <- adult.count.byrace.twocol$`<=50K` / adult.count.byrace.twocol$Total * 100
adult.count.byrace.twocol$`>50K` <- adult.count.byrace.twocol$`>50K` / adult.count.byrace.twocol$Total * 100
adult.count.byrace.twocol$Total <- NULL
adult.count.byrace.perc <- melt(adult.count.byrace.twocol, id.vars = c('Race'), variable.name = 'Salary', value.name = 'Perc')
ggplot(data = adult.count.byrace.perc, aes(x = Race, y = Perc, fill = Salary)) +
  geom_bar(stat = "identity") 


# Preparacion de datos

# 1) Eiminar education-num
adult <- adult[, !(names(adult) %in% c("Education.num", "status_sp"))]

# 2) Reducir el número de variables con muchos valores (education)
ggplot(data = adult, aes(x = Education, fill = Education)) + geom_bar() 
adult$Education <- as.character(adult$Education)
adult <- within(adult, Education[Education %in% c("12th", "11th", "10th", "9th", "7th-8th", "5th-6th", "1st-4th", "Preschool")] <- "Unfinished" )
adult$Education <- as.factor(adult$Education)
ggplot(data = adult, aes(x = Education, fill = Education)) + geom_bar() 

# 3) Detectar y eliminar outliers (age, hours per week)
ggplot(data = adult, aes(x = Age, fill = Class)) + geom_histogram(binwidth = 1) 
age_sd <- sd(adult$Age)
age_mean <- mean(adult$Age)
age_upper <- round(age_mean + 3 * age_sd, 0)
age_lower <- 17
adult <- adult[adult$Age >= age_lower & adult$Age <= age_upper, ]
ggplot(data = adult, aes(x = Age, fill = Class)) + geom_histogram(binwidth = 1) 

ggplot(data = adult, aes(x = Hours.per.week, fill = Class)) + geom_histogram(binwidth = 1) 
hoursperweek_sd <- sd(adult$Hours.per.week)
hoursperweek_mean <- mean(adult$Hours.per.week)
hoursperweek_upper <- round(hoursperweek_mean + 3 * hoursperweek_sd, 0)
hoursperweek_lower <- round(hoursperweek_mean - 3 * hoursperweek_sd, 0)
adult <- adult[adult$Hours.per.week >= hoursperweek_lower & adult$Hours.per.week <= hoursperweek_upper, ]
ggplot(data = adult, aes(x = Hours.per.week, fill = Class)) + geom_histogram(binwidth = 1) 

# 4) Eliminar missing values (quitamos filas con missing values, cambiar a media de cada columna)
adult <- adult[apply(adult, 1, function(row) !any (row %in% c("?"))), ]

# 5) Construir predictor
require(rpart)
require(rattle)
require(rpart.plot)
require(RColorBrewer)
require(caret)

sample_size <- floor(0.75 * nrow(adult))
set.seed(123)
train_ind <- sample(seq_len(nrow(adult)), size = sample_size)
adult.training   <- adult[train_ind, ]
adult.validation <- adult[-train_ind, ]

# Creación del arbol de decisión
class_tree <- rpart(Class ~ Age + Workclass + Fnlwgt + Education + Marital.status + Occupation + Relationship + Race + Sex + Capital.gain + Capital.loss + Hours.per.week + Native.country, 
                    data=adult.training,
                    method="class")
#plot(predictor)
#text(predictor)
fancyRpartPlot(class_tree)

prediction.validation <- predict(class_tree, adult.validation, type = "class")
prediction.training   <- predict(class_tree, adult.training, type = "class")
prediction <- rbind(cbind(adult.training, Prediction=prediction.training), cbind(adult.validation, Prediction=prediction.validation))
confTable <- table(prediction$Class, prediction$Prediction)
