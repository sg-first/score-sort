Q1
========
产生函数
--------
先定义一下组合：五个专家组成的一个集合。3000题，每题都要选一个组合

我们找了一个产生组合的方法，比如叫“产生函数”，输入一个中心元素（一位专家），生成一个对应的组合。这样可以使得每个专家对应一个组合，该过程可以描述为：
```
专家i对应的组合=产生函数(专家i)
```

最简单的产生函数
-------
由于有125位专家，我们应该都用上，因此需要均匀，同时又希望尽量使交集最大。那么最朴素的产生函数就是，对于专家i，取集合`{i, i+1, i+2, i+3, i+4}`

这里用的“加法”需要打个补丁，如果`i+j>125`，那么我们令其等于`i+j-125`（即超过了125就循环回1），如果不打这个补丁，那`1~4`和`121~125`所属的组合个数就和中间的不一样了。

扩大每个专家的共事范围
---------
可以观察到，我们用这种最简单的产生函数产生的前125种选择可以使每个专家都和其相邻的专家共同出现在五个集合中了。对于“尽量使交集最大”这个目标而言，相邻的两个专家i、j对应的组合一定重合四个，所以在相邻的情况下，实现“交集最大”了。

但专家i前面最远是i-4个专家，后面最远是i+4个专家，它与且仅与这9个专家共同出现过，我们现在要扩大这个范围，让它在其它组合中与更多的专家共同出现（即不仅在相邻的情况下有交集）——那么我们就需要其它的产生函数（每种产生函数产生125种组合，一共3000种组合，用24个产生函数）

产生函数要怎么变呢？刚才我们那种朴素的产生函数是取集合`{i, i+1, i+2, i+3, i+4}`。那我们想让专家i与更远的专家同时出现（而非仅与相邻的），那只需要把产生函数改成`{i, i+1+k, i+2+k……}`就可以控制其它专家和i的“距离”了

评估指标
-----------
题里要的是使交集尽可能大，那么我们要找个办法评估这个效果。对于3000题中的任一组合`{a1, a2, a3, a4, a5}`，我们可以计算其与剩下2999个组合的交集个数之和（此处应有公式，而且要给这个指标起个名，我这里先叫它`交集数和`了）。我们上面那个方法产生的结果是均匀的，不管是哪个元素，这个`交集数和`值都为595，而且极差为0

需要注意的是，我们不能片面地最大化`交集数和`，因为显然所有题都选同样组合的情况下`交集数和`最大（达到14995），然而这种情况我们只用了5个专家，剩下120个全都没用上。

我们以随机选择作为baseline和我们的方法对比。随机选择专家构成3000种组合的情况下，3000个`交集数和`服从正态分布，均值和中位数均为600。然而其`交集数和`较大是因为部分专家被重复抽取，看各个专家被抽的次数可以看出：
![](随机选择各专家被抽取数量.png)

从`交集数和`的频数分布直方图可以看出，方差较大：
![](随机选择交集数和直方图.png)

重复生成五次（每次生成3000个组合），`交集数和`的极差为146、154、133、155、146。显然这会造成大量题目选到的组合`交集数和`远远低于平均水平，造成不公平。

Q2
=========
假设一共有两道题，N个专家给分，此时标准分算法是适用的，因为这N个专家打分的对象是相同的，此时每个专家都有一个长度为2的特征向量，描述了该专家的打分风格，不同专家的打分风格是可以基于这个向量比较的。

但假设一共3000道题，构成一个长度为3000的向量，每个专家只打其中的一小部分，那么得到的特征矩阵是稀疏的，由于不同专家打分的题不同，他们的特征向量中非零值所在位置也不同，此时两个特征向量是无法比较的。

那么我们要把N个专家的特征向量构成的稀疏矩阵转化为能描述专家特征的稠密矩阵。可以使用奇异值分解或者自编码器。

获得稠密矩阵之后我们就知道了每个专家的稠密特征向量，就可以基于余弦相似度比较两个专家的距离，就可以参照一个专家的分修正另一个专家的分了（类似SSLM）

评估
--------
由于题里说了**一等奖作品排序是准确的**（按复议分算的）。所以标准分计算方法好坏的评估标准为**按该标准分产生的排序与一等奖作品排序的一致程度**。我们以新排序和正确排序之差的绝对值之和（此处应有公式）衡量。
* 题中所给出的标准分，该指标为120