# Vim mode：其它上下文

包含未归入前面 Vim 模块的剩余上下文，仍然全部来自 `assets/keymaps/vim.json`。


## `showing_completions`

- 源文件：`assets/keymaps/vim.json`
- Section：`8`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：向下滚动半屏 | `ctrl-d` | `vim::ScrollDown` |
| Vim：向上滚动半屏 | `ctrl-u` | `vim::ScrollUp` |
| Vim：屏幕向下滚动一行 | `ctrl-e` | `vim::LineDown` |
| Vim：屏幕向上滚动一行 | `ctrl-y` | `vim::LineUp` |

## `vim_mode == operator`

- 源文件：`assets/keymaps/vim.json`
- Section：`18`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Clear Operators | `ctrl-c` | `vim::ClearOperators` |
| Vim：执行 Clear Operators | `ctrl-[` | `vim::ClearOperators` |
| Vim：执行 Clear Operators | `escape` | `vim::ClearOperators` |
| Vim：执行 Comment | `g c` | `vim::Comment` |

## `BufferSearchBar && !in_replace`

- 源文件：`assets/keymaps/vim.json`
- Section：`41`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Search Submit | `enter` | `vim::SearchSubmit` |
| 关闭当前文件搜索 | `escape` | `buffer_search::Dismiss` |

## `OutlinePanel && not_editing`

- 源文件：`assets/keymaps/vim.json`
- Section：`45`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| outline panel：折叠Selected Entry | `h` | `outline_panel::CollapseSelectedEntry` |
| Vim：执行 Menu Select Next | `j` | `vim::MenuSelectNext` |
| Vim：执行 Menu Select Previous | `k` | `vim::MenuSelectPrevious` |
| Vim：执行 Menu Select Next | `down` | `vim::MenuSelectNext` |
| Vim：执行 Menu Select Previous | `up` | `vim::MenuSelectPrevious` |
| outline panel：展开Selected Entry | `l` | `outline_panel::ExpandSelectedEntry` |
| 选择菜单/列表中的最后一项 | `shift-g` | `menu::SelectLast` |
| 选择菜单/列表中的第一项 | `g g` | `menu::SelectFirst` |
| outline panel：选择Parent | `-` | `outline_panel::SelectParent` |
| 编辑器：切换Focus | `enter` | `editor::ToggleFocus` |
| 取消菜单/关闭当前弹出层 | `/` | `menu::Cancel` |
| outline panel：执行 Scroll Up | `ctrl-u` | `outline_panel::ScrollUp` |
| outline panel：执行 Scroll Down | `ctrl-d` | `outline_panel::ScrollDown` |
| outline panel：执行 Scroll Cursor Top | `z t` | `outline_panel::ScrollCursorTop` |
| outline panel：执行 Scroll Cursor Center | `z z` | `outline_panel::ScrollCursorCenter` |
| outline panel：执行 Scroll Cursor Bottom | `z b` | `outline_panel::ScrollCursorBottom` |
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

## `OutlinePanel && editing`

- 源文件：`assets/keymaps/vim.json`
- Section：`46`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消菜单/关闭当前弹出层 | `enter` | `menu::Cancel` |

## `GitGraph`

- 源文件：`assets/keymaps/vim.json`
- Section：`47`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| git graph：聚焦Next Tab Stop | `tab` | `git_graph::FocusNextTabStop` |
| git graph：聚焦Previous Tab Stop | `shift-tab` | `git_graph::FocusPreviousTabStop` |

## `GitGraphSearchBar > Editor`

- 源文件：`assets/keymaps/vim.json`
- Section：`48`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| git graph：聚焦Next Tab Stop | `tab` | `git_graph::FocusNextTabStop` |
| git graph：聚焦Previous Tab Stop | `shift-tab` | `git_graph::FocusPreviousTabStop` |

## `GitGraph && !GitGraphSearchBar`

- 源文件：`assets/keymaps/vim.json`
- Section：`49`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Vim：执行 Menu Select Next | `j` | `vim::MenuSelectNext` |
| Vim：执行 Menu Select Previous | `k` | `vim::MenuSelectPrevious` |
| git graph：执行 Scroll Down | `ctrl-d` | `git_graph::ScrollDown` |
| git graph：执行 Scroll Up | `ctrl-u` | `git_graph::ScrollUp` |
| 选择菜单/列表中的最后一项 | `shift-g` | `menu::SelectLast` |
| 选择菜单/列表中的第一项 | `g g` | `menu::SelectFirst` |

## `GitPanel && ChangesList && !GitBranchSelector`

