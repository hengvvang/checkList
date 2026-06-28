# Vim mode：Insert、Visual、Replace、Literal 与输入相关模式

包含插入模式、可视模式、替换模式、literal 输入、find/mark 等临时输入状态。


## `vim_mode == normal || vim_mode == visual || vim_mode == operator`

- 源文件：`assets/keymaps/vim.json`
- Section：`2`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Next Section Start | `] ]` | `vim::NextSectionStart` |
| Vim：执行 Next Section End | `] [` | `vim::NextSectionEnd` |
| Vim：执行 Previous Section Start | `[ [` | `vim::PreviousSectionStart` |
| Vim：执行 Previous Section End | `[ ]` | `vim::PreviousSectionEnd` |
| Vim：执行 Next Method Start | `] m` | `vim::NextMethodStart` |
| Vim：执行 Next Method End | `] shift-m` | `vim::NextMethodEnd` |
| Vim：执行 Previous Method Start | `[ m` | `vim::PreviousMethodStart` |
| Vim：执行 Previous Method End | `[ shift-m` | `vim::PreviousMethodEnd` |
| Vim：执行 Previous Comment | `[ *` | `vim::PreviousComment` |
| Vim：执行 Previous Comment | `[ /` | `vim::PreviousComment` |
| Vim：执行 Next Comment | `] *` | `vim::NextComment` |
| Vim：执行 Next Comment | `] /` | `vim::NextComment` |
| Vim：执行 Previous Lesser Indent | `[ -` | `vim::PreviousLesserIndent` |
| Vim：执行 Previous Greater Indent | `[ +` | `vim::PreviousGreaterIndent` |
| Vim：执行 Previous Same Indent | `[ =` | `vim::PreviousSameIndent` |
| Vim：执行 Next Lesser Indent | `] -` | `vim::NextLesserIndent` |
| Vim：执行 Next Greater Indent | `] +` | `vim::NextGreaterIndent` |
| Vim：执行 Next Same Indent | `] =` | `vim::NextSameIndent` |
| 窗格：执行 Activate Next Item | `] b` | `pane::ActivateNextItem` |
| 窗格：执行 Activate Previous Item | `[ b` | `pane::ActivatePreviousItem` |
| 窗格：执行 Activate Last Item | `] shift-b` | `pane::ActivateLastItem` |
| 窗格：执行 Activate Item | `[ shift-b` | `pane::ActivateItem`; 参数 `[0]` |
| Vim：执行 Insert Empty Line Below | `] space` | `vim::InsertEmptyLineBelow` |
| Vim：执行 Insert Empty Line Above | `[ space` | `vim::InsertEmptyLineAbove` |
| 编辑器：移动Line Up | `[ e` | `editor::MoveLineUp` |
| 编辑器：移动Line Down | `] e` | `editor::MoveLineDown` |
| 工作区：执行 Follow Next Collaborator | `[ f` | `workspace::FollowNextCollaborator` |
| 工作区：执行 Follow Next Collaborator | `] f` | `workspace::FollowNextCollaborator` |
| Vim：执行 Unmatched Forward | `] }` | `vim::UnmatchedForward`; 参数 `[{"char":"}"}]` |
| Vim：执行 Unmatched Backward | `[ {` | `vim::UnmatchedBackward`; 参数 `[{"char":"{"}]` |
| Vim：执行 Unmatched Forward | `] )` | `vim::UnmatchedForward`; 参数 `[{"char":")"}]` |
| Vim：执行 Unmatched Backward | `[ (` | `vim::UnmatchedBackward`; 参数 `[{"char":"("}]` |
| Vim：跳转到Previous Reference | `[ r` | `vim::GoToPreviousReference` |
| Vim：跳转到Next Reference | `] r` | `vim::GoToNextReference` |
| Vim：选择Larger Syntax Node | `[ x` | `vim::SelectLargerSyntaxNode` |
| Vim：选择Smaller Syntax Node | `] x` | `vim::SelectSmallerSyntaxNode` |

## `vim_mode == visual`

