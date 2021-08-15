# MySQL基本类型、操作

## 前言（~~一些废话，可以不看~~）

为什么学习数据库呢，大家都知道，~~为了学习删库跑路~~，因为数据库在工作中起着至关重要的作用，**只会写代码的是码农；学好数据库，基本能混口饭吃；在此基础上再学好操作系统和计算机网络，就能当一个不错的程序员。 如果能再把离散数学、数字电路、体系结构、数据结构/算法、编译原理学通透，再加上丰富的实践经验与领域特定知识，就能算是一个优秀的工程师了。**~~（这是百度的）~~



> 在没有认识到数据库之前，我们程序运行的数据需要我们每次的输入，但是程序一旦结束，数据也就消失不见了，所以我们才要学习数据库，这样才能在网络中，~~混口饭吃~~真正的步入程序开发的一步



**数据库** ( **DataBase** , 简称**DB** )

**概念** : 数据库是“按照数据结构来组织、存储和管理数据的仓库”。是一个长期存储在**计算机**内的、有组织的、可共享的、统一管理的大量数据的集合。**(~~废话~~)**

数据库根据类型分为**关系型数据库**和**非关系型数据库**

常用关系型数据库（SQL）有：MySQL、Oracle、SQL Server等等，通过外键关联实现行与行、列与列、表与表的关系

常用的非关系型数据库（NOSQL ）有：Redis 、MongoDB等等，以对象的方式存储

**数据库管理系统** ( DataBase Management System )

数据库管理软件 , 科学组织和存储数据 , 高效地获取和维护数据，MySQL其实就是一个数据库管理系统。

**MySQL** 是最流行的**关系型数据库管理系统**，在 WEB 应用方面 MySQL 是最好的 RDBMS(Relational Database Management System：关系数据库管理系统)应用软件之一。

对于数据库的操作大概也分为了这四种，**增删查改**，大体又分为，**操作数据库**、**操作数据库中的表**、**操作表中的数据**

## 操作数据库

- **创建数据库**

首先在Navicat上新建一个查询

```mysql
create database wostos;# 创造一个database（数据库） 数据库的名字叫wostos
#当我们数据库中有这个名字的话，那么我们就会创建失败
#为了避免这种错误的发生，我们在建立数据库的时候，可以按照下面这种方式创建
create database if not exists wostos;#加上if not exists，就会先判断是否有这个名字存在，没有才会创建
```

- **删除数据库**

```mysql
drop database wostos;#删除数据库
#同理，如果没有这个名字，也会报错，所以我们通常也加上一个判断
drop database if exists wostos;#如果存在，我们就删除
```

- **查看数据库**

```mysql
show databases;#查看所有数据库，会把你的数据库一一列出来

show create database `数据库名称`;# 查看数据库定义
show create table `表名`;# 查看表的定义
```



## 数据类型

```mysql
#均可以加unsigned使其变成无符号，并范围加倍
```

- **粗体记一下就可以了，其他可以先不急**

| **MySQL数据类型** | **含义（有符号）**                                  |
| ----------------- | --------------------------------------------------- |
| tinyint           | 1个字节 范围(-128~127)                              |
| smallint          | 2个字节 范围(-32768~32767)                          |
| mediumint         | 3个字节 范围(-8388608~8388607)                      |
| **int**           | **4个字节 范围(-2147483648~2147483647)**            |
| bigint            | 8个字节 范围(+-9.22*10的18次方)                     |
| float             | 单精度浮点型  8位精度(4字节)      m总个数，d小数位  |
| double            | 双精度浮点型  16位精度(8字节)      m总个数，d小数位 |
| char              | 固定长度，最多255个字符                             |
| **varchar**       | **可变长度，最多65535个字符**                       |
| tinytext          | 可变长度，最多255个字符                             |
| **text**          | **可变长度，最多65535个字符**                       |
| mediumtext        | 可变长度，最多2的24次方-1个字符                     |
| longtext          | 可变长度，最多2的32次方-1个字符                     |

