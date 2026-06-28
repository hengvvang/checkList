# VS Code 默认布局：工作区、窗格、标签与窗口

包含 Workspace/Pane/Tab/Item 相关快捷键，例如分屏、切换窗格、标签页、窗口级命令等。


## `Pane`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`38`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 窗格：执行 Activate Item | `alt-1` | `pane::ActivateItem`; 参数 `[0]` |
| 窗格：执行 Activate Item | `alt-2` | `pane::ActivateItem`; 参数 `[1]` |
| 窗格：执行 Activate Item | `alt-3` | `pane::ActivateItem`; 参数 `[2]` |
| 窗格：执行 Activate Item | `alt-4` | `pane::ActivateItem`; 参数 `[3]` |
| 窗格：执行 Activate Item | `alt-5` | `pane::ActivateItem`; 参数 `[4]` |
| 窗格：执行 Activate Item | `alt-6` | `pane::ActivateItem`; 参数 `[5]` |
| 窗格：执行 Activate Item | `alt-7` | `pane::ActivateItem`; 参数 `[6]` |
| 窗格：执行 Activate Item | `alt-8` | `pane::ActivateItem`; 参数 `[7]` |
| 窗格：执行 Activate Item | `alt-9` | `pane::ActivateItem`; 参数 `[8]` |
| 窗格：执行 Activate Last Item | `alt-0` | `pane::ActivateLastItem` |
| 窗格：执行 Activate Previous Item | `ctrl-pageup` | `pane::ActivatePreviousItem` |
| 窗格：执行 Activate Next Item | `ctrl-pagedown` | `pane::ActivateNextItem` |
| 窗格：执行 Swap Item Left | `ctrl-shift-pageup` | `pane::SwapItemLeft` |
| 窗格：执行 Swap Item Right | `ctrl-shift-pagedown` | `pane::SwapItemRight` |
| 窗格：关闭Active Item | `ctrl-f4` | `pane::CloseActiveItem`; 参数 `[{"close_pinned":false}]` |
| 窗格：关闭Active Item | `ctrl-w` | `pane::CloseActiveItem`; 参数 `[{"close_pinned":false}]` |
| 窗格：关闭Other Items | `ctrl-shift-alt-t` | `pane::CloseOtherItems`; 参数 `[{"close_pinned":false}]` |
| 工作区：关闭Inactive Tabs And Panes | `ctrl-shift-alt-w` | `workspace::CloseInactiveTabsAndPanes` |
| 窗格：关闭Items To The Left | `ctrl-k e` | `pane::CloseItemsToTheLeft`; 参数 `[{"close_pinned":false}]` |
| 窗格：关闭Items To The Right | `ctrl-k t` | `pane::CloseItemsToTheRight`; 参数 `[{"close_pinned":false}]` |
| 窗格：关闭Clean Items | `ctrl-k u` | `pane::CloseCleanItems`; 参数 `[{"close_pinned":false}]` |
| 窗格：关闭All Items | `ctrl-k w` | `pane::CloseAllItems`; 参数 `[{"close_pinned":false}]` |
| 工作区：关闭All Items And Panes | `ctrl-k ctrl-w` | `workspace::CloseAllItemsAndPanes` |
| 导航后退 | `back` | `pane::GoBack` |
| 导航后退 | `alt--` | `pane::GoBack` |
| 导航后退 | `alt-left` | `pane::GoBack` |
| 导航前进 | `forward` | `pane::GoForward` |
| 导航前进 | `alt-=` | `pane::GoForward` |
| 导航前进 | `alt-right` | `pane::GoForward` |
| 跳到下一个搜索结果 | `f3` | `search::SelectNextMatch` |
| 跳到上一个搜索结果 | `shift-f3` | `search::SelectPreviousMatch` |
| 项目搜索：切换Focus | `ctrl-shift-f` | `project_search::ToggleFocus` |
| 显示/隐藏替换输入框 | `shift-alt-h` | `search::ToggleReplace` |
| 切换搜索选区范围 | `alt-l` | `search::ToggleSelection` |
| 选中所有搜索结果 | `alt-enter` | `search::SelectAllMatches` |
| 搜索：切换Case Sensitive | `alt-c` | `search::ToggleCaseSensitive` |
| 搜索：切换Whole Word | `alt-w` | `search::ToggleWholeWord` |
| 项目搜索：切换Filters | `alt-f` | `project_search::ToggleFilters` |
| 项目搜索：切换All Search Results | `ctrl-shift-enter` | `project_search::ToggleAllSearchResults` |
| 搜索：切换Regex | `alt-r` | `search::ToggleRegex` |
| 窗格：切换Pin Tab | `ctrl-k shift-enter` | `pane::TogglePinTab` |

