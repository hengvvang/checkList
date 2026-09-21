在 Git 的分支集成分流中，`git merge` 与 `git rebase` 代表了两种截然不同的工程哲学：**保留历史的完整拓扑结构（Merge）** 与 **构建线性的清晰演进轨迹（Rebase）**。

---

## 1. 底层运作原理深度对比

### 1.1 `git merge` 的底层原理

Merge 是一种非破坏性（Non-destructive）操作，它不会改写任何既有提交的历史哈希值。

```
Fast-Forward 合并:
A --- B (main)
       \
        C --- D (feature)
-> 合并后 (HEAD 指针直接前移到 D):
A --- B --- C --- D (main, feature)

三方合并 (Three-Way Merge):
A --- B --- C (main)
 \
  D --- E (feature)
-> 合并后 (生成新的 Merge Commit M):
A --- B --- C ------- M (main)
 \                   /
  D ------- E ------- (feature)
  [Base = A, Ours = C, Theirs = E]

```

* **Fast-Forward（快进合并）**：
* **触发条件**：当前分支的顶端提交是目标分支的直接祖先（即两者之间没有分叉）。
* **内部行为**：Git 仅需将当前分支的引用指针直接向前推移至目标分支对应的 Commit SHA-1，无需做三方比对，也不创建新的 Commit 对象。


* **Three-Way Merge（三方合并）**：
* **触发条件**：两个分支的历史自某个分叉点起均有独立的提交推进。
* **定位祖先**：Git 利用图算法寻找两个分支的**最近公共祖先（LCA, Lowest Common Ancestor）**，记作 `Base`。当前检出分支的顶端记作 `Ours`，要并入的分支顶端记作 `Theirs`。
* **差异计算**：计算 `Base -> Ours` 与 `Base -> Theirs` 的两组 Diff 并进行并集计算。
* **生成节点**：若无冲突，Git 会自动创建一个拥有两个父节点（Parents）的全新提交节点（Merge Commit）。



---

### 1.2 `git rebase` 的底层原理

Rebase 是一种重写历史（History Rewriting）**的操作。它将一系列已存在的提交**临时剥离并依序重新应用（Replay）到另一个基础基线之上。

```
Rebase 变基操作演进:
A --- B --- C (main)
 \
  D --- E (feature)

1. 计算范围: feature..main 之外的提交，即 D 和 E。
2. 暂存补丁: 将 D, E 的变更转化为临时补丁并保存在 .git/rebase-apply 或 .git/rebase-merge 中。
3. 重置起点: 将当前 feature 分支强行 reset 到 main 的顶端 C。
4. 依次重放: 将补丁 D 应用生成 D'，再将 E 应用生成 E' (SHA-1 发生变化)。
5. 最终结果:
A --- B --- C (main)
             \
              D' --- E' (feature)

```

> **黄金法则（The Golden Rule of Rebase）**：
> 永远不要在**已经推送到公开共享远程仓库（如团队公共协作分支）的分支**上执行 Rebase。由于变基会生成全新 Commit SHA-1 并丢弃旧 Commit，一旦推送到公共分支，会导致其他协作者的历史断裂并引发严重的重复提交与合并混乱。

---

## 2. `git merge` 核心参数与使用场景

### 2.1 语法结构

```bash
git merge [-n] [--stat] [--no-commit] [--squash] [--[no-]edit]
          [--no-verify] [-s <strategy>] [-X <strategy-option>]
          [-S[<keyid>]] [--[no-]rerere-autoupdate]
          [--autostash | --no-autostash]
          [--ff | --no-ff | --ff-only]
          [-m <msg>] [-F <file>] [<commit>...]
git merge (--abort | --continue | --quit)

```

### 2.2 核心参数详解

* `--ff`：默认模式。如果可以快进，则执行快进合并；否则执行三方合并。
* `--no-ff`：**强制生成 Merge Commit**。即使当前历史满足 Fast-Forward 条件，也强制生成一个独立的合并提交节点。常用于保留发布或特性集成的完整语义边界。
* `--ff-only`：**仅允许快进合并**。如果存在分叉、无法通过简单移动指针完成合并，Git 会直接拒绝并中断报错。
* `--squash`：**压缩合并**。将目标分支上的所有提交差异提取出来，作为一个平整的工作目录改动放入当前分支的暂存区，**不保留原分支的提交历史和图谱连接**，由用户手动执行一次单节点提交。
* `--no-commit`：执行合并逻辑并解决差异，但在生成合并提交前暂停，保留在暂存区，允许开发者在最终提交前进行审查或微调。
* `-m <msg>`, `--message=<msg>`：直接在命令行指定生成的 Merge Commit 的提交说明。
* `-s <strategy>`, `--strategy=<strategy>`：指定合并策略（如 `ort` [现代默认]、`recursive` [旧版默认]、`resolve`、`ours`、`subtree`）。
* `-X <strategy-option>`, `--strategy-option=<strategy-option>`：向合并策略传递高级子选项（如 `-X ours`、`-X theirs`、`-X ignore-space-change`）。
* `--autostash` / `--no-autostash`：在合并执行前，自动执行 `git stash create` 保存当前脏工作区，合并完成后自动恢复弹栈。
* `--abort`：**安全中止**。在遇到冲突或未完成状态时，完全恢复到合并触发前的原始分支状态。
* `--continue`：手动解决冲突并暂存变更后，继续完成剩余的合并提交流程。

