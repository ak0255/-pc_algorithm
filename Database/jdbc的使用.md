# JDBC连接数据库（一步步来）

## 需要：

>  idea或者eclipse等可以编译java的
>
>  MySQL（这里为8.0版本）
>
>  jdbc的jar包（同需要8.0的版本）

[MySQL官方下载](https://dev.mysql.com/downloads/installer/)

下载的时候选择那个体积大的是客户端的，那个体积小的是web的，都是32位，不用找64位了，没有64的

[jdbc的jar包官方下载](https://dev.mysql.com/downloads/connector/j/)

1、点击Select Operating System:下的选项

2、选择platform Independent

3、第一个是tar.gz的压缩包，第二个zip的压缩包，一般下第二个

下载完以后解压缩，点进去找到mysql-connector-java-8.0.25.jar就行了

这个就是我们需要用到的jar包

## 准备环境

打开idea，新建一个项目jdbc，在项目的当前目录下创建一个lib的目录
![](https://img2020.cnblogs.com/blog/2449877/202108/2449877-20210813162557697-65496817.png)
将我们上面讲到的jar包单个文件**(不要复制整个文件夹)**
![](https://img2020.cnblogs.com/blog/2449877/202108/2449877-20210813162852660-1217445962.png)

复制粘贴到lib目录下，右键lib目录
![](https://img2020.cnblogs.com/blog/2449877/202108/2449877-20210813163002008-1058192711.png)
点击，然后直接确定，我这里是汉化过的，如果是英文的，找一下对应的就行
这时你的jar包在lib目录应该是这样的
![](https://img2020.cnblogs.com/blog/2449877/202108/2449877-20210813163104582-1387196979.png)
那么就代表添加jar包成功了，就可以使用了
## 基本应用
前提是已经掌握了基本的数据库中表的增删改查，不掌握也问题不大，下面会解释
先建一个数据库，这里我直接拿狂神说的mysql中一个数据库
```sql
 # 创建一个名为jdbc数据库，编码用utf-8
CREATE DATABASE jdbcstudy CHARACTER SET utf8 COLLATE utf8_general_ci;

USE jdbcstudy;
# 在这个数据库中创建一个名为users的表，里面有5个数据id、NAME 、PASSWORD 、email 、birthday 
CREATE TABLE `users`(
	id INT PRIMARY KEY,#primary key表示这个是主键
	`NAME` VARCHAR(40),
	`PASSWORD` VARCHAR(40),
	email VARCHAR(60),
	birthday datetime
);
# 为表添加一些信息
INSERT INTO `users`(id,`NAME`,`PASSWORD`,email,birthday)
VALUES(1,'zhansan','123456','zs@sina.com','1980-12-04'),
(2,'lisi','123456','lisi@sina.com','1981-12-04'),
(3,'wangwu','123456','wangwu@sina.com','1979-12-04');
```
这样我们就建好一个表了，然后到idea中
在src中新建目录和java项目，先填写一下基本的结构，然后一个一个讲
```java
package com.ou.lesson01;

import com.mysql.cj.protocol.Resultset;

import java.sql.*;

//我的第一个JDBC程序
public class jdbcFirstDemo {
    public static void main(String[] args) {
        // 1、加载驱动
        Connection connection = null;
        Statement statement = null;
        ResultSet resultSet = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");//加载驱动、8.0写法，如果是5.0就不用写cj

            // 2、用户信息和url
            String url = "jdbc:mysql://localhost:3306/jdbcstudy?useUnicode=true&characterEncoding=utf8&usrSSl=true";
            String username = "root";
            String password = "root";

            // 3、连接成功，数据库对象
            connection = DriverManager.getConnection(url, username, password);

            // 4、执行SQL对象
            statement = connection.createStatement();

            // 5、执行SQL，可能存在加过，查看返回结果
            String sql = "select * from users;";
            resultSet = statement.executeQuery(sql);
            while(resultSet.next()){
                System.out.println("id = " + resultSet.getInt("id"));
                System.out.println("name = " + resultSet.getString("NAME"));
                System.out.println("pwd = " + resultSet.getObject("PASSWORD"));
                System.out.println("email = " + resultSet.getObject("email"));
                System.out.println("birth = " + resultSet.getObject("birthday"));
            }
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            // 6、释放连接
            try {
                assert connection != null;
                assert statement != null;
                assert resultSet != null;
                connection.close();
                statement.close();
                resultSet.close();
            } catch (SQLException throwables) {
                throwables.printStackTrace();
            }
        }
    }
}
```

## jdbc中三个常用类
- **前言**

**加载驱动 `Class.forName("com.mysql.cj.jdbc.Driver");`**

**`String url = "jdbc:mysql://localhost:3306/jdbcstudy?useUnicode=true&characterEncoding=utf8&usrSSl=true";`**
**这相当于一些信息，如果你用的Oracle的话，就不是这样写，这里只针对MySQL，首先jdbc:mysql://声明一下，然后跟自己主机端号localhost:3306，其中MySQL对应的是3306，之后再跟jdbcstudy数据库名称，你的是什么就填什么**
**写到这里其实已经结束了，为了准确性和稳定性，一般再用?隔开加上三个属性，之间用&隔开useUnicode=true&characterEncoding=utf8&usrSSl=true**
**其中useUnicode=true表示是否使用Unicode字符集，true就是使用，characterEncoding=utf8表示使用utf8编码，usrSSl=true可以使我们减少一些不必要的错误，一般情况我们也会加上serverTimezone=UTC是指定时区时间为世界统一时间**
`String username = "root";`
`String password = "root";`
这两个比较容易理解，就是我们数据库最初的账号和密码，我最开始设置的root

由于数据库的连接可能失败，所以我先把三个类的对象放在了外面初始化，并用try catch环绕了其他代码
```java
Connection connection = null;
Statement statement = null;
ResultSet resultSet = null;
```

### Connection
connection其实就相当于一个数据库对象，我们通过`connection = DriverManager.getConnection(url, username, password);`来把我们的数据库信息、账号和密码传入，然后通过DriverManager的getConnection方法连接到数据库
### Statement

连接到了数据库，我们需要有一个SQL对象，也就是Statement这个类，通过`statement = connection.createStatement();`来通过数据库，得到我们的statement对象，然后就可以通过对这个对象的execute方法来进行操作了

**execute稍微提一下这个方法，它有很多种实现方式，比如executeQuery、executeUpdate都是字面意思，一个对应查询，一个对应更新，更新的话就是增删那些，execute是通用的**

那么如果操作呢，只要先把sql语句写好，然后放入就可以了，当然直接在方法里面写也是可以的
![](https://img2020.cnblogs.com/blog/2449877/202108/2449877-20210813170032267-172257918.png)


### ResultSet
操作也做了，那值呢，这就需要一个ResultSet类来接收了，`resultSet = statement.executeQuery(sql);`，这样resultSet就拿到了这个值

resultSet其实是一个指向其当前数据行的指针，为了得到我们的结果，我们要用一个方法叫next()，通过while就可以一行一行的遍历了
![](https://img2020.cnblogs.com/blog/2449877/202108/2449877-20210813170240294-7572520.png)

当然，上面只是遍历了，对于每一行的值，我们只要get方法就行了，对于int我们有getInt方法，对于字符串我们有getString，还有通用的getObject

通过将我们要查找的这一行的那个元素的名称传入，就可以查到这一行的数据了

`System.out.println("id = " + resultSet.getInt("id"));`

最后别忘了关闭资源