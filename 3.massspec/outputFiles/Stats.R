tryp <-read.csv("enzyme_t_stats.csv")
ArgC <- read.csv("enzyme_a_stats.csv")
LysC <- read.csv("enzyme_l_stats.csv")
GluC <- read.csv("enzyme_e_stats.csv")
test <- read.csv("enzyme_test_stats.csv")

hist(tryp$peptides)
hist(ArgC$peptides)
hist(LysC$peptides)
hist(GluC$peptides)
hist(GluC$peptides)

mean(tryp$peptides)
8.663212
mean(ArgC$peptides)
5.134872
mean(LysC$peptides)
4.528339
mean(GluC$peptides)
4.221838

tryp1500 <-read.csv("enzyme_t_1500_stats.csv")
ArgC1500 <- read.csv("enzyme_a_1500_stats.csv")
LysC1500 <- read.csv("enzyme_l_1500_stats.csv")
GluC1500 <- read.csv("enzyme_e_1500_stats.csv")

mean(tryp1500$peptides)
3.094002
mean(ArgC1500$peptides)
2.152046
mean(LysC1500$peptides)
1.806213
mean(GluC1500$peptides)
2.106612