### 2.3 实战示例

```bash
# 1. 规范的集成合并：即使满足快进也保留完整的特性合并节点
git merge --no-ff feature/order-api -m "Merge branch 'feature/order-api' into develop"

# 2. CI/CD 安全合入：只允许线性推进，存在分叉则失败
git merge --ff-only origin/main

# 3. 压缩合并：将 feature 分支上的 20 个琐碎提交压缩为一个清晰整洁的提交合入 main
git merge --squash feature/user-profile
git commit -m "feat(user): add user profile module complete"

# 4. 冲突策略覆盖：在合并特定配置文件时，指定遇到冲突以当前分支（ours）为准
git merge -X ours release/configs

# 5. 合并中断与撤销
git merge --abort

```

---

## 3. `git rebase` 核心参数与使用场景

### 3.1 语法结构

```bash
git rebase [-i | --interactive] [<options>] [--exec <cmd>] [--onto <newbase> [<upstream> [<branch>]]]
git rebase [-i | --interactive] [<options>] [--root] [<branch>]
git rebase (--continue | --skip | --abort | --quit | --edit-todo | --show-current-patch)

```

### 3.2 核心参数详解

* `-i`, `--interactive`：**交互式变基**。弹出一个待办列表（Todo List），允许开发者逐一调整将要重放的历史提交序列（重排、丢弃、合并、拆分、重写说明）。
* `--onto <newbase>`：精确指定新嫁接点的基线。常用于将某个特性分支从一个基础分支“剪切”并“粘贴”到另一个完全不同的分支之上。
* `--exec <cmd>`, `-x <cmd>`：在交互式变基过程中，每重放成功一个提交后，自动在后台运行一次指定的 Shell 命令（如 `npm test` 或 `cargo check`）。如果命令执行失败，变基会在此提交处暂停，便于自动化排查坏提交。
* `--root`：对仓库自初始提交（Initial Commit）以来的全部历史执行变基。
* `--autostash`：变基前自动暂存未跟踪/未提交的文件，变基完毕后自动恢复工作区。
* `--continue`：当解决完某一重放步骤的冲突并 `git add` 后，恢复并推进变基过程。
* `--skip`：**跳过当前补丁**。放弃应用当前的冲突提交，直接推进到下一个补丁应用。**慎用**，会导致对应的变更内容彻底丢失。
* `--abort`：完全撤销当前的 Rebase 操作，分支指针与文件系统瞬间退回到变基发起前的状态。
* `--quit`：退出变基流程，但**不重置**工作区已经应用完成的中间提交。

### 3.3 交互式变基指令表（Todo List Actions）

在执行 `git rebase -i` 时，编辑器中每行提交前面可配置的操作指令如下：

| 指令 | 简写 | 含义与行为 |
| --- | --- | --- |
| `pick` | `p` | 保留该提交，按原样应用。 |
| `reword` | `r` | 保留该提交内容，但在应用时弹出编辑器**修改其 Commit Message**。 |
| `edit` | `e` | 保留该提交，但在应用后**暂停变基**，允许修改提交内容、拆分提交或添加文件。 |
| `squash` | `s` | **挤压合并**：将该提交与前一个提交合并为一个提交，并**拼接两者的提交说明**。 |
| `fixup` | `f` | 类似于 `squash`，将内容合入前一个提交，但**直接丢弃本提交的日志说明**。 |
| `drop` | `d` | **丢弃该提交**（等价于在待办列表中直接删除整行）。 |
| `exec` | `x` | 插入一行 Shell 命令并在该阶段执行。 |
| `break` | `b` | 在此处强行暂停（断点），便于开发者调试。 |

### 3.4 实战示例

```bash
# 1. 本地分支跟进远程 main：将本地未推送的提交平移到最新的 origin/main 之上（保持绝对线性）
git fetch origin
git rebase origin/main

# 2. 交互式整理最近 4 次本地提交（合并琐碎提交、精简提交历史）
git rebase -i HEAD~4

# 3. 自动测试验证：变基重放过程中，确保每一个提交都能通过单元测试
git rebase -i origin/main --exec "npm test"

# 4. 高级分支嫁接 (--onto)：
# 场景：基于 feature-v1 分支拉出了 feature-v2；现在 feature-v1 废弃，需将 feature-v2 移植到 main
# 语法：git rebase --onto <新基座> <旧分叉点基座> <要移动的分支>
git rebase --onto main feature-v1 feature-v2

```

---

## 4. 冲突解决策略与全流程实操

无论执行 Merge 还是 Rebase，当两个分支**对同一个文件的同一位置**进行了互斥修改时，Git 都会暂停并标记文件为 **Unmerged（未合并状态）**。

