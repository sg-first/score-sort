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
由于有125位专家，我们应该都用上，因此需要均匀，同时又希望尽量使交集最大。那么最朴素的产生函数就是，对于专家i，取集合`{i, i+1, i+2, i+3, i+4, i+5}`

这里用的“加法”需要打个补丁，如果`i+j>125`，那么我们令其等于`i+j-125`（即超过了125就循环回1），如果不打这个补丁，那1~4和121~125所属的组合个数就和中间的不一样了。

扩大每个专家的共事范围
---------
可以观察到，我们用这种最简单的产生函数产生的前125种选择可以使每个专家都和其相邻的专家共同出现在五个集合中了。对于“尽量使交集最大”这个目标而言，相邻的两个专家i、j对应的组合一定重合四个，所以从相邻这个角度来讲，实现“交集最大”了。

但专家i前面最远是i-4个专家，后面最远是i+4个专家，它与且仅与这9个专家共同出现过，我们现在要扩大这个范围，让它在其它组合中与更多的专家共同出现——那么我们就需要其它的产生函数（每种产生函数产生125种组合，一共3000种组合，用24个产生函数）

产生函数要怎么变呢？刚才我们那种朴素的产生函数是取集合`{i, i+1, i+2, i+3, i+4, i+5}`。那我们想让专家i与更远的专家同时出现（而非仅与相邻的），那只需要把产生函数改成`{i, i+1+k, i+2+k……}`就可以控制其它专家和i的“距离”了
