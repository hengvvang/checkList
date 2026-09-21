`git tag` 是 Git 中用于给仓库历史中的某一提交打上永久性标记的命令，常用于标记软件发布版本（如 `v1.0.0`）。

在 Git 底层，标签本质上是一个指向特定提交对象的引用，存储在 `.git/refs/tags/` 目录下。

---

## 1. 核心概念：轻量标签 vs 附注标签

Git 标签分为两种主要类型：

| 特性 | 轻量标签 (Lightweight Tag) | 附注标签 (Annotated Tag) |
| --- | --- | --- |
| **底层实现** | 纯引用（直接指向 Commit 对象的 SHA-1） | 独立对象（包含 Tag 对象，再指向 Commit） |
| **元数据** | 不包含打标签者、日期或独立消息 | 包含打标签者、打标时间、GPG 签名及附注消息 |
| **存储位置** | `.git/refs/tags/<tagname>` 存 Commit 校验和 | `.git/refs/tags/<tagname>` 存 Tag 对象校验和 |
| **适用场景** | 临时标记、个人本地调试、工作流内部断点 | 正式发布（Release）、生产部署、团队共享 |

---

## 2. 标签的创建 (Creation)

### 2.1 语法结构

```bash
git tag [-a | -s | -u <keyid>] [-f] [-m <msg> | -F <file>] <tagname> [<commit> | <object>]
git tag <tagname> [<commit>] # 轻量标签

```

### 2.2 核心参数详解

* `-a`, `--annotate`：创建附注标签（Annotated tag）。如果不提供 `-m`，Git 会启动配置的文本编辑器要求输入标签说明。
* `-m <msg>`, `--message=<msg>`：直接在命令行指定标签附注说明文字。
* `-F <file>`, `--file=<file>`：从指定文本文件中读取标签说明信息。若传入 `-`，则从标准输入（stdin）读取。
* `-s`, `--sign`：使用系统默认的 GPG 密钥对标签进行加密签名。
* `-u <keyid>`, `--local-user=<keyid>`：使用指定的 GPG 密钥 ID 对标签进行签名。该参数会隐式开启 `-a`。
* `-f`, `--force`：强制覆盖已存在的同名标签。
* `<tagname>`：标签名称。推荐遵循语义化版本规范（如 `v2.1.0`）。
* `[<commit>]`：可选参数。指定标签绑定的 Commit SHA-1、分支名或相对引用（如 `HEAD~2`）。若缺省，默认指向当前检出的 `HEAD`。

### 2.3 命令示例

```bash
# 1. 在当前 HEAD 创建轻量标签
git tag v1.0.0-light

# 2. 在当前 HEAD 创建附注标签并附带单行消息
git tag -a v1.0.0 -m "Release version 1.0.0: Initial public release"

# 3. 指定历史特定提交（SHA-1 为 9fceb02）打附注标签
git tag -a v0.9.0 9fceb02 -m "Beta release before refactoring"

# 4. 从 release_notes.txt 文件中读取长文本作为标签说明
git tag -a v1.1.0 -F ./docs/release_notes.txt

# 5. 使用 GPG 默认密钥创建已签名的标签
git tag -s v1.2.0 -m "Signed release 1.2.0"

# 6. 使用特定的 GPG 密钥（Key ID: ABCD1234）创建签名标签
git tag -u ABCD1234 v1.2.1 -m "Signed release with specific key"

# 7. 强制移动/更新已存在的标签到当前提交
git tag -f -a v1.0.0 -m "Updated release 1.0.0 tag to include hotfix"

```

---

## 3. 标签的查看与检索 (Listing & Inspection)

### 3.1 语法结构

```bash
git tag [-l | --list] [-n[<num>]] [--sort=<key>] [--points-at <object>] 
        [--contains [<commit>]] [--no-contains [<commit>]] [--merged [<commit>]] 
        [--no-merged [<commit>]] [<pattern>...]
git show <tagname>
git describe [<commit-ish>...]

```

### 3.2 核心参数详解

* `-l`, `--list`：列出匹配模式的标签。缺省 pattern 时等同于列出全部标签。
* `-n[<num>]`：在列表输出中显示每个标签说明的前 `<num>` 行。默认 `<num>` 为 1；如果未指定 `-n`，则仅显示标签名。
* `--sort=<key>`：指定排序规则。常用键值包括：
* `refname` 或 `version:refname`（按语义化版本排序，如 `v1.2` 排在 `v1.10` 前面）。
* `creatordate`（按标签创建时间排序）。
* 在键名前加 `-` 表示降序（例如 `--sort=-version:refname`）。


* `--points-at <object>`：筛选出直接指向特定对象（Commit、Tag 等）的所有标签。
* `--contains [<commit>]`：仅列出包含指定提交的历史链中的标签。
* `--no-contains [<commit>]`：仅列出不包含指定提交的标签。
* `--merged [<commit>]`：仅列出其指向的提交已被指定提交所合并的标签。
* `--no-merged [<commit>]`：仅列出其指向的提交尚未被合并进指定提交的标签。
* `<pattern>`：支持通配符模式匹配（如 `"v1.*"` 或 `"*-beta"`）。
* `--format=<format>`：使用自定义格式串格式化输出（支持与 `git for-each-ref` 相同的占位符语法，如 `%(refname:short)`、`%(taggerdate)`）。

