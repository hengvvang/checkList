# Vim mode：窗口、窗格、项目面板、终端与侧栏

包含 `ctrl-w` 窗格命令、ProjectPanel、Workspace、Terminal、Threads/Agents sidebar 等非编辑区 Vim 风格快捷键。


## `(vim_mode == helix_normal || vim_mode == helix_select) && !menu`

- 源文件：`assets/keymaps/vim.json`
- Section：`12`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：向左移动，必要时换到上一行 | `h` | `vim::WrappingLeft` |
| Vim：向左移动，必要时换到上一行 | `left` | `vim::WrappingLeft` |
| Vim：向右移动，必要时换到下一行 | `l` | `vim::WrappingRight` |
| Vim：向右移动，必要时换到下一行 | `right` | `vim::WrappingRight` |
| Vim：输入字符并向前查找 | `t` | `vim::PushFindForward`; 参数 `[{"before":true,"multiline":true}]` |
| Vim：输入字符并向前查找 | `f` | `vim::PushFindForward`; 参数 `[{"before":false,"multiline":true}]` |
| Vim：输入字符并向后查找 | `shift-t` | `vim::PushFindBackward`; 参数 `[{"after":true,"multiline":true}]` |
| Vim：输入字符并向后查找 | `shift-f` | `vim::PushFindBackward`; 参数 `[{"after":false,"multiline":true}]` |
| Vim：重复上次字符查找 | `alt-.` | `vim::RepeatFind` |
| 粘贴剪贴板内容 | `shift-r` | `editor::Paste` |
| Vim：执行 Convert To Lower Case | `` ` `` | `vim::ConvertToLowerCase` |
| Vim：执行 Convert To Upper Case | `` alt-` `` | `vim::ConvertToUpperCase` |
| Vim：执行 Insert Before | `insert` | `vim::InsertBefore` |
| 重做被撤销的编辑 | `shift-u` | `editor::Redo` |
| Vim：重做 | `ctrl-r` | `vim::Redo` |
| Vim：执行 Helix Yank | `y` | `vim::HelixYank` |
| Vim：执行 Helix Paste | `p` | `vim::HelixPaste` |
| Vim：执行 Helix Paste | `shift-p` | `vim::HelixPaste`; 参数 `[{"before":true}]` |
| Vim：增加缩进 | `>` | `vim::Indent` |
| Vim：减少缩进 | `<` | `vim::Outdent` |
| Vim：执行 Auto Indent | `=` | `vim::AutoIndent` |
| Vim：执行 Helix Delete | `d` | `vim::HelixDelete` |
| 向后删除字符 | `alt-d` | `editor::Delete` |
| Vim：执行 Helix Substitute | `c` | `vim::HelixSubstitute` |
| Vim：执行 Helix Substitute No Yank | `alt-c` | `vim::HelixSubstituteNoYank` |
| Vim：执行 Helix Select Regex | `s` | `vim::HelixSelectRegex` |
| 编辑器：执行 Split Selection Into Lines | `alt-s` | `editor::SplitSelectionIntoLines`; 参数 `[{"keep_selections":true}]` |
| Vim：执行 Helix Collapse Selection | `;` | `vim::HelixCollapseSelection` |
| Vim：执行 Other End | `alt-;` | `vim::OtherEnd` |
| Vim：执行 Helix Keep Newest Selection | `,` | `vim::HelixKeepNewestSelection` |
| Vim：执行 Helix Duplicate Below | `shift-c` | `vim::HelixDuplicateBelow` |
| Vim：执行 Helix Duplicate Above | `alt-shift-c` | `vim::HelixDuplicateAbove` |
| 全选当前编辑器内容 | `%` | `editor::SelectAll` |
| Vim：执行 Helix Select Line | `x` | `vim::HelixSelectLine` |
| 选中当前行 | `shift-x` | `editor::SelectLine` |
| 编辑器：切换Comments | `ctrl-c` | `editor::ToggleComments` |
| 扩大语法节点选区 | `alt-o` | `editor::SelectLargerSyntaxNode` |
| 缩小语法节点选区 | `alt-i` | `editor::SelectSmallerSyntaxNode` |
| 编辑器：选择Previous Syntax Node | `alt-p` | `editor::SelectPreviousSyntaxNode` |
| 编辑器：选择Next Syntax Node | `alt-n` | `editor::SelectNextSyntaxNode` |
| Vim：执行 Helix Select Next | `n` | `vim::HelixSelectNext` |
| Vim：执行 Helix Select Previous | `shift-n` | `vim::HelixSelectPrevious` |
| Vim：执行 Replay Last Recording | `q` | `vim::ReplayLastRecording` |
| Vim：切换Record | `shift-q` | `vim::ToggleRecord` |
| Vim：移动到文档末尾 | `g e` | `vim::EndOfDocument` |
| Vim：移动到行首 | `g h` | `vim::StartOfLine` |
| Vim：移动到行尾 | `g l` | `vim::EndOfLine` |
| Vim：移动到行首第一个非空字符 | `g s` | `vim::FirstNonWhitespace` |
| Vim：移动到窗口顶部 | `g t` | `vim::WindowTop` |
| Vim：移动到窗口中部 | `g c` | `vim::WindowMiddle` |
| Vim：移动到窗口底部 | `g b` | `vim::WindowBottom` |
| 查找所有引用 | `g r` | `editor::FindAllReferences` |
| 跳转到实现 | `g i` | `editor::GoToImplementation` |
| 窗格：执行 Alternate File | `g a` | `pane::AlternateFile` |
| 窗格：执行 Activate Next Item | `g n` | `pane::ActivateNextItem` |
| 窗格：执行 Activate Next Item | `shift-l` | `pane::ActivateNextItem` |
| 窗格：执行 Activate Previous Item | `g p` | `pane::ActivatePreviousItem` |
| 窗格：执行 Activate Previous Item | `shift-h` | `pane::ActivatePreviousItem` |
| Vim：执行 Helix Jump To Word | `g w` | `vim::HelixJumpToWord` |
| Vim：执行 Helix Goto Last Modification | `g .` | `vim::HelixGotoLastModification` |
| 折叠/展开选中的 diff hunk | `g o` | `editor::ToggleSelectedDiffHunks` |
| Git：切换Staged | `g shift-o` | `git::ToggleStaged` |
| 还原 Git 变更 | `g shift-r` | `git::Restore` |
| 暂存当前变更并跳到下一处 | `g u` | `git::StageAndNext` |
| 取消暂存当前变更并跳到下一处 | `g shift-u` | `git::UnstageAndNext` |
| 向右拆分窗格 | `space w v` | `pane::SplitRight` |
| 向下拆分窗格 | `space w s` | `pane::SplitDown` |
| 切换焦点到左侧窗格 | `space w h` | `workspace::ActivatePaneLeft` |
| 切换焦点到下方窗格 | `space w j` | `workspace::ActivatePaneDown` |
| 切换焦点到上方窗格 | `space w k` | `workspace::ActivatePaneUp` |
| 切换焦点到右侧窗格 | `space w l` | `workspace::ActivatePaneRight` |
| 窗格：关闭Active Item | `space w q` | `pane::CloseActiveItem` |
| 向右拆分窗格 | `space w r` | `pane::SplitRight` |
| 向下拆分窗格 | `space w d` | `pane::SplitDown` |
| tab switcher：切换All | `space b` | `tab_switcher::ToggleAll` |
| 打开/关闭文件快速查找 | `space f` | `file_finder::Toggle` |
| 显示悬停信息 | `space k` | `editor::Hover` |
| 打开/关闭文件符号大纲 | `space s` | `outline::Toggle` |
| 打开/关闭项目符号搜索 | `space shift-s` | `project_symbols::Toggle` |
| 跳转到下一个诊断 | `space d` | `editor::GoToDiagnostic` |
| 重命名符号 | `space r` | `editor::Rename` |
| 打开代码操作/快速修复菜单 | `space a` | `editor::ToggleCodeActions` |
| 选择所有匹配项 | `space h` | `editor::SelectAllMatches` |
| 编辑器：切换Comments | `space c` | `editor::ToggleComments` |
| 粘贴剪贴板内容 | `space p` | `editor::Paste` |
| 复制选区或当前行 | `space y` | `editor::Copy` |
| 在窗格中打开搜索 | `space /` | `pane::DeploySearch` |
| 开始调试 | `space shift-g l` | `debugger::Start` |
| 调试器：重启操作 | `space shift-g r` | `debugger::Restart` |
| 切换当前行断点 | `space shift-g b` | `editor::ToggleBreakpoint` |
| 调试器：执行 Continue | `space shift-g c` | `debugger::Continue` |
| 暂停调试 | `space shift-g h` | `debugger::Pause` |
| 调试时单步进入 | `space shift-g i` | `debugger::StepInto` |
| 调试时单步跳出 | `space shift-g o` | `debugger::StepOut` |
| 调试时单步跳过 | `space shift-g n` | `debugger::StepOver` |
| 停止调试 | `space shift-g t` | `debugger::Stop` |
| 编辑日志断点 | `space shift-g ctrl-l` | `editor::EditLogBreakpoint` |
| 打开/关闭命令面板 | `:` | `command_palette::Toggle` |
| Vim：执行 Push Helix Match | `m` | `vim::PushHelixMatch` |
| Vim：执行 Push Helix Next | `]` | `vim::PushHelixNext`; 参数 `[{"around":true}]` |
| Vim：执行 Push Helix Previous | `[` | `vim::PushHelixPrevious`; 参数 `[{"around":true}]` |
| 编辑器：保存Location | `ctrl-s` | `editor::SaveLocation` |
| Vim：执行 Push Rewrap | `g q` | `vim::PushRewrap` |

