---
title: 排版测试

# 目录
toc: true
toc-title: 目录

# 参考文献
bibliography: [1.bib]
csl: china-national-standard-gb-t-7714-2015-numeric.csl
nocite: |
    @*

secnos-cleveref: True
secnos-plus-name: 章节
secnos-star-name: 章节

fignos-cleveref: True
fignos-caption-separator: colon
fignos-caption-name: 图
fignos-plus-name: 图
fignos-star-name: 图
fignos-number-by-section: True

eqnos-cleveref: True
eqnos-plus-name: 公式
eqnos-star-name: 公式
eqnos-number-by-section: True

---
# 数理统计作业-15组-第3周

|  姓名  |   学号   |       题目       |
| :----: | :------: | :--------------: |
| 姜昊成 | 20181977 |       1,2        |
| 杨子涵 | 20181974 |       3,4        |
| 罗少航 | 20171904 | 5,6&排版（组长） |
| 何鑫云 | 20181978 |       7,8        |
| 潘一达 | 20174860 |     9,10,11      |

1. 学习随机变量的数字特征有什么意义？
    * 研究随机变量的数字特征可以总体上掌握随机变量某一侧面的性质,如期望表征随机变量的取值水平即平均数,方差表征随机变量取值的分散或集中程度。
2. 常见的数字特征有哪些？
    * 数学期望
        1. 连续型数据
        2. 离散型数据
    * 方差与矩
        1. 方差
        2. 矩
        3. 协方差
    * 相关系数