- 源文件：`assets/keymaps/vim.json`
- Section：`5`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Visual Command | `:` | `vim::VisualCommand` |
| Vim：执行 Convert To Lower Case | `u` | `vim::ConvertToLowerCase` |
| Vim：执行 Convert To Upper Case | `shift-u` | `vim::ConvertToUpperCase` |
| Vim：执行 Other End | `shift-o` | `vim::OtherEnd` |
| Vim：执行 Other End Row Aware | `o` | `vim::OtherEndRowAware` |
| Vim：执行 Visual Delete | `d` | `vim::VisualDelete` |
| Vim：执行 Visual Delete | `x` | `vim::VisualDelete` |
| Vim：执行 Visual Delete | `delete` | `vim::VisualDelete` |
| Vim：执行 Visual Delete Line | `shift-d` | `vim::VisualDeleteLine` |
| Vim：执行 Visual Delete Line | `shift-x` | `vim::VisualDeleteLine` |
| Vim：执行 Visual Yank | `y` | `vim::VisualYank` |
| Vim：执行 Visual Yank Line | `shift-y` | `vim::VisualYankLine` |
| Vim：粘贴 | `p` | `vim::Paste` |
| Vim：粘贴 | `shift-p` | `vim::Paste`; 参数 `[{"preserve_clipboard":true}]` |
| Vim：执行 Substitute | `c` | `vim::Substitute` |
| Vim：执行 Substitute | `s` | `vim::Substitute` |
| Vim：执行 Substitute Line | `shift-r` | `vim::SubstituteLine` |
| Vim：执行 Substitute Line | `shift-s` | `vim::SubstituteLine` |
| Vim：执行 Change Case | `~` | `vim::ChangeCase` |
| Vim：跳到下一个匹配/目标 | `*` | `vim::MoveToNext`; 参数 `[{"partial_word":true}]` |
| Vim：跳到上一个匹配/目标 | `#` | `vim::MoveToPrevious`; 参数 `[{"partial_word":true}]` |
| Vim：执行 Increment | `ctrl-a` | `vim::Increment` |
| Vim：执行 Decrement | `ctrl-x` | `vim::Decrement` |
| Vim：执行 Increment | `g ctrl-a` | `vim::Increment`; 参数 `[{"step":true}]` |
| Vim：执行 Decrement | `g ctrl-x` | `vim::Decrement`; 参数 `[{"step":true}]` |
| Vim：执行 Insert Before | `shift-i` | `vim::InsertBefore` |
| Vim：执行 Insert After | `shift-a` | `vim::InsertAfter` |
| Vim：执行 Visual Insert First Non White Space | `g shift-i` | `vim::VisualInsertFirstNonWhiteSpace` |
| Vim：执行 Visual Insert End Of Line | `g shift-a` | `vim::VisualInsertEndOfLine` |
| Vim：合并行 | `shift-j` | `vim::JoinLines` |
| Vim：执行 Join Lines No Whitespace | `g shift-j` | `vim::JoinLinesNoWhitespace` |
| Vim：执行 Push Replace | `r` | `vim::PushReplace` |
| Vim：切回普通模式 | `ctrl-c` | `vim::SwitchToNormalMode` |
| Vim：切回普通模式 | `ctrl-[` | `vim::SwitchToNormalMode` |
| Vim：切回普通模式 | `escape` | `vim::SwitchToNormalMode` |
| Vim：增加缩进 | `>` | `vim::Indent` |
| Vim：减少缩进 | `<` | `vim::Outdent` |
| Vim：执行 Auto Indent | `=` | `vim::AutoIndent` |
| Vim：执行 Shell Command | `!` | `vim::ShellCommand` |
| Vim：选择/指定文本对象 | `i` | `vim::PushObject`; 参数 `[{"around":false}]` |
| Vim：选择/指定文本对象 | `a` | `vim::PushObject`; 参数 `[{"around":true}]` |
| Vim：粘贴 | `g shift-r` | `vim::Paste`; 参数 `[{"preserve_clipboard":true}]` |
| Vim：切换Comments | `g c` | `vim::ToggleComments` |
| Vim：切换Block Comments | `g b` | `vim::ToggleBlockComments` |
| Vim：执行 Rewrap | `g q` | `vim::Rewrap` |
| Vim：执行 Rewrap | `g w` | `vim::Rewrap` |
| Vim：执行 Convert To Rot13 | `g ?` | `vim::ConvertToRot13` |
| Vim：执行 Push Register | `"` | `vim::PushRegister` |

## `vim_mode == insert`