## `VimControl && !menu || !Editor && !Terminal`

- 源文件：`assets/keymaps/vim.json`
- Section：`42`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消/屏蔽该快捷键在当前上下文中的默认行为 | `ctrl-w` | `null` |
| 切换焦点到左侧窗格 | `ctrl-w left` | `workspace::ActivatePaneLeft` |
| 切换焦点到右侧窗格 | `ctrl-w right` | `workspace::ActivatePaneRight` |
| 切换焦点到上方窗格 | `ctrl-w up` | `workspace::ActivatePaneUp` |
| 切换焦点到下方窗格 | `ctrl-w down` | `workspace::ActivatePaneDown` |
| 切换焦点到左侧窗格 | `ctrl-w ctrl-h` | `workspace::ActivatePaneLeft` |
| 切换焦点到右侧窗格 | `ctrl-w ctrl-l` | `workspace::ActivatePaneRight` |
| 切换焦点到上方窗格 | `ctrl-w ctrl-k` | `workspace::ActivatePaneUp` |
| 切换焦点到下方窗格 | `ctrl-w ctrl-j` | `workspace::ActivatePaneDown` |
| 切换焦点到左侧窗格 | `ctrl-w h` | `workspace::ActivatePaneLeft` |
| 切换焦点到右侧窗格 | `ctrl-w l` | `workspace::ActivatePaneRight` |
| 切换焦点到上方窗格 | `ctrl-w k` | `workspace::ActivatePaneUp` |
| 切换焦点到下方窗格 | `ctrl-w j` | `workspace::ActivatePaneDown` |
| 工作区：执行 Swap Pane Left | `ctrl-w shift-left` | `workspace::SwapPaneLeft` |
| 工作区：执行 Swap Pane Right | `ctrl-w shift-right` | `workspace::SwapPaneRight` |
| 工作区：执行 Swap Pane Up | `ctrl-w shift-up` | `workspace::SwapPaneUp` |
| 工作区：执行 Swap Pane Down | `ctrl-w shift-down` | `workspace::SwapPaneDown` |
| 工作区：执行 Swap Pane Adjacent | `ctrl-w x` | `workspace::SwapPaneAdjacent` |
| 工作区：执行 Swap Pane Adjacent | `ctrl-w ctrl-x` | `workspace::SwapPaneAdjacent` |
| 工作区：移动Pane Left | `ctrl-w shift-h` | `workspace::MovePaneLeft` |
| 工作区：移动Pane Right | `ctrl-w shift-l` | `workspace::MovePaneRight` |
| 工作区：移动Pane Up | `ctrl-w shift-k` | `workspace::MovePaneUp` |
| 工作区：移动Pane Down | `ctrl-w shift-j` | `workspace::MovePaneDown` |
| Vim：执行 Resize Pane Right | `ctrl-w >` | `vim::ResizePaneRight` |
| Vim：执行 Resize Pane Left | `ctrl-w <` | `vim::ResizePaneLeft` |
| Vim：执行 Resize Pane Down | `ctrl-w -` | `vim::ResizePaneDown` |
| Vim：执行 Resize Pane Up | `ctrl-w +` | `vim::ResizePaneUp` |
| Vim：执行 Maximize Pane | `ctrl-w _` | `vim::MaximizePane` |
| Vim：执行 Reset Pane Sizes | `ctrl-w =` | `vim::ResetPaneSizes` |
| 窗格：执行 Activate Next Item | `ctrl-w g t` | `pane::ActivateNextItem` |
| 窗格：执行 Activate Next Item | `ctrl-w ctrl-g t` | `pane::ActivateNextItem` |
| 窗格：执行 Activate Previous Item | `ctrl-w g shift-t` | `pane::ActivatePreviousItem` |
| 窗格：执行 Activate Previous Item | `ctrl-w ctrl-g shift-t` | `pane::ActivatePreviousItem` |
| 工作区：执行 Activate Next Pane | `ctrl-w w` | `workspace::ActivateNextPane` |
| 工作区：执行 Activate Next Pane | `ctrl-w ctrl-w` | `workspace::ActivateNextPane` |
| 工作区：执行 Activate Previous Pane | `ctrl-w p` | `workspace::ActivatePreviousPane` |
| 工作区：执行 Activate Previous Pane | `ctrl-w ctrl-p` | `workspace::ActivatePreviousPane` |
| 工作区：执行 Activate Previous Pane | `ctrl-w shift-w` | `workspace::ActivatePreviousPane` |
| 工作区：执行 Activate Previous Pane | `ctrl-w ctrl-shift-w` | `workspace::ActivatePreviousPane` |
| 窗格：执行 Split Vertical | `ctrl-w ctrl-v` | `pane::SplitVertical` |
| 窗格：执行 Split Vertical | `ctrl-w v` | `pane::SplitVertical` |
| 窗格：执行 Split Horizontal | `ctrl-w shift-s` | `pane::SplitHorizontal` |
| 窗格：执行 Split Horizontal | `ctrl-w ctrl-s` | `pane::SplitHorizontal` |
| 窗格：执行 Split Horizontal | `ctrl-w s` | `pane::SplitHorizontal` |
| 窗格：关闭Active Item | `ctrl-w ctrl-c` | `pane::CloseActiveItem` |
| 窗格：关闭Active Item | `ctrl-w c` | `pane::CloseActiveItem` |
| 窗格：关闭Active Item | `ctrl-w ctrl-q` | `pane::CloseActiveItem` |
| 窗格：关闭Active Item | `ctrl-w q` | `pane::CloseActiveItem` |
| 窗格：关闭All Items | `ctrl-w ctrl-a` | `pane::CloseAllItems` |
| 窗格：关闭All Items | `ctrl-w a` | `pane::CloseAllItems` |
| 工作区：关闭Inactive Tabs And Panes | `ctrl-w ctrl-o` | `workspace::CloseInactiveTabsAndPanes` |
| 工作区：关闭Inactive Tabs And Panes | `ctrl-w o` | `workspace::CloseInactiveTabsAndPanes` |
| 工作区：新建File Split Horizontal | `ctrl-w ctrl-n` | `workspace::NewFileSplitHorizontal` |
| 工作区：新建File Split Horizontal | `ctrl-w n` | `workspace::NewFileSplitHorizontal` |
| Vim：跳转到Tab | `g t` | `vim::GoToTab` |
| Vim：跳转到Previous Tab | `g shift-t` | `vim::GoToPreviousTab` |

