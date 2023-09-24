df = read.table('极差.csv', header=T, sep=',')

jicha = sort(df$极差2.2)
print(barplot(jicha))
print(jicha)
