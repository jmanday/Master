var1=1:5
var2=(1:5)/10
var3=c("R","and","data mining","Examples","Case Estudies")
df1=data.frame(var1,var2,var3)
names(df1)=c("Enteros","Reales","String")
write.csv(df1,"./Ejemplos manejo de datos/Data/tontos.csv",row.names=FALSE) 