3. 均值（数学期望）、方差的定义、计算公式、性质有哪些？
    * 期望的定义：随机变量X的期望(expectation)或均值EX是它全部取值的平均值，也是分布律或密度函数的中心位置，因此，期望有时也称位置参数(location parameter).期望在实际中应用广泛，常被用作随机变量分布的代表性指标。
    * 期望的计算公式：
        * $$ E(g(X))=\left\{\begin{array}{l}\sum_{i=1}^{\infty} g\left(x_{i}\right) P\{X=x_{i}\}, P\{X=x_{i}\}(i=1,2, \cdots) \text { 为 } X \text { 的分布律 } \\ \int_{-\infty}^{+\infty} g(x) f(x) \mathrm{d} x, f(x) \text { 为 } X \text { 的密度函数 }\end{array}\right. $$
        * 设二维随机变量$(X,Y)$的联合分布律为 $P\left\{X=x_{i}, Y=y_{j}\right\}=p_{i j}, i, j=1,2,\cdots$ ，若联合密度函数为$f_{X,Y}(x,y)$，则随机变量 $g(X,Y)$  的数学期望的计算公式为 $$ E[g(X, Y)]=\left\{\begin{array}{ll}\sum_{i=1}^{+\infty} \sum_{j=1}^{+\infty} g\left(x_{i}, y_{j}\right) P\{X=x_{i}, Y=y_{j}\} & (X, Y) \text{为离散型} \\ \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} g(x, y) f_{X, Y}(x, y) \mathrm{d} x \mathrm{d} y, & (X, Y) \text{为连续型}\end{array}\right. $$
    * 期望的性质
        1. 线性性：若 $a_{1}, a_{2}, \cdots, a_{n}$ 及 $c$ 为常数， $X_{1}, X_{2}, \cdots, X_{n}$ 为 $n$ 个随机变量，则 $$ E\left(\sum_{i=1}^{n} a_{i} X_{i}+c\right)=\sum_{i=1}^{n} a_{i} E X_{i}+c $$
        2. 若 $X_{1}, X_{2}, \cdots, X_{n}$ 相互独立，则 $E\left(X_{1} \cdot X_{2} \cdots \cdots X_{n}\right)=E X_{1} \cdot E X_{2} \cdot \cdots \cdot E X_n$
    * 方差的定义：方差(variance) $DX$刻画了随机变量X取值的“波动”大小或稳定性，度量了随机变量$X$偏离期望$EX$的平均幅度。
    * 方差的计算公式：
    * 方差的性质：
        * 随机变量的方差具有如下性质(假设所涉及的方差都存在) ：
        * 若 $X_{1}, X_{2}, \cdots, X_{n}$ 相互独立，$a_{1}, a_{2}, \cdots, a_{n}$ 及 $c$ 为常数，则 $$ D\left(\sum_{i=1}^{n} a_{i} X_{i}+c\right)=\sum_{i=1}^{n} a_{i}^{2} D\left(X_{i}\right) $$
        * 设 $a、b$ 是常数，对随机变量$X$和$Y$，有 $$ D(a X \pm b Y)=a^{2} D X+b^{2} D Y \pm 2 a b E[(X-E X)(Y-E Y)] $$
        * **(切比雪夫不等式)** 设$X$的方差存在, 则对任意正数$\varepsilon$，有 $$ P\{|X-E X| \geqslant \varepsilon\} \leqslant \frac{D X}{\varepsilon^{2}} $$或 $$ P\{|X-E X|<\varepsilon \} \geqslant 1-\frac{D X}{\varepsilon^{2}} $$
        * 若随机变量$X$的方差存在，则$DX=0$的充分必要条件是$X$以概率$1$取某个常数$c$，即$P\{X=c\}=1$。
4. 常见分布的期望、方差是什么？
5. 协方差、相关系数的定义、计算公式是什么？它们有什么作用？
    * 协方差、相关系数的定义
        * 设 $(X,Y)$ 为二维随机变量，如果 $E[(X-E(X))(Y-E(Y))]$ 存在，则称 $E[(X-E(X))(Y-E(Y))]$ 为$X$与$Y$的**协方差**，记为 $$ \operatorname{cov}(X, Y)=E[(X-E(X))(Y-E(Y))] $$
        * 若 $D(X) \neq 0, D(Y) \neq 0$ ，则称 $\frac{\operatorname{cov}(X, Y)}{\sqrt{D(X)} \sqrt{D(Y)}}$ 为$X$与$Y$的**相关系数**，记为 $\rho(X,Y)$ 或 $\rho_{X,Y}$ ，即 $$ \rho(X, Y)=\frac{\operatorname{cov}(X, Y)}{\sqrt{D(X)} \sqrt{D(Y)}} $$
    * 协方差的计算公式
        * $$ \operatorname{cov}(X, Y)=E(X Y)-E(X) \cdot E(Y) $$
    * 协方差、相关系数的作用
        * 当事件$X$与$Y$相互独立时，有 $$E[(X-E(X))(Y-E(Y))]=0$$ 这意味着若 $E[(X-E(X))(Y-E(Y))]\neq 0$，则$X$与$Y$必然不相互独立，因而$X$与$Y$之间存在则某种关联。因此可以用量 $E[(X-E(X))(Y-E(Y))]$，即**用相关系数来描述$X$与$Y$之间的关联程度**
        * 对相关系数，令 $X^{*}=\frac{X-E(X)}{\sqrt{D(X)}}$ ，$Y^{*}=\frac{Y-E(Y)}{\sqrt{D(Y)}}$ ，则 $\rho(X, Y)=\operatorname{cov}\left(X^{*}, Y^{*}\right) . \operatorname{cov}(X, Y)$ 。$\operatorname{cov}(X, Y)$ 是一个有量纲的数，而$\rho(X,Y)$是一个无量纲的数。**相关系数能很好地反映随机变量$X$与$Y$之间的关系**
6. 协方差、相关系数的基本性质是什么？
    * 协方差的性质
        1. 设$c$为常数，则 $\operatorname{cov}(c, X)=0$
        2. $\operatorname{cov}(X, X)=D(X)$
        3. $\operatorname{cov}(X, Y)=\operatorname{cov}(Y, X)$
        4. 设 $a,b$为常数，则 $\operatorname{cov}(a X, b Y)=a b \operatorname{cov}(X, Y)$
        5. $\operatorname{cov}(X+Y, Z)=\operatorname{cov}(X, Z)+\operatorname{cov}(Y, Z)$
        6. $D(X \pm Y)=D(X)+D(Y) \pm 2 \operatorname{cov}(X, Y)$
        * $n$维随机变量推广
            1. $\operatorname{cov}\left(\sum_{i=1}^{n} a_{i} X_{i}, Z\right)=\sum_{i=1}^{n} a_{i} \operatorname{cov}\left(X_{i}, Z\right)$
            2. 设 $a_{i}(i=1,2, \cdots, n)$ 为常数 $$ D\left(\sum_{i=1}^{n} a_{i} X_{i}\right)=\sum_{i=1}^{n} a_{i}^{2} D\left(X_{i}\right)+\sum_{i=1}^{n} \sum_{j=1, j \neq i}^{n} a_{i} a_{j} \operatorname{cov}\left(X_{i}, X_{j}\right) $$
    * 相关系数的性质
        1. $|\rho(X, Y)| \leqslant 1$
        2. $\rho(X, Y) \pm 1$ 的充要条件为 $X$ 与 $Y$ 以概率为$1$线性相关，即 $$ P\left(\frac{X-E(X)}{\sqrt{D(X)}}=\pm \frac{Y-E(Y)}{\sqrt{D(Y)}}\right)=1 $$
7. 怎样认识变量之间的不相关关系与独立关系？
    * 变量间的关系可以用相关系数来刻画。
    * 对二维随机变量 $(X,Y)$ 而言，如果 $E[(X-E(X))(Y-E(Y))]$ 存在，则称 $E[(X-E(X))(Y-E(Y))]$ 为$X$与$Y$的**协方差**，记为 $$ \operatorname{cov}(X, Y)=E[(X-E(X))(Y-E(Y))] $$
    * 当$\rho\left(X,Y\right)$取值为$0$，则称$X$和$Y$为不相关关系。
    * 变量的不相关关系和独立关系之间存在如下推导性质：$$ X和Y相互独立\Rightarrow X和Y不相关；$$但 $$ X和Y不相关\nRightarrow X和Y相互独立； $$此外，当随机变量的联合分布是正态分布时，有$$X和Y相互独立\Leftrightarrow X和Y不相关。$$
8. 随机变量的 k 阶原点矩、中心矩的定义是什么？混合矩的定义是什么？
    * 对随机变量$X$和$Y$，若以下的数学期望都存在，
    * 则称$μ_k=EX^k (k=1, 2, \cdots)$ 为$X$的$k$阶原点矩；
    * 称$\nu_k=E(X-EX)^k(k=1, 2, \cdots)$ 为$X$的$k$阶中心矩；
    * 称$E(X^kY^l)  (k, l=1, 2, \cdots)$为$X$和$Y$的$k + l$阶混合原点矩；
    * 称$E[(X-EX)^k (Y-EY)^l ]  (k, l=1, 2, \cdots)$ 为$X$和$Y$的$k + l$阶混合中心矩。
    * 由上述原点矩和中心矩的定义可知，一阶原点矩就是数学期望，二阶中心矩就是方差。同时，因${\mid x\mid}^{k-1}\le{\mid x\mid}^k+1$，故随机变量$X$的$k$阶矩存在时，$k-1$阶矩也存在，从而小于$k$的各阶矩都存在。
9. 极限定理描述什么现象？
    * 极限定理是概率论的基本理论，阐述了大量观测或试验中随机现象的统计规律性，在理论研究和应用中起着重要作用。随机变量序列的极限反映了当实验次数充分大时序列$\{X_k，k=1，2，3\cdots\}$的变化趋势。随机变量序列的极限有两种基本的描述方法，即依概率收敛和依分布收敛。
10. 辛钦大数定律、贝努里大数定律是什么？有什么应用？
    * 辛钦大数定律：
    * 伯努利大数定律：
        * 设$f_n(A)$是$n$重伯努利试验中事件$A$发生的频率，事件$A$在每次试验中发生的概率为$P(A)$。则对任意正数$\varepsilon> 0$。有：$$ \begin{array}{c}\lim_{n \rightarrow+\infty} P\left\{\left|f_{n}(A)-P(A)\right|<\varepsilon\right\}=1 \\ \lim_{n \rightarrow+\infty} P\left\{\left|f_{n}(A)-P(A)\right| \geqslant \varepsilon\right\}=0\end{array} $$ 记作，即对给定的很小正数$\varepsilon$，当$n$足够大时，“频率$f_n(A)$与概率$P(A)$的偏差小于$\varepsilon$”几乎是一个必然事件，这就是以频率定义概率的理论依据所在。
    * 大数定律不仅可以用于总体的均值估计，还可以用于其他参数的估计问题。例如，用于定积分$I[f(x)]=\int_0^1f(x)\mathrm{d}x$的估计，当随机变量$X_1,X_2,\cdots,X_n$相互独立，都服从$\bigcup[0,1]$时，则$f(X_1),f(X_2,),\cdots,f(X_n)$也为独立同分布的随机变量序列，且$I\left[f\left(x\right)\right]=\int_{0}^{1}f\left(x\right)dx=E[f(X_i)], i=1,2,…,n$。那么由大数定律得，当$n$足够大时，$\frac{1}{n}\sum_{i=1}^{n}{f(X_i)}$可以作为参数$I[f(x)]$的估计值，由此可见，只要能获取来自均匀分布$\bigcup[0,1]$的观测数据$x_1,x_2,\cdots,x_n$，就可以用$\frac{1}{n}\sum_{i=1}^{n}{f(X)_i}$去估计参数$I[f(x)]$。
11. 独立同分布的中心极限定理是什么？有什么应用？
    * 中心极限定理是研究独立随机变量和的分布在一定条件下以正态分布为极限分布，是数理统计和误差分析的基础。
    * 独立同分布的中心极限定理：
        * 设${X_k,k=1,2,3\cdots}$独立同分布，数学期望存在且$E(X_k)=\mu,D(X_k)=\sigma^2>0,k=1,2,\cdots$，则对于任意实数$x$：$$ \lim _{n \rightarrow+\infty} P\left\{\frac{\sum_{i=1}^{n} X_{k}-n \mu}{\sqrt{n} \sigma} \leqslant x\right\}=\int_{-\infty}^{x} \frac{1}{\sqrt{2 \pi}} \mathrm{e}^{-\frac{i^{2}}{2}} \mathrm{d} t=\Phi(x) $$
        * 此定理表明：若对某个随机变量进行大量的独立重复观测实验，则实验结果的和近似服从正态分布$N(n\mu,n\sigma^2)$。
    * 应用：以在误差分析上的应用为例
        * 对一个物理量独立地测量$n$次，每次测量产生的随机误差都服从$(-1,1)$上的均匀分布，如果取$n$次测量的算术平均值作为测量结果，求它与真值得差小于指定的正数$u$的概率。
        * 解：随机误差的期望与方差为：$E(x)=\frac{a+b}{2}=0, D(x)=\frac{(b-a)^{2}}{12}=\frac{1}{3}$  ，则：$$ \begin{aligned} P\left(\left|\frac{\bar{X}-\mu}{\sigma / \sqrt{n}}\right| \leq \frac{u-\mu}{\sigma / \sqrt{n}}\right) &=P(\sqrt{3 n}|\bar{X}| \leq \sqrt{3 n} * u) \\&= P(-\sqrt{3 n} * u \leq \sqrt{3 n} \bar{X} \leq \sqrt{3 n} * u) \\&= \Phi(\sqrt{3 n} * u)-\Phi(-\sqrt{3 n} * u) \\&= \Phi(\sqrt{3 n} * u)-(1-\Phi(\sqrt{3 n} * u)) \\&= 2 \Phi(\sqrt{3 n} * u)-1 \end{aligned} $$
