```markdown
# Git 架构解析与权威命令参考手册

---

## 目录
- [第一部分：Git 全命令系统分类清单](#第一部分git-全命令系统分类清单)
- [第二部分：核心命令全维度详解](#第二部分核心命令全维度详解)
  - [1. 项目初始化与配置 (Repository Setup & Configuration)](#1-项目初始化与配置-repository-setup--configuration)
  - [2. 状态追踪与工作区快照 (Snapshotting & Working Tree)](#2-状态追踪与工作区快照-snapshotting--working-tree)
  - [3. 提交与历史审计 (Commits & Audit)](#3-提交与历史审计-commits--audit)
  - [4. 分支与引用漫游 (Branching & Navigation)](#4-分支与引用漫游-branching--navigation)
  - [5. 分支集成与历史重写 (Integration & Rewriting)](#5-分支集成与历史重写-integration--rewriting)
  - [6. 远端协同与传输 (Remote Collaboration)](#6-远端协同与传输-remote-collaboration)
  - [7. 工作进度隔离 (Stashing)](#7-工作进度隔离-stashing)
  - [8. 数据抢救与故障排查 (Forensics & Debugging)](#8-数据抢救与故障排查-forensics--debugging)
  - [9. 核心底层管线命令 (Core Plumbing)](#9-核心底层管线命令-core-plumbing)
- [第三部分：语法糖与全命令规范对照基准表](#第三部分语法糖与全命令规范对照基准表)

---

# 第一部分：Git 全命令系统分类清单

```text
GIT SYSTEM TAXONOMY
├─ 1. 项目初始化与配置 (Repository Setup & Configuration)
│  ├─ git init
│  ├─ git clone
│  └─ git config
├─ 2. 状态追踪与工作区快照 (Snapshotting & Working Tree)
│  ├─ git status
│  ├─ git add
│  ├─ git restore (现代核心规范)
│  ├─ git rm
│  └─ git mv
├─ 3. 提交与历史审计 (Commits & Audit)
│  ├─ git commit
│  ├─ git log
│  ├─ git diff
│  ├─ git show
│  └─ git blame
├─ 4. 分支与引用漫游 (Branching & Navigation)
│  ├─ git switch (现代核心规范)
│  ├─ git branch
│  ├─ git checkout (传统复用命令)
│  └─ git tag
├─ 5. 分支集成与历史重写 (Integration & Rewriting)
│  ├─ git merge
│  ├─ git rebase
│  ├─ git cherry-pick
│  ├─ git revert
│  └─ git reset
├─ 6. 远端协同与传输 (Remote Collaboration)
│  ├─ git remote
│  ├─ git fetch
│  ├─ git pull
│  └─ git push
├─ 7. 工作进度隔离 (Stashing)
│  └─ git stash
├─ 8. 数据抢救与故障排查 (Forensics & Debugging)
│  ├─ git reflog
│  ├─ git bisect
│  └─ git clean
└─ 9. 底层核心管线 (Core Plumbing)
   ├─ git cat-file
   ├─ git hash-object
   ├─ git ls-tree
   └─ git rev-parse

```

---

# 第二部分：核心命令全维度详解

---

## 1. 项目初始化与配置 (Repository Setup & Configuration)

### 1.1 `git config`

* **内核机制**：操作三级配置文件系统：
1. 系统级：`/etc/gitconfig`
2. 全局级：`~/.gitconfig`
3. 仓库级：`.git/config`
优先级依次递增（仓库级覆盖全局级）。



| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 范围指定 | `--system` | 无 | 操作操作系统级配置 | 影响机器上所有系统用户 |
| 范围指定 | `--global` | 无 | 操作当前操作系统的用户配置 | 影响当前用户的所有 Git 仓库 |
| 范围指定 | `--local` | 无 | 操作当前仓库配置 | 默认缺省选项，写入 `.git/config` |
| 范围指定 | `--worktree` | 无 | 操作特定工作树配置 | 仅当启用多工作树（worktree）时生效 |
| 读写控制 | `--get <key>` | 无 | 读取指定键的值 | 直接读取单项配置 |
| 读写控制 | `--get-all <key>` | 无 | 读取多值键的所有值 | 用于包含多个同名值的配置项 |
| 属性修饰 | `--list` | `-l` | 打印当前有效的所有变量列表 | 会按优先级合并所有层级文件 |
| 编辑控制 | `--edit` | `-e` | 调出系统编辑器直接编辑配置 | 打开对应作用域的文件 |
| 移除变量 | `--unset <key>` | 无 | 彻底移除指定键 | 不存在时返回状态码 5 |

```bash
# 标准规范写法 (显式指定范围与键值)
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
git config --local core.autocrlf false

