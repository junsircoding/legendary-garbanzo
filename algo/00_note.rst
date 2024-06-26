什么是时间复杂度
-----------------------------------

数据结构和算法致力于让程序运行更快和更省存储空间，由此首要一点就是要会分析一段程序的时间、空间复杂度。

程序的执行效率，就是代码的执行时间。

比如这段代码，求 1,2,3...n 的累加和。

.. code-block:: c
    :linenos:

    int cal(int n) {
        int sum = 0;
        int i = 1;
        for (; i <= n; ++i) {
            sum += i;
        }
        return sum;
    }


假设每行代码的执行时间都一样，为 ``unit_time`` 。所有代码执行时间 :math:`T(n) = (2n + 2) \times unit\_time` 。

再看一段代码：

.. code-block:: c
    :linenos:

    int cal(int n) {
        int sum = 0;
        int i = 1;
        int j = 1;
        for (; i <= n; ++i) {
            j = 1;
            for (; j <= n; ++j) {
                sum = sum + i * j;
            }
        }
        return sum;
    }


.. math::

    T(n)=(2n^2+2n+3) \times unit\_time

由此可以得出结论，代码总执行时间 ``T(n)`` 和每行代码执行次数 ``f(n)`` 成正比，即 :math:`T(n) = O( f(n) )` 。


 | ``T(n)`` 表示代码执行时间
 | ``n`` 表示数据规模大小
 | ``f(n)`` 表示每代码执行的次数总和
 | ``O`` 表示 ``T(n)`` 与 ``f(n)`` 成正比 

所以，第一个例子中的 :math:`T(n) = O(2n + 2)` ，第二个例子中的 :math:`T(n)=O(2n^2+2n+3)` ，这就是 **大O时间复杂度表示法** 。

它其实并不具体表示代码执行时间，而是表示 **代码执行时间随数据规模增长的趋势** ，也叫做 **渐进时间复杂度** ，简称 **时间复杂度** 。

当 ``n`` 很大时，比如大到 ``10000`` 、 ``100000`` ，的话，公式中的低阶、常量、系数三不忿并不左右增长趋势，所以都可忽略，只关注最大量级就可以。

由此刚才的两个公式可以这样表示， :math:`T(n) = O(n)` ； :math:`T(n)=O(n^2)` 。

如何分析程序的时间复杂度
-----------------------------------------------------

分析一段代码的时间复杂度，有以下三个方法：

1. 只关注循环执行次数最多的一段代码。
2. 加法法则：总复杂度等于量级最大的那段代码的复杂度。
3. 乘法法则：嵌套代码的复杂度等于嵌套内外代码复杂度的乘积。

方法 1 很明显，方法 2 看下面这个例子：

.. code-block:: c
    :linenos:

    int cal(int n) {
        int sum_1 = 0;
        int p = 1;
        for (; p < 100; ++p) {
            sum_1 = sum_1 + p;
        }
        
        int sum_2 = 0;
        int q = 1;
        for (; q < n; ++q) {
            sum_2 = sum_2 + q;
        }

        int sum_3 = 0;
        int i = 1;
        int j = 1;
        for (;, i <= n; ++i) {
            j = 1;
            for (; j <= n; ++j) {
                sum_3 = sum_3 + i * j;
            }
        }

        return sum_1 + sum_2 + sum_3;
    }


这里 :math:`T1(n) = O(f(n))` ， :math:`T2(n) = O(n^2)` ， :math:`T(n) = max(T1, T2) = T2 = O(n^2)` 。

方法 3 看下面这个例子：

.. code-block:: c
    :linenos:

    int cal(int n) {
        int ret = 0;
        int i = 1;
        for (; i < n; ++i) {
            ret = ret + f(i);
        }
    }

    int f(int n) {
        int sum = 0;
        int i = 1;
        for (; i < n; ++i) {
            sum = sum + i;
        }
        return sum;
    }


在这个代码中， ``cal()`` 函数的 :math:`T(n) = T1(n) \times T2(n) = O(n) \times O(n) = O(n^2)` 。

几种常见的时间复杂度
--------------------------------------