- 源文件：`assets/keymaps/vim.json`
- Section：`7`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：退出插入/可视状态并回到普通模式 | `ctrl-c` | `vim::NormalBefore` |
| Vim：退出插入/可视状态并回到普通模式 | `ctrl-[` | `vim::NormalBefore` |
| Vim：退出插入/可视状态并回到普通模式 | `escape` | `vim::NormalBefore` |
| 取消/屏蔽该快捷键在当前上下文中的默认行为 | `ctrl-x` | `null` |
| 显示代码补全 | `ctrl-x ctrl-o` | `editor::ShowCompletions` |
| 打开行内 AI 助手 | `ctrl-x ctrl-a` | `assistant::InlineAssist` |
| 编辑器：显示Edit Prediction | `ctrl-x ctrl-c` | `editor::ShowEditPrediction` |
| 打开代码操作/快速修复菜单 | `ctrl-x ctrl-l` | `editor::ToggleCodeActions` |
| 取消当前编辑器操作 | `ctrl-x ctrl-z` | `editor::Cancel` |
| Vim：屏幕向下滚动一行 | `ctrl-x ctrl-e` | `vim::LineDown` |
| Vim：屏幕向上滚动一行 | `ctrl-x ctrl-y` | `vim::LineUp` |
| 删除到上一个单词开头 | `ctrl-w` | `editor::DeleteToPreviousWordStart`; 参数 `[{"ignore_newlines":false,"ignore_brackets":false}]` |
| 编辑器：删除To Beginning Of Line | `ctrl-u` | `editor::DeleteToBeginningOfLine` |
| Vim：增加缩进 | `ctrl-t` | `vim::Indent` |
| Vim：减少缩进 | `ctrl-d` | `vim::Outdent` |
| Vim：执行 Insert From Above | `ctrl-y` | `vim::InsertFromAbove` |
| Vim：执行 Insert From Below | `ctrl-e` | `vim::InsertFromBelow` |
| Vim：执行 Push Digraph | `ctrl-k` | `vim::PushDigraph`; 参数 `[{}]` |
| Vim：执行 Push Literal | `ctrl-v` | `vim::PushLiteral`; 参数 `[{}]` |
| 粘贴剪贴板内容 | `ctrl-shift-v` | `editor::Paste` |
| Vim：执行 Push Literal | `ctrl-q` | `vim::PushLiteral`; 参数 `[{}]` |
| Vim：执行 Push Literal | `ctrl-shift-q` | `vim::PushLiteral`; 参数 `[{}]` |
| Vim：执行 Push Register | `ctrl-r` | `vim::PushRegister` |
| Vim：切换替换模式 | `insert` | `vim::ToggleReplace` |
| Vim：执行 Temporary Normal | `ctrl-o` | `vim::TemporaryNormal` |
| 显示函数签名帮助 | `ctrl-s` | `editor::ShowSignatureHelp` |

## `vim_mode == insert && !(showing_code_actions || showing_completions)`

- 源文件：`assets/keymaps/vim.json`
- Section：`13`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：显示Word Completions | `ctrl-p` | `editor::ShowWordCompletions` |
| 编辑器：显示Word Completions | `ctrl-n` | `editor::ShowWordCompletions` |

## `vim_mode == replace`

- 源文件：`assets/keymaps/vim.json`
- Section：`15`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：退出插入/可视状态并回到普通模式 | `ctrl-c` | `vim::NormalBefore` |
| Vim：退出插入/可视状态并回到普通模式 | `ctrl-[` | `vim::NormalBefore` |
| Vim：退出插入/可视状态并回到普通模式 | `escape` | `vim::NormalBefore` |
| Vim：执行 Push Digraph | `ctrl-k` | `vim::PushDigraph`; 参数 `[{}]` |
| Vim：执行 Push Literal | `ctrl-v` | `vim::PushLiteral`; 参数 `[{}]` |
| 粘贴剪贴板内容 | `ctrl-shift-v` | `editor::Paste` |
| Vim：执行 Push Literal | `ctrl-q` | `vim::PushLiteral`; 参数 `[{}]` |
| Vim：执行 Push Literal | `ctrl-shift-q` | `vim::PushLiteral`; 参数 `[{}]` |
| Vim：执行 Undo Replace | `backspace` | `vim::UndoReplace` |
| Vim：执行 Tab 跳转/补全导航 | `tab` | `vim::Tab` |
| Vim：执行 Enter | `enter` | `vim::Enter` |
| Vim：执行 Insert Before | `insert` | `vim::InsertBefore` |

## `vim_mode == literal`

