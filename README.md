# 哈尔滨工业大学高级算法实验

by GJ.
## 实验一：分治算法

1. 枚举方法 
1. Graham-Scan
1. 分治方法

```shell
$ python -m divide_and_conquer --help

options:
  -h, --help       show this help message and exit
  --num NUM        number of points to generate
  --method METHOD  method to use: enum, graham, divide, all
  --plot           plot the points and the convex hull
  --seed SEED      seed for random number generation
  --profile        profile the code
```

## 实验二：A*搜索算法

1. 单向A*搜索
1. 双向A*搜索

```shell
$ python -m a_star_search --help 

options:
  -h, --help       show this help message and exit
  --maze MAZE      maze to use
  --method METHOD  method to use: uni, bi
```


## 实验三：近似算法

1. 基于贪心搜索的方法
1. 基于线性规划的方法

```shell
$ python -m approximate --help

options:
  -h, --help       show this help message and exit
  --num NUM        number of data points
  --method METHOD  method to use: greedy, lp
  --seed SEED      random seed
```