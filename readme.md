# AutoBackup

定时自动备份网页的脚本

## 开发思路

- Blazing fast generating
- Support for GitHub Flavored Markdown and most Octopress plugins
- One-command deploy to GitHub Pages, Heroku, etc.
- Powerful plugin system

**确定功能**

- 可以指定网页的地址
- 定时自动备份
- 指定输出的文件夹
- 不同的备份以时间作为目录名分开存储

**总体思路**

程序由几个部分组成：下载网页，分析网页提取其中的链接，下载静态资源，定时备份控制部分。
在把所有资源下载好之后，还要修改网页中的链接，使其指向本地的资源。

