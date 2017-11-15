#!/usr/bin/env Rscript
library(clusterCrit) # Rand index, Accuracy, Jaccard, Folkes_Mallows
library(NMI) # NMI
library(clues) # ARI
suppressMessages(library(IntNMF)) # Entropy, Purity

# args[1] ground Truth classification file
# args[2] classification result file
# args[3] output file if the file already exist, append at the end of the file


args <- commandArgs(TRUE)
vt <- scan(file=args[1],what=integer(),quiet = TRUE)
#data <- read.matrix(file=args[2], header = FALSE, sep = " ", skip = 1)
data <-as.matrix(read.table(file=args[2], header=FALSE,sep=" "))
res <- scan(file=args[3],what=integer(),quiet = TRUE)

#intCriteria(data, vt, c("C_index","Calinski_Harabasz","Log_SS_Ratio","Ball_Hall","sd_dis","sd_scat","Xie_Beni", "Ray_Turi", "Gamma", "tau", "silhouette"))

extCriteria(vt, res, c("all"))

# compute Normalized Mutual information
x <- data.frame(c(1:length(vt)),as.vector(as.integer(vt)))
y <- data.frame(c(1:length(res)),as.vector(as.integer(res)))
NMI(x,y)

adjustedRand(res,vt,randMethod = "HA")

# compute Entropy
entropy <-ClusterEntropy(res,vt)
entropy
entropy(res,vt,method = "best")
#compute Purity
purity<-ClusterPurity(res,vt)
purity
