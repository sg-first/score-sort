df = read.table('极差.csv', header=T, sep=',')
chengji = na.omit(df$一阶段成绩1)

print(quantile(chengji, c(0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.85)))