#!/usr/bin/Rscript

# Load libraries
suppressMessages(library(Biobase))
suppressMessages(library(lumi))
suppressMessages(library(ggplot2))
suppressMessages(library(reshape))

inputdir='W:/SERVICES/Microarrays/GX-Toray/Toray Free Trial Projects/P.Ovando-roche/Results/Data/merged/'
#inputdir=commandArgs(TRUE )[1]
outputdir='W:/SERVICES/Microarrays/GX-Toray/Toray Free Trial Projects/P.Ovando-roche/Results/QC/'
#outputdir=commandArgs(TRUE )[2]
#nsamples=commandArgs(TRUE )[3]
nsamples=4

setwd(inputdir)

# Read file and set expression set
data<-read.csv("merged_data.csv")
exprset_matrix<-as.matrix(data[,c(11:(11+nsamples-1))])
exprset_matrix[is.na(exprset_matrix)] <- 0
rownames(exprset_matrix)<-data[,1]
exprset<-ExpressionSet(as.matrix(exprset_matrix))

# Number of detected probes
nprobes0=as.data.frame(matrix(table(exprs(exprset)[,1]==0)))
colnames(nprobes0)=colnames(exprs(exprset))[1]

for (i in 2:dim(exprs(exprset))[2]){
  nprobes0=cbind(nprobes0,data.frame(table(exprs(exprset)[,i]==0))[,2])
  colnames(nprobes0)[i]=colnames(exprs(exprset))[i]
}
rownames(nprobes0)=c('Detected','NotDetected')
write.csv(nprobes0,file = paste0(outputdir,'nprobes_detected.csv'))

#png('Results/QC/NDetected_probes.png', width = 880, height = 530)
#par(mar=c(10.1,4.1,4.1,8.1),  xpd=TRUE)
#barplot(as.matrix(nprobes0), las=2, col=c('black','gray'))
#legend("topright", inset=c(-0.12,0), c('Detected','Not Detected'), col=c('black','gray'), pch=15)
#dev.off()

# Distribution of data
# Boxplot
png(paste0(outputdir,'boxplot_normData.png'), width = 880, height = 630)
temp=melt(exprs(exprset))
temp$X2=factor(temp$X2, levels=colnames(exprs(exprset)))
ggplot(temp, aes(factor(X2), value)) + geom_boxplot(aes(fill = X2), show_guide=FALSE) + 
  theme(axis.title.x = element_blank(), axis.text.x  = element_text(angle=90, vjust=0.5, size=17, colour="black"),
        axis.title.y = element_blank(), axis.text.y  = element_text(size=16, colour="black"))
dev.off()

# Sample relationship, subset of most variable genes
png(paste0(outputdir,'mds.png'), width = 930, height = 650)
plotSampleRelation(exprset, method='mds')
dev.off()

png(paste0(outputdir,'dendogram.png'), width = 900, height = 680)
plotSampleRelation(exprset, method='cluster')
dev.off()

# Density
png(paste0(outputdir,'density.png'), width = 880, height = 680)
plot(exprset, what="density")
abline(v=0)
dev.off()

#nameFile=paste("Report/QC/scatter_plot_png",sep="")
png(paste0(outputdir,'scatterplot.png'),width=1024,height=748)
plot(exprset, what="p", subset=NULL)
dev.off()