## `ApplicationMenu`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`49`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消菜单/关闭当前弹出层 | `f10` | `menu::Cancel` |
| app menu：执行 Activate Menu Left | `left` | `app_menu::ActivateMenuLeft` |
| app menu：执行 Activate Menu Right | `right` | `app_menu::ActivateMenuRight` |

## `Pane`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`51`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 向上拆分窗格 | `ctrl-k up` | `pane::SplitUp` |
| 向下拆分窗格 | `ctrl-k down` | `pane::SplitDown` |
| 向左拆分窗格 | `ctrl-k left` | `pane::SplitLeft` |
| 向右拆分窗格 | `ctrl-k right` | `pane::SplitRight` |

## `!AcpThread > Editor && mode == full`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`63`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 打开当前搜索摘录/引用摘录 | `alt-enter` | `editor::OpenExcerpts` |
| 编辑器：展开Excerpts | `shift-enter` | `editor::ExpandExcerpts` |
| 编辑器：打开Excerpts Split | `ctrl-alt-enter` | `editor::OpenExcerptsSplit` |
| 窗格：执行 Reveal In Project Panel | `ctrl-shift-e` | `pane::RevealInProjectPanel` |
| 编辑器：跳转到Hunk | `ctrl-f8` | `editor::GoToHunk` |
| 编辑器：跳转到Previous Hunk | `ctrl-shift-f8` | `editor::GoToPreviousHunk` |
| 打开行内 AI 助手 | `ctrl-enter` | `assistant::InlineAssist` |
| 编辑器：切换Inlay Hints | `ctrl-shift-;` | `editor::ToggleInlayHints` |

## `OutlinePanel && not_editing`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`67`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| outline panel：折叠Selected Entry | `left` | `outline_panel::CollapseSelectedEntry` |
| outline panel：展开Selected Entry | `right` | `outline_panel::ExpandSelectedEntry` |
| outline panel：复制Path | `shift-alt-c` | `outline_panel::CopyPath` |
| 工作区：复制Relative Path | `ctrl-shift-alt-c` | `workspace::CopyRelativePath` |
| outline panel：执行 Reveal In File Manager | `ctrl-alt-r` | `outline_panel::RevealInFileManager` |
| outline panel：打开Selected Entry | `space` | `outline_panel::OpenSelectedEntry` |
| 选择菜单/列表中的下一项 | `shift-down` | `menu::SelectNext` |
| 选择菜单/列表中的上一项 | `shift-up` | `menu::SelectPrevious` |
| 打开当前搜索摘录/引用摘录 | `alt-enter` | `editor::OpenExcerpts` |
| 编辑器：打开Excerpts Split | `ctrl-alt-enter` | `editor::OpenExcerptsSplit` |

## `GitPanel && CommitEditor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`72`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Git：执行 Cancel | `escape` | `git::Cancel` |

## `GitPanel`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`74`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Git：执行 Fetch | `ctrl-g ctrl-g` | `git::Fetch` |
| Git：执行 Push | `ctrl-g up` | `git::Push` |
| Git：执行 Pull | `ctrl-g down` | `git::Pull` |
| Git：执行 Pull Rebase | `ctrl-g shift-down` | `git::PullRebase` |
| Git：执行 Force Push | `ctrl-g shift-up` | `git::ForcePush` |
| Git：执行 Diff | `ctrl-g d` | `git::Diff` |
| Git：执行 Restore Tracked Files | `ctrl-g backspace` | `git::RestoreTrackedFiles` |
| Git：执行 Trash Untracked Files | `ctrl-g shift-backspace` | `git::TrashUntrackedFiles` |
| Git：暂存All | `ctrl-space` | `git::StageAll` |
| Git：取消暂存All | `ctrl-shift-space` | `git::UnstageAll` |
| Git：执行 Commit | `ctrl-enter` | `git::Commit` |
| Git：执行 Amend | `ctrl-shift-enter` | `git::Amend` |

## `CollabPanel && not_editing`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`81`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| collab panel：移除操作 | `ctrl-backspace` | `collab_panel::Remove` |
| 确认当前菜单/列表选择 | `space` | `menu::Confirm` |

## `CollabPanel`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`82`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| collab panel：移动Channel Up | `alt-up` | `collab_panel::MoveChannelUp` |
| collab panel：移动Channel Down | `alt-down` | `collab_panel::MoveChannelDown` |
| collab panel：打开Selected Channel Notes | `alt-enter` | `collab_panel::OpenSelectedChannelNotes` |
| collab panel：切换Selected Channel Favorite | `shift-enter` | `collab_panel::ToggleSelectedChannelFavorite` |

## `(CollabPanel && editing) > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`83`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| collab panel：执行 Insert Space | `space` | `collab_panel::InsertSpace` |

