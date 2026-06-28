# VS Code 默认布局：全局、菜单与编辑器基础

包含无 context 的全局绑定、菜单、基础编辑器输入/选择/移动、Markdown/Jupyter 等与编辑器主体直接相关的默认快捷键。


## `全局 / 无 context`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`1`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 选择菜单/列表中的第一项 | `home` | `menu::SelectFirst` |
| 选择菜单/列表中的第一项 | `shift-pageup` | `menu::SelectFirst` |
| 选择菜单/列表中的第一项 | `pageup` | `menu::SelectFirst` |
| 选择菜单/列表中的最后一项 | `end` | `menu::SelectLast` |
| 选择菜单/列表中的最后一项 | `shift-pagedown` | `menu::SelectLast` |
| 选择菜单/列表中的最后一项 | `pagedown` | `menu::SelectLast` |
| 选择菜单/列表中的下一项 | `ctrl-n` | `menu::SelectNext` |
| 选择菜单/列表中的下一项 | `tab` | `menu::SelectNext` |
| 选择菜单/列表中的下一项 | `down` | `menu::SelectNext` |
| 选择菜单/列表中的上一项 | `ctrl-p` | `menu::SelectPrevious` |
| 选择菜单/列表中的上一项 | `shift-tab` | `menu::SelectPrevious` |
| 选择菜单/列表中的上一项 | `up` | `menu::SelectPrevious` |
| 确认当前菜单/列表选择 | `enter` | `menu::Confirm` |
| 执行当前选择的次级确认操作 | `ctrl-enter` | `menu::SecondaryConfirm` |
| 取消菜单/关闭当前弹出层 | `ctrl-c` | `menu::Cancel` |
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |
| 重启/重新运行当前菜单流程 | `shift-alt-enter` | `menu::Restart` |
| 确认 Picker 输入内容 | `alt-enter` | `picker::ConfirmInput`; 参数 `[{"secondary":false}]` |
| 确认 Picker 输入内容 | `ctrl-alt-enter` | `picker::ConfirmInput`; 参数 `[{"secondary":true}]` |
| 关闭当前窗口 | `ctrl-shift-w` | `workspace::CloseWindow` |
| 切换工作区缩放/聚焦显示 | `shift-escape` | `workspace::ToggleZoom` |
| 打开文件 | `ctrl-o` | `workspace::OpenFiles` |
| 打开项目/文件入口 | `ctrl-k ctrl-o` | `workspace::Open` |
| 增大编辑器字体大小 | `ctrl-=` | `zed::IncreaseBufferFontSize`; 参数 `[{"persist":false}]` |
| 增大编辑器字体大小 | `ctrl-shift-=` | `zed::IncreaseBufferFontSize`; 参数 `[{"persist":false}]` |
| 减小编辑器字体大小 | `ctrl--` | `zed::DecreaseBufferFontSize`; 参数 `[{"persist":false}]` |
| 重置编辑器字体大小 | `ctrl-0` | `zed::ResetBufferFontSize`; 参数 `[{"persist":false}]` |
| 打开设置 JSON 文件 | `ctrl-alt-,` | `zed::OpenSettingsFile` |
| 退出 Zed | `ctrl-q` | `zed::Quit` |
| 开始调试 | `f4` | `debugger::Start` |
| 停止调试 | `shift-f5` | `debugger::Stop` |
| 重新运行调试会话 | `ctrl-shift-f5` | `debugger::RerunSession` |
| 暂停调试 | `f6` | `debugger::Pause` |
| 调试时单步跳过 | `f10` | `debugger::StepOver` |
| 调试时单步跳出 | `shift-f11` | `debugger::StepOut` |
| 切换全屏 | `f11` | `zed::ToggleFullScreen` |
| 切换编辑预测菜单 | `ctrl-shift-i` | `edit_prediction::ToggleMenu` |
| 打开/关闭 LSP 工具菜单 | `shift-alt-l` | `lsp_tool::ToggleMenu` |
| 显示协作光标名称 | `ctrl-shift-alt-c` | `editor::DisplayCursorNames` |
| 工作区：切换Worktree Security | `ctrl-shift-alt-s` | `workspace::ToggleWorktreeSecurity` |

