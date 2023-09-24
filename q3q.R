df = read.table('Q3相关性分析.csv', header=T, sep=',')
chengji = df$一阶段成绩

print(quantile(chengji, c(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9)))