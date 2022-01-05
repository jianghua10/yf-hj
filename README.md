基于Windows(仅限于yf的电脑)：#本地仓库:/桌面/yf-hj/yf-hj; 远端仓库: 网页上的 https://github.com/jianghua10/yf-hj.git

一. 从github远程仓库更新代码到本地，即从这个网页上下载最新的代码到自己的电脑
1. 打开桌面上的"yf-hj"文件夹，再进入一次里面的"yf-hj"文件夹（即本地仓库）
2. 在空白处右键，再点击”Git Bash“打开cmd（必须在本地仓库里打开这个）
3. git status #在Git Bash里面执行该命令，可以查看本地仓库和远端仓库的代码是否一致； 这步也可以省略
4. git checkout main #切换到main分支上，这步是以防万一；不用理解，直接执行就好。
5. git pull https://github.com/jianghua10/yf-hj.git #下载远端仓库的代码到本地仓库
6. 下载完毕！

二. 从本地仓库添加代码到远端仓库
0. 在本地仓库进入Git Bash
(0.1 git checkout 分支名 #在自己的分支下工作，可不执行。特殊的这里是：git checkout yf)
1. 在本地仓库做改动，比如修改文件，添加文件啥的都行
2. git add 文件名 #创建文件和仓库的连接
3. git commit -m”想说的注释的话“ #给上传加个注释，比如说git commit -m"change Hello.txt"意味着这次上传我改变了Hello.txt文件。最好加上
5. git status #可不执行
6. git checkout main #最好执行，切换到main分支上
(6.1 git merge --no-ff -m"注释" yf #合并分支，并且不删除yf分支)
7. git push origin main #上传本地仓库的代码到远端仓库
(7.1 git push origin yf #更新yf分支)
8. 上传结束！

Mac Os系统操作类似。