### 4.1 理解冲突标记标记（Conflict Markers）

打开冲突文件，Git 会用特定标识区分变更来源：

```plaintext
<<<<<<< HEAD (在 merge 时代表当前检出分支；在 rebase 时代表基础基线 Target Base)
const API_URL = "https://api.production.internal/v1";
=======
const API_URL = "https://api.staging.internal/v2";
>>>>>>> feature/new-api (在 merge 时代表被并入分支；在 rebase 时代表当前正被重放的补丁)

```

> **注意 Rebase 的角色反转**：在 Rebase 期间解决冲突时，`HEAD` 代表的是接收重放的基线（如 `main`），而所谓的“当前变更”反而是原来分支上的一个个提交。

---

### 4.2 实战场景 A：`git merge` 冲突解决标准流程

```bash
# 1. 触发合并
git merge feature/auth

# 2. 终端提示 Automatic merge failed; fix conflicts and then commit the result.
# 查看具体处于冲突状态的文件清单
git status

# 3. 开发者介入：手工编辑解决冲突，删除 <<<<<<<, =======, >>>>>>> 标记
# 或使用第三方可视化 Diff 工具辅助解决
git mergetool

# 4. 标记冲突已解决（将改动加入暂存区）
git add src/config.js

# 5. 最终完成合并
# 方式 1: 直接使用 git commit 完成（Git 会保留预设的默认合并描述）
git commit
# 方式 2: 使用专门的 continue 命令
git merge --continue

# 若中途判断冲突过于复杂，希望放弃本次合并操作：
git merge --abort

```

---

### 4.3 实战场景 B：`git rebase` 冲突解决标准流程

与 Merge 的**一次性解决**不同，Rebase 是对补丁**逐一重放**。如果 5 个 Commit 都触碰了冲突代码，开发者可能会连续经历多次暂停与解决。

```bash
# 1. 触发变基
git rebase origin/main

# 2. 变基在某个补丁应用时发生冲突，Git 提示：
# Could not apply 3a7f8b9... feat(auth): add token refresh
git status

# 3. 开发者介入：手动编辑冲突文件并消除标记
vim src/auth/token.js

# 4. 将解决后的文件加入暂存区（注意：千万不要在此处运行 git commit！）
git add src/auth/token.js

# 5. 驱动继续应用下一个补丁
git rebase --continue

# 6. 如果遇到某个补丁的所有内容已经被上游完全吸收、已无有效差异时，可以跳过该补丁：
# git rebase --skip

# 7. 若操作混乱，随时一键安全回退撤销：
git rebase --abort

```

---

### 4.4 生产级加速利器：`git rerere` (Reuse Recorded Resolution)

在长期维护特性分支或高频重构场景中，开发者常常需要多次反复重放相同的合并操作，导致一模一样的冲突反复出现。Git 提供了 `rerere` 机制，能够**自动记忆你如何解决过特定文件的代码冲突**。

```bash
# 1. 开启全局冲突解决记忆功能
git config --global rerere.enabled true

# 2. 运作机制：
# - 当发生冲突时，Git 会记录冲突前的指纹
# - 当你手工解决冲突并提交后，Git 会在 .git/rr-cache 中缓存冲突前后的映射补丁
# - 下次无论在 merge 还是 rebase 中遇到相同代码冲突时，Git 自动直接套用你的历史解决方案

```

---

## 5. 团队选型决策指南 (Decision Framework)

| 考量维度 | 推荐采用 `git merge` | 推荐采用 `git rebase` |
| --- | --- | --- |
| **分支属性** | 公共分支（`main`, `develop`, `release/*`） | 本地独立特性分支（未推送或私有开发分支） |
| **可追溯性** | 极高。真实反映分支合入的时间顺序与拓扑边界 | 较高。但会抹去真实开发交叉的时间先后脉络 |
| **Commit 图谱** | 复杂网络网状图，节点多，容易产生气泡合并图 | **严格单向直线**，整洁清晰，极易通过 `git bisect` 排查缺陷 |
| **冲突处理成本** | 一次性集中解决（Single pass） | 可能需要随补丁应用阶段经历多次处理（Iterative） |
| **合并语义保留** | 完整记录“某特性何时整体并入主干” | 特性提交直接打散重排在主干最新头部 |

**行业通用标准工作流（Trunk-based / Feature Branch 组合模型）**：

1. **本地开发时（本地与远程同步）**：使用 `git pull --rebase` 或 `git fetch + git rebase`，确保本地特性分支始终挂在最新的主干顶端，形成线性结构。
2. **提 PR / MR 前夕**：使用 `git rebase -i` 压缩、整理本地琐碎调试提交（如 `fix typo`, `debug`），呈现语义清晰的原子提交（Atomic Commits）。
3. **合入生产主干时（Merge to Main）**：使用 `git merge --no-ff`（或者平台上的 Squash & Merge / Rebase & Merge 策略），在主干上清晰保留一次功能发布的生命周期边界。