## `Picker || menu`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`2`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 选择菜单/列表中的上一项 | `up` | `menu::SelectPrevious` |
| 选择菜单/列表中的下一项 | `down` | `menu::SelectNext` |

## `menu`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`3`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 进入子菜单或展开当前项 | `right` | `menu::SelectChild` |
| 返回父菜单或收起当前项 | `left` | `menu::SelectParent` |

## `Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`4`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消当前编辑器操作 | `escape` | `editor::Cancel` |
| 向前删除字符 | `shift-backspace` | `editor::Backspace` |
| 向前删除字符 | `backspace` | `editor::Backspace` |
| 向后删除字符 | `delete` | `editor::Delete` |
| 插入缩进或跳到下一个输入位置 | `tab` | `editor::Tab` |
| 反向缩进或跳到上一个输入位置 | `shift-tab` | `editor::Backtab` |
| 重新换行/重排当前段落 | `ctrl-k ctrl-q` | `editor::Rewrap` |
| 重新换行/重排当前段落 | `ctrl-k q` | `editor::Rewrap` |
| 删除到上一个单词开头 | `ctrl-backspace` | `editor::DeleteToPreviousWordStart`; 参数 `[{"ignore_newlines":false,"ignore_brackets":false}]` |
| 删除到下一个单词结尾 | `ctrl-delete` | `editor::DeleteToNextWordEnd`; 参数 `[{"ignore_newlines":false,"ignore_brackets":false}]` |
| 剪切选区或当前行 | `shift-delete` | `editor::Cut` |
| 剪切选区或当前行 | `ctrl-x` | `editor::Cut` |
| 复制选区或当前行 | `ctrl-insert` | `editor::Copy` |
| 复制选区或当前行 | `ctrl-c` | `editor::Copy` |
| 粘贴剪贴板内容 | `shift-insert` | `editor::Paste` |
| 粘贴剪贴板内容 | `ctrl-v` | `editor::Paste` |
| 撤销上一步编辑 | `ctrl-z` | `editor::Undo` |
| 重做被撤销的编辑 | `ctrl-y` | `editor::Redo` |
| 重做被撤销的编辑 | `ctrl-shift-z` | `editor::Redo` |
| 光标上移 | `up` | `editor::MoveUp` |
| 向上滚动一行 | `ctrl-up` | `editor::LineUp` |
| 向下滚动一行 | `ctrl-down` | `editor::LineDown` |
| 向上翻页移动光标 | `pageup` | `editor::MovePageUp` |
| 向上翻页 | `alt-pageup` | `editor::PageUp` |
| 向上翻页并扩展选区 | `shift-pageup` | `editor::SelectPageUp` |
| 移动到行首 | `home` | `editor::MoveToBeginningOfLine`; 参数 `[{"stop_at_soft_wraps":true,"stop_at_indent":true}]` |
| 光标下移 | `down` | `editor::MoveDown` |
| 向下翻页移动光标 | `pagedown` | `editor::MovePageDown` |
| 向下翻页 | `alt-pagedown` | `editor::PageDown` |
| 向下翻页并扩展选区 | `shift-pagedown` | `editor::SelectPageDown` |
| 移动到行尾 | `end` | `editor::MoveToEndOfLine`; 参数 `[{"stop_at_soft_wraps":true}]` |
| 光标左移 | `left` | `editor::MoveLeft` |
| 光标右移 | `right` | `editor::MoveRight` |
| 移动到上一个单词开头 | `ctrl-left` | `editor::MoveToPreviousWordStart` |
| 移动到下一个单词结尾 | `ctrl-right` | `editor::MoveToNextWordEnd` |
| 移动到文件开头 | `ctrl-home` | `editor::MoveToBeginning` |
| 移动到文件末尾 | `ctrl-end` | `editor::MoveToEnd` |
| 向上扩展选区 | `shift-up` | `editor::SelectUp` |
| 向下扩展选区 | `shift-down` | `editor::SelectDown` |
| 向左扩展选区 | `shift-left` | `editor::SelectLeft` |
| 向右扩展选区 | `shift-right` | `editor::SelectRight` |
| 扩展选区到上一个单词开头 | `ctrl-shift-left` | `editor::SelectToPreviousWordStart` |
| 扩展选区到下一个单词结尾 | `ctrl-shift-right` | `editor::SelectToNextWordEnd` |
| 扩展选区到文件开头 | `ctrl-shift-home` | `editor::SelectToBeginning` |
| 扩展选区到文件末尾 | `ctrl-shift-end` | `editor::SelectToEnd` |
| 全选当前编辑器内容 | `ctrl-a` | `editor::SelectAll` |
| 选中当前行 | `ctrl-l` | `editor::SelectLine` |
| 格式化代码 | `shift-alt-f` | `editor::Format` |
| 整理导入语句 | `shift-alt-o` | `editor::OrganizeImports` |
| 扩展选区到行首 | `shift-home` | `editor::SelectToBeginningOfLine`; 参数 `[{"stop_at_soft_wraps":true,"stop_at_indent":true}]` |
| 扩展选区到行尾 | `shift-end` | `editor::SelectToEndOfLine`; 参数 `[{"stop_at_soft_wraps":true}]` |
| 打开字符选择面板 | `ctrl-alt-space` | `editor::ShowCharacterPalette` |
| 显示/隐藏行号 | `ctrl-;` | `editor::ToggleLineNumbers` |
| 折叠/展开选中的 diff hunk | `ctrl-'` | `editor::ToggleSelectedDiffHunks` |
| 展开所有 diff hunk | `ctrl-"` | `editor::ExpandAllDiffHunks` |
| 显示函数签名帮助 | `ctrl-i` | `editor::ShowSignatureHelp` |
| 打开 Git blame | `alt-g b` | `git::Blame` |
| 打开已修改文件列表 | `alt-g m` | `git::OpenModifiedFiles` |
| 查看 Git diff | `alt-g r` | `git::ReviewDiff` |
| 打开编辑器上下文菜单 | `menu` | `editor::OpenContextMenu` |
| 打开编辑器上下文菜单 | `shift-f10` | `editor::OpenContextMenu` |
| 编辑器：切换Edit Prediction | `ctrl-alt-e` | `editor::ToggleEditPrediction` |
| 切换当前行断点 | `f9` | `editor::ToggleBreakpoint` |
| 编辑日志断点 | `shift-f9` | `editor::EditLogBreakpoint` |

