# Vim mode：操作符、文本对象、surround 与 exchange

包含 `d/c/y/gc/ys/cs/ds/cx` 等操作符链、文本对象、语法对象、surround/change surround/delete surround 与 exchange 相关绑定。


## `vim_mode == waiting`

- 源文件：`assets/keymaps/vim.json`
- Section：`16`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Tab 跳转/补全导航 | `tab` | `vim::Tab` |
| Vim：执行 Enter | `enter` | `vim::Enter` |
| Vim：执行 Clear Operators | `ctrl-c` | `vim::ClearOperators` |
| Vim：执行 Clear Operators | `ctrl-[` | `vim::ClearOperators` |
| Vim：执行 Clear Operators | `escape` | `vim::ClearOperators` |
| Vim：执行 Push Digraph | `ctrl-k` | `vim::PushDigraph`; 参数 `[{}]` |
| Vim：执行 Push Literal | `ctrl-v` | `vim::PushLiteral`; 参数 `[{}]` |
| Vim：执行 Push Literal | `ctrl-q` | `vim::PushLiteral`; 参数 `[{}]` |

## `Editor && vim_mode == waiting && (vim_operator == ys || vim_operator == cs)`

- 源文件：`assets/keymaps/vim.json`
- Section：`17`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：切回普通模式 | `escape` | `vim::SwitchToNormalMode` |

## `vim_operator == a || vim_operator == i || vim_operator == cs || vim_operator == helix_next || vim_operator == helix_previous`

- 源文件：`assets/keymaps/vim.json`
- Section：`19`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Word | `w` | `vim::Word` |
| Vim：执行 Word | `shift-w` | `vim::Word`; 参数 `[{"ignore_punctuation":true}]` |
| Vim：执行 Tag | `t` | `vim::Tag` |
| Vim：执行 Sentence | `s` | `vim::Sentence` |
| Vim：执行 Paragraph | `p` | `vim::Paragraph` |
| Vim：执行 Quotes | `'` | `vim::Quotes` |
| Vim：执行 Back Quotes | `` ` `` | `vim::BackQuotes` |
| Vim：执行 Double Quotes | `"` | `vim::DoubleQuotes` |
| Vim：执行 Mini Quotes | `q` | `vim::MiniQuotes` |
| Vim：选择竖线包围的文本对象 | `|` | `vim::VerticalBars` |
| Vim：执行 Parentheses | `(` | `vim::Parentheses`; 参数 `[{"opening":true}]` |
| Vim：执行 Parentheses | `)` | `vim::Parentheses` |
| Vim：执行 Parentheses | `b` | `vim::Parentheses` |
| Vim：执行 Square Brackets | `[` | `vim::SquareBrackets`; 参数 `[{"opening":true}]` |
| Vim：执行 Square Brackets | `]` | `vim::SquareBrackets` |
| Vim：执行 Square Brackets | `r` | `vim::SquareBrackets` |
| Vim：执行 Curly Brackets | `{` | `vim::CurlyBrackets`; 参数 `[{"opening":true}]` |
| Vim：执行 Curly Brackets | `}` | `vim::CurlyBrackets` |
| Vim：执行 Curly Brackets | `shift-b` | `vim::CurlyBrackets` |
| Vim：执行 Angle Brackets | `<` | `vim::AngleBrackets`; 参数 `[{"opening":true}]` |
| Vim：执行 Angle Brackets | `>` | `vim::AngleBrackets` |
| Vim：执行 Argument | `a` | `vim::Argument` |
| Vim：执行 Indent Obj | `i` | `vim::IndentObj` |
| Vim：执行 Indent Obj | `shift-i` | `vim::IndentObj`; 参数 `[{"include_below":true}]` |
| Vim：执行 Method | `f` | `vim::Method` |
| Vim：执行 Class | `c` | `vim::Class` |
| Vim：执行 Entire File | `e` | `vim::EntireFile` |

## `vim_operator == helix_m`

- 源文件：`assets/keymaps/vim.json`
- Section：`20`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：跳转到匹配的括号/结构 | `m` | `vim::Matching`; 参数 `[{"match_quotes":true}]` |
| Vim：执行 Push Helix Surround Add | `s` | `vim::PushHelixSurroundAdd` |
| Vim：执行 Push Helix Surround Replace | `r` | `vim::PushHelixSurroundReplace` |
| Vim：执行 Push Helix Surround Delete | `d` | `vim::PushHelixSurroundDelete` |

## `vim_operator == helix_next`

- 源文件：`assets/keymaps/vim.json`
- Section：`21`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Next Section Start | `z` | `vim::NextSectionStart` |
| Vim：执行 Next Section End | `shift-z` | `vim::NextSectionEnd` |
| Vim：执行 Next Comment | `*` | `vim::NextComment` |
| Vim：执行 Next Comment | `/` | `vim::NextComment` |
| Vim：执行 Next Lesser Indent | `-` | `vim::NextLesserIndent` |
| Vim：执行 Next Greater Indent | `+` | `vim::NextGreaterIndent` |
| Vim：执行 Next Same Indent | `=` | `vim::NextSameIndent` |
| 窗格：执行 Activate Next Item | `b` | `pane::ActivateNextItem` |
| 窗格：执行 Activate Last Item | `shift-b` | `pane::ActivateLastItem` |
| 缩小语法节点选区 | `x` | `editor::SelectSmallerSyntaxNode` |
| 跳转到下一个诊断 | `d` | `editor::GoToDiagnostic` |
| 编辑器：跳转到Hunk | `c` | `editor::GoToHunk` |
| Vim：执行 Insert Empty Line Below | `space` | `vim::InsertEmptyLineBelow` |

