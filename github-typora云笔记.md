# 利用github和typora进行云笔记配置

## typora配置

### 找到CSS文件

打开**文件——偏好设置——外观——打开主题文件夹**，可以进入typora存放主题的文件夹，以.css为后缀的文件表示主题的样式，如github.css可以控制github的主题，在修改之前先对原文件进行复制，**对复制的文件进行修改然后改名**，否则一旦typora更新，所有的修改会恢复原样，修改时可以可以用vscode打开文件。

### 修改字体

将正文文本修改成微软雅黑要在body参数下修改，将代码块中的字体更改为[更纱黑体](https://mirrors.tuna.tsinghua.edu.cn/github-release/be5invis/Sarasa-Gothic/)或者[source code pro](https://github.com/adobe-fonts/source-code-pro)则要在code下的tt参数下修改，代码如下：

```css
body{
    font-family:"微软雅黑";/*将正文文本修改为微软雅黑*/
    color:#rgb(51,51,51);
    line-height:1.6;
}
--------------------------------------------------------------------------------------------------------
tt{
    font-family:更纱黑体；/*修改代码块字体为更纱黑体*/
}

```

### 修改背景

github默认的白色背景看久了眼睛不舒服，可以修改背景，也可以换主题，这是是修改参数，:root是设置typora背景色的参数，位于第一行，但要注意它不会影响正文版面，只会修改大纲页面的背景颜色，所以还要添加content参数，才能将整个背景修改；还有代码块的背景，它需要修改.code下面的.md-fences参数；将大纲和正文版面以及代码块都设置为羊皮纸类似的颜色 :#d9d0bc,代码如下：

```css
:root{
    --side-bar-bg-color:#d9d0bc;/*将大纲页面设置成羊皮纸的颜色*/
    --control-text-color:#777;
}
--------------------------------------------------------------------------------------------------------
content{
    backgroud-color:#d9d0bc;/*将正文版面设置成羊皮纸的颜色*/
}
--------------------------------------------------------------------------------------------------------
.md-fences {
    background-color:#d9d0bc/*代码块颜色*/
}
```

## git配置

### git下载和创建存储库

本人使用的是WSL(Windows系统下的Linux子系统)进行安装的，发行版本是Arch Linux，打开Windows Terminal后输入命令sudo pacman -S git 就可以安装完成，然后就在github上创建一个repository(存储库)，，创建的时候可以勾选readme(自述文件)，然后就可以准备将本地的文件push(推送)到新建的存储库中。

### 设置SSH key

在推送之前要设置SSH key，打开windows powershell,输入以下命令：

```
ssh-keygen -t rsa -C "email"  //email是github上注册的邮箱
```

接着会出现以下提示，这是要求设置存放密钥文件的名字，可任意设置，如当输入key后，就在C:\Users\username下面建立了一个key.pub的文件，这个文件里面存放着ssh密钥，然后就会让你设置密码，可设可不设，不设可直接按enter键跳过，如下：

```powershell
Enter file in which to save the key (C:\Users\username/.ssh/id_rsa): key /*设置文件名*/
Enter passphrase (empty for no passphrase)：/*若不设密码可按enter键跳过，接下来会有多个类似的提示出现，但都可以跳过*/

/*出现下面的图形时说明已经设好了，可以在C:\Users\Username下面找到key.psh,用记事本打开就是密钥，然后将其复制到github setting 里的ssh key中就完成了。*/
+---[RSA 3072]----+
|E.o..            |
|o++o +           |
|*o+.+ o.         |
|=* ..++.         |
|o.o. o=oS        |
|.o  .++o. . .    |
|+   o... . o     |
| .   +.. ...     |
|    *B=.. ..o.   |
+----[SHA256]-----+
```

### 推送本地文件到github

如果在本地有一个名为TEST文件夹里面的文件需要推送到GITHUB的存储库中，要先打开wsl，利用命令cd /mnt/c/../test定位到这个文件目录中,其中ｃ表示ｃ盘，然后输入以下命令：

```shell
git init　 //对文件夹初始化，在此文件夹中生成.git文件
find . -name ".git" | xargs rm -Rf //删除生成的.git文件

git config user.email "email" //告诉github注册的邮箱
git config user.name "name" 　//告诉github用户名
git add .   //.后面有空格，将所有的文件添加到暂存目录中
git '文件名' //添加单个文件

/*如果要同步vim的配置文件，可以将.vimrc移动到.vim目录，再进行软链接,命令如下：*/
mv ~/.vimrc ~/.vim/.vimrc
ln -s ~/.vim/.vimrc ~/.vimrc

git status  //查看文件添加状态
git commit -m "注释 "  
/*对添加的文件拍照，然后提交给commit history*/

git remote add origin https://github.com/name/test.git   
/*将github的存储库与本地仓库进行关联，在repositories/name/code/http复制*/

git remote -v //查看远程库信息
git remote rm origin  
/*若地址输入错误，可解除本地库与远程库的绑定*/


git pull origin main --allow-unrelated-histories  /*若本地没有云端的readme文件，可用此命令将远程分支和本地分支合并再推送代码*/

git checkout -b main // 将分支从master切换到main
git push origin main -f /*f是强制的意思，将本地库的内容强制推送到远程仓库中的main分支上，后面会提示需要输入密码，有可能会出现错误提示*/
```

当出现错误提示：fatal: unable to access '存储库地址': HTTP/2 stream 1 was not closed cleanly before end of the underlying stream时，可能是代理问题，输入下面命令：

```shell
git config --global  --unset http.proxy
git config --global  --unset https.proxy
```

当出现错误提示：fatal: Authentication failed时，可能是输入了错误的密码，其密码不是github的登陆密码，而是[个人访问令牌](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)，生成令牌的页面不要马上退出，因为退出后令牌页面就无法进入，所以要先将令牌复制后再退出，**忘记令牌的话直接再生成一个访问令牌，**在wsl终端中输入令牌建议不要直接输入，本人失败了好几次，建议使用windows快捷键win+v打开剪贴板进行粘贴，成功率高。

### 更新变动的本地文件

当对本地文件进行了修改，并且想要将变动过的文件推送到云端存储库，可输入以下命令：

```shell
git status //查看文件是否更改并进行跟踪
git add -A //表示把status中的所有跟踪文件中被修改过或已删除文件信息添加到暂存区
git commit -a -m "update" 
git push origin main -f 
```



