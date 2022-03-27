### 一、安装git

1. 官方网址：[Git - Downloading Package (git-scm.com)](https://git-scm.com/download/mac)

2. 命令行：```brew install git```



### 二、配置Git SSH

1. 是否配置SSH的区别

   HTTPS可随意clone或者push项目于或到github，不管谁的项目； SSH必须是项目的拥有者，且需要添加SSH key。

   HTTPS url在push时需要验证用户名和密码；
   SSH在push时可设置成无用户名密码，相对方便。
   
1. 生成SSH

   ```
   ssh-keygen -t rsa -C 邮箱地址
   ```

   ```
   例：ssh-keygen -t rsa -C liuyenzhe@163.com
   ```
   
   <img src="/Users/liuyanzhe/Library/Application Support/typora-user-images/image-20220326000758191.png" alt="image-20220326000758191" style="zoom:50%;" />
   
   *如有问题，可查看：[(270条消息) Mac配置Git SSH秘钥_高先生的猫的博客-CSDN博客_mac配置git ssh](https://blog.csdn.net/z591102/article/details/105817938/)*
   
3. Github添加SSH

   id_rsa.pub 文件中的内容复制到GitHub设置中。

   Settings -> SSH and GPG keys -> New SSH key

   *如有问题，可查看：[(270条消息) Mac配置Git SSH秘钥_高先生的猫的博客-CSDN博客_mac配置git ssh](https://blog.csdn.net/z591102/article/details/105817938/)[(270条消息) github设置添加SSH_風月长情的博客-CSDN博客_github添加ssh](https://blog.csdn.net/Aaron_Miller/article/details/90269019)*

3. 验证是否成功

   ```
   ssh -T git@github.com
   ```

​		<img src="/Users/liuyanzhe/Library/Application Support/typora-user-images/image-20220326001517001.png" alt="image-20220326001517001" style="zoom:50%;" />

### 三、使用Git

1. ##### 初始化

   1）选择目录

   ```console
   cd 路径
   例：cd /Users/liuyanzhe/GitProject
   ```

   2）初始化

   ```console
   git init
   ```

   *如有问题，可查看[Git - 获取 Git 仓库 (git-scm.com)](https://git-scm.com/book/zh/v2/Git-基础-获取-Git-仓库)*

2. ##### 克隆仓库到本地

   ```
   git clone git@github.com:lyz21/untitled.git
   ```

3. ##### 更改/添加 文件

   必须按照顺序

   1）将更改文件放入暂存区

   ```
   git add ./readme.md
   ```

   ```
   git add . 	#添加所有更改的文件
   ```

   2）将更改文件提交本地仓库

   ```
   git commit -m '更改信息'
   ```

   3）将更改文件提交GitHub

   ```
   git push <远程主机名> <本地分支名>:<远程分支名>
   若本地分支与远程分支名字相同，则可省略:<远程分支名>
   git push <远程主机名> <本地分支名>
   
   例：git push origin master #将本地master分支推送到origin主机的master分支
   或
   git push -u origin master	#第一次提交需要加-u
   
   ```
   
   origin是远程库的默认名字
   
   master是一般github的分支名
   
   main是该项目的分支名
   
4. ##### 查看信息

   1） 获取远程分支数据

   与push类似

   ```
   git pull git push <远程主机名> <本地分支名>:<远程分支名>
   例：
   git pull origin master
   ```

   2） 查看状态

   ```
   git status
   ```

   3） 查看分支

   ```
   git branch
   ```

   *其他可参考：*

   *[Git - 关于版本控制 (git-scm.com)](https://git-scm.com/book/zh/v2/起步-关于版本控制)*

   *[Mac Git 安装和配置 - 阿豪的girl - 博客园 (cnblogs.com)](https://www.cnblogs.com/jaelynl/p/10330042.html)*

5. ##### 附录

   1）Git下载地址

   [Git - Downloading Package (git-scm.com)](https://git-scm.com/download/mac)

   2）Git官方文档

   [Git - 关于版本控制 (git-scm.com)](https://git-scm.com/book/zh/v2/起步-关于版本控制)

其它参考：

1. [Github 简明教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/w3cnote/git-guide.html)
2. [Git和Github简单教程 - schaepher - 博客园 (cnblogs.com)](https://www.cnblogs.com/schaepher/p/5561193.html)
2. [Mac Git 安装和配置 - 阿豪的girl - 博客园 (cnblogs.com)](https://www.cnblogs.com/jaelynl/p/10330042.html)