## `TabSwitcher`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`90`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 选择菜单/列表中的上一项 | `ctrl-shift-tab` | `menu::SelectPrevious` |
| 选择菜单/列表中的上一项 | `ctrl-up` | `menu::SelectPrevious` |
| 选择菜单/列表中的下一项 | `ctrl-down` | `menu::SelectNext` |
| tab switcher：关闭Selected Item | `ctrl-backspace` | `tab_switcher::CloseSelectedItem` |

## `RunModal`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`101`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 窗格：执行 Activate Next Item | `ctrl-tab` | `pane::ActivateNextItem` |
| 窗格：执行 Activate Previous Item | `ctrl-shift-tab` | `pane::ActivatePreviousItem` |

## `Welcome`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`108`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 新建文件 | `ctrl-n` | `workspace::NewFile` |
| Zed：执行 Increase Ui Font Size | `ctrl-=` | `zed::IncreaseUiFontSize`; 参数 `[{"persist":false}]` |
| Zed：执行 Increase Ui Font Size | `ctrl-+` | `zed::IncreaseUiFontSize`; 参数 `[{"persist":false}]` |
| Zed：执行 Decrease Ui Font Size | `ctrl--` | `zed::DecreaseUiFontSize`; 参数 `[{"persist":false}]` |
| Zed：执行 Reset Ui Font Size | `ctrl-0` | `zed::ResetUiFontSize`; 参数 `[{"persist":false}]` |
| welcome：打开Recent Project | `ctrl-1` | `welcome::OpenRecentProject`; 参数 `[0]` |
| welcome：打开Recent Project | `ctrl-2` | `welcome::OpenRecentProject`; 参数 `[1]` |
| welcome：打开Recent Project | `ctrl-3` | `welcome::OpenRecentProject`; 参数 `[2]` |
| welcome：打开Recent Project | `ctrl-4` | `welcome::OpenRecentProject`; 参数 `[3]` |
| welcome：打开Recent Project | `ctrl-5` | `welcome::OpenRecentProject`; 参数 `[4]` |

## `SettingsWindow`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`110`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 关闭当前窗口 | `ctrl-w` | `workspace::CloseWindow` |
| 关闭当前窗口 | `escape` | `workspace::CloseWindow` |
| settings editor：执行 Minimize | `ctrl-m` | `settings_editor::Minimize` |
| 聚焦搜索输入框 | `ctrl-f` | `search::FocusSearch` |
| settings editor：打开Current File | `ctrl-,` | `settings_editor::OpenCurrentFile` |
| settings editor：切换Focus Nav | `left` | `settings_editor::ToggleFocusNav` |
| settings editor：切换Focus Nav | `ctrl-shift-e` | `settings_editor::ToggleFocusNav` |
| settings editor：聚焦File | `ctrl-1` | `settings_editor::FocusFile`; 参数 `[0]` |
| settings editor：聚焦File | `ctrl-2` | `settings_editor::FocusFile`; 参数 `[1]` |
| settings editor：聚焦File | `ctrl-3` | `settings_editor::FocusFile`; 参数 `[2]` |
| settings editor：聚焦File | `ctrl-4` | `settings_editor::FocusFile`; 参数 `[3]` |
| settings editor：聚焦File | `ctrl-5` | `settings_editor::FocusFile`; 参数 `[4]` |
| settings editor：聚焦File | `ctrl-6` | `settings_editor::FocusFile`; 参数 `[5]` |
| settings editor：聚焦File | `ctrl-7` | `settings_editor::FocusFile`; 参数 `[6]` |
| settings editor：聚焦File | `ctrl-8` | `settings_editor::FocusFile`; 参数 `[7]` |
| settings editor：聚焦File | `ctrl-9` | `settings_editor::FocusFile`; 参数 `[8]` |
| settings editor：聚焦File | `ctrl-0` | `settings_editor::FocusFile`; 参数 `[9]` |
| settings editor：聚焦Previous File | `ctrl-pageup` | `settings_editor::FocusPreviousFile` |
| settings editor：聚焦Next File | `ctrl-pagedown` | `settings_editor::FocusNextFile` |

## `SkillCreator`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`124`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 关闭当前窗口 | `ctrl-w` | `workspace::CloseWindow` |
| skill creator：保存Skill | `ctrl-enter` | `skill_creator::SaveSkill` |
| skill creator：聚焦Next Field | `tab` | `skill_creator::FocusNextField` |
| skill creator：聚焦Previous Field | `shift-tab` | `skill_creator::FocusPreviousField` |

## `SkillCreator > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`125`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 关闭当前窗口 | `ctrl-w` | `workspace::CloseWindow` |
| skill creator：保存Skill | `ctrl-enter` | `skill_creator::SaveSkill` |
| skill creator：聚焦Next Field | `tab` | `skill_creator::FocusNextField` |
| skill creator：聚焦Previous Field | `shift-tab` | `skill_creator::FocusPreviousField` |