## `vim_operator == helix_previous`

- 源文件：`assets/keymaps/vim.json`
- Section：`22`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Previous Section Start | `z` | `vim::PreviousSectionStart` |
| Vim：执行 Previous Section End | `shift-z` | `vim::PreviousSectionEnd` |
| Vim：执行 Previous Comment | `*` | `vim::PreviousComment` |
| Vim：执行 Previous Comment | `/` | `vim::PreviousComment` |
| Vim：执行 Previous Lesser Indent | `-` | `vim::PreviousLesserIndent` |
| Vim：执行 Previous Greater Indent | `+` | `vim::PreviousGreaterIndent` |
| Vim：执行 Previous Same Indent | `=` | `vim::PreviousSameIndent` |
| 窗格：执行 Activate Previous Item | `b` | `pane::ActivatePreviousItem` |
| 窗格：执行 Activate Item | `shift-b` | `pane::ActivateItem`; 参数 `[0]` |
| 扩大语法节点选区 | `x` | `editor::SelectLargerSyntaxNode` |
| 跳转到上一个诊断 | `d` | `editor::GoToPreviousDiagnostic` |
| 编辑器：跳转到Previous Hunk | `c` | `editor::GoToPreviousHunk` |
| Vim：执行 Insert Empty Line Above | `space` | `vim::InsertEmptyLineAbove` |

## `vim_operator == c`

- 源文件：`assets/keymaps/vim.json`
- Section：`23`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `c` | `vim::CurrentLine` |
| Vim：执行 Exchange | `x` | `vim::Exchange` |
| 重命名符号 | `d` | `editor::Rename` |
| Vim：执行 Push Change Surrounds | `s` | `vim::PushChangeSurrounds`; 参数 `[{}]` |

## `vim_operator == d`

- 源文件：`assets/keymaps/vim.json`
- Section：`24`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `d` | `vim::CurrentLine` |
| Vim：执行 Push Delete Surrounds | `s` | `vim::PushDeleteSurrounds` |
| Vim：执行 Push Forced Motion | `v` | `vim::PushForcedMotion` |
| 折叠/展开选中的 diff hunk | `o` | `editor::ToggleSelectedDiffHunks` |
| Git：切换Staged | `shift-o` | `git::ToggleStaged` |
| 还原 Git 变更 | `p` | `git::Restore` |
| 暂存当前变更并跳到下一处 | `u` | `git::StageAndNext` |
| 取消暂存当前变更并跳到下一处 | `shift-u` | `git::UnstageAndNext` |

## `vim_operator == gu`

- 源文件：`assets/keymaps/vim.json`
- Section：`25`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `g u` | `vim::CurrentLine` |
| Vim：执行 Current Line | `u` | `vim::CurrentLine` |

## `vim_operator == gU`

- 源文件：`assets/keymaps/vim.json`
- Section：`26`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `g shift-u` | `vim::CurrentLine` |
| Vim：执行 Current Line | `shift-u` | `vim::CurrentLine` |

## `vim_operator == g~`

- 源文件：`assets/keymaps/vim.json`
- Section：`27`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `g ~` | `vim::CurrentLine` |
| Vim：执行 Current Line | `~` | `vim::CurrentLine` |

## `vim_operator == g?`

- 源文件：`assets/keymaps/vim.json`
- Section：`28`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `g ?` | `vim::CurrentLine` |
| Vim：执行 Current Line | `?` | `vim::CurrentLine` |

## `vim_operator == gq`

- 源文件：`assets/keymaps/vim.json`
- Section：`29`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `g q` | `vim::CurrentLine` |
| Vim：执行 Current Line | `q` | `vim::CurrentLine` |
| Vim：执行 Current Line | `g w` | `vim::CurrentLine` |
| Vim：执行 Current Line | `w` | `vim::CurrentLine` |

## `vim_operator == y`

- 源文件：`assets/keymaps/vim.json`
- Section：`30`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `y` | `vim::CurrentLine` |
| Vim：执行 Push Forced Motion | `v` | `vim::PushForcedMotion` |
| Vim：执行 Push Add Surrounds | `s` | `vim::PushAddSurrounds`; 参数 `[{}]` |

## `vim_operator == ys`

- 源文件：`assets/keymaps/vim.json`
- Section：`31`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `s` | `vim::CurrentLine` |

## `vim_operator == >`

- 源文件：`assets/keymaps/vim.json`
- Section：`32`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `>` | `vim::CurrentLine` |

## `vim_operator == <`

- 源文件：`assets/keymaps/vim.json`
- Section：`33`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `<` | `vim::CurrentLine` |

## `vim_operator == eq`

- 源文件：`assets/keymaps/vim.json`
- Section：`34`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `=` | `vim::CurrentLine` |

## `vim_operator == sh`

- 源文件：`assets/keymaps/vim.json`
- Section：`35`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `!` | `vim::CurrentLine` |

## `vim_operator == gc`

- 源文件：`assets/keymaps/vim.json`
- Section：`36`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `c` | `vim::CurrentLine` |

## `vim_operator == gb`

- 源文件：`assets/keymaps/vim.json`
- Section：`37`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `c` | `vim::CurrentLine` |

## `vim_operator == gR`

- 源文件：`assets/keymaps/vim.json`
- Section：`38`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `r` | `vim::CurrentLine` |
| Vim：执行 Current Line | `shift-r` | `vim::CurrentLine` |

## `vim_operator == cx`

- 源文件：`assets/keymaps/vim.json`
- Section：`39`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Current Line | `x` | `vim::CurrentLine` |
| Vim：执行 Clear Exchange | `c` | `vim::ClearExchange` |