# 读取与查看全量配置来源
git config --list --show-origin

```

> **专著注释**：在自动化构建流水线与 Docker 容器镜像编译中，必须显式通过 `--system` 或环境变量 `GIT_CONFIG_GLOBAL` 指定配置源，避免由于缺省 `~/.gitconfig` 导致构建时提交签名与鉴权校验失败。

---

### 1.2 `git init`

* **内核机制**：在目标目录中构建 `.git` 目录架构，包含对象数据库（`objects`）、引用指针（`refs`）、分支符号引用（`HEAD`）与配置文件（`config`）。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 初始化形态 | `--bare` | 无 | 创建裸仓库（不含工作目录） | 服务端中央仓库标准形态，不保存工作区文件 |
| 默认分支名 | `--initial-branch=<name>` | `-b <name>` | 指定初始主干分支名称 | 现代官方规范，替代旧版默认生成的 `master` |
| 权限掩码 | `--shared[=<perms>]` | 无 | 设定仓库组共享访问权限 | 自动调整 `.git` 目录权限（`group`/`all` 等） |
| 模板设定 | `--template=<dir>` | 无 | 指定脚手架模板目录 | 自定义 hooks 脚本模板注入 |

```bash
# 完整无语法糖版本 (用于现代规范的主机代码库初始化)
git init --initial-branch=main --shared=group

# 裸仓库创建 (作为远程服务端中心节点)
git init --bare /var/git/project.git