### 3.3 命令示例

```bash
# 1. 基础列出所有标签（字母序）
git tag

# 2. 匹配列出所有 v1.x 系列的标签，并展示附注说明的前 2 行
git tag -l "v1.*" -n2

# 3. 按语义化版本降序排列（最新版本显示在最上方）
git tag -l --sort=-version:refname

# 4. 按创建时间升序排列显示
git tag -l --sort=creatordate

# 5. 查找指向当前 HEAD 的所有标签
git tag --points-at HEAD

# 6. 查找包含某个 Bug 修复提交（Commit: a1b2c3d）的所有后续发布标签
git tag --contains a1b2c3d

# 7. 查看标签元数据及关联的提交详情
git show v1.0.0

# 8. 验证 GPG 签名标签的合法性
git tag -v v1.2.0

# 9. 格式化输出：输出“标签名 | 创建日期 | 创建者”
git tag -l --format="%(refname:short) | %(creatordate:iso8601) | %(taggername)"

```

---

## 4. 标签的删除与重命名 (Deletion & Renaming)

Git 原生没有独立的 `rename` 子命令，标签的重命名通过“建立新标签 + 删除旧标签”实现。

### 4.1 语法结构

```bash
git tag -d <tagname>...
git tag --delete <tagname>...

```

### 4.2 核心参数详解

* `-d`, `--delete`：从本地仓库删除指定的标签引用。支持一次性传入多个标签名。

### 4.3 命令示例

```bash
# 1. 删除本地单个标签
git tag -d v0.9.0-alpha

# 2. 批量删除多个本地标签
git tag -d v0.9.0-rc1 v0.9.0-rc2

# 3. 重命名本地标签（将 old-tag 重命名为 new-tag）
git tag new-tag old-tag
git tag -d old-tag

```

---

## 5. 远程标签同步 (Remote Operations)

`git push` 默认策略**不会**自动将本地创建的标签推送到远程仓库，必须显式声明。

### 5.1 推送标签到远程

```bash
# 1. 推送单个指定标签到远程仓库 origin
git push origin v1.0.0

# 2. 推送本地所有尚未推送到远程的标签
git push origin --tags

# 3. 随分支提交同时推送相关标签（仅推送该分支可达的附注标签，常用且安全）
git push origin main --follow-tags

# 4. 强制更新远程标签（当本地通过 -f 覆盖了同名标签时使用）
git push origin v1.0.0 --force

```

### 5.2 删除远程标签

```bash
# 1. 使用 --delete 参数显式删除远程标签（推荐，现代 Git 语法）
git push origin --delete v1.0.0

# 2. 传统 Refspec 语法删除（推送一个空引用覆盖远程标签）
git push origin :refs/tags/v1.0.0

```

### 5.3 从远程拉取/同步标签

```bash
# 1. 抓取远程所有提交和标签
git fetch origin

# 2. 仅抓取远程标签，不抓取其他引用
git fetch origin 'refs/tags/*:refs/tags/*'

# 3. 强制拉取远程标签并覆盖本地冲突的同名标签
git fetch origin --tags --force

```

---

## 6. 标签的检出与操作 (Checkout & Workflows)

标签指向不可变的提交对象。如果直接针对标签执行检出，Git 会进入“头指针分离”（Detached HEAD）状态。

### 6.1 常用操作与工作流

```bash
# 1. 查看/体验指定标签的代码（进入 Detached HEAD 状态，不可直接在此状态下做提交）
git checkout v1.0.0
# 或者使用 switch（需要脱离当前分支）
git switch --detach v1.0.0

# 2. 基于标签创建并切换到一个新的开发分支（修复发布分支常见做法）
git checkout -b hotfix-v1.0.1 v1.0.0
# 或者使用现代命令
git switch -c hotfix-v1.0.1 v1.0.0

# 3. 生成最接近当前提交的易读版本描述（基于标签生成版本号）
# 格式输出形如：<最近标签>-<自该标签以来的commit数>-g<当前commit简短hash>
git describe --tags --always

```

---

## 7. 常见问题排查与高级维护

### 7.1 本地存在远程已删除的孤立标签

如果团队成员在远程删除了标签，执行普通的 `git fetch` 或 `git pull` 不会自动清理你本地的旧标签缓存。

```bash
# 1. 清理本地所有在远程已经不存在的标签引用（同步删除）
git fetch origin --prune --prune-tags

# 2. 或者在全局/本地配置中默认开启自动清理
git config fetch.pruneTags true

```

### 7.2 区分轻量标签与附注标签的底层状态

通过底层命令 `cat-file` 可以直接验证对象类型：

```bash
# 验证轻量标签：输出为 commit，直接指向提交
git cat-file -t v1.0.0-light

# 验证附注标签：输出为 tag，指向一个独立的 Tag 对象
git cat-file -t v1.0.0

# 查看附注标签本身的底层对象信息（创建者、时间戳、绑定的 Commit SHA-1 等）
git cat-file -p v1.0.0

```
