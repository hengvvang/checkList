# Vim mode：Helix 兼容与特殊集成

包含 Zed 复用 Vim layer 的 Helix 模式绑定，以及未归入核心 Vim 模态编辑的特殊集成上下文。


## `vim_mode == helix_select`

- 源文件：`assets/keymaps/vim.json`
- Section：`6`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：退出插入/可视状态并回到普通模式 | `v` | `vim::NormalBefore` |
| Vim：执行 Helix Collapse Selection | `;` | `vim::HelixCollapseSelection` |
| Vim：执行 Change Case | `~` | `vim::ChangeCase` |
| Vim：执行 Increment | `ctrl-a` | `vim::Increment` |
| Vim：执行 Decrement | `ctrl-x` | `vim::Decrement` |
| Vim：合并行 | `shift-j` | `vim::JoinLines` |
| Vim：执行 Insert Before | `i` | `vim::InsertBefore` |
| Vim：执行 Helix Append | `a` | `vim::HelixAppend` |
| Vim：执行 Insert Line Below | `o` | `vim::InsertLineBelow` |
| Vim：执行 Insert Line Above | `shift-o` | `vim::InsertLineAbove` |
| Vim：粘贴 | `p` | `vim::Paste` |
| Vim：撤销 | `u` | `vim::Undo` |
| Vim：执行 Push Replace | `r` | `vim::PushReplace` |
| Vim：执行 Substitute | `s` | `vim::Substitute` |
| 窗格：执行 Activate Previous Item | `ctrl-pageup` | `pane::ActivatePreviousItem` |
| 窗格：执行 Activate Next Item | `ctrl-pagedown` | `pane::ActivateNextItem` |
| Vim：执行 Repeat | `.` | `vim::Repeat` |
| Vim：重复上次字符查找 | `alt-.` | `vim::RepeatFind` |

## `(vim_mode == normal || vim_mode == helix_normal) && !menu`

- 源文件：`assets/keymaps/vim.json`
- Section：`9`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消当前编辑器操作 | `escape` | `editor::Cancel` |
| Vim：删除To End Of Line | `shift-d` | `vim::DeleteToEndOfLine` |
| Vim：合并行 | `shift-j` | `vim::JoinLines` |
| Vim：执行 Yank Line | `shift-y` | `vim::YankLine` |
| Vim：执行 Insert First Non Whitespace | `shift-i` | `vim::InsertFirstNonWhitespace` |
| Vim：执行 Insert End Of Line | `shift-a` | `vim::InsertEndOfLine` |
| Vim：执行 Insert Line Below | `o` | `vim::InsertLineBelow` |
| Vim：执行 Insert Line Above | `shift-o` | `vim::InsertLineAbove` |
| Vim：执行 Change Case | `~` | `vim::ChangeCase` |
| Vim：执行 Increment | `ctrl-a` | `vim::Increment` |
| Vim：执行 Decrement | `ctrl-x` | `vim::Decrement` |
| Vim：粘贴 | `p` | `vim::Paste` |
| Vim：粘贴 | `shift-p` | `vim::Paste`; 参数 `[{"before":true}]` |
| Vim：撤销 | `u` | `vim::Undo` |
| Vim：执行 Undo Last Line | `shift-u` | `vim::UndoLastLine` |
| Vim：执行 Push Replace | `r` | `vim::PushReplace` |
| Vim：执行 Substitute | `s` | `vim::Substitute` |
| Vim：执行 Substitute Line | `shift-s` | `vim::SubstituteLine` |
| Vim：执行 Push Register | `"` | `vim::PushRegister` |
| 窗格：执行 Activate Next Item | `ctrl-pagedown` | `pane::ActivateNextItem` |
| 窗格：执行 Activate Previous Item | `ctrl-pageup` | `pane::ActivatePreviousItem` |

## `VimControl && vim_mode == helix_normal && !menu && !BufferSearchBar`

- 源文件：`assets/keymaps/vim.json`
- Section：`10`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：向下移动 | `j` | `vim::Down`; 参数 `[{"display_lines":true}]` |
| Vim：向下移动 | `down` | `vim::Down`; 参数 `[{"display_lines":true}]` |
| Vim：向上移动 | `k` | `vim::Up`; 参数 `[{"display_lines":true}]` |
| Vim：向上移动 | `up` | `vim::Up`; 参数 `[{"display_lines":true}]` |
| Vim：向下移动 | `g j` | `vim::Down` |
| Vim：向下移动 | `g down` | `vim::Down` |
| Vim：向上移动 | `g k` | `vim::Up` |
| Vim：向上移动 | `g up` | `vim::Up` |
| Vim：执行 Switch To Helix Normal Mode | `escape` | `vim::SwitchToHelixNormalMode` |
| Vim：执行 Helix Insert | `i` | `vim::HelixInsert` |
| Vim：执行 Helix Append | `a` | `vim::HelixAppend` |
| Vim：执行 Helix Insert End Of Line | `shift-a` | `vim::HelixInsertEndOfLine` |
| 取消当前编辑器操作 | `ctrl-[` | `editor::Cancel` |

## `vim_mode == helix_select && !menu && !BufferSearchBar`

- 源文件：`assets/keymaps/vim.json`
- Section：`11`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Switch To Helix Normal Mode | `escape` | `vim::SwitchToHelixNormalMode` |