## `!Editor && !Terminal`

- 源文件：`assets/keymaps/vim.json`
- Section：`43`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 打开/关闭命令面板 | `:` | `command_palette::Toggle` |
| 在窗格中打开搜索 | `g /` | `pane::DeploySearch` |
| 窗格：执行 Activate Next Item | `] b` | `pane::ActivateNextItem` |
| 窗格：执行 Activate Previous Item | `[ b` | `pane::ActivatePreviousItem` |
| 窗格：执行 Activate Last Item | `] shift-b` | `pane::ActivateLastItem` |
| 窗格：执行 Activate Item | `[ shift-b` | `pane::ActivateItem`; 参数 `[0]` |
| 打开/关闭文件快速查找 | `space f` | `file_finder::Toggle` |
| 在窗格中打开搜索 | `space /` | `pane::DeploySearch` |
| 打开/关闭项目符号搜索 | `space shift-s` | `project_symbols::Toggle` |
| 切换焦点到左侧窗格 | `space w h` | `workspace::ActivatePaneLeft` |
| 切换焦点到下方窗格 | `space w j` | `workspace::ActivatePaneDown` |
| 切换焦点到上方窗格 | `space w k` | `workspace::ActivatePaneUp` |
| 切换焦点到右侧窗格 | `space w l` | `workspace::ActivatePaneRight` |
| 窗格：关闭Active Item | `space w q` | `pane::CloseActiveItem` |