## `Editor && mode == full`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`5`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 插入换行 | `shift-enter` | `editor::Newline` |
| 插入换行 | `enter` | `editor::Newline` |
| 在下方新建一行 | `ctrl-enter` | `editor::NewlineBelow` |
| 在上方新建一行 | `ctrl-shift-enter` | `editor::NewlineAbove` |
| 切换自动换行 | `ctrl-k ctrl-z` | `editor::ToggleSoftWrap` |
| 切换自动换行 | `ctrl-k z` | `editor::ToggleSoftWrap` |
| 打开当前文件搜索 | `ctrl-f` | `buffer_search::Deploy` |
| 打开当前文件替换 | `ctrl-h` | `buffer_search::DeployReplace` |
| Agent/AI：添加Selection To Thread | `ctrl-shift-.` | `agent::AddSelectionToThread` |
| 编辑器：选择Enclosing Symbol | `shift-alt-e` | `editor::SelectEnclosingSymbol` |
| 跳转到上一处变更 | `ctrl-shift-backspace` | `editor::GoToPreviousChange` |
| 跳转到下一处变更 | `ctrl-shift-alt-backspace` | `editor::GoToNextChange` |
| 在多缓冲区中打开选区 | `alt-enter` | `editor::OpenSelectionsInMultibuffer` |

## `Editor && mode == full && edit_prediction`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`6`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：执行 Next Edit Prediction | `alt-]` | `editor::NextEditPrediction` |
| 编辑器：执行 Previous Edit Prediction | `alt-[` | `editor::PreviousEditPrediction` |

## `Editor && !edit_prediction`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`7`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：显示Edit Prediction | `alt-\` | `editor::ShowEditPrediction` |

## `Editor && mode == auto_height`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`8`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 插入换行 | `ctrl-enter` | `editor::Newline` |
| 插入换行 | `shift-enter` | `editor::Newline` |
| 在下方新建一行 | `ctrl-shift-enter` | `editor::NewlineBelow` |

## `Markdown`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`9`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 复制 Markdown 内容 | `ctrl-c` | `markdown::Copy` |

