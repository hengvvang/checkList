# Zed 快捷键与高产指南 (Vim & 默认快捷键)

本指南旨在详细介绍 Zed 编辑器中的所有常用 Vim 模拟模式快捷键、默认 Windows 快捷键，以及面向开发和生产力的核心指令。所有数据均直接核对自 Zed 官方源码 [vim.json](file:///C:/Users/hengvvang/Desktop/zed/assets/keymaps/vim.json) 和 [default-windows.json](file:///C:/Users/hengvvang/Desktop/zed/assets/keymaps/default-windows.json) 进行核对，确保准确无误。

---

## 目录
1. [配置与启用](#配置与启用)
2. [工作空间面板与 Dock 控制](#1-工作空间面板与-dock-控制)
3. [文件导航与搜索面板](#2-文件导航与搜索面板)
4. [LSP 代码导航与跳转](#3-lsp-代码导航与跳转)
5. [编译诊断与 Git Hunk 差异操作](#4-编译诊断与-git-hunk-差异操作)
6. [高级代码编辑与多光标操作](#5-高级代码编辑与多光标操作)
7. [分屏窗口与标签页布局](#6-分屏窗口与标签页布局)
8. [Vim 环绕字符与语义文本对象](#7-vim-环绕字符与语义文本对象)
9. [智能 AI 编程与自动补全](#8-智能-ai-编程与自动补全)
10. [任务管理器与外部终端](#9-任务管理器与外部终端)
11. [项目侧边栏 Netrw 兼容模式](#10-项目侧边栏-netrw-兼容模式)
12. [DAP 交互式调试器快捷键](#11-dap-交互式调试器快捷键)
13. [高级代码折叠 (Code Folding)](#12-高级代码折叠-code-folding)
14. [Helix 模拟模式 (Helix Mode)](#13-helix-模拟模式-helix-mode)
15. [核心生产力实战场景示例](#核心生产力实战场景示例)

---

## 配置与启用

在 Zed 中，您可以在全局用户设置（`settings.json`）中自由切换 **Vim 模式** 和 **默认模式**：

```json
{
  "vim_mode": true
}
```

* **Vim 模式**：通过 [crates/vim](file:///C:/Users/hengvvang/Desktop/zed/crates/vim) 模块提供熟悉的 Vim 指令集，并高度整合 Zed LSP 特性。
* **默认模式**：采用类似于 VS Code / Sublime Text 的标准现代键位。

---

## 1. 工作空间面板与 Dock 控制

Zed 的界面设计高度可定制。通过底栏、左栏和右栏的 Docks，您可以快速收起或展开不同的辅助面板。

| 功能描述 | Vim 模式快捷键 (Normal) | 默认 Windows 快捷键 | 绑定 Action |
| :--- | :--- | :--- | :--- |
| **切换左侧 Dock** (文件树等) | `Ctrl-b` | `Ctrl-b` | `workspace::ToggleLeftDock` |
| **切换右侧 Dock** (AI 助手等) | `Ctrl-Alt-b` | `Ctrl-Alt-b` | `workspace::ToggleRightDock` |
| **切换底部 Dock** (终端面板等) | `Ctrl-j` | `Ctrl-j` | `workspace::ToggleBottomDock` |
| **隐藏/显示所有活动 Docks** | `Ctrl-Shift-y` | `Ctrl-Shift-y` | `workspace::ToggleAllDocks` |
| **一键开关/聚焦内置终端** | `Ctrl-`` | `Ctrl-`` | `terminal_panel::Toggle` |
| **切换全屏状态** | `F11` | `F11` | `zed::ToggleFullScreen` |
| **最大化当前编辑区 (Zoom)** | `Shift-Escape` | `Shift-Escape` | `workspace::ToggleZoom` |
| **打开/切换工作空间侧边栏** | `Ctrl-Alt-j` | `Ctrl-Alt-j` | `multi_workspace::ToggleWorkspaceSidebar` |
| **聚焦工作空间侧边栏** | 无 | `Ctrl-Alt-;` | `multi_workspace::FocusWorkspaceSidebar` |

---

## 2. 文件导航与搜索面板

用于快速在全项目检索文件和代码内容的生产力热键。

| 功能描述 | Vim 模式快捷键 (Normal) | 默认 Windows 快捷键 | 绑定 Action |
| :--- | :--- | :--- | :--- |
| **打开文件搜索框** (Go to File) | `Space f` 或 `Ctrl-p` | `Ctrl-p` | `file_finder::Toggle` |
| **打开命令面板** (Command Palette)| `:` 或 `Ctrl-Shift-p` | `Ctrl-Shift-p` | `command_palette::Toggle` |
| **当前文件内搜索** (Find) | `/` | `Ctrl-f` | `buffer_search::Deploy` |
| **当前文件内替换** (Replace) | 无 | `Ctrl-h` | `buffer_search::DeployReplace` |
| **全项目模糊文本检索** (Search) | `Space /` 或 `g /` | `Ctrl-Shift-f` | `pane::DeploySearch` |
| **最近标签页切换器** (Switcher) | `Ctrl-Tab` | `Ctrl-Tab` | `tab_switcher::Toggle` |
| **全项目高级文本搜索器** | 无 | `Ctrl-Alt-f` | `project_search::OpenTextFinder` |
| **全局替换搜索结果中的全部项** | 无 | `Ctrl-Alt-Enter` | `search::ReplaceAll` |

---

## 3. LSP 代码导航与跳转

依托于后端 Language Server，Zed 支持精准的语义跳转。

| 功能描述 | Vim 模式快捷键 (Normal) | 默认 Windows 快捷键 | 绑定 Action |
| :--- | :--- | :--- | :--- |
| **跳转至定义** | `g d` 或 `Ctrl-]` | `F12` | `editor::GoToDefinition` |
| **分屏打开并跳转至定义** | `Ctrl-w d` 或 `Ctrl-w ]` | `Alt-f12` | `editor::GoToDefinitionSplit` |
| **跳转至声明** | `g Shift-d` | 无 | `editor::GoToDeclaration` |
| **跳转至类型定义** | `g y` | 无 | `editor::GoToTypeDefinition` |
| **跳转至接口/Trait实现** | `g r i` 或 `g Shift-i` | `Ctrl-f12` | `editor::GoToImplementation` |
| **查找所有引用** (全项目) | `g r r` 或 `g Shift-a` | `Shift-Alt-f12` | `editor::FindAllReferences` |
| **展开当前文件大纲面板** | `g s` 或 `g Shift-o` | 无 | `outline::Toggle` |
| **模糊查找项目所有符号** | `g Shift-s` | 无 | `project_symbols::Toggle` |

---

## 4. 编译诊断与 Git Hunk 差异操作

当您在进行迭代式重构时，以下快捷键能帮助您在报错行和 Git 改动点之间秒级跳转。

| 功能描述 | Vim 模式快捷键 (Normal) | 默认 Windows 快捷键 | 绑定 Action |
| :--- | :--- | :--- | :--- |
| **跳转到下一个编译错误/警告** | `] d` 或 `g ]` | `F8` | `editor::GoToDiagnostic` |
| **跳转到上一个编译错误/警告** | `[ d` 或 `g [` | `Shift-f8` | `editor::GoToPreviousDiagnostic` |
| **打开全局报错诊断面板** | 无 | `Ctrl-Shift-m` | `diagnostics::Deploy` |
| **跳转到下一个 Git 修改块** (Hunk)| `] c` | 无 | `editor::GoToHunk` |
| **跳转到上一个 Git 修改块** | `[ c` | 无 | `editor::GoToPreviousHunk` |
| **内联展示当前 Git 块修改差异** | `d o` | `Ctrl-'` | `editor::ToggleSelectedDiffHunks` |
| **一键放弃当前 Git 块修改** | `d p` | `Ctrl-k Ctrl-r` | `git::Restore` |
| **暂存当前修改块并跳转下一个** | `d u` | `Alt-y` | `git::StageAndNext` |
| **取消暂存当前修改块** | `d Shift-u` | `Shift-Alt-y` | `git::UnstageAndNext` |
| **跳转至上一个未保存/未提交的改动点**| 无 | `Ctrl-Shift-Backspace`| `editor::GoToPreviousChange` |
| **跳转至下一个未保存/未提交的改动点**| 无 | `Ctrl-Shift-Alt-Backspace`| `editor::GoToNextChange` |

---

## 5. 高级代码编辑与多光标操作

多光标和驼峰式子词（Subword）选择是高阶程序员编写繁琐代码时的终极生产力工具。

| 功能描述 | Vim 模式快捷键 (Normal) | 默认 Windows 快捷键 | 绑定 Action |
| :--- | :--- | :--- | :--- |
| **重命名当前符号** (安全重构) | `g r n` 或 `c d` | `F2` | `editor::Rename` |
| **触发代码动作/快速修复** (QuickFix) | `g .` 或 `g r a` | `Ctrl-.` | `editor::ToggleCodeActions` |
| **显示悬浮文档提示** (Hover) | `g h` 或 `Shift-k` | `Ctrl-i` | `editor::Hover` |
| **添加多光标到下一个相同单词** | `g n` | `Ctrl-d` | `editor::SelectNext` (不跳过) |
| **跳过当前匹配并添加多光标** | 无 | `Ctrl-k Ctrl-d` | `editor::SelectNext` (带 `replace_newest: true`) |
| **多光标选择当前词的所有匹配** | `g a` | `Ctrl-f2` | `editor::SelectAllMatches` |
| **在当前行上方插入新光标** | 无 | `Ctrl-Alt-Up` | `editor::AddSelectionAbove` |
| **在当前行下方插入新光标** | 无 | `Ctrl-Alt-Down` | `editor::AddSelectionBelow` |
| **按驼峰子词向左移动光标** | 无 | `Ctrl-Alt-Left` | `editor::MoveToPreviousSubwordStart` |
| **按驼峰子词向右移动光标** | 无 | `Ctrl-Alt-Right` | `editor::MoveToNextSubwordEnd` |
| **向左删除至驼峰子词开头** | 无 | `Ctrl-Alt-Backspace`| `editor::DeleteToPreviousSubwordStart` |
| **向右删除至驼峰子词结尾** | 无 | `Ctrl-Alt-Delete` | `editor::DeleteToNextSubwordEnd` |
| **选择闭包/封闭结构语法树节点** | 无 | `Shift-Alt-e` | `editor::SelectEnclosingSymbol` |
| **将多光标选中的行在多缓冲区打开** | 无 | `Alt-Enter` | `editor::OpenSelectionsInMultibuffer` |

---

## 6. 分屏窗口与标签页布局

Zed 拥有一流的多分屏引擎，无需使用鼠标即可进行灵活排版。

| 功能描述 | Vim 模式快捷键 (Normal) | 默认 Windows 快捷键 | 绑定 Action |
| :--- | :--- | :--- | :--- |
| **垂直拆分当前编辑区** (向右分屏) | `Ctrl-w v` 或 `Ctrl-w Ctrl-v` | `Ctrl-\` 或 `Ctrl-k Right` | `pane::SplitVertical` |
| **水平拆分当前编辑区** (向下分屏) | `Ctrl-w s` 或 `Ctrl-w Ctrl-s` | `Ctrl-k Down` | `pane::SplitHorizontal` |
| **向左/向上/向右垂直/水平拆分分屏** | 无 | `Ctrl-k Left / Up / Right` | `pane::SplitLeft / SplitUp ...` |
| **将焦点转移至 左/下/上/右 分屏** | `Ctrl-w h / j / k / l` | `Ctrl-k Ctrl-Left / Down ...` | `workspace::ActivatePaneLeft / Down ...` |
| **直接跳转到第 1~9 个分屏** | 无 | `Alt-1` ~ `Alt-9` | `workspace::ActivatePane` (基于索引) |
| **跳转至当前分屏的第 1~9 个标签页** | 无 | `Alt-1` ~ `Alt-9` (在当前分屏激活时)| `pane::ActivateItem` (基于索引) |
| **跳转至当前分屏的最后一个标签页** | 无 | `Alt-0` | `pane::ActivateLastItem` |
| **将标签页向左/向右交换位置 (重排序)**| 无 | `Ctrl-Shift-PageUp / PageDown` | `pane::SwapItemLeft / SwapItemRight` |
| **关闭当前标签页/分屏** | `Ctrl-w c` 或 `Ctrl-w q` | `Ctrl-w` 或 `Ctrl-F4` | `pane::CloseActiveItem` |
| **关闭除当前页外的其他所有页** | `Ctrl-w o` | `Ctrl-Shift-Alt-w` | `workspace::CloseInactiveTabsAndPanes` |
| **关闭当前分屏左侧/右侧的所有标签页**| 无 | `Ctrl-k e` / `Ctrl-k t` | `pane::CloseItemsToTheLeft / Right` |
| **关闭所有未修改 (Clean) 的标签页** | 无 | `Ctrl-k u` | `pane::CloseCleanItems` |
| **关闭当前分屏的所有标签页** | 无 | `Ctrl-k w` | `pane::CloseAllItems` |
| **关闭所有分屏的所有标签页** | `Ctrl-w a` 或 `Ctrl-w Ctrl-a` | `Ctrl-k Ctrl-w` | `workspace::CloseAllItemsAndPanes` |

---

## 7. Vim 环绕字符与语义文本对象

仅在 **Vim 模式** 下生效的进阶文本编辑器级功能（源于经典的 `vim-surround` 功能拓展）。

### A. 环绕操作 (Surround)
* **`y s <motion> <char>`**: **添加**环绕字符。例如：`y s w "` 表示用双引号包围当前单词。
* **`d s <char>`**: **删除**指定的外部环绕字符。例如：`d s "` 表示删除外层的双引号。
* **`c s <old_char> <new_char>`**: **更改**指定的外部环绕字符。例如：`c s " '` 表示把外层的双引号替换为单引号。

### B. 语义代码文本对象 (Text Objects)
配合操作符如 `d` (删除), `c` (修改), `y` (复制), `v` (选择) 等使用：
* **`a`**: **参数 (Argument)**。表示函数参数列表中的某一项（包含前后的逗号与空白符）。
* **`f`**: **方法/函数 (Method/Function)**。表示一整段函数体。
* **`c`**: **类/结构体 (Class/Struct)**。表示一整个类或者 Struct 定义块。
* **`e`**: **整篇文档 (Entire file)**。表示文件的全部缓冲区内容。
* **`q`**: **任意成对引号 (Any Quotes)**。自动抓取最近的单/双/反引号范围。
* **`b`** 或 **`(` / `)`**: **小括号**范围。
* **`r`** 或 **`[` / `]`**: **中括号**范围。
* **`B`** 或 **`{` / `}`**: **大括号**范围。

---

## 8. 智能 AI 编程与自动补全

Zed 的深度特色在于将 AI 编程能力集成到了编辑器的核心部分。

| 功能描述 | Vim 模式快捷键 (Insert) | 默认 Windows 快捷键 | 绑定 Action |
| :--- | :--- | :--- | :--- |
| **唤醒行内 AI 助手** (Inline AI) | `Ctrl-x Ctrl-a` | `Ctrl-i` (可在终端唤醒!) | [assistant::InlineAssist](file:///C:/Users/hengvvang/Desktop/zed/crates/assistant) |
| **接受 AI 生成结果** | `Ctrl-Shift-Enter` | `Ctrl-Shift-Enter` | `inline_assistant::ThumbsUpResult` |
| **拒绝 AI 生成结果** | `Ctrl-Shift-Delete` | `Ctrl-Shift-Delete` | `inline_assistant::ThumbsDownResult` |
| **接受 AI 行内编辑预测建议** | `Tab` (若处于 eager 模式) | `Tab` | `editor::AcceptEditPrediction` |
| **手动显示 AI 行内编辑预测** | `Ctrl-x Ctrl-c` | `Alt-\` | `editor::ShowEditPrediction` |
| **将选中的代码追加入 AI 对话线程** | `Ctrl-Shift-.` | `Ctrl-Shift-.` | `agent::AddSelectionToThread` |
| **强制召唤 LSP 补全菜单** | `Ctrl-x Ctrl-o` | `Ctrl-Space` | `editor::ShowCompletions` |

---

## 9. 任务管理器与外部终端

Zed 允许您通过工作空间根目录下的 `.zed/tasks.json` 自定义运行/测试任务。

| 功能描述 | 快捷键 (全局) | 绑定 Action | 详细说明 |
| :--- | :--- | :--- | :--- |
| **启动/选择任务** (Spawn Task) | `Shift-Alt-t` | `task::Spawn` | 扫描并弹窗列出项目中已定义的所有 Tasks 并执行 |
| **重新执行上一次任务** (Rerun) | `Ctrl-Shift-r` 或 `Alt-t` | `task::Rerun` | 不弹窗，直接重新启动上次执行完毕或被停止的任务 |
| **在新分屏中展示任务输出** | `Shift-Alt-r` | `task::Spawn` (带属性) | 启动任务，但强制将输出端口对齐到正中央分屏 |
| **终端清屏** | `Ctrl-Shift-l` | `terminal::Clear` | 当焦点在内置终端时，快速清空终端显示缓冲区 |
| **运行/调试启动** | `F4` | `debugger::Start` | 调起调试器 (DAP) 执行当前的编译/启动配置 |

---

## 10. 项目侧边栏 Netrw 兼容模式

当您使用 `Ctrl-b` 打开项目文件侧边栏，并使用快捷键聚焦它时（如 Vim 模式下的 `escape` 等操作），文件树将进入高度契合键盘流的导航模式。

| 快捷键 | 绑定 Action | 详细说明 |
| :--- | :--- | :--- |
| **`j`** / **`k`** | `vim::MenuSelectNext / Previous` | 光标在文件树列表中**向下/向上**移动 |
| **`h`** / **`l`** | `project_panel::Collapse / ExpandSelectedEntry` | **折叠/展开**当前选中的文件夹目录 |
| **`%`** | `project_panel::NewFile` | 在光标所在的目录下**创建新文件** |
| **`d`** | `project_panel::NewDirectory` | 在光标所在的目录下**创建新文件夹** |
| **`v`** | `project_panel::OpenSplitVertical` | 将选中的文件在**垂直分屏**中打开 |
| **`o`** | `project_panel::OpenSplitHorizontal` | 将选中的文件在**水平分屏**中打开 |
| **`Shift-d`** | `project_panel::Delete` | 弹出提示并**删除**当前选中的文件/文件夹 |
| **`Shift-r`** | `project_panel::Rename` | 弹出输入框对当前选中项进行**重命名** |
| **`x`** | `project_panel::RevealInFileManager` | 在操作系统的资源管理器中高亮打开当前文件所在的目录 |

---

## 11. DAP 交互式调试器快捷键

Zed 支持交互式调试 (Debug Adapter Protocol)。通过下方按键，开发期间可以直接单步走读和管理断点。

| 功能描述 | 全局快捷键 | 面板内快捷键 | 绑定 Action |
| :--- | :--- | :--- | :--- |
| **启动调试配置** | `F4` | 无 | `debugger::Start` |
| **停止调试会话** | `Shift-F5` | 无 | `debugger::Stop` |
| **重跑当前调试配置** | `Ctrl-Shift-F5` | 无 | `debugger::RerunSession` |
| **暂停执行** | `F6` | 无 | `debugger::Pause` |
| **恢复执行 (Continue)** | `F5` (仅在会话中) | 无 | `debugger::Continue` |
| **单步跳过 (Step Over)** | `F10` | 无 | `debugger::StepOver` |
| **单步跳出 (Step Out)** | `Shift-F11` | 无 | `debugger::StepOut` |
| **一键开关/切换当前行断点** | `F9` | `Space` (断点面板) | `editor::ToggleBreakpoint` |
| **编辑日志断点 (Logpoint)** | `Shift-F9` | 无 | `editor::EditLogBreakpoint` |
| **删除当前选中断点** | 无 | `Backspace` (断点面板) | `debugger::UnsetBreakpoint` |
| **切换调试线程选择器** | 无 | `Ctrl-t` | `debugger::ToggleThreadPicker` |
| **切换会话选择器** | 无 | `Ctrl-i` | `debugger::ToggleSessionPicker` |

---

## 12. 高级代码折叠 (Code Folding)

针对阅读长函数和大型逻辑块，代码折叠能够极大保持脑图的清爽。

| 折叠层级或动作 | Vim 模式快捷键 | 默认 Windows 快捷键 | 绑定 Action |
| :--- | :--- | :--- | :--- |
| **折叠当前光标所在代码块** | `z c` | `Ctrl-Shift-[` | `editor::Fold` |
| **展开当前光标所在代码块** | `z o` | `Ctrl-Shift-]` | `editor::UnfoldLines` |
| **一键折叠/展开当前光标所在块** | `z a` | `Ctrl-k Ctrl-l` | `editor::ToggleFold` |
| **递归折叠当前块的所有子块** | `z Shift-c` | `Ctrl-k Ctrl-[` | `editor::FoldRecursive` |
| **递归展开当前块的所有子块** | `z Shift-o` | `Ctrl-k Ctrl-]` | `editor::UnfoldRecursive` |
| **折叠第 1~9 层缩进代码块** | 无 | `Ctrl-k Ctrl-1` ~ `9` | `editor::FoldAtLevel_1` ~ `9` |
| **全部折叠** | `z Shift-m` | `Ctrl-k Ctrl-0` | `editor::FoldAll` |
| **全部展开** | `z Shift-r` | `Ctrl-k Ctrl-j` | `editor::UnfoldAll` |

---

## 13. Helix 模拟模式 (Helix Mode)

在 [vim.json](file:///C:/Users/hengvvang/Desktop/zed/assets/keymaps/vim.json) 中，Zed 内置了对现代编辑器 **Helix** 模式的深入仿真。在上下文为 `vim_mode == helix_normal` 或 `vim_mode == helix_select` 时，可以使用下方按键动作：

| 快捷键 | 绑定 Action | 详细说明 |
| :--- | :--- | :--- |
| **`space f`** | `file_finder::Toggle` | 唤起文件查找器 (类似 Vim 模式下的 `Space f`) |
| **`space s`** / **`space Shift-s`** | `outline::Toggle` / `project_symbols::Toggle` | 展开大纲 / 全局搜索符号 |
| **`space w v`** / **`space w s`** | `pane::SplitRight` / `pane::SplitDown` | 垂直/水平拆分窗口 (Helix 专有组合键) |
| **`space w h / j / k / l`** | `workspace::ActivatePaneLeft / Down / Up / Right` | 切换焦点到左/下/上/右分屏 |
| **`x`** | `vim::HelixSelectLine` | **扩展选中**当前整行行，多次按下会连续向下加选 |
| **`;`** | `vim::HelixCollapseSelection` | **折叠当前多选区域**为单光标 (Collapse selection) |
| **`alt-;`** | `vim::OtherEnd` | 在当前选择区域的**头部与尾部**之间来回切换光标焦点 |
| **`g h`** / **`g l`** | `vim::StartOfLine` / `vim::EndOfLine` | 快速飞到行首 / 行尾 |
| **`g e`** | `vim::EndOfDocument` | 飞到文件最后一行的行尾 |

---

## 核心生产力实战场景示例

### 示例 A：Vim Surround 环绕操作
假设有如下 Rust 代码：
```rust
let name = hello_world;
```
您的光标停留在 `hello_world` 上，处于 Normal 模式：
1. 输入 **`y s w "`**：
   * `y s`（环绕）+ `w`（当前单词）+ `"`（环绕目标字符）。
   * 结果：
     ```rust
     let name = "hello_world";
     ```
2. 输入 **`c s " {`**：
   * `c s`（修改环绕）+ `"`（原环绕）+ `{`（新环绕）。
   * 结果（左大括号 `{` 会在闭合时自动追加空格，而 `}` 则不会）：
     ```rust
     let name = { hello_world };
     ```
3. 输入 **`d s {`**：
   * 删除环绕括号。
   * 结果还原为：
     ```rust
     let name = hello_world;
     ```

### 示例 B：多光标秒级变量重写 (默认模式)
假设要将一小段代码里的所有局部变量 `index` 改为 `idx`：
```rust
let offset = index * 4;
let next_index = index + 1;
```
1. 双击选中第一个 `index`（光标处）。
2. 按下 **`Ctrl-d`**。此时 Zed 会自动向下搜索到第二个 `index`（注意：它足够智能，**不会**误选 `next_index` 中的 `index` 部分，因为它按整词匹配）。
3. 此时屏幕上有两个活动光标。直接输入 `idx`，即可同时完成两处修改。
4. （进阶）如果您在按下 `Ctrl-d` 时，想跳过某一个匹配项，可以按下 **`Ctrl-k Ctrl-d`**，这会**撤销最新一次光标的添加**，并自动高亮并选中再往下的那一个匹配项。

### 示例 C：大范围代码结构修改 (语义文本对象)
假设有如下 Rust 函数：
```rust
fn construct_payload(id: u64, name: String, options: Options) -> Payload {
    Payload {
        id,
        name,
        options,
        active: true,
    }
}
```
1. 您的光标停在 `Payload {` 内部。
2. 您想删除整个函数的内容重新编写。无需手动拉动鼠标，直接在 Normal 模式下输入 **`c i f`** (Change Inner Function)。
3. 函数体花括号 `{ ... }` 内部的 4 行代码瞬间被清空，且光标停在空白函数体内，直接处于 Insert 模式准备输入：
   ```rust
   fn construct_payload(id: u64, name: String, options: Options) -> Payload {
       |
   }
   ```
4. 如果您需要改写参数列表，将光标放在 `id` 处，按下 **`d a`** (Delete Argument)，会连同逗号一起删掉第一个参数。

### 示例 D：AI 与终端的敏捷协作
1. 按下 **`Ctrl-``** 调出底部终端。
2. 即使在终端内部，按下 **`Ctrl-i`** 也能唤起 Inline AI 助手，在终端中直接命令 AI 编写一条命令，例如输入：“获取包含 zed 字符串的所有进行名字”，AI 会直接输出命令，按下 `Ctrl-Shift-Enter` 自动接受填入终端，随后回车即可直接执行！
3. 执行任务出错时，回到代码，按 **`Ctrl-Shift-Backspace`** 回到上一个最近的改动行，修复后按 **`Alt-t`** 一键重新执行上次任务。