## `ProjectPanel && not_editing`

- 源文件：`assets/keymaps/vim.json`
- Section：`44`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 打开/关闭命令面板 | `:` | `command_palette::Toggle` |
| 在项目面板中新建文件 | `%` | `project_panel::NewFile` |
| 项目面板：新建Search In Directory | `/` | `project_panel::NewSearchInDirectory` |
| 在项目面板中新建目录 | `d` | `project_panel::NewDirectory` |
| 项目面板：打开Permanent | `enter` | `project_panel::OpenPermanent` |
| Vim：切换Project Panel Focus | `escape` | `vim::ToggleProjectPanelFocus` |
| 项目面板：折叠Selected Entry | `h` | `project_panel::CollapseSelectedEntry` |
| Vim：执行 Menu Select Next | `j` | `vim::MenuSelectNext` |
| Vim：执行 Menu Select Previous | `k` | `vim::MenuSelectPrevious` |
| Vim：执行 Menu Select Next | `down` | `vim::MenuSelectNext` |
| Vim：执行 Menu Select Previous | `up` | `vim::MenuSelectPrevious` |
| 项目面板：展开Selected Entry | `l` | `project_panel::ExpandSelectedEntry` |
| 删除项目面板选中项 | `shift-d` | `project_panel::Delete` |
| 重命名项目面板选中项 | `shift-r` | `project_panel::Rename` |
| 项目面板：打开Permanent | `t` | `project_panel::OpenPermanent` |
| 项目面板：打开Split Vertical | `v` | `project_panel::OpenSplitVertical` |
| 项目面板：打开Split Horizontal | `o` | `project_panel::OpenSplitHorizontal` |
| 打开项目面板选中项 | `p` | `project_panel::Open` |
| 项目面板：执行 Reveal In File Manager | `x` | `project_panel::RevealInFileManager` |
| 工作区：打开With System | `s` | `workspace::OpenWithSystem` |
| 项目面板：执行 Compare Marked Files | `z d` | `project_panel::CompareMarkedFiles` |
| 项目面板：选择Next Git Entry | `] c` | `project_panel::SelectNextGitEntry` |
| 项目面板：选择Prev Git Entry | `[ c` | `project_panel::SelectPrevGitEntry` |
| 项目面板：选择Next Diagnostic | `] d` | `project_panel::SelectNextDiagnostic` |
| 项目面板：选择Prev Diagnostic | `[ d` | `project_panel::SelectPrevDiagnostic` |
| 项目面板：选择Next Directory | `}` | `project_panel::SelectNextDirectory` |
| 项目面板：选择Prev Directory | `{` | `project_panel::SelectPrevDirectory` |
| 选择菜单/列表中的最后一项 | `shift-g` | `menu::SelectLast` |
| 选择菜单/列表中的第一项 | `g g` | `menu::SelectFirst` |
| 项目面板：选择Parent | `-` | `project_panel::SelectParent` |
| 项目面板：执行 Scroll Up | `ctrl-u` | `project_panel::ScrollUp` |
| 项目面板：执行 Scroll Down | `ctrl-d` | `project_panel::ScrollDown` |
| 项目面板：执行 Scroll Cursor Top | `z t` | `project_panel::ScrollCursorTop` |
| 项目面板：执行 Scroll Cursor Center | `z z` | `project_panel::ScrollCursorCenter` |
| 项目面板：执行 Scroll Cursor Bottom | `z b` | `project_panel::ScrollCursorBottom` |
| Vim：执行 Number | `0` | `vim::Number`; 参数 `[0]` |
| Vim：执行 Number | `1` | `vim::Number`; 参数 `[1]` |
| Vim：执行 Number | `2` | `vim::Number`; 参数 `[2]` |
| Vim：执行 Number | `3` | `vim::Number`; 参数 `[3]` |
| Vim：执行 Number | `4` | `vim::Number`; 参数 `[4]` |
| Vim：执行 Number | `5` | `vim::Number`; 参数 `[5]` |
| Vim：执行 Number | `6` | `vim::Number`; 参数 `[6]` |
| Vim：执行 Number | `7` | `vim::Number`; 参数 `[7]` |
| Vim：执行 Number | `8` | `vim::Number`; 参数 `[8]` |
| Vim：执行 Number | `9` | `vim::Number`; 参数 `[9]` |

