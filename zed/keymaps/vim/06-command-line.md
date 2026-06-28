# Vim mode：命令行 `:` 命令

这些不是 `assets/keymaps/vim.json` 的按键绑定，而是 `crates/vim/src/command.rs` 中 `generate_commands` 与 `command_interceptor` 定义/解析的 Vim 命令行命令。

| 命令 | 行为 |
|---|---|
| `:w[rite][!] [file]` | 保存；`!` 对应覆盖保存；支持范围写入。 |
| `:e[dit][!] [file]` | 重载当前文件，或打开指定文件。 |
| `:r[ead] [file]` | 读取文件内容插入缓冲区；支持范围。 |
| `:sp[lit] [file]` | 水平分屏，可打开指定文件。 |
| `:vs[plit] [file]` | 垂直分屏，可打开指定文件。 |
| `:tabe[dit] [file]` | 新标签/新文件，可打开指定文件。 |
| `:tabnew [file]` | 新标签/新文件，可打开指定文件。 |
| `:q[uit][!]` | 关闭当前项；`!` 跳过保存。 |
| `:wq[!]` | 保存并关闭当前项；`!` 覆盖保存。 |
| `:x[it][!]` | 保存所有并关闭当前项；`!` 覆盖保存。 |
| `:exi[t][!]` | 保存所有并关闭当前项；`!` 覆盖保存。 |
| `:up[date]` | 保存所有。 |
| `:wa[ll][!]` | 保存全部；`!` 覆盖保存。 |
| `:qa[ll][!]` | 关闭全部；`!` 跳过保存。 |
| `:quita[ll][!]` | 关闭全部；`!` 跳过保存。 |
| `:xa[ll][!]` | 保存全部并关闭全部；`!` 覆盖保存。 |
| `:wqa[ll][!]` | 保存全部并关闭全部；`!` 覆盖保存。 |
| `:cq[uit]` | 退出 Zed。 |
| `:bd[elete][!]` | 在所有 pane 中关闭当前 buffer；`!` 跳过保存。 |
| `:norm[al] {keys}` | 按 Normal 模式执行按键序列；支持范围。 |
| `:bn[ext]` | 下一个 buffer/tab；支持计数。 |
| `:bN[ext]` | 上一个 buffer/tab；支持计数。 |
| `:bp[revious]` | 上一个 buffer/tab；支持计数。 |
| `:bf[irst]` | 第一个 buffer/tab。 |
| `:br[ewind]` | 第一个 buffer/tab。 |
| `:bl[ast]` | 最后一个 buffer/tab。 |
| `:buffers` | 打开所有 tab/buffer 切换器。 |
| `:ls` | 打开所有 tab/buffer 切换器。 |
| `:new` | 新建水平分屏文件。 |
| `:vne[w]` | 新建垂直分屏文件。 |
| `:tabn[ext]` | 下一个标签；支持计数。 |
| `:tabp[revious]` | 上一个标签；支持计数。 |
| `:tabN[ext]` | 上一个标签；支持计数。 |
| `:tabc[lose]` | 关闭当前标签。 |
| `:tabo[nly][!]` | 仅保留当前标签；`!` 跳过保存。 |
| `:on[ly][!]` | 关闭非活动 tab/pane；`!` 跳过保存。 |
| `:cl[ist]` | 打开 diagnostics 列表。 |
| `:cc` | 显示 hover。 |
| `:ll` | 显示 hover。 |
| `:cn[ext]` | 下一个诊断；支持计数/范围。 |
| `:cp[revious]` | 上一个诊断；支持计数/范围。 |
| `:cN[ext]` | 上一个诊断；支持计数/范围。 |
| `:lp[revious]` | 上一个诊断；支持计数/范围。 |
| `:lN[ext]` | 上一个诊断；支持计数/范围。 |
| `:j[oin]` | 合并行；支持范围。 |
| `:reflow [width]` | 按可选宽度重排文本；支持范围。 |
| `:fo[ld]` | 折叠选中范围；支持范围。 |
| `:foldo[pen][!]` | 展开行；`!` 递归展开；支持范围。 |
| `:foldc[lose][!]` | 折叠；`!` 递归折叠；支持范围。 |
| `:dif[fupdate]` | 切换选中 diff hunk；支持范围。 |
| `:rev[ert]` | Git restore；支持范围。 |
| `:d[elete]` | 删除行；支持范围。 |
| `:y[ank]` | 复制行；支持范围。 |
| `:reg[isters][!]` | 切换 registers 视图。 |
| `:di[splay][!]` | 切换 registers 视图。 |
| `:marks[!]` | 切换 marks 视图。 |
| `:delm[arks][!] {marks}` | 删除 marks；`!` 删除所有 local marks。 |
| `:sor[t]` | 排序；默认整 buffer，支持范围。 |
| `:sort i` | 忽略大小写排序；默认整 buffer，支持范围。 |
| `:E[xplore]` | 切换项目面板焦点。 |
| `:H[explore]` | 切换项目面板焦点。 |
| `:L[explore]` | 切换项目面板焦点。 |
| `:S[explore]` | 切换项目面板焦点。 |
| `:Ve[xplore]` | 切换项目面板焦点。 |
| `:te[rm]` | 切换终端面板。 |
| `:T[erm]` | 切换终端面板。 |
| `:C[ollab]` | 切换协作面板。 |
| `:A[I]` | 切换 Agent/AI 面板。 |
| `:G[it]` | 切换 Git 面板。 |
| `:D[ebug]` | 切换 Debug 面板。 |
| `:noh[lsearch]` | 清除搜索高亮。 |
| `:$` | 跳到文档末尾。 |
| `:%` | 跳到文档末尾。 |
| `:0` | 跳到文档开头。 |
| `:ex[!]` | 重载当前文件；支持 `!`。 |
| `:cpp[link]` | 复制当前行 permalink；支持范围。 |
| `:opt[ions]` | 打开默认设置。 |
| `:map` | 打开默认 Vim keymap。 |
| `:h[elp]` | 打开文档。 |

## 额外解析规则

- `:<数字>` / `:$` / 范围前缀会进入行跳转或范围动作。
- `:/pattern` 与 `:?pattern` 调用 Vim 搜索。
- `:s...` / `:substitute...` 调用替换。
- 含 `!` 的 shell 形式由 `ShellExec::parse` 处理。
- `:set ...` / `:se ...` 解析 `wrap`、`number`/`nu`、`relativenumber`/`rnu`、`ignorecase`/`ic`、`gdefault`/`gd` 及其 `no...` 版本。