- 源文件：`assets/keymaps/vim.json`
- Section：`40`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：插入 literal 控制字符 | `ctrl-@` | `vim::Literal`; 参数 `[["ctrl-@","\u0000"]]` |
| Vim：插入 literal 控制字符 | `ctrl-a` | `vim::Literal`; 参数 `[["ctrl-a","\u0001"]]` |
| Vim：插入 literal 控制字符 | `ctrl-b` | `vim::Literal`; 参数 `[["ctrl-b","\u0002"]]` |
| Vim：插入 literal 控制字符 | `ctrl-c` | `vim::Literal`; 参数 `[["ctrl-c","\u0003"]]` |
| Vim：插入 literal 控制字符 | `ctrl-d` | `vim::Literal`; 参数 `[["ctrl-d","\u0004"]]` |
| Vim：插入 literal 控制字符 | `ctrl-e` | `vim::Literal`; 参数 `[["ctrl-e","\u0005"]]` |
| Vim：插入 literal 控制字符 | `ctrl-f` | `vim::Literal`; 参数 `[["ctrl-f","\u0006"]]` |
| Vim：插入 literal 控制字符 | `ctrl-g` | `vim::Literal`; 参数 `[["ctrl-g","\u0007"]]` |
| Vim：插入 literal 控制字符 | `ctrl-h` | `vim::Literal`; 参数 `[["ctrl-h","\b"]]` |
| Vim：插入 literal 控制字符 | `ctrl-i` | `vim::Literal`; 参数 `[["ctrl-i","\t"]]` |
| Vim：插入 literal 控制字符 | `ctrl-j` | `vim::Literal`; 参数 `[["ctrl-j","\n"]]` |
| Vim：插入 literal 控制字符 | `ctrl-k` | `vim::Literal`; 参数 `[["ctrl-k","\u000b"]]` |
| Vim：插入 literal 控制字符 | `ctrl-l` | `vim::Literal`; 参数 `[["ctrl-l","\f"]]` |
| Vim：插入 literal 控制字符 | `ctrl-m` | `vim::Literal`; 参数 `[["ctrl-m","\r"]]` |
| Vim：插入 literal 控制字符 | `ctrl-n` | `vim::Literal`; 参数 `[["ctrl-n","\u000e"]]` |
| Vim：插入 literal 控制字符 | `ctrl-o` | `vim::Literal`; 参数 `[["ctrl-o","\u000f"]]` |
| Vim：插入 literal 控制字符 | `ctrl-p` | `vim::Literal`; 参数 `[["ctrl-p","\u0010"]]` |
| Vim：插入 literal 控制字符 | `ctrl-q` | `vim::Literal`; 参数 `[["ctrl-q","\u0011"]]` |
| Vim：插入 literal 控制字符 | `ctrl-r` | `vim::Literal`; 参数 `[["ctrl-r","\u0012"]]` |
| Vim：插入 literal 控制字符 | `ctrl-s` | `vim::Literal`; 参数 `[["ctrl-s","\u0013"]]` |
| Vim：插入 literal 控制字符 | `ctrl-t` | `vim::Literal`; 参数 `[["ctrl-t","\u0014"]]` |
| Vim：插入 literal 控制字符 | `ctrl-u` | `vim::Literal`; 参数 `[["ctrl-u","\u0015"]]` |
| Vim：插入 literal 控制字符 | `ctrl-v` | `vim::Literal`; 参数 `[["ctrl-v","\u0016"]]` |
| Vim：插入 literal 控制字符 | `ctrl-w` | `vim::Literal`; 参数 `[["ctrl-w","\u0017"]]` |
| Vim：插入 literal 控制字符 | `ctrl-x` | `vim::Literal`; 参数 `[["ctrl-x","\u0018"]]` |
| Vim：插入 literal 控制字符 | `ctrl-y` | `vim::Literal`; 参数 `[["ctrl-y","\u0019"]]` |
| Vim：插入 literal 控制字符 | `ctrl-z` | `vim::Literal`; 参数 `[["ctrl-z","\u001a"]]` |
| Vim：插入 literal 控制字符 | `ctrl-[` | `vim::Literal`; 参数 `[["ctrl-[","\u001b"]]` |
| Vim：插入 literal 控制字符 | `ctrl-\` | `vim::Literal`; 参数 `[["ctrl-\\","\u001c"]]` |
| Vim：插入 literal 控制字符 | `ctrl-]` | `vim::Literal`; 参数 `[["ctrl-]","\u001d"]]` |
| Vim：插入 literal 控制字符 | `ctrl-^` | `vim::Literal`; 参数 `[["ctrl-^","\u001e"]]` |
| Vim：插入 literal 控制字符 | `ctrl-_` | `vim::Literal`; 参数 `[["ctrl-_","\u001f"]]` |
| Vim：插入 literal 控制字符 | `escape` | `vim::Literal`; 参数 `[["escape","\u001b"]]` |
| Vim：插入 literal 控制字符 | `enter` | `vim::Literal`; 参数 `[["enter","\r"]]` |
| Vim：插入 literal 控制字符 | `tab` | `vim::Literal`; 参数 `[["tab","\t"]]` |
| Vim：插入 literal 控制字符 | `backspace` | `vim::Literal`; 参数 `[["backspace","\b"]]` |
| Vim：插入 literal 控制字符 | `delete` | `vim::Literal`; 参数 `[["delete",""]]` |