## `Editor && jupyter`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`10`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| repl：运行操作 | `ctrl-shift-enter` | `repl::Run` |
| repl：运行In Place | `ctrl-alt-enter` | `repl::RunInPlace` |

## `Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`39`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：执行 Outdent | `ctrl-[` | `editor::Outdent` |
| 编辑器：执行 Indent | `ctrl-]` | `editor::Indent` |
| 编辑器：添加Selection Above | `ctrl-alt-up` | `editor::AddSelectionAbove`; 参数 `[{"skip_soft_wrap":true}]` |
| 编辑器：添加Selection Below | `ctrl-alt-down` | `editor::AddSelectionBelow`; 参数 `[{"skip_soft_wrap":true}]` |
| 编辑器：删除Line | `ctrl-shift-k` | `editor::DeleteLine` |
| 编辑器：移动Line Up | `alt-up` | `editor::MoveLineUp` |
| 编辑器：移动Line Down | `alt-down` | `editor::MoveLineDown` |
| 编辑器：执行 Duplicate Line Up | `shift-alt-up` | `editor::DuplicateLineUp` |
| 编辑器：执行 Duplicate Line Down | `shift-alt-down` | `editor::DuplicateLineDown` |
| 扩大语法节点选区 | `shift-alt-right` | `editor::SelectLargerSyntaxNode` |
| 缩小语法节点选区 | `shift-alt-left` | `editor::SelectSmallerSyntaxNode` |
| 选择所有匹配项 | `ctrl-shift-l` | `editor::SelectAllMatches` |
| 选择所有匹配项 | `ctrl-f2` | `editor::SelectAllMatches` |
| 选择下一个匹配项/添加下一个选择 | `ctrl-d` | `editor::SelectNext`; 参数 `[{"replace_newest":false}]` |
| 选择下一个匹配项/添加下一个选择 | `ctrl-f3` | `editor::SelectNext`; 参数 `[{"replace_newest":false}]` |
| 选择下一个匹配项/添加下一个选择 | `ctrl-k ctrl-d` | `editor::SelectNext`; 参数 `[{"replace_newest":true}]` |
| 选择上一个匹配项/添加上一个选择 | `ctrl-shift-f3` | `editor::SelectPrevious`; 参数 `[{"replace_newest":false}]` |
| 显示悬停信息 | `ctrl-k ctrl-i` | `editor::Hover` |
| 显示 Git blame 悬停信息 | `ctrl-k ctrl-b` | `editor::BlameHover` |
| 编辑器：执行 Format Selections | `ctrl-k ctrl-f` | `editor::FormatSelections` |
| 编辑器：切换Comments | `ctrl-/` | `editor::ToggleComments`; 参数 `[{"advance_downwards":false}]` |
| 编辑器：切换Comments | `ctrl-k ctrl-c` | `editor::ToggleComments`; 参数 `[{"advance_downwards":false}]` |
| 编辑器：切换Block Comments | `ctrl-k ctrl-/` | `editor::ToggleBlockComments` |
| 编辑器：切换Block Comments | `shift-alt-a` | `editor::ToggleBlockComments` |
| 跳转到下一个诊断 | `f8` | `editor::GoToDiagnostic`; 参数 `[{"severity":{"min":"hint","max":"error"}}]` |
| 跳转到上一个诊断 | `shift-f8` | `editor::GoToPreviousDiagnostic`; 参数 `[{"severity":{"min":"hint","max":"error"}}]` |
| 重命名符号 | `f2` | `editor::Rename` |
| 跳转到定义 | `f12` | `editor::GoToDefinition` |
| 编辑器：跳转到Definition Split | `alt-f12` | `editor::GoToDefinitionSplit` |
| 跳转到实现 | `ctrl-f12` | `editor::GoToImplementation` |
| 查找所有引用 | `shift-alt-f12` | `editor::FindAllReferences` |
| 编辑器：移动To Enclosing Bracket | `ctrl-shift-\` | `editor::MoveToEnclosingBracket` |
| 折叠当前代码块 | `ctrl-shift-[` | `editor::Fold` |
| 编辑器：展开Lines | `ctrl-shift-]` | `editor::UnfoldLines` |
| 切换当前代码块折叠 | `ctrl-k ctrl-l` | `editor::ToggleFold` |
| 递归折叠当前代码块 | `ctrl-k ctrl-[` | `editor::FoldRecursive` |
| 递归展开当前代码块 | `ctrl-k ctrl-]` | `editor::UnfoldRecursive` |
| 编辑器：折叠At Level 1 | `ctrl-k ctrl-1` | `editor::FoldAtLevel_1` |
| 编辑器：折叠At Level 2 | `ctrl-k ctrl-2` | `editor::FoldAtLevel_2` |
| 编辑器：折叠At Level 3 | `ctrl-k ctrl-3` | `editor::FoldAtLevel_3` |
| 编辑器：折叠At Level 4 | `ctrl-k ctrl-4` | `editor::FoldAtLevel_4` |
| 编辑器：折叠At Level 5 | `ctrl-k ctrl-5` | `editor::FoldAtLevel_5` |
| 编辑器：折叠At Level 6 | `ctrl-k ctrl-6` | `editor::FoldAtLevel_6` |
| 编辑器：折叠At Level 7 | `ctrl-k ctrl-7` | `editor::FoldAtLevel_7` |
| 编辑器：折叠At Level 8 | `ctrl-k ctrl-8` | `editor::FoldAtLevel_8` |
| 编辑器：折叠At Level 9 | `ctrl-k ctrl-9` | `editor::FoldAtLevel_9` |
| 折叠所有代码块 | `ctrl-k ctrl-0` | `editor::FoldAll` |
| 展开所有代码块 | `ctrl-k ctrl-j` | `editor::UnfoldAll` |
| 显示代码补全 | `ctrl-space` | `editor::ShowCompletions` |
| 编辑器：显示Word Completions | `ctrl-shift-space` | `editor::ShowWordCompletions` |
| 打开代码操作/快速修复菜单 | `ctrl-.` | `editor::ToggleCodeActions` |
| 编辑器：执行 Reveal In File Manager | `ctrl-k r` | `editor::RevealInFileManager` |
| 编辑器：复制Path | `ctrl-k p` | `editor::CopyPath` |
| 向右拆分窗格 | `ctrl-\` | `pane::SplitRight` |
| 编辑器：跳转到Hunk | `alt-.` | `editor::GoToHunk` |
| 编辑器：跳转到Previous Hunk | `alt-,` | `editor::GoToPreviousHunk` |

## `Editor && mode == full`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`42`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 打开/关闭文件符号大纲 | `ctrl-shift-o` | `outline::Toggle` |
| go to line：切换操作 | `ctrl-g` | `go_to_line::Toggle` |

## `Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`50`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：执行 Undo Selection | `ctrl-u` | `editor::UndoSelection` |
| 编辑器：执行 Redo Selection | `ctrl-shift-u` | `editor::RedoSelection` |
| 编辑器：执行 Join Lines | `ctrl-shift-j` | `editor::JoinLines` |
| 编辑器：删除To Previous Subword Start | `ctrl-alt-backspace` | `editor::DeleteToPreviousSubwordStart` |
| 编辑器：删除To Previous Subword Start | `shift-alt-h` | `editor::DeleteToPreviousSubwordStart` |
| 编辑器：删除To Next Subword End | `ctrl-alt-delete` | `editor::DeleteToNextSubwordEnd` |
| 编辑器：删除To Next Subword End | `shift-alt-d` | `editor::DeleteToNextSubwordEnd` |
| 编辑器：移动To Previous Subword Start | `ctrl-alt-left` | `editor::MoveToPreviousSubwordStart` |
| 编辑器：移动To Next Subword End | `ctrl-alt-right` | `editor::MoveToNextSubwordEnd` |
| 编辑器：选择To Previous Subword Start | `ctrl-shift-alt-left` | `editor::SelectToPreviousSubwordStart` |
| 编辑器：选择To Next Subword End | `ctrl-shift-alt-right` | `editor::SelectToNextSubwordEnd` |

## `全局 / 无 context`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`61`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 工作区：执行 Follow Next Collaborator | `ctrl-shift-alt-f` | `workspace::FollowNextCollaborator` |
| dev：切换Inspector | `shift-alt-i` | `dev::ToggleInspector` |
