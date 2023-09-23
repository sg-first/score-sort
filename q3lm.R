df = read.table('Q3相关性分析.csv', header=T, sep=',')
fit = lm(df$最终成绩~df$一阶段成绩)
print(summary(fit))

plot(df$一阶段成绩, df$最终成绩)
abline(fit)