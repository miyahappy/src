rm(list=ls())
library(Rtsne)
library(ggplot2)
setwd('/home/userroot/GDC/protein/')
a <- read.table('./BRCA_protein.txt',sep = '\t',header = F,stringsAsFactors = F)
a <- a[-2,]
names(a) <- paste('BRCA-',substr(a[1, ],6,12),sep = '')
a <- a[-1, ]
a <- na.omit(a)
row.names(a) <- a[ ,1]
a <- a[ ,-1]
a <- as.data.frame(t(a),stringsAsFactors = F)

tsne <- Rtsne(a,dims = 2,initial_dims = 226,perplexity = 30,verbose=T,max_iter = 1000)
result <- as.data.frame(tsne$Y)

p <- ggplot(result,aes(x=result$V1,y = result$V2))+geom_point()
ggsave('test.tiff',p,width = 3.15, height = 3.15)

plot(result$V1,result$V2)                                                                                                             



