# Zed 默认 VS Code 布局与 Vim 快捷键总览

本目录已按模块拆分，不再把所有快捷键堆在一个文件里。`all.md` 只作为总览和导航；完整列表请进入下面各模块。

- 抽取依据：Zed 源码 commit `afaef857b987d924c5ec09265a83feb030283f48`
- 平台口径：Windows
- 默认布局口径：`base_keymap = VSCode`，即 Zed 默认 VS Code 布局
- 内容组织：按功能场景拆分模块，每个快捷键表第一列直接说明功能。

## 建议阅读顺序

1. 先看[来源、加载逻辑与统计口径](keymaps/reference/source-and-loading-logic.md)，确认哪些源文件被纳入。
2. 再看 VS Code 默认布局模块：从全局/编辑器 → 工作区/窗格 → 搜索/Picker → 面板 → 终端/Git/Agent → 特殊上下文。
3. 如果启用 Vim mode，再看 Vim 模块：Normal → 操作符/文本对象 → Insert/Visual → 窗口/项目/终端 → Helix/特殊集成 → `:` 命令。

## 模块目录

| 模块 | 文件 | 说明 |
|---|---|---|
| 来源、加载逻辑与统计口径 | [`keymaps/reference/source-and-loading-logic.md`](keymaps/reference/source-and-loading-logic.md) | 说明为什么这些文件属于默认 VS Code/Vim 快捷键范围。 |
| VS Code 默认布局：全局、菜单与编辑器基础 | [`keymaps/vscode/01-global-editor.md`](keymaps/vscode/01-global-editor.md) | 全局命令、菜单、基础编辑、移动、选择、格式化等。 |
| VS Code 默认布局：工作区、窗格、标签与窗口 | [`keymaps/vscode/02-workspace-panes-tabs.md`](keymaps/vscode/02-workspace-panes-tabs.md) | 窗口、标签页、分屏、窗格焦点与工作区级操作。 |
| VS Code 默认布局：搜索、替换、Picker 与命令入口 | [`keymaps/vscode/03-search-pickers-command.md`](keymaps/vscode/03-search-pickers-command.md) | 文件查找、文本搜索、替换、命令面板、符号跳转等。 |
| VS Code 默认布局：侧边栏与面板 | [`keymaps/vscode/04-panels-sidebars.md`](keymaps/vscode/04-panels-sidebars.md) | 项目、侧栏、通知、协作等面板类操作。 |
| VS Code 默认布局：终端、调试、Git 与 Agent/AI | [`keymaps/vscode/05-terminal-debug-git-agent.md`](keymaps/vscode/05-terminal-debug-git-agent.md) | 终端、调试、Git、AI/Agent、LSP 工具相关快捷键。 |
| VS Code 默认布局：其它特殊上下文 | [`keymaps/vscode/06-special-contexts.md`](keymaps/vscode/06-special-contexts.md) | Notebook、任务、扩展、特殊 UI 状态等上下文。 |
| VS Code 默认布局：specific overrides 高优先级覆盖 | [`keymaps/vscode/07-specific-overrides.md`](keymaps/vscode/07-specific-overrides.md) | 默认加载链路最后应用的内置覆盖快捷键。 |
| Vim mode：Normal/VimControl 移动、导航与 Zed 语义跳转 | [`keymaps/vim/01-normal-motion-navigation.md`](keymaps/vim/01-normal-motion-navigation.md) | 普通模式移动、搜索、跳转、LSP、诊断和滚动。 |
| Vim mode：操作符、文本对象、surround 与 exchange | [`keymaps/vim/02-operators-textobjects-surround.md`](keymaps/vim/02-operators-textobjects-surround.md) | 操作符、文本对象、surround、exchange 等组合命令。 |
| Vim mode：Insert、Visual、Replace、Literal 与输入相关模式 | [`keymaps/vim/03-insert-visual-replace-literal.md`](keymaps/vim/03-insert-visual-replace-literal.md) | 插入、可视、替换、literal 输入等模式快捷键。 |
| Vim mode：窗口、窗格、项目面板、终端与侧栏 | [`keymaps/vim/04-window-project-terminal-panels.md`](keymaps/vim/04-window-project-terminal-panels.md) | Vim 风格窗格、项目面板、终端、侧栏导航。 |
| Vim mode：Helix 兼容与特殊集成 | [`keymaps/vim/05-helix-and-special-integrations.md`](keymaps/vim/05-helix-and-special-integrations.md) | Helix 兼容层和特殊集成上下文。 |
| Vim mode：其它上下文 | [`keymaps/vim/07-other-vim-contexts.md`](keymaps/vim/07-other-vim-contexts.md) | 未归入前面分类的 Vim 上下文快捷键。 |
| Vim mode：命令行 `:` 命令 | [`keymaps/vim/06-command-line.md`](keymaps/vim/06-command-line.md) | Vim 命令行命令说明，不是 JSON keymap 按键表。 |

## 核心结论

- VS Code 默认布局在源码中没有单独的 `vscode.json`，而是使用平台默认 keymap；Windows 对应 `assets/keymaps/default-windows.json`。
- `specific-overrides.json` 也属于默认加载链路的一部分，且比默认/base/vim 内置绑定优先级更高，所以单独列为模块。
- Vim 快捷键来自 `assets/keymaps/vim.json`；Vim `:` 命令行命令来自 `crates/vim/src/command.rs`，不是 JSON keymap。
- 每个模块保留原始 `context`、源文件、section 编号、快捷键序列、Action 和参数，并在第一列直接说明快捷键功能。

## 主要源码/文档依据

- `docs/src/key-bindings.md`：预设 keymap、用户 keymap、key sequence、context 语法。
- `docs/src/vim.md`：Vim mode 设计、Zed-specific Vim 功能、插入模式快捷键与命令行说明。
- `crates/settings/src/base_keymap_setting.rs`：`BaseKeymap` 默认值与各布局资产路径。
- `crates/settings/src/settings.rs`：平台默认 keymap、Vim keymap、specific overrides 的资产常量。
- `crates/zed/src/zed.rs::load_default_keymap`：运行时 keymap 加载顺序。
- `assets/keymaps/default-windows.json`：Windows 默认 VS Code 布局快捷键。
- `assets/keymaps/specific-overrides.json`：非 macOS 通用高优先级覆盖绑定。
- `assets/keymaps/vim.json`：Vim mode 快捷键定义。
- `crates/vim/src/command.rs`：Vim `:` 命令行命令、范围/搜索/替换/set 解析。
