Git Remote（远程仓库管理）是协同开发中不可或缺的核心功能。它用于连接本地仓库与托管在 GitHub、GitLab、Gitee 等平台上的远程仓库。

以下是 `git remote` 的所有常用命令及详细用法解析：

---

### 一、 查看与检索

* **`git remote`**
* **作用**：列出所有远程仓库的简写名称（通常默认是 `origin`）。


* **`git remote -v`** (或 `--verbose`)
* **作用**：列出所有远程仓库的简写及其对应的 **URL 地址**（区分 fetch 和 push 地址）。


* **`git remote show <remote>`**
* **作用**：查看某个特定远程仓库的详细信息，包括 URL、分支跟踪情况、`git pull` 和 `git push` 的默认设置。



---

### 二、 添加与配置

* **`git remote add <remote> <url>`**
* **作用**：添加一个新的远程仓库。
* **示例**：`git remote add origin [https://github.com/username/repo.git](https://github.com/username/repo.git)`


* **`git remote rename <old> <new>`**
* **作用**：重命名远程仓库的简写。
* **示例**：`git remote rename origin upstream`


* **`git remote remove <remote>`** (或 `rm`)
* **作用**：删除指定的远程仓库（仅解除本地关联，不影响远程服务器上的代码）。
* **示例**：`git remote remove origin`



---

### 三、 修改 URL

* **`git remote set-url <remote> <newurl>`**
* **作用**：修改指定远程仓库的 URL（常用于从 HTTPS 切换到 SSH，或迁移仓库地址）。
* **示例**：`git remote set-url origin git@github.com:username/repo.git`


* **`git remote set-url --add <remote> <newurl>`**
* **作用**：为同一个远程仓库添加一个**额外的推送 URL**（实现一次 push 推送到多个托管平台）。



---

### 四、 同步与清理

* **`git remote prune <remote>`**
* **作用**：清理远程仓库上已经被删除、但本地仍然存在的远程跟踪分支（例如清理别人在远程已经删除的分支）。
* **示例**：`git remote prune origin`


* **`git fetch --prune <remote>`** (或简写 `git fetch -p`)
* **作用**：在抓取远程更新的同时，顺便清理本地失效的远程分支（比单独执行 prune 更常用）。
