df = read.table('复议分极差.csv', header=T, sep=',')
df = na.omit(df)

fit = lm(df$复议后极差~df$专家一标准分 + df$专家二标准分 + df$专家三标准分)
print(summary(fit))

# plot(df$第二次评审标准分极差, df$复议后极差)
# abline(fit)