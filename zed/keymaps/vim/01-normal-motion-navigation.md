# Vim mode：Normal/VimControl 移动、导航与 Zed 语义跳转

包含普通模式控制、光标移动、搜索、跳转、LSP 导航、滚动、fold、marks、diagnostics 等核心 VimControl 绑定。


## `VimControl && !menu`

- 源文件：`assets/keymaps/vim.json`
- Section：`1`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：选择/指定文本对象 | `i` | `vim::PushObject`; 参数 `[{"around":false}]` |
| Vim：选择/指定文本对象 | `a` | `vim::PushObject`; 参数 `[{"around":true}]` |
| Vim：向左移动 | `left` | `vim::Left` |
| Vim：向左移动 | `h` | `vim::Left` |
| Vim：向左移动，必要时换到上一行 | `backspace` | `vim::WrappingLeft` |
| Vim：向下移动 | `down` | `vim::Down` |
| Vim：向下移动 | `ctrl-j` | `vim::Down` |
| Vim：向下移动 | `j` | `vim::Down` |
| Vim：移动到下一行行首 | `ctrl-m` | `vim::NextLineStart` |
| Vim：移动到下一行行首 | `+` | `vim::NextLineStart` |
| Vim：移动到下一行行首 | `enter` | `vim::NextLineStart` |
| Vim：移动到上一行行首 | `-` | `vim::PreviousLineStart` |
| Vim：执行 Tab 跳转/补全导航 | `shift-tab` | `vim::Tab` |
| Vim：执行 Tab 跳转/补全导航 | `tab` | `vim::Tab` |
| Vim：向上移动 | `up` | `vim::Up` |
| Vim：向上移动 | `k` | `vim::Up` |
| Vim：向右移动 | `right` | `vim::Right` |
| Vim：向右移动 | `l` | `vim::Right` |
| Vim：向右移动，必要时换到下一行 | `space` | `vim::WrappingRight` |
| Vim：移动到行尾 | `end` | `vim::EndOfLine` |
| Vim：移动到行尾 | `$` | `vim::EndOfLine` |
| Vim：移动到行首第一个非空字符 | `^` | `vim::FirstNonWhitespace` |
| Vim：按行移动并到行首 | `_` | `vim::StartOfLineDownward` |
| Vim：按行移动并到行尾 | `g _` | `vim::EndOfLineDownward` |
| Vim：移动到文档末尾 | `shift-g` | `vim::EndOfDocument` |
| Vim：移动到段落开头 | `{` | `vim::StartOfParagraph` |
| Vim：移动到段落结尾 | `}` | `vim::EndOfParagraph` |
| Vim：移动到上一句 | `(` | `vim::SentenceBackward` |
| Vim：移动到下一句 | `)` | `vim::SentenceForward` |
| Vim：跳转到指定列 | `|` | `vim::GoToColumn` |
| Vim：移动到下一个单词开头 | `w` | `vim::NextWordStart` |
| Vim：移动到下一个单词结尾 | `e` | `vim::NextWordEnd` |
| Vim：移动到上一个单词开头 | `b` | `vim::PreviousWordStart` |
| Vim：移动到上一个单词结尾 | `g e` | `vim::PreviousWordEnd` |
| Vim：移动到下一个单词开头 | `shift-w` | `vim::NextWordStart`; 参数 `[{"ignore_punctuation":true}]` |
| Vim：移动到下一个单词结尾 | `shift-e` | `vim::NextWordEnd`; 参数 `[{"ignore_punctuation":true}]` |
| Vim：移动到上一个单词开头 | `shift-b` | `vim::PreviousWordStart`; 参数 `[{"ignore_punctuation":true}]` |
| Vim：移动到上一个单词结尾 | `g shift-e` | `vim::PreviousWordEnd`; 参数 `[{"ignore_punctuation":true}]` |
| Vim：打开搜索 | `/` | `vim::Search` |
| 在窗格中打开搜索 | `g /` | `pane::DeploySearch` |
| Vim：打开搜索 | `?` | `vim::Search`; 参数 `[{"backwards":true}]` |
| Vim：跳到下一个匹配/目标 | `*` | `vim::MoveToNext` |
| Vim：跳到上一个匹配/目标 | `#` | `vim::MoveToPrevious` |
| Vim：跳到下一个搜索匹配 | `n` | `vim::MoveToNextMatch` |
| Vim：跳到上一个搜索匹配 | `shift-n` | `vim::MoveToPreviousMatch` |
| Vim：跳转到匹配的括号/结构 | `%` | `vim::Matching`; 参数 `[{"match_quotes":true}]` |
| Vim：输入字符并向前查找 | `f` | `vim::PushFindForward`; 参数 `[{"before":false,"multiline":false}]` |
| Vim：输入字符并向前查找 | `t` | `vim::PushFindForward`; 参数 `[{"before":true,"multiline":false}]` |
| Vim：输入字符并向后查找 | `shift-f` | `vim::PushFindBackward`; 参数 `[{"after":false,"multiline":false}]` |
| Vim：输入字符并向后查找 | `shift-t` | `vim::PushFindBackward`; 参数 `[{"after":true,"multiline":false}]` |
| Vim：设置 mark 标记 | `m` | `vim::PushMark` |
| Vim：跳转到 mark 标记 | `'` | `vim::PushJump`; 参数 `[{"line":true}]` |
| Vim：跳转到 mark 标记 | `` ` `` | `vim::PushJump`; 参数 `[{"line":false}]` |
| Vim：重复上次字符查找 | `;` | `vim::RepeatFind` |
| Vim：反向重复上次字符查找 | `,` | `vim::RepeatFindReversed` |
| 导航后退 | `ctrl-o` | `pane::GoBack` |
| 导航前进 | `ctrl-i` | `pane::GoForward` |
| 跳转到定义 | `ctrl-]` | `editor::GoToDefinition` |
| 跳转到更早的标签位置 | `ctrl-t` | `pane::GoToOlderTag` |
| Vim：切回普通模式 | `escape` | `vim::SwitchToNormalMode` |
| Vim：切回普通模式 | `ctrl-[` | `vim::SwitchToNormalMode` |
| Vim：切换字符可视模式 | `v` | `vim::ToggleVisual` |
| Vim：切换行可视模式 | `shift-v` | `vim::ToggleVisualLine` |
| Vim：显示当前位置 | `ctrl-g` | `vim::ShowLocation` |
| Vim：切换块可视模式 | `ctrl-v` | `vim::ToggleVisualBlock` |
| Vim：切换块可视模式 | `ctrl-q` | `vim::ToggleVisualBlock` |
| 显示悬停信息 | `shift-k` | `editor::Hover` |
| Vim：切换替换模式 | `shift-r` | `vim::ToggleReplace` |
| Vim：移动到行首 | `0` | `vim::StartOfLine` |
| Vim：移动到行首 | `home` | `vim::StartOfLine` |
| Vim：向下翻页 | `ctrl-f` | `vim::PageDown` |
| Vim：向下翻页 | `pagedown` | `vim::PageDown` |
| Vim：向上翻页 | `ctrl-b` | `vim::PageUp` |
| Vim：向上翻页 | `pageup` | `vim::PageUp` |
| Vim：向下滚动半屏 | `ctrl-d` | `vim::ScrollDown` |
| Vim：向上滚动半屏 | `ctrl-u` | `vim::ScrollUp` |
| Vim：屏幕向下滚动一行 | `ctrl-e` | `vim::LineDown` |
| Vim：屏幕向上滚动一行 | `ctrl-y` | `vim::LineUp` |
| Vim：准备使用寄存器内容替换 | `g shift-r` | `vim::PushReplaceWithRegister` |
| 重命名符号 | `g r n` | `editor::Rename` |
| 查找所有引用 | `g r r` | `editor::FindAllReferences` |
| 跳转到实现 | `g r i` | `editor::GoToImplementation` |
| 打开代码操作/快速修复菜单 | `g r a` | `editor::ToggleCodeActions` |
| Vim：移动到文档开头 | `g g` | `vim::StartOfDocument` |
| 显示悬停信息 | `g h` | `editor::Hover` |
| 显示 Git blame 悬停信息 | `g B` | `editor::BlameHover` |
| 跳转到定义 | `g d` | `editor::GoToDefinition` |
| 跳转到声明 | `g shift-d` | `editor::GoToDeclaration` |
| 跳转到类型定义 | `g y` | `editor::GoToTypeDefinition` |
| 跳转到实现 | `g shift-i` | `editor::GoToImplementation` |
| 打开光标处链接 | `g x` | `editor::OpenUrl` |
| 打开选中的文件名 | `g f` | `editor::OpenSelectedFilename` |
| Vim：选择下一个匹配项 | `g n` | `vim::SelectNextMatch` |
| Vim：选择上一个匹配项 | `g shift-n` | `vim::SelectPreviousMatch` |
| Vim：添加/选择下一个相同文本 | `g l` | `vim::SelectNext` |
| Vim：添加/选择上一个相同文本 | `g shift-l` | `vim::SelectPrevious` |
| 选择下一个匹配项/添加下一个选择 | `g >` | `editor::SelectNext`; 参数 `[{"replace_newest":true}]` |
| 选择上一个匹配项/添加上一个选择 | `g <` | `editor::SelectPrevious`; 参数 `[{"replace_newest":true}]` |
| 选择所有匹配项 | `g a` | `editor::SelectAllMatches` |
| 打开/关闭文件符号大纲 | `g s` | `outline::Toggle` |
| 打开/关闭文件符号大纲 | `g shift-o` | `outline::Toggle` |
| 打开/关闭项目符号搜索 | `g shift-s` | `project_symbols::Toggle` |
| 打开代码操作/快速修复菜单 | `g .` | `editor::ToggleCodeActions` |
| 查找所有引用 | `g shift-a` | `editor::FindAllReferences` |
| 打开当前搜索摘录/引用摘录 | `g space` | `editor::OpenExcerpts` |
| Vim：跳到下一个匹配/目标 | `g *` | `vim::MoveToNext`; 参数 `[{"partial_word":true}]` |
| Vim：跳到上一个匹配/目标 | `g #` | `vim::MoveToPrevious`; 参数 `[{"partial_word":true}]` |
| Vim：向下移动 | `g j` | `vim::Down`; 参数 `[{"display_lines":true}]` |
| Vim：向下移动 | `g down` | `vim::Down`; 参数 `[{"display_lines":true}]` |
| Vim：向上移动 | `g k` | `vim::Up`; 参数 `[{"display_lines":true}]` |
| Vim：向上移动 | `g up` | `vim::Up`; 参数 `[{"display_lines":true}]` |
| Vim：移动到行尾 | `g $` | `vim::EndOfLine`; 参数 `[{"display_lines":true}]` |
| Vim：移动到行尾 | `g end` | `vim::EndOfLine`; 参数 `[{"display_lines":true}]` |
| Vim：移动到行首 | `g 0` | `vim::StartOfLine`; 参数 `[{"display_lines":true}]` |
| Vim：移动到行首 | `g home` | `vim::StartOfLine`; 参数 `[{"display_lines":true}]` |
| Vim：执行 Middle Of Line | `g shift-m` | `vim::MiddleOfLine`; 参数 `[{"display_lines":true}]` |
| Vim：移动到行首第一个非空字符 | `g ^` | `vim::FirstNonWhitespace`; 参数 `[{"display_lines":true}]` |
| Vim：恢复上次可视选区 | `g v` | `vim::RestoreVisualSelection` |
| 跳转到下一个诊断 | `g ]` | `editor::GoToDiagnostic` |
| 跳转到上一个诊断 | `g [` | `editor::GoToPreviousDiagnostic` |
| Vim：跳到上次插入位置 | `g i` | `vim::InsertAtPrevious` |
| Vim：跳到更新的变更位置 | `g ,` | `vim::ChangeListNewer` |
| Vim：跳到更早的变更位置 | `g ;` | `vim::ChangeListOlder` |
| Vim：移动到窗口顶部 | `shift-h` | `vim::WindowTop` |
| Vim：移动到窗口中部 | `shift-m` | `vim::WindowMiddle` |
| Vim：移动到窗口底部 | `shift-l` | `vim::WindowBottom` |
| Vim：切换Record | `q` | `vim::ToggleRecord` |
| Vim：执行 Replay Last Recording | `shift-q` | `vim::ReplayLastRecording` |
| Vim：执行 Push Replay Register | `@` | `vim::PushReplayRegister` |
| 工作区：执行 Send Keystrokes | `z enter` | `workspace::SendKeystrokes`; 参数 `["z t ^"]` |
| 工作区：执行 Send Keystrokes | `z -` | `workspace::SendKeystrokes`; 参数 `["z b ^"]` |
| 工作区：执行 Send Keystrokes | `z ^` | `workspace::SendKeystrokes`; 参数 `["shift-h k z b ^"]` |
| 工作区：执行 Send Keystrokes | `z +` | `workspace::SendKeystrokes`; 参数 `["shift-l j z t ^"]` |
| 编辑器：执行 Scroll Cursor Top | `z t` | `editor::ScrollCursorTop` |
| 编辑器：执行 Scroll Cursor Center | `z z` | `editor::ScrollCursorCenter` |
| 工作区：执行 Send Keystrokes | `z .` | `workspace::SendKeystrokes`; 参数 `["z z ^"]` |
| 编辑器：执行 Scroll Cursor Bottom | `z b` | `editor::ScrollCursorBottom` |
| 切换当前代码块折叠 | `z a` | `editor::ToggleFold` |
| 编辑器：切换Fold Recursive | `z shift-a` | `editor::ToggleFoldRecursive` |
| 折叠当前代码块 | `z c` | `editor::Fold` |
| 递归折叠当前代码块 | `z shift-c` | `editor::FoldRecursive` |
| 编辑器：展开Lines | `z o` | `editor::UnfoldLines` |
| 递归展开当前代码块 | `z shift-o` | `editor::UnfoldRecursive` |
| 编辑器：折叠Selected Ranges | `z f` | `editor::FoldSelectedRanges` |
| 折叠所有代码块 | `z shift-m` | `editor::FoldAll` |
| 展开所有代码块 | `z shift-r` | `editor::UnfoldAll` |
| Vim：执行 Column Right | `z l` | `vim::ColumnRight` |
| Vim：执行 Column Left | `z h` | `vim::ColumnLeft` |
| Vim：执行 Half Page Right | `z shift-l` | `vim::HalfPageRight` |
| Vim：执行 Half Page Left | `z shift-h` | `vim::HalfPageLeft` |
| 窗格：关闭Active Item | `shift-z shift-q` | `pane::CloseActiveItem`; 参数 `[{"save_intent":"skip"}]` |
| 窗格：关闭Active Item | `shift-z shift-z` | `pane::CloseActiveItem`; 参数 `[{"save_intent":"save_all"}]` |
| Vim：执行 Number | `1` | `vim::Number`; 参数 `[1]` |
| Vim：执行 Number | `2` | `vim::Number`; 参数 `[2]` |
| Vim：执行 Number | `3` | `vim::Number`; 参数 `[3]` |
| Vim：执行 Number | `4` | `vim::Number`; 参数 `[4]` |
| Vim：执行 Number | `5` | `vim::Number`; 参数 `[5]` |
| Vim：执行 Number | `6` | `vim::Number`; 参数 `[6]` |
| Vim：执行 Number | `7` | `vim::Number`; 参数 `[7]` |
| Vim：执行 Number | `8` | `vim::Number`; 参数 `[8]` |
| Vim：执行 Number | `9` | `vim::Number`; 参数 `[9]` |
| 编辑器：跳转到Definition Split | `ctrl-w d` | `editor::GoToDefinitionSplit` |
| 编辑器：跳转到Definition Split | `ctrl-w g d` | `editor::GoToDefinitionSplit` |
| 编辑器：跳转到Definition Split | `ctrl-w ]` | `editor::GoToDefinitionSplit` |
| 编辑器：跳转到Definition Split | `ctrl-w ctrl-]` | `editor::GoToDefinitionSplit` |
| 编辑器：跳转到Type Definition Split | `ctrl-w shift-d` | `editor::GoToTypeDefinitionSplit` |
| 编辑器：跳转到Type Definition Split | `ctrl-w g shift-d` | `editor::GoToTypeDefinitionSplit` |
| 编辑器：打开Excerpts Split | `ctrl-w space` | `editor::OpenExcerptsSplit` |
| 编辑器：打开Excerpts Split | `ctrl-w g space` | `editor::OpenExcerptsSplit` |
| 窗格：执行 Alternate File | `ctrl-^` | `pane::AlternateFile` |
| Vim：执行 Repeat | `.` | `vim::Repeat` |

## `vim_mode == normal`

- 源文件：`assets/keymaps/vim.json`
- Section：`3`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Insert Before | `i` | `vim::InsertBefore` |
| Vim：执行 Insert After | `a` | `vim::InsertAfter` |
| 取消当前编辑器操作 | `ctrl-[` | `editor::Cancel` |
| 打开/关闭命令面板 | `:` | `command_palette::Toggle` |
| Vim：执行 Push Change | `c` | `vim::PushChange` |
| Vim：执行 Change To End Of Line | `shift-c` | `vim::ChangeToEndOfLine` |
| Vim：执行 Push Delete | `d` | `vim::PushDelete` |
| Vim：删除Right | `delete` | `vim::DeleteRight` |
| Vim：执行 Join Lines No Whitespace | `g shift-j` | `vim::JoinLinesNoWhitespace` |
| Vim：执行 Push Yank | `y` | `vim::PushYank` |
| Vim：执行 Yank Line | `shift-y` | `vim::YankLine` |
| Vim：删除Right | `x` | `vim::DeleteRight` |
| Vim：删除Left | `shift-x` | `vim::DeleteLeft` |
| Vim：执行 Increment | `ctrl-a` | `vim::Increment` |
| Vim：执行 Decrement | `ctrl-x` | `vim::Decrement` |
| Vim：重做 | `ctrl-r` | `vim::Redo` |
| Vim：执行 Push Indent | `>` | `vim::PushIndent` |
| Vim：执行 Push Outdent | `<` | `vim::PushOutdent` |
| Vim：执行 Push Auto Indent | `=` | `vim::PushAutoIndent` |
| Vim：执行 Push Shell Command | `!` | `vim::PushShellCommand` |
| Vim：执行 Push Lowercase | `g u` | `vim::PushLowercase` |
| Vim：执行 Push Uppercase | `g shift-u` | `vim::PushUppercase` |
| Vim：执行 Push Opposite Case | `g ~` | `vim::PushOppositeCase` |
| Vim：执行 Push Rot13 | `g ?` | `vim::PushRot13` |
| Vim：执行 Push Rewrap | `g w` | `vim::PushRewrap` |
| Vim：执行 Push Rewrap | `g q` | `vim::PushRewrap` |
| Vim：执行 Insert Before | `insert` | `vim::InsertBefore` |
| 跳转到下一个诊断 | `] d` | `editor::GoToDiagnostic` |
| 跳转到上一个诊断 | `[ d` | `editor::GoToPreviousDiagnostic` |
| 编辑器：跳转到Hunk | `] c` | `editor::GoToHunk` |
| 编辑器：跳转到Previous Hunk | `[ c` | `editor::GoToPreviousHunk` |
| Vim：执行 Push Toggle Comments | `g c` | `vim::PushToggleComments` |
| Vim：执行 Push Toggle Block Comments | `g b` | `vim::PushToggleBlockComments` |

## `VimControl && VimCount`

- 源文件：`assets/keymaps/vim.json`
- Section：`4`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Number | `0` | `vim::Number`; 参数 `[0]` |
| Vim：执行 Count Command | `:` | `vim::CountCommand` |
| Vim：跳转到Percentage | `%` | `vim::GoToPercentage` |

## `(vim_mode == insert || vim_mode == normal) && showing_signature_help && !showing_completions`

- 源文件：`assets/keymaps/vim.json`
- Section：`14`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：执行 Signature Help Previous | `ctrl-p` | `editor::SignatureHelpPrevious` |
| 编辑器：执行 Signature Help Next | `ctrl-n` | `editor::SignatureHelpNext` |

## `Editor && mode == auto_height && VimControl`

- 源文件：`assets/keymaps/vim.json`
- Section：`51`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消/屏蔽该快捷键在当前上下文中的默认行为 | `/` | `null` |
| 取消/屏蔽该快捷键在当前上下文中的默认行为 | `?` | `null` |
| 取消/屏蔽该快捷键在当前上下文中的默认行为 | `#` | `null` |
| 取消/屏蔽该快捷键在当前上下文中的默认行为 | `*` | `null` |
| 取消/屏蔽该快捷键在当前上下文中的默认行为 | `n` | `null` |
| 取消/屏蔽该快捷键在当前上下文中的默认行为 | `shift-n` | `null` |

## `GitCommit > Editor && VimControl && vim_mode == normal`

- 源文件：`assets/keymaps/vim.json`
- Section：`53`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消菜单/关闭当前弹出层 | `ctrl-c` | `menu::Cancel` |
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |

## `NotebookEditor > Editor && VimControl && vim_mode == normal`

- 源文件：`assets/keymaps/vim.json`
- Section：`59`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| notebook：执行 Notebook Move Down | `j` | `notebook::NotebookMoveDown` |
| notebook：执行 Notebook Move Up | `k` | `notebook::NotebookMoveUp` |
| notebook：执行 Enter Command Mode | `escape` | `notebook::EnterCommandMode` |