```

---

### 1.3 `git clone`

* **内核机制**：初始化本地目录、注册远程仓库源（默认分配标识名 `origin`）、拉取远端对象数据库、更新引用并将远程默认分支检出至工作区。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 深度限制 | `--depth <n>` | 无 | 浅克隆，仅获取最近 $n$ 次提交历史 | 大幅缩减拉取时间，丢弃深层历史提交 |
| 分支控制 | `--branch <name>` | `-b <name>` | 检出指定的远程分支而非主干 | 自动将 HEAD 绑定到指定分支 |
| 单分支优化 | `--single-branch` | 无 | 仅克隆 `--branch` 所指定的分支引用 | 默认情况下即便浅克隆也会拉取全部分支元数据 |
| 子模块控制 | `--recurse-submodules` | 无 | 递归初始化并克隆所有内嵌子模块 | 替代后续分步执行的 `git submodule update` |
| 仓库形态 | `--bare` | 无 | 克隆为无工作树的裸仓库 | 等效于 `git clone --mirror` 的一部分 |
| 镜像模式 | `--mirror` | 无 | 完整镜像所有 refs（含 notes、tags） | 严格一对一全量迁移，覆盖式同步 |

```bash
# 语法糖版本 (常见于开发者本地操作)
git clone -b dev --depth 1 [https://github.com/org/repo.git](https://github.com/org/repo.git)

# 完全显式无语法糖写法 (工程规范与生产镜像)
git clone --branch dev --depth 1 --single-branch --recurse-submodules [https://github.com/org/repo.git](https://github.com/org/repo.git) destination_dir

```

---

## 2. 状态追踪与工作区快照 (Snapshotting & Working Tree)

### 2.1 `git status`

* **内核机制**：执行三次比对校验：HEAD 提交快照 $\leftrightarrow$ Index 暂存区 $\leftrightarrow$ 工作区文件系统。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 格式紧凑 | `--short` | `-s` | 输出紧凑双列状态码 | 机器可读，第一列为暂存区，第二列为工作区 |
| 分支标识 | `--branch` | `-b` | 在短格式模式下显示当前分支与追踪状态 | 常与 `--short` 组合使用 |
| 未追踪扫描 | `--untracked-files=<mode>` | `-u[<mode>]` | 设定未追踪文件的探测深度 | 参数可选：`no`、`normal`、`all` |
| 忽略文件控制 | `--ignored` | 无 | 显式列出所有被 `.gitignore` 规则屏蔽的文件 | 诊断忽略规则异常时使用 |

```bash
# 语法糖写法
git status -sb

# 完整无语法糖规范写法
git status --short --branch --untracked-files=all

```

---

### 2.2 `git add`

* **内核机制**：读取工作区文件，在 `.git/objects` 建立对应的 Blob 对象，并将对应的数据路径与 SHA-1/SHA-256 哈希更新至 `.git/index` 文件中。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 范围选择 | `--all` | `-A` | 暂存所有工作区修改、新增与删除 | 扫描整个工作树的顶层目录 |
| 更新跟踪 | `--update` | `-u` | 仅暂存已受跟踪文件的修改与删除 | 不暂存任何全新的未跟踪（Untracked）文件 |
| 交互式块暂存 | `--patch` | `-p` | 开启按代码块（Hunk）逐段审查暂存 | 将单文件内的多项逻辑修改拆解为独立提交 |
| 强制添加 | `--force` | `-f` | 忽略 `.gitignore` 校验，强行暂存目标文件 | 绕过安全保护机制 |

```bash
# 常见语法糖 (容易误将无关未跟踪文件全部暂存)
git add .

# 严谨无语法糖写法
git add --all
git add --update
git add --patch src/core/engine.c

```

---

### 2.3 `git restore` (Git 2.23+ 现代规范，取代文件级 checkout/reset)

* **内核机制**：控制工作区或暂存区的内容重置，不变更分支指针。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 暂存区目标 | `--staged` | `-S` | 恢复暂存区的内容（移出暂存状态） | 替代老式命令 `git reset HEAD <file>` |
| 工作区目标 | `--worktree` | `-W` | 恢复工作区的内容（放弃本地编辑修改） | 默认缺省选项，替代 `git checkout -- <file>` |
| 来源指定 | `--source=<tree>` | `-s <tree>` | 指定恢复快照的基准提交对象（默认 HEAD） | 可指定任意 commit、tag 或 tree 的哈希 |
| 代码块选择 | `--patch` | `-p` | 交互式选择恢复某个代码块 | 仅撤销特定代码块的修改 |

```bash
# 场景 1：撤销工作区文件的未暂存修改 (替代 git checkout -- main.go)
git restore --worktree main.go

# 场景 2：将暂存区的文件移出暂存区，保留本地代码 (替代 git reset HEAD main.go)
git restore --staged main.go

# 场景 3：同时将暂存区与工作区全部复原到某一次提交
git restore --source=HEAD~2 --staged --worktree main.go

```

---

## 3. 提交与历史审计 (Commits & Audit)

### 3.1 `git commit`

* **内核机制**：基于暂存区（Index）写入一个 Tree 对象，并生成一个指向该 Tree 的 Commit 对象，Commit 对象的 Parent 指针指向当前的 HEAD 提交，最后更新当前分支的引用。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 提交信息 | `--message=<msg>` | `-m <msg>` | 直接指定提交日志，绕过文本编辑器 | 自动化 CI/CD 标准选项 |
| 自动暂存 | `--all` | `-a` | 自动将所有已追踪文件的修改和删除提交 | 语法糖：内部自动串联执行 `git add -u` |
| 追加修正 | `--amend` | 无 | 覆盖最新一次提交，替换 Tree 和 Message | 丢弃旧 Commit 节点，重写指针（生成新哈希） |
| 绕过检查 | `--no-verify` | `-n` | 绕过 pre-commit 与 commit-msg 等钩子 | 紧急故障规避本地校验 |
| 签名认证 | `--gpg-sign[=<keyid>]` | `-S` | 使用指定或默认的 GPG 秘钥签署提交 | 提供不可抵赖的安全身份认证 |

```bash
# 语法糖写法 (快速但容易跳过钩子检查或漏掉未跟踪文件)
git commit -am "hotfix: resolve null pointer"

# 规范完整无语法糖写法
git add --all
git commit --message="fix(core): resolve null pointer vulnerability" --gpg-sign

```

---

### 3.2 `git log`

* **内核机制**：顺着 Commit 对象的 Parent 指针向后递归遍历 DAG（有向无环图），按指定拓扑或时间顺序打印历史快照元数据。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 单行紧凑 | `--oneline` | 无 | 输出短哈希和标题 | 语法糖：`--pretty=oneline --abbrev-commit` |
| 图形化结构 | `--graph` | 无 | 在左侧以 ASCII 字符绘制分支合并图 | 展示分支分叉与汇合拓扑 |
| 全引用扫描 | `--all` | 无 | 遍历所有 refs（含远程分支与标签） | 默认只输出当前 HEAD 能到达的历史 |
| 数量限制 | `--max-count=<n>` | `-n <n>` 或 `-<n>` | 仅输出最近的 $n$ 条记录 | 截断输出，提升渲染性能 |
| 差异对比 | `--patch` | `-p` | 展开显示每次提交的具体代码差异（Diff） | 查看每次提交的代码变更详情 |

```bash
# 经典研发拓扑可视化命令 (无语法糖完整形态)
git log --graph --oneline --all --decorate

# 生产级代码审计追踪：检索特定函数变更
git log --patch --max-count=5 -- src/security/token.c

```

---

### 3.3 `git diff`

* **内核机制**：比对两个数据源（工作区、暂存区、Commit 树或工作目录树）之间的差异，计算并输出符合 Unified Diff 标准的补丁数据。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 暂存区比对 | `--staged` 或 `--cached` | 无 | 对比暂存区（Index）与最新提交（HEAD） | 检验即将被提交的代码变更 |
| 统计摘要 | `--stat` | 无 | 输出改动文件清单、插入与删除行数统计 | 不展开具体代码改动 |
| 空白控制 | `--ignore-all-space` | `-w` | 忽略所有空格与换行符的变动 | 排查代码格式化对真正逻辑的干扰 |
| 命名状态 | `--name-status` | 无 | 仅输出变动文件的状态码（M/A/D 等） | 专用于 CI/CD 自动化分析改动清单 |

```bash
# 对比工作区与暂存区
git diff

# 对比暂存区与最新提交 (HEAD)
git diff --staged

# 对比两个不同的提交节点
git diff --stat 9a2f1c 4b8d7e

```

---

## 4. 分支与引用漫游 (Branching & Navigation)

### 4.1 `git switch` (Git 2.23+ 现代规范，专注于分支移动)

* **内核机制**：将工作区与暂存区调整为目标分支状态，并将 `.git/HEAD` 文件中的符号引用指向 `refs/heads/<target>`。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 创建并切换 | `--create <new-branch>` | `-c <new-branch>` | 创建新分支并立刻切换过去 | 替代传统语法糖 `git checkout -b <branch>` |
| 追踪创建 | `--track <remote>/<branch>` | `-t` | 基于远程分支创建同名本地分支并绑定上游 | 自动关联远程分支 |
| 强制分离 | `--detach` | `-d` | 切换到指定 commit 但不绑定任何分支 | 进入 Detached HEAD 状态 |
| 强制丢弃改动 | `--discard-changes` | 无 | 切换时直接丢弃当前工作区所有未提交变更 | 危险操作，规避切换失败保护 |

```bash
# 语法糖版本
git checkout -b feature/auth

# 规范完整无语法糖版本
git switch --create feature/auth

# 切换到远程分支并显式建立追踪
git switch --track origin/feature/auth

```

---

### 4.2 `git branch`

* **内核机制**：操作 `.git/refs/heads/` 目录下的分支引用指针文件，处理分支的新增、重命名与删除。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 安全删除 | `--delete` | `-d` | 仅在分支已完全合并后才允许删除 | 防止丢失未合入代码 |
| 强制删除 | `--delete --force` | `-D` | 强制删除分支，无论是否合并 | `-D` 是 `--delete --force` 的复合语法糖 |
| 重命名 | `--move` | `-m` | 重命名指定分支 | 若未指定旧分支，则重命名当前分支 |
| 查看全部分支 | `--all` | `-a` | 列出本地分支以及远程追踪分支 | 本地分支通常为绿色，远程分支为红色 |
| 关联上游 | `--set-upstream-to=<upstream>` | `-u <upstream>` | 将现有本地分支绑定到远程跟踪分支 | 建立 Tracking 配置关系 |

```bash
# 语法糖写法
git branch -D old-branch

# 严谨无语法糖写法
git branch --delete --force old-branch

# 为当前分支配置上游基准
git branch --set-upstream-to=origin/main feature/auth

```

---

## 5. 分支集成与历史重写 (Integration & Rewriting)

### 5.1 `git merge`

* **内核机制**：计算两个分支的历史共同祖先（Best Common Ancestor），如果未分叉则执行快进（Fast-forward）；若存在分叉，则进行三方合并（Three-way Merge）并在暂存区准备一个拥有两个 Parent 的合并提交对象。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 禁止快进 | `--no-ff` | 无 | 强制创建一个合并节点，保留分支演化拓扑 | 杜绝隐式平铺历史 |
| 仅允许快进 | `--ff-only` | 无 | 如果无法直接快进合并，则立即拒绝退出 | 保证主干绝对线性 |
| 压缩合并 | `--squash` | 无 | 将目标分支所有修改压缩为一个工作区改动 | 不保留分支历史提交节点，不产生两父节点 |
| 放弃合并 | `--abort` | 无 | 在冲突发生后中止合并，还原到合并前状态 | 保护现场免受破损影响 |

```bash
# 严谨的主干合并规范 (强制生成 Merge 节点供发布审计)
git merge --no-ff feature/order-system

# CI/CD 自动部署脚本安全拉取策略 (杜绝产生意外合并提交)
git merge --ff-only origin/main

```

---

### 5.2 `git rebase`

* **内核机制**：找出当前分支与基准分支的最近共同祖先，将当前分支的所有提交依次导出为临时补丁（Patch），重置分支指针到目标基准点，再将补丁依次应用上去，生成全新的 Commit 对象（哈希全部改变）。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 交互模式 | `--interactive` | `-i` | 开启交互式界面，支持压缩、编辑、重排提交 | 提交整理与重构利器 |
| 解决后继续 | `--continue` | 无 | 解决冲突并暂存后，应用下一个补丁 | 推动变基流程继续 |
| 放弃操作 | `--abort` | 无 | 完全取消变基，指针回滚到操作开始前 | 彻底清除变基现场 |
| 跳过补丁 | `--skip` | 无 | 丢弃当前产生冲突的补丁，应用下一个 | 放弃当前冲突提交修改 |

```bash
# 交互式变基整理最近 3 次提交 (无语法糖完整写法)
git rebase --interactive HEAD~3

# 将当前开发分支线性变基到最新的主干上
git rebase origin/main

```

---

### 5.3 `git reset`

* **内核机制**：调整 `HEAD` 指针的指向，并根据指定的重置级别，选择性地将 `HEAD` 对应快照同步到 Index 暂存区以及工作目录中。

| 选项类型 | 核心长选项 | 影响 HEAD | 影响 Index (暂存区) | 影响 Worktree (工作区) | 应用场景与行为语义 |
| --- | --- | --- | --- | --- | --- |
| 软重置 | `--soft` | **是** | 否 | 否 | 撤销提交，所有代码改动保留在暂存区 |
| 混合重置 | `--mixed` | **是** | **是** | 否 | 默认行为。撤销提交并清空暂存区，代码留在工作区 |
| 硬重置 | `--hard` | **是** | **是** | **是** | 彻底销毁目标提交之后的所有修改（极度危险） |

```bash
# 安全场景：将最新提交回滚，准备重新修改提交信息与暂存范围
git reset --soft HEAD~1

# 彻底丢弃本地一切未推送的提交与修改
git reset --hard origin/main

```

---

### 5.4 `git revert`

* **内核机制**：不修改现有的提交历史链条，而是通过对比指定提交与它父节点的差异，反向计算出一个补丁，并作为一次**全新的提交**追加到当前分支末端。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 不自动提交 | `--no-commit` | `-n` | 反向操作作用于工作区与暂存区，但不自动提交 | 允许连续反转多个提交并手动合并为一次反转提交 |
| 合并提交反转 | `--mainline <parent-number>` | `-m <parent-number>` | 指定保留的主线父节点编号（1 或 2） | 必须显式传入，否则反转 Merge 节点时必定抛错 |

```bash
# 反转单一提交并自动生成 Revert 提交
git revert 8a3f2b1

# 反转一个两路合并提交（保留第一个父节点所在的业务主干历史）
git revert --mainline 1 d7c9e3f

```

---

## 6. 远端协同与传输 (Remote Collaboration)

### 6.1 `git remote`

* **内核机制**：读取并维护 `.git/config` 文件中声明的 `[remote "<name>"]` 节点，配置 fetch/push 专用的 URL 及 Refspec 映射。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 |
| --- | --- | --- | --- |
| 详细清单 | `--verbose` | `-v` | 输出每个远程仓库对应的 fetch 与 push URL |
| 增添远端 | `add <name> <url>` | 无 | 注册新的远程仓库标识 |
| 变更地址 | `set-url <name> <newurl>` | 无 | 修改指定仓库的远程连接路径 |
| 增修推送源 | `set-url --add <name> <url>` | 无 | 追加额外的推送 URL，一次推送同步到多个平台 |
| 移除远端 | `remove <name>` | `rm` | 解除本地与该远程仓库的关联，不删除远端数据 |
| 修剪失效分支 | `prune <name>` | 无 | 显式清理本地记录中已在远程删除的追踪分支 |

```bash
# 完整无语法糖查看
git remote --verbose

# 显式注册与迁移
git remote add upstream [https://github.com/upstream-org/project.git](https://github.com/upstream-org/project.git)
git remote set-url origin git@github.com:personal-org/project.git

```

---

### 6.2 `git fetch`

* **内核机制**：仅下载远程仓库所有的对象数据库内容，更新本地的远程追踪分支引用（如 `refs/remotes/origin/*`），**绝不修改**本地的任何工作树与本地活跃分支（`refs/heads/*`）。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 修剪清理 | `--prune` | `-p` | 自动删除远程已不存在的跟踪分支 | 保持本地远程分支引用的时效性 |
| 标签获取 | `--tags` | `-t` | 强制拉取远端所有的标签引用 | 默认只拉取与提交相关的标签 |
| 全远端获取 | `--all` | 无 | 获取配置文件中声明的所有 remote 仓库 | 适用于多远端环境 |

```bash
# 规范完整的抓取与清理命令
git fetch --prune --all

```

---

### 6.3 `git pull`

* **内核机制**：组合命令，底层依次执行 `git fetch` 抓取远程对象，随后自动根据配置调用 `git merge` 或 `git rebase` 将远端分支并入本地工作树。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 变基拉取 | `--rebase` | `-r` | 拉取后采用变基合并，避免多余的 Merge 节点 | 保持团队主干线性提交记录 |
| 传统合并 | `--no-rebase` | 无 | 显式采用传统合并提交模式 | 生成一个分叉合并节点 |
| 仅快进拉取 | `--ff-only` | 无 | 必须能够快进合并，否则直接终止报错 | 避免自动拉取时意外产生冲突或合并节点 |
| 修剪分支 | `--prune` | `-p` | 拉取时顺便清理本地失效的远程分支 | 避免冗余的无效远程跟踪引用 |

```bash
# 规范无语法糖：线性历史拉取
git pull --rebase origin main

# 生产级保护拉取：仅允许快进
git pull --ff-only origin main

```

---

### 6.4 `git push`

* **内核机制**：将本地对象数据库中的缺失对象传输到远程服务器，并请求远程仓库更新其引用（Refspec：`local_ref:remote_ref`）。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 关联上游 | `--set-upstream` | `-u` | 将本地分支与远端目标分支建立 Tracking 关联 | 后续简化推送的前提 |
| 安全强推 | `--force-with-lease` | 无 | 强制推送前，检查远端引用是否被他人并发修改 | 避免直接用 `--force` 覆盖同事提交 |
| 绝对强推 | `--force` | `-f` | 强制使用本地引用覆盖远程引用（极度危险） | 容易造成远程数据丢失 |
| 删除远程分支 | `--delete` | `-d` | 请求远程仓库删除指定分支或标签 | 替代老式语法糖 `git push origin :branch` |
| 推送全部分支 | `--all` | 无 | 推送本地所有的分支指针 | 适合仓库迁移初始化 |
| 模拟演练 | `--dry-run` | `-n` | 仅输出推送决策，不进行实际网络传输 | 推送前安全校验 |

```bash
# 场景 1：完全无语法糖的显式 Refspec 推送并建立追踪关系
git push --set-upstream origin feature-login:feature-login

# 场景 2：生产级安全强制推送 (禁止使用 -f)
git push --force-with-lease origin main:main

# 场景 3：显式删除远程分支
git push origin --delete feature-legacy

```

---

## 7. 工作进度隔离 (Stashing)

### 7.1 `git stash`

* **内核机制**：通过底层的 `git commit-tree` 将当前工作区和暂存区的修改分别包装为独立的 Commit 对象，挂载在 `refs/stash` 引用栈上，然后执行工作区清理。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义与参数说明 | 语法糖解构与隐式行为 |
| --- | --- | --- | --- | --- |
| 入栈并命名 | `push --message <msg>` | `save <msg>` | 保存当前修改并打上语义化备注 | `save` 已被官方弃用，统一使用 `push` |
| 包含未跟踪 | `--include-untracked` | `-u` | 一同备份当前未受版本控制的文件 | 避免因未跟踪文件干扰导致后续切分支失败 |
| 包含全量文件 | `--all` | `-a` | 一同备份被 `.gitignore` 忽略的文件 | 最彻底的现场封存 |
| 恢复并弹出 | `pop` | 无 | 应用栈顶备份并立即从暂存栈中彻底移除 | 等效于 `apply` + `drop` 组合 |
| 恢复并保留 | `apply` | 无 | 应用指定的备份（默认栈顶），保留在栈中 | 适合在多个分支间复制工作现场 |
| 清空操作 | `clear` | 无 | 清空全部暂存栈历史 | 不可逆操作，谨慎执行 |

```bash
# 现代规范推荐写法 (包含未追踪文件并附带清晰信息)
git stash push --include-untracked --message "WIP: refactoring database connection layer"

# 审查现有暂存列表
git stash list

# 安全恢复：先应用，验证无误后再删除
git stash apply stash@{0}
git stash drop stash@{0}

```

---

## 8. 数据抢救与故障排查 (Forensics & Debugging)

### 8.1 `git reflog`

* **内核机制**：记录本地所有分支与 `HEAD` 指针在**本地**发生的一切变动（包括 `reset`、`rebase`、`checkout` 等），位于 `.git/logs/` 目录下。该记录不与远程同步，属于本地操作的安全防护网。

```bash
# 检索全局 HEAD 移动全量日志
git reflog show HEAD

# 数据抢救示范：回滚误操作的 hard reset
# 1. 查找被丢弃提交对应的原始哈希值（例如发现是 HEAD@{1}）
# 2. 强制恢复指针到该状态
git reset --hard HEAD@{1}

```

---

### 8.2 `git bisect`

* **内核机制**：利用**二分查找法（Binary Search）**，在指定的良好（Good）提交与损坏（Bad）提交之间进行自动化快速定位，找出引入 Bug 的具体提交。

```bash
# 启动二分排查流程
git bisect start

# 标记当前检出的 HEAD 版本包含缺陷
git bisect bad

# 标记某一个已验证正常的历史版本
git bisect good v1.2.0

# Git 自动切换到中点，开发者运行编译测试后输入状态继续：
git bisect good   # 如果当前版本运行正常
# 或
git bisect bad    # 如果当前版本复现了缺陷

# 定位完成，重置并退出二分会话，回到原始开发分支
git bisect reset

```

---

### 8.3 `git clean`

* **内核机制**：彻底清理工作区中没有被 Git 跟踪的文件。

| 选项类型 | 长选项 (Canonical) | 短选项 / 简写 | 功能语义说明 |
| --- | --- | --- | --- |
| 强制执行 | `--force` | `-f` | Git 默认禁止清理，必须显式加此参数执行删除 |
| 包含目录 | `-d` | 无 | 连同未跟踪的空目录或子目录一起递归移除 |
| 演练检查 | `--dry-run` | `-n` | 仅输出将被删除的文件清单，不进行实际磁盘操作 |

```bash
# 演习预览将删除的内容
git clean --dry-run -d

# 彻底清理未追踪的临时文件与构建中间产物
git clean --force -d

```

---

## 9. 核心底层管线命令 (Core Plumbing)

Git 本质上是一个**内容寻址文件系统（Content-Addressable Filesystem）**，上层业务命令均构建在以下底层管线命令之上：

### 9.1 `git hash-object`

* **功能**：计算指定内容的 SHA 哈希值，并可直接将数据作为对象写入 `.git/objects` 数据库生成 Blob 对象。

```bash
# 将一段文本计算哈希并写入对象库 (-w 代表 write)
echo "Hello Git Architecture" | git hash-object -w --stdin

```

### 9.2 `git cat-file`

* **功能**：检查对象数据库中任意对象的类型、大小和原始内容。

```bash
# 打印对象类型 (commit, tree, blob, tag)
git cat-file -t <hash>

# 打印对象的原始内容 (Pretty-print)
git cat-file -p <hash>

```

### 9.3 `git ls-tree`

* **功能**：打印指定 Tree 对象的内容清单，类似 UNIX 系统的 `ls`。

```bash
git ls-tree HEAD

```

---

# 第三部分：语法糖与全命令规范对照基准表

| 业务场景 | 常见语法糖 (Shorthand / Conventional) | 官方推荐或无语法糖完整规范 (Long-form / Canonical) | 架构设计目的与工程考量 |
| --- | --- | --- | --- |
| **创建并切分支** | `git checkout -b <name>` | `git switch --create <name>` | 剥离 `checkout` 的多重职责，消除与文件恢复的语义混淆 |
| **撤销工作区修改** | `git checkout -- <file>` | `git restore --worktree <file>` | 统一文件状态回滚命令入口，由 `restore` 专门掌管 |
| **暂存区撤回** | `git reset HEAD <file>` | `git restore --staged <file>` | 避免滥用具备移动分支指针能力的 `reset` 命令 |
| **全量追踪** | `git add .` | `git add --all` | `.` 受当前子目录限制，`--all` 显式保证全工作树遍历 |
| **强推代码** | `git push -f origin main` | `git push --force-with-lease origin main:main` | 保证并发安全校验，明确指定 Refspec 映射两侧 |
| **快照暂存** | `git stash` | `git stash push --include-untracked` | 避免隐式遗漏未受版本控制的文件（Untracked Files） |
| **删除远程分支** | `git push origin :<branch>` | `git push origin --delete <branch>` | 用自解释的 `--delete` 替代冒号左侧置空的黑客语法糖 |
| **拉取防冲突** | `git pull` | `git pull --rebase origin main` | 强制采用 Rebase 机制，消除不必要的交叉合并节点 |

```

```