| 特殊类型      | 含义                                                         |
| ------------- | :----------------------------------------------------------- |
| date          | 日期 '2008-12-2' ，YYYY-MM-DD                                |
| time          | 时间 '12:25:36'，HH-mm-ss（h小写表示12小时制，H大写表示24小时制) |
| **datetime**  | **日期时间 '2008-12-2 22:06:44'**                            |
| **timestamp** | **时间戳 1970.1.1到现在的毫秒数**                            |
| year          | 年份表示                                                     |

| **MySQL关键字**    | **含义**                                                     |
| ------------------ | ------------------------------------------------------------ |
| NULL               | 数据列可包含NULL值                                           |
| NOT NULL           | 数据列不允许包含NULL值                                       |
| DEFAULT            | 默认值                                                       |
| PRIMARY KEY        | 设置主键                                                     |
| AUTO_INCREMENT     | 自动递增，适用于整数类型，通常用于设置**主键** , 且为整数类型 |
| UNSIGNED           | 无符号                                                       |
| CHARACTER SET name | 指定一个字符集                                               |

## 操作数据库中的表

**提示：在数据库中也有很多关键字，不管是取什么名称，尽量不要取关键字的名称，实在要取的话，需要在名字两边加上这个反引号`**

### 表的建立与删除

```sql
create table if not exists test (id int(4) primary key, `name` varchar(255), age int(4));
# create新建表，括号中是表的表的属性比如这里就是有三个属性id、name、age，类型分别为int、varchar、int，同理if not exists是判断当没有这个表的时候才创立，防止出错
drop table if exists test cascade;# drop删除表，cascade表示一种删除方式，不细讲，差不多是强制删的意思吧
```

### 表的修改

```sql
alter table test rename as test01;#修改表名称，将test改为了test01
alter table test add email varchar(255);# alter修改表，add表示添加字段
alter table test drop email;# 同理可以删除
#还有一个change，有兴趣可以搜索一下
```

### 增删改查

#### 查
**对这个表操作**
![](https://img2020.cnblogs.com/blog/2449877/202108/2449877-20210814094641803-1016083956.png)

```sql
select * from student;# select查询表（所有），*代表查询student表中所以信息

select id as 学号, `name` as 姓名 from student;# 查询列，起别名，这样我们查询出来结果，就是以我们起的别名显示（as可以省略）

select distinct `name` 姓名 from student;# distinct表示去重，有时候我们查出的结果会有重复，这样查询出内容并不重复的显示

select `name` 姓名 from student where sex = "男";# where待条件查询 where后跟条件（大部分条件会在代码下方放出来）

select count from student;# 查询表有多少行，还可以加一下修饰

select count(distinct `name`) from student;# 查询表有多少行name不重复的

select `name` from student group by `name` having name="张三";# 了解即可，group by分组查询会自动去掉重复的，条件需要用having，且只能但对象查询，比如这里只能看name
```

**常用条件**

**AND、OR、NOT分别对应且、或、非**

 **=，！=，<>分别对应等于、不等于、不等于**

**between and一起用，例如查询时`where age between 15 and 20;`表示查询年龄在15到20之间的**

**in, not in，分别表示包含、不包含**

**查询时也可以接受正则表达式，例如_表示一个通用字符，%可以表示任意个字符，但是需要用到like**

**where name like '__a'; 表示谁的name是三个字符，并且第三个是a**

**where name like '%a'; 表示谁的name中含有a在最后一个**

**对于判断是否为空需要使用 is NULL，值得一提的是没有判断NULL相等的**

#### 增删改

```sql
insert into student (ID, `name`, age, sex) values (1005, '哈哈', 19, '未知');# insert into插入 列可以省略表示全部插入
insert into test values # 批量插入 这里省略了指定列，所以表示全部插入，每一行的数据都要写全
(001, 'zhangshan', 18, 123),# 用，号隔开，最后一个不要加，
(002, 'wangwu', 19, 234),
(003, 'lisi', 20, 345);

update test set `name` = '哈哈' where id = 3;# update修改单个字段，可以配合where使用
update test set `name` = '哈哈', age = 666 where id = 3;# 修改多个字段

delete from test where id = 3;#delete删除，如果不指定where会全部删除
```













