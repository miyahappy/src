library(dplyr)
library(ggplot2)
library(parallel)
rm(list = ls())
#work_dir <- "E:/bioinformatics/project/GDC/fpkm_2" #目录参数：工作目录
work_dir <- "/home/userroot/GDC/fpkm"
setwd(work_dir)
a <- list.files('./Primary Tumor/')
a <- a[which(grepl('KIRP',a)==T)]
n <- length(a)
#dir_file <- './Primary Tumor/'
data <- read.table(paste('./Primary Tumor/',a[1],sep = ''))

ensg <- substr(as.character(data[,1]),1,15)

for (i in ensg){
dir.create(paste('./output/',i,sep = '')) 
}


func_1 <- function(i){
  for (j in 1:60483){
  data <- read.table(paste('./Primary Tumor/',i,sep = ''))[j,]
  #data <- filter(data,data$V1=='ENSG00000167740.8')
  write.csv(data,paste('./output/',substr(as.character(data[1,1]),1,15),'/',i,sep = ''))
  }
}

cl <- makeCluster(40) # 初始化四核心集群
results <- parLapply(cl,a,func_1) # lapply的并行版本
#res.df <- do.call('rbind',results) # 整合结果
stopCluster(cl) # 关闭集群



#ggplot(data, aes(x=data$V2))+geom_histogram(binwidth=1, fill="white", colour="black")
#ggsave('1.jpg',plot = last_plot())