- 常量阶 :math:`O(1)`
- 对数阶 :math:`O(log n)`
- 线性阶 :math:`O(n)`
- 线性对数阶 :math:`O(n logn)`
- 平方阶 :math:`O(n^2)` ， 立方阶 :math:`O(N^3)` ， k 次方阶 :math:`O(n^k)`
- 指数阶 :math:`O(2^n)`
- 阶乘阶 :math:`O(n!)`

这几个时间复杂度可以分为两类： **多项式量级** 和 **非多项式量级** ，其中非多项式量级只有两个： :math:`O(2^n)` 和 :math:`O(n!)` ，这类算法问题叫做 NP 问题（非确定多项式问题，Non-Deterministic Polynomial）。

当数据规模 n 越来越大时， NP 问题的执行时间会变得无限长，所以 NP 类型的算法是非常低效的算法，不要使用，主要考虑 **多项式时间复杂度** 。

1. :math:`O(1)`

:math:`O(1)` 只是常量级时间复杂度的一种表示方法，并不是只执行了一行代码。下面这段代码有三行，但仍然是 :math:`O(1)` 。

.. code-block:: c
    :linenos:

    int i = 8;
    int j = 6;
    int sum = i + j;


一般情况下，只要算法中不存在循环语句、递归语句，即使有成千上万行的代码，其时间复杂度也是 :math:`O(1)` 。

2. :math:`O(logn)` 、 :math:`O(nlogn)`

对数阶时间复杂度非常常见，同时也是最难分析的一种时间复杂度，下面是一个例子：

.. code-block:: c
    :linenos:

    i = 1;
    while (i <= n) {
        i = i * 2;
    }


上面这个代码的 while 循环中， ``i`` 的取值是个等比数列：

.. math::

    2^0 \quad 2^1 \quad 2^2 \quad 2^3 \quad \dots \quad 2^k \quad \dots \quad 2^x = n


由 :math:`2^x = n` 可求解 :math:`x = log_2{n}`

所以，这段代码的时间复杂度是 :math:`O(log_2{n})` 。

如果某个代码的时间复杂度是 :math:`O(log_3{n})` ，因为 :math:`log_3{n} = log_3{2} \times log_2{n}` ，所以不管对数的底数是多少，都可以看做 :math:`O(logn)` 。

结合之前的思路，如果一个函数调用了 n 次一个时间复杂度为 :math:`O(logn)` 的函数，那么整体程序的时间复杂度就是 :math:`O(nlogn)` 。

另外，归并排序和快速排序的时间复杂度都是 :math:`O(n logn)` 。

3. :math:`O(m+n)` 、 :math:`O(m \times n)`
    
看下面这个代码：

.. code-block:: c
    :linenos:

    int cal(int m, int n) {
        int sum_1 = 0;
        int i = 1;
        for (; i < m; ++i) {
            sum_1 = sum_1 + i;
        }

        int sum_2 = 0;
        int j = 1;
        for (; j < n; ++j) {
            sum_2 = sum_2 + j;
        }
        return sum_1 + sum_2;
    }


上面的代码中，m 和 n 都表示数据规模，无法判断谁大谁小，因此都要考虑，所以这个程序的时间复杂度就是 :math:`O(m+n)` 。


什么是空间复杂度
------------------------------------

空间复杂度是 **算法的存储空间与数据规模之间的增长关系** 。

看下面这个代码：

.. code-block:: c
    :linenos:

    void print(int n) {
        int i = 0;
        int[] a = new int[n];
        for (i; i < n; ++i) {
            a[i] = i * i;
        }
        for (i = n - 1; i >= 0; --i) {
            print out a[i]
        }
    }


这段代码的空间复杂度是 :math:`O(n)` ，因为都是在长度为 n 的一个数组里面操作。

常见的空间复杂度就是 :math:`O(1)` 、 :math:`O(n)` 、 :math:`O(n^2)` ，像 :math:`O(logn)` 、 :math:`O(nlogn)` 这样的基本见不到。

有四个复杂度方面的知识点： **最好情况时间复杂度** 、 **最坏情况时间复杂度** 、 **平均情况时间复杂度** 、 **均摊时间复杂度** 。

最好、最坏情况时间复杂度
-------------------------------------------------------

看这段代码：

.. code-block:: c
    :linenos:

    // n 表示数组 array 的长度
    int find(int[] array, int n, int x) {
        int i = 0;
        int pos = -1;
        for (; i < n; ++i) {
            if (array[i] == x) pos = i;
        }
        return pos;
    }

这段代码的作用是返回 x 在 array 中的索引，如果没找到，就返回 -1 ，按照上面的思路，这段代码的复杂度是 :math:`O(n)` 。

实际上，如果中途找到了这个数据，就不用继续遍历了，所以代码可以这样修改：

.. code-block:: c
    :linenos:

    // n 表示数组 array 的长度
    int find(int[] array, int n, int x) {
        int i = 0;
        int pos = -1;
        for (; i < n; ++i) {
            if (array[i] == x) {
                pos = i;
                break;
            } 
        }
        return pos;
    }


修改后确实达到了目的，但这时的代码再用之前的方法去分析时间复杂度，好像就不太清晰了。

如果 x 恰好在数组的第一位，那么就是 :math:`O(1)` ，如果 x 恰好在数组的最后一位，那么就是 :math:`O(n)` 。 也就是说，不同的情况下，复杂度是不一样的。

为了表示代码在不同情况下的时间复杂度，就引入了三个概念： **最好情况时间复杂度** （ :math:`O(1)` ）、 **最坏情况时间复杂度** （ :math:`O(n)` ）和 **平均情况时间复杂度** 。

最好和最坏都是比较极端的情况，发生的概率并不大，所以还要分析平均情况时间复杂度。

数据 x 在 array 中的情况共有 n+1 种。如果 x 在 array 中，有 0~n-1 ，也就是 n 种， x 还可能不在 array 中。

把每种情况下，需要查找的次数累加起来，然后再除以 n+1 ，就可以算出平均时间复杂度。

.. math::

    \frac{1+2+3+\dots+n+n}{n+1}=\frac{n(n+3)}{2(n+1)}

按照原则，常量、系数、低阶可以省略，所以这个公式简化之后就是 :math:`O(n)` 。

   
 | # pandoc 编译 rst 的 latex 方法
 | pandoc 00_note.rst --webtex -o 00_note.html

但是，其实这 n+1 种情况，每一种出现的概率并不是一样的。

假设 x 在 array 中的概率和不在的概率均为 :math:`\frac{1}{2}` 。

在 x 存在于 array 的情况下， x 出现在 0~n-1 这 n 个位置上的概率也是一样的，都是 :math:`\frac{1}{n}` 。

所以， x 出现在 0~n-1 这 n 个位置的概率为： :math:`\frac{1}{2} \times \frac{1}{n} = \frac{1}{2n}` 。

由此，把各种情况发生的概率都考虑上，计算如下：

.. math::

   1 \times \frac{1}{2n} + 2 \times \frac{1}{2n} + 3 \times \frac{1}{2n} + \dots + n \times \frac{1}{2n} + n \times \frac{1}{2} = \frac{3n+1}{4}

这个值就是概率论中的 **加权平均值** ，也叫做 **期望值** ，所以平均时间复杂度的全称应该叫  **加权平均时间复杂度** 或者 **期望时间复杂度** 。

去掉系数和常量之后，这段代码的加权平均时间复杂度是 :math:`O(n)` 。

均摊时间复杂度
------------------------------

平均复杂度用的比较少，均摊时间复杂度用的更少。看下面的代码：

.. code-block::c
   :linenos:

   // arrary 表示一个长度为 n 的数组
   // 代码中的 array.length 就等于 n
   
   int[] array = new int[n];
   int count = 0;

   void insert(int val) {
       if (count == array.length) {
           int sum = 0;
           for (int i = 0; i < array.length; ++i) {
               sum = sum + array[i];
           }
           array[0] = sum;
           count = 1;
       }

       array[count] = val;
       ++count;

   }
   