- 源文件：`assets/keymaps/vim.json`
- Section：`50`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 选择菜单/列表中的上一项 | `k` | `menu::SelectPrevious` |
| 选择菜单/列表中的下一项 | `j` | `menu::SelectNext` |
| 选择菜单/列表中的第一项 | `g g` | `menu::SelectFirst` |
| 选择菜单/列表中的最后一项 | `shift-g` | `menu::SelectLast` |
| 确认当前菜单/列表选择 | `g f` | `menu::Confirm` |
| Git 面板：聚焦Editor | `i` | `git_panel::FocusEditor` |
| Git：切换Staged | `x` | `git::ToggleStaged` |
| Git：暂存All | `shift-x` | `git::StageAll` |
| Git：暂存Range | `g x` | `git::StageRange` |
| Git：取消暂存All | `shift-u` | `git::UnstageAll` |

## `Picker > Editor`

- 源文件：`assets/keymaps/vim.json`
- Section：`52`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 向前删除字符 | `ctrl-h` | `editor::Backspace` |
| 编辑器：删除To Beginning Of Line | `ctrl-u` | `editor::DeleteToBeginningOfLine` |
| 删除到上一个单词开头 | `ctrl-w` | `editor::DeleteToPreviousWordStart` |
| 选择菜单/列表中的上一项 | `ctrl-p` | `menu::SelectPrevious` |
| 选择菜单/列表中的下一项 | `ctrl-n` | `menu::SelectNext` |

## `Editor && edit_prediction && edit_prediction_mode == eager && !showing_completions`

- 源文件：`assets/keymaps/vim.json`
- Section：`54`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：接受Edit Prediction | `tab` | `editor::AcceptEditPrediction` |

## `MessageEditor > Editor && VimControl`

- 源文件：`assets/keymaps/vim.json`
- Section：`55`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Agent/AI：执行 Chat | `enter` | `agent::Chat` |

## `SettingsWindow > NavigationMenu && !search`

- 源文件：`assets/keymaps/vim.json`
- Section：`56`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| settings editor：展开Nav Entry | `l` | `settings_editor::ExpandNavEntry` |
| settings editor：折叠Nav Entry | `h` | `settings_editor::CollapseNavEntry` |
| settings editor：聚焦Previous Nav Entry | `k` | `settings_editor::FocusPreviousNavEntry` |
| settings editor：聚焦Next Nav Entry | `j` | `settings_editor::FocusNextNavEntry` |
| settings editor：聚焦First Nav Entry | `g g` | `settings_editor::FocusFirstNavEntry` |
| settings editor：聚焦Last Nav Entry | `shift-g` | `settings_editor::FocusLastNavEntry` |

## `MarkdownPreview`

- 源文件：`assets/keymaps/vim.json`
- Section：`57`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Markdown：执行 Scroll Page Up | `ctrl-u` | `markdown::ScrollPageUp` |
| Markdown：执行 Scroll Page Down | `ctrl-d` | `markdown::ScrollPageDown` |
| Markdown：执行 Scroll Up | `ctrl-y` | `markdown::ScrollUp` |
| Markdown：执行 Scroll Down | `ctrl-e` | `markdown::ScrollDown` |
| Markdown：执行 Scroll To Top | `g g` | `markdown::ScrollToTop` |
| Markdown：执行 Scroll To Bottom | `shift-g` | `markdown::ScrollToBottom` |
| 打开当前文件搜索 | `/` | `buffer_search::Deploy` |

## `FileHistoryView`

- 源文件：`assets/keymaps/vim.json`
- Section：`58`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 选择菜单/列表中的下一项 | `j` | `menu::SelectNext` |
| 选择菜单/列表中的上一项 | `k` | `menu::SelectPrevious` |
| 选择菜单/列表中的第一项 | `g g` | `menu::SelectFirst` |
| 选择菜单/列表中的最后一项 | `shift-g` | `menu::SelectLast` |

## `NotebookEditor && notebook_mode == command`

- 源文件：`assets/keymaps/vim.json`
- Section：`60`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 选择菜单/列表中的下一项 | `j` | `menu::SelectNext` |
| 选择菜单/列表中的上一项 | `k` | `menu::SelectPrevious` |
| 选择菜单/列表中的第一项 | `g g` | `menu::SelectFirst` |
| 选择菜单/列表中的最后一项 | `shift-g` | `menu::SelectLast` |
| notebook：执行 Enter Edit Mode | `i` | `notebook::EnterEditMode` |
| notebook：执行 Enter Edit Mode | `a` | `notebook::EnterEditMode` |
| notebook：执行 Enter Edit Mode | `enter` | `notebook::EnterEditMode` |
| notebook：运行And Advance | `shift-enter` | `notebook::RunAndAdvance` |
| notebook：运行操作 | `ctrl-enter` | `notebook::Run` |