## `ThreadsSidebar && !Editor`

- 源文件：`assets/keymaps/vim.json`
- Section：`61`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 选择菜单/列表中的下一项 | `j` | `menu::SelectNext` |
| 选择菜单/列表中的上一项 | `k` | `menu::SelectPrevious` |
| 返回父菜单或收起当前项 | `h` | `menu::SelectParent` |
| 进入子菜单或展开当前项 | `l` | `menu::SelectChild` |
| 选择菜单/列表中的第一项 | `g g` | `menu::SelectFirst` |
| 选择菜单/列表中的最后一项 | `shift-g` | `menu::SelectLast` |
| agents sidebar：聚焦Sidebar Filter | `/` | `agents_sidebar::FocusSidebarFilter` |
| Agent/AI：移除Selected Thread | `d d` | `agent::RemoveSelectedThread` |
| agents sidebar：新建Thread In Group | `o` | `agents_sidebar::NewThreadInGroup` |
| agents sidebar：新建Thread In Group | `shift-o` | `agents_sidebar::NewThreadInGroup` |
| multi workspace：执行 Next Project | `] p` | `multi_workspace::NextProject` |
| multi workspace：执行 Previous Project | `[ p` | `multi_workspace::PreviousProject` |
| 切换当前代码块折叠 | `z a` | `editor::ToggleFold` |
| 返回父菜单或收起当前项 | `z c` | `menu::SelectParent` |
| 进入子菜单或展开当前项 | `z o` | `menu::SelectChild` |
| 折叠所有代码块 | `z shift-m` | `editor::FoldAll` |
| 展开所有代码块 | `z shift-r` | `editor::UnfoldAll` |

## `ThreadsSidebar > Editor && VimControl && vim_mode == normal`

- 源文件：`assets/keymaps/vim.json`
- Section：`62`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 光标下移 | `j` | `editor::MoveDown` |
| 光标上移 | `k` | `editor::MoveUp` |
| Vim：进入插入模式 | `/` | `vim::SwitchToInsertMode` |
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |
| 插入换行 | `enter` | `editor::Newline` |

## `SkillCreator`

- 源文件：`assets/keymaps/vim.json`
- Section：`63`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| skill creator：聚焦Next Field | `tab` | `skill_creator::FocusNextField` |
| skill creator：聚焦Previous Field | `shift-tab` | `skill_creator::FocusPreviousField` |

## `SkillCreator > Editor`

- 源文件：`assets/keymaps/vim.json`
- Section：`64`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| skill creator：聚焦Next Field | `tab` | `skill_creator::FocusNextField` |
| skill creator：聚焦Previous Field | `shift-tab` | `skill_creator::FocusPreviousField` |

