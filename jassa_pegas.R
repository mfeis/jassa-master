setwd ("//zeus.nioz.nl/cos/users/luttik/nioz_data/data/JassaINSITE")
library(pegas) #for analyses and haplotype network
library(magrittr)
library(dplyr)
x <- read.dna(file="jassa_cropped.fas",format="fasta")
h <- haplotype(x,labels=c(1:44))
h
h_indices<-attr(h, "index")
names(h_indices)<-c(1:44)
str(h_indices)
net <- haploNet(h)
plot(net,
     size=attr(net, "freq"),
     scale.ratio = 30,
     cex = 0.8,
     show.mutation=0,
     threshold=0)

names<-data.frame(labels(x))
str(names)

haploFreq(x,haplo=h)
locations<-read.csv(file="jassa_names.csv",header=TRUE)
str(locations)

#per unique site
freq_unique<-haploFreq(x,fac=locations$site_unique,haplo=h)

#plot the new haplotype
plot(net,
     size=attr(net, "freq"),
     scale.ratio = 30,
     cex = 0.8,
     pie=freq_unique,
     show.mutation=0,
     threshold=0)
legend("topright",cex=0.3,
       colnames(freq_unique),
       col=rainbow(ncol(freq_unique)),
       pch=20,bty="n")

#amova NOT WORKING
dm<-dist.dna(x)
(res<-amova(dm~freq_unique))
sigma2<-res$varcomp[1,1]
(phi_st<-(sigma2/(sigma2-res$tab[1,2])))