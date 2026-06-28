# VS Code 默认布局：搜索、替换、Picker 与命令入口

包含文件查找、文本查找、buffer/project search、outline、symbol、命令面板、语言/主题选择等快捷键。


## `AcpThread`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`18`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 新建 Agent 对话线程 | `ctrl-n` | `agent::NewThread` |
| 导航后退 | `ctrl--` | `pane::GoBack` |
| Agent/AI：执行 Manage Skills | `shift-alt-l` | `agent::ManageSkills` |
| Agent/AI：执行 Manage Profiles | `shift-alt-p` | `agent::ManageProfiles` |
| Agent/AI：切换Profile Selector | `ctrl-i` | `agent::ToggleProfileSelector` |
| Agent/AI：执行 Cycle Mode Selector | `shift-tab` | `agent::CycleModeSelector` |
| Agent/AI：切换Model Selector | `shift-alt-/` | `agent::ToggleModelSelector` |
| Agent/AI：执行 Cycle Favorite Models | `alt-tab` | `agent::CycleFavoriteModels` |
| Agent/AI：执行 Cycle Favorite Models | `alt-l` | `agent::CycleFavoriteModels` |
| Agent/AI：展开Message Editor | `shift-alt-escape` | `agent::ExpandMessageEditor` |
| Agent/AI：添加Selection To Thread | `ctrl-shift-.` | `agent::AddSelectionToThread` |
| Agent/AI：执行 Allow Always | `shift-alt-q` | `agent::AllowAlways` |
| Agent/AI：执行 Allow Once | `shift-alt-a` | `agent::AllowOnce` |
| Agent/AI：打开Permission Dropdown | `ctrl-alt-a` | `agent::OpenPermissionDropdown` |
| Agent/AI：拒绝Once | `shift-alt-x` | `agent::RejectOnce` |
| Agent/AI：执行 Scroll Output Page Up | `pageup` | `agent::ScrollOutputPageUp` |
| Agent/AI：执行 Scroll Output Page Down | `pagedown` | `agent::ScrollOutputPageDown` |
| Agent/AI：执行 Scroll Output To Top | `home` | `agent::ScrollOutputToTop` |
| Agent/AI：执行 Scroll Output To Bottom | `end` | `agent::ScrollOutputToBottom` |
| Agent/AI：执行 Scroll Output Line Up | `up` | `agent::ScrollOutputLineUp` |
| Agent/AI：执行 Scroll Output Line Down | `down` | `agent::ScrollOutputLineDown` |
| Agent/AI：执行 Scroll Output To Previous Message | `shift-pageup` | `agent::ScrollOutputToPreviousMessage` |
| Agent/AI：执行 Scroll Output To Next Message | `shift-pagedown` | `agent::ScrollOutputToNextMessage` |
| Agent/AI：执行 Scroll Output Page Up | `ctrl-alt-pageup` | `agent::ScrollOutputPageUp` |
| Agent/AI：执行 Scroll Output Page Down | `ctrl-alt-pagedown` | `agent::ScrollOutputPageDown` |
| Agent/AI：执行 Scroll Output To Top | `ctrl-alt-home` | `agent::ScrollOutputToTop` |
| Agent/AI：执行 Scroll Output To Bottom | `ctrl-alt-end` | `agent::ScrollOutputToBottom` |
| Agent/AI：执行 Scroll Output Line Up | `ctrl-alt-up` | `agent::ScrollOutputLineUp` |
| Agent/AI：执行 Scroll Output Line Down | `ctrl-alt-down` | `agent::ScrollOutputLineDown` |
| Agent/AI：执行 Scroll Output To Previous Message | `ctrl-alt-shift-pageup` | `agent::ScrollOutputToPreviousMessage` |
| Agent/AI：执行 Scroll Output To Next Message | `ctrl-alt-shift-pagedown` | `agent::ScrollOutputToNextMessage` |
| Agent/AI：切换Search | `ctrl-f` | `agent::ToggleSearch` |
| Agent/AI：选择Next Thread Match | `f3` | `agent::SelectNextThreadMatch` |
| Agent/AI：选择Previous Thread Match | `shift-f3` | `agent::SelectPreviousThreadMatch` |
| 搜索：切换Case Sensitive | `alt-c` | `search::ToggleCaseSensitive` |
| 搜索：切换Whole Word | `alt-w` | `search::ToggleWholeWord` |
| 搜索：切换Regex | `alt-r` | `search::ToggleRegex` |

## `AcpThreadSearchBar`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`19`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Agent/AI：执行 Dismiss Thread Search | `escape` | `agent::DismissThreadSearch` |
| Agent/AI：选择Next Thread Match | `enter` | `agent::SelectNextThreadMatch` |
| Agent/AI：选择Previous Thread Match | `shift-enter` | `agent::SelectPreviousThreadMatch` |
| 聚焦搜索输入框 | `ctrl-f` | `search::FocusSearch` |

## `AcpThreadSearchBar > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`20`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Agent/AI：选择Previous Thread Match | `shift-enter` | `agent::SelectPreviousThreadMatch` |

## `BufferSearchBar`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`29`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 关闭当前文件搜索 | `escape` | `buffer_search::Dismiss` |
| 文件内搜索：聚焦Editor | `tab` | `buffer_search::FocusEditor` |
| 跳到下一个搜索结果 | `enter` | `search::SelectNextMatch` |
| 跳到上一个搜索结果 | `shift-enter` | `search::SelectPreviousMatch` |
| 编辑器：切换Fold All | `ctrl-shift-enter` | `editor::ToggleFoldAll` |
| 选中所有搜索结果 | `alt-enter` | `search::SelectAllMatches` |
| 聚焦搜索输入框 | `ctrl-f` | `search::FocusSearch` |
| 显示/隐藏替换输入框 | `ctrl-h` | `search::ToggleReplace` |
| 切换搜索选区范围 | `ctrl-l` | `search::ToggleSelection` |

## `BufferSearchBar && in_replace > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`30`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 搜索：执行 Replace Next | `enter` | `search::ReplaceNext` |
| 搜索：执行 Replace All | `ctrl-enter` | `search::ReplaceAll` |

## `BufferSearchBar && !in_replace > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`31`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 插入换行 | `ctrl-enter` | `editor::Newline` |
| 跳到上一个搜索结果 | `shift-enter` | `search::SelectPreviousMatch` |

## `BufferSearchBar && !in_replace > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`32`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 搜索：执行 Previous History Query | `up` | `search::PreviousHistoryQuery` |
| 搜索：执行 Next History Query | `down` | `search::NextHistoryQuery` |

## `ProjectSearchBar`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`33`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 项目搜索：切换Focus | `escape` | `project_search::ToggleFocus` |
| 聚焦搜索输入框 | `ctrl-shift-f` | `search::FocusSearch` |
| 显示/隐藏替换输入框 | `ctrl-shift-h` | `search::ToggleReplace` |
| 搜索：切换Regex | `alt-r` | `search::ToggleRegex` |
| 项目搜索：打开Text Finder | `ctrl-alt-f` | `project_search::OpenTextFinder` |

## `ProjectSearchBar > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`34`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 搜索：执行 Previous History Query | `up` | `search::PreviousHistoryQuery` |
| 搜索：执行 Next History Query | `down` | `search::NextHistoryQuery` |

## `ProjectSearchBar && in_replace > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`35`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 搜索：执行 Replace Next | `enter` | `search::ReplaceNext` |
| 搜索：执行 Replace All | `ctrl-alt-enter` | `search::ReplaceAll` |

## `ProjectSearchBar && !in_replace > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`36`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 插入换行 | `ctrl-enter` | `editor::Newline` |

## `ProjectSearchView`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`37`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 项目搜索：切换Focus | `escape` | `project_search::ToggleFocus` |
| 显示/隐藏替换输入框 | `ctrl-shift-h` | `search::ToggleReplace` |
| 搜索：切换Regex | `alt-r` | `search::ToggleRegex` |
| 项目搜索：打开Text Finder | `ctrl-alt-f` | `project_search::OpenTextFinder` |

## `Workspace`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`43`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| projects：打开Recent | `ctrl-r` | `projects::OpenRecent` |
| projects：打开Remote | `ctrl-shift-alt-o` | `projects::OpenRemote`; 参数 `[{"from_existing_connection":false}]` |
| branches：打开Recent | `shift-alt-b` | `branches::OpenRecent` |
| Git：执行 Worktree | `shift-alt-w` | `git::Worktree` |
| toast：运行Action | `shift-alt-enter` | `toast::RunAction` |
| 新建终端 | `` ctrl-shift-` `` | `workspace::NewTerminal` |
| 保存当前文件 | `ctrl-s` | `workspace::Save` |
| 工作区：保存Without Format | `ctrl-k ctrl-shift-s` | `workspace::SaveWithoutFormat` |
| 当前文件另存为 | `ctrl-shift-s` | `workspace::SaveAs` |
| 新建文件 | `ctrl-n` | `workspace::NewFile` |
| 新建窗口 | `ctrl-shift-n` | `workspace::NewWindow` |
| 显示/隐藏终端面板 | `` ctrl-` `` | `terminal_panel::Toggle` |
| app menu：打开Application Menu | `f10` | `app_menu::OpenApplicationMenu`; 参数 `["Zed"]` |
| 工作区：执行 Activate Pane | `alt-1` | `workspace::ActivatePane`; 参数 `[0]` |
| 工作区：执行 Activate Pane | `alt-2` | `workspace::ActivatePane`; 参数 `[1]` |
| 工作区：执行 Activate Pane | `alt-3` | `workspace::ActivatePane`; 参数 `[2]` |
| 工作区：执行 Activate Pane | `alt-4` | `workspace::ActivatePane`; 参数 `[3]` |
| 工作区：执行 Activate Pane | `alt-5` | `workspace::ActivatePane`; 参数 `[4]` |
| 工作区：执行 Activate Pane | `alt-6` | `workspace::ActivatePane`; 参数 `[5]` |
| 工作区：执行 Activate Pane | `alt-7` | `workspace::ActivatePane`; 参数 `[6]` |
| 工作区：执行 Activate Pane | `alt-8` | `workspace::ActivatePane`; 参数 `[7]` |
| 工作区：执行 Activate Pane | `alt-9` | `workspace::ActivatePane`; 参数 `[8]` |
| 工作区：切换Right Dock | `ctrl-alt-b` | `workspace::ToggleRightDock` |
| 工作区：切换Left Dock | `ctrl-b` | `workspace::ToggleLeftDock` |
| 工作区：切换Bottom Dock | `ctrl-j` | `workspace::ToggleBottomDock` |
| multi workspace：切换Workspace Sidebar | `ctrl-alt-j` | `multi_workspace::ToggleWorkspaceSidebar` |
| multi workspace：聚焦Workspace Sidebar | `ctrl-alt-;` | `multi_workspace::FocusWorkspaceSidebar` |
| 工作区：切换All Docks | `ctrl-shift-y` | `workspace::ToggleAllDocks` |
| 工作区：执行 Reset Active Dock Size | `alt-r` | `workspace::ResetActiveDockSize` |
| 工作区：执行 Decrease Active Dock Size | `shift-alt--` | `workspace::DecreaseActiveDockSize`; 参数 `[{"px":0}]` |
| 工作区：执行 Increase Active Dock Size | `shift-alt-=` | `workspace::IncreaseActiveDockSize`; 参数 `[{"px":0}]` |
| 工作区：执行 Reset Open Docks Size | `shift-alt-0` | `workspace::ResetOpenDocksSize` |
| 在窗格中打开搜索 | `ctrl-shift-f` | `pane::DeploySearch` |
| 在窗格中打开搜索 | `ctrl-shift-h` | `pane::DeploySearch`; 参数 `[{"replace_enabled":true}]` |
| 窗格：执行 Reopen Closed Item | `ctrl-shift-t` | `pane::ReopenClosedItem` |
| 打开快捷键配置 | `ctrl-k ctrl-s` | `zed::OpenKeymap` |
| 打开主题选择器 | `ctrl-k ctrl-t` | `theme_selector::Toggle` |
| theme：切换Mode | `ctrl-k ctrl-shift-t` | `theme::ToggleMode` |
| settings profile selector：切换操作 | `ctrl-alt-super-p` | `settings_profile_selector::Toggle` |
| 打开/关闭项目符号搜索 | `ctrl-t` | `project_symbols::Toggle` |
| 打开/关闭文件快速查找 | `ctrl-p` | `file_finder::Toggle` |
| tab switcher：切换操作 | `ctrl-shift-tab` | `tab_switcher::Toggle`; 参数 `[{"select_last":true}]` |
| tab switcher：切换操作 | `ctrl-tab` | `tab_switcher::Toggle` |
| 打开/关闭文件快速查找 | `ctrl-e` | `file_finder::Toggle` |
| 打开/关闭命令面板 | `f1` | `command_palette::Toggle` |
| 打开/关闭命令面板 | `ctrl-shift-p` | `command_palette::Toggle` |
| diagnostics：执行 Deploy | `ctrl-shift-m` | `diagnostics::Deploy` |
| 切换项目文件面板焦点 | `ctrl-shift-e` | `project_panel::ToggleFocus` |
| outline panel：切换Focus | `ctrl-shift-b` | `outline_panel::ToggleFocus` |
| 切换 Git 面板焦点 | `ctrl-shift-g` | `git_panel::ToggleFocus` |
| debug panel：切换Focus | `ctrl-shift-d` | `debug_panel::ToggleFocus` |
| 切换 Agent/AI 面板焦点 | `ctrl-shift-/` | `agent::ToggleFocus` |
| 保存所有文件 | `ctrl-k s` | `workspace::SaveAll` |
| encoding selector：切换操作 | `ctrl-k n` | `encoding_selector::Toggle` |
| 打开语言模式选择器 | `ctrl-k m` | `language_selector::Toggle` |
| toolchain：添加Toolchain | `ctrl-m ctrl-m` | `toolchain::AddToolchain` |
| 工作区：执行 Unfollow | `escape` | `workspace::Unfollow` |
| 切换焦点到左侧窗格 | `ctrl-k ctrl-left` | `workspace::ActivatePaneLeft` |
| 切换焦点到右侧窗格 | `ctrl-k ctrl-right` | `workspace::ActivatePaneRight` |
| 切换焦点到上方窗格 | `ctrl-k ctrl-up` | `workspace::ActivatePaneUp` |
| 切换焦点到下方窗格 | `ctrl-k ctrl-down` | `workspace::ActivatePaneDown` |
| 工作区：执行 Swap Pane Left | `ctrl-k shift-left` | `workspace::SwapPaneLeft` |
| 工作区：执行 Swap Pane Right | `ctrl-k shift-right` | `workspace::SwapPaneRight` |
| 工作区：执行 Swap Pane Up | `ctrl-k shift-up` | `workspace::SwapPaneUp` |
| 工作区：执行 Swap Pane Down | `ctrl-k shift-down` | `workspace::SwapPaneDown` |
| Zed：执行 Extensions | `ctrl-shift-x` | `zed::Extensions` |
| task：执行 Rerun | `ctrl-shift-r` | `task::Rerun`; 参数 `[{"reevaluate_context":false}]` |
| task：执行 Rerun | `alt-t` | `task::Rerun` |
| task：执行 Spawn | `shift-alt-t` | `task::Spawn` |
| task：执行 Spawn | `shift-alt-r` | `task::Spawn`; 参数 `[{"reveal_target":"center"}]` |
| 调试器：执行 Rerun | `f5` | `debugger::Rerun` |
| 工作区：关闭Active Dock | `ctrl-f4` | `workspace::CloseActiveDock` |
| 工作区：关闭Active Dock | `ctrl-w` | `workspace::CloseActiveDock` |

## `ThreadsSidebar && not_searching`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`47`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 确认当前菜单/列表选择 | `space` | `menu::Confirm` |
| Agent/AI：重命名Selected Thread | `shift-r` | `agent::RenameSelectedThread` |

## `ProjectSearchBar && !in_replace`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`66`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 项目搜索：执行 Search In New | `ctrl-enter` | `project_search::SearchInNew` |

## `ProjectPanel`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`68`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 项目面板：折叠Selected Entry | `left` | `project_panel::CollapseSelectedEntry` |
| 项目面板：折叠All Entries | `ctrl-left` | `project_panel::CollapseAllEntries` |
| 项目面板：展开Selected Entry | `right` | `project_panel::ExpandSelectedEntry` |
| 项目面板：展开All Entries | `ctrl-right` | `project_panel::ExpandAllEntries` |
| 在项目面板中新建文件 | `ctrl-n` | `project_panel::NewFile` |
| 在项目面板中新建目录 | `alt-n` | `project_panel::NewDirectory` |
| 剪切项目面板选中项 | `ctrl-x` | `project_panel::Cut` |
| 复制项目面板选中项 | `ctrl-insert` | `project_panel::Copy` |
| 复制项目面板选中项 | `ctrl-c` | `project_panel::Copy` |
| 粘贴到项目面板 | `shift-insert` | `project_panel::Paste` |
| 粘贴到项目面板 | `ctrl-v` | `project_panel::Paste` |
| 项目面板：复制Path | `shift-alt-c` | `project_panel::CopyPath` |
| 工作区：复制Relative Path | `ctrl-k ctrl-shift-c` | `workspace::CopyRelativePath` |
| 项目面板：执行 Undo | `ctrl-z` | `project_panel::Undo` |
| 项目面板：执行 Redo | `ctrl-shift-z` | `project_panel::Redo` |
| 重命名项目面板选中项 | `enter` | `project_panel::Rename` |
| 重命名项目面板选中项 | `f2` | `project_panel::Rename` |
| 项目面板：执行 Trash | `backspace` | `project_panel::Trash`; 参数 `[{"skip_prompt":false}]` |
| 项目面板：执行 Trash | `delete` | `project_panel::Trash`; 参数 `[{"skip_prompt":false}]` |
| 删除项目面板选中项 | `shift-delete` | `project_panel::Delete`; 参数 `[{"skip_prompt":false}]` |
| 删除项目面板选中项 | `ctrl-backspace` | `project_panel::Delete`; 参数 `[{"skip_prompt":false}]` |
| 删除项目面板选中项 | `ctrl-delete` | `project_panel::Delete`; 参数 `[{"skip_prompt":false}]` |
| 项目面板：执行 Reveal In File Manager | `ctrl-alt-r` | `project_panel::RevealInFileManager` |
| 项目面板：打开With System | `ctrl-shift-enter` | `project_panel::OpenWithSystem` |
| 项目面板：执行 Compare Marked Files | `alt-d` | `project_panel::CompareMarkedFiles` |
| 项目面板：新建Search In Directory | `ctrl-k ctrl-shift-f` | `project_panel::NewSearchInDirectory` |
| 选择菜单/列表中的下一项 | `shift-down` | `menu::SelectNext` |
| 选择菜单/列表中的上一项 | `shift-up` | `menu::SelectPrevious` |
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |

## `DebugPanel`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`78`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 调试器：切换Thread Picker | `ctrl-t` | `debugger::ToggleThreadPicker` |
| 调试器：切换Session Picker | `ctrl-i` | `debugger::ToggleSessionPicker` |
| 调试器：切换Expand Item | `shift-alt-escape` | `debugger::ToggleExpandItem` |

## `Picker > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`85`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |
| 选择菜单/列表中的上一项 | `up` | `menu::SelectPrevious` |
| 选择菜单/列表中的下一项 | `down` | `menu::SelectNext` |
| 选择器：执行 Confirm Completion | `tab` | `picker::ConfirmCompletion` |
| 确认 Picker 输入内容 | `alt-enter` | `picker::ConfirmInput`; 参数 `[{"secondary":false}]` |

## `ChannelModal > Picker > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`86`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| channel modal：切换Mode | `tab` | `channel_modal::ToggleMode` |

## `FileFinder || (FileFinder > Picker > Editor)`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`88`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 打开/关闭文件快速查找 | `ctrl-p` | `file_finder::Toggle` |
| 搜索：切换Include Ignored | `ctrl-shift-i` | `search::ToggleIncludeIgnored` |

## `RecentProjects || (RecentProjects > Picker > Editor)`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`89`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| recent projects：切换Actions Menu | `ctrl-k` | `recent_projects::ToggleActionsMenu` |
| 工作区：添加Folder To Project | `ctrl-shift-a` | `workspace::AddFolderToProject` |
| recent projects：移除Selected | `shift-backspace` | `recent_projects::RemoveSelected` |
| recent projects：添加To Workspace | `ctrl-shift-enter` | `recent_projects::AddToWorkspace` |

## `StashList || (StashList > Picker > Editor)`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`91`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| stash picker：执行 Drop Stash Item | `ctrl-shift-backspace` | `stash_picker::DropStashItem` |
| stash picker：显示Stash Item | `ctrl-shift-v` | `stash_picker::ShowStashItem` |

## `Terminal`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`92`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 执行终端相关操作 | `ctrl-alt-space` | `terminal::ShowCharacterPalette` |
| 执行终端相关操作 | `ctrl-insert` | `terminal::Copy` |
| 执行终端相关操作 | `ctrl-shift-c` | `terminal::Copy` |
| 执行终端相关操作 | `shift-insert` | `terminal::Paste` |
| 执行终端相关操作 | `ctrl-v` | `terminal::Paste` |
| 执行终端相关操作 | `ctrl-shift-v` | `terminal::Paste` |
| 执行终端相关操作 | `ctrl-alt-v` | `terminal::PasteText` |
| 打开行内 AI 助手 | `ctrl-i` | `assistant::InlineAssist` |
| 执行终端相关操作 | `alt-b` | `terminal::SendText`; 参数 `["\u001bb"]` |
| 执行终端相关操作 | `alt-f` | `terminal::SendText`; 参数 `["\u001bf"]` |
| 执行终端相关操作 | `alt-.` | `terminal::SendText`; 参数 `["\u001b."]` |
| 执行终端相关操作 | `ctrl-delete` | `terminal::SendText`; 参数 `["\u001bd"]` |
| 新建终端 | `ctrl-n` | `workspace::NewTerminal` |
| 关闭当前窗口 | `alt-f4` | `workspace::CloseWindow` |
| 执行终端相关操作 | `ctrl-b` | `terminal::SendKeystroke`; 参数 `["ctrl-b"]` |
| 执行终端相关操作 | `ctrl-c` | `terminal::SendKeystroke`; 参数 `["ctrl-c"]` |
| 执行终端相关操作 | `ctrl-e` | `terminal::SendKeystroke`; 参数 `["ctrl-e"]` |
| 执行终端相关操作 | `ctrl-o` | `terminal::SendKeystroke`; 参数 `["ctrl-o"]` |
| 执行终端相关操作 | `ctrl-w` | `terminal::SendKeystroke`; 参数 `["ctrl-w"]` |
| 执行终端相关操作 | `ctrl-q` | `terminal::SendKeystroke`; 参数 `["ctrl-q"]` |
| 执行终端相关操作 | `ctrl-r` | `terminal::SendKeystroke`; 参数 `["ctrl-r"]` |
| 执行终端相关操作 | `ctrl-backspace` | `terminal::SendKeystroke`; 参数 `["ctrl-w"]` |
| 全选当前编辑器内容 | `ctrl-shift-a` | `editor::SelectAll` |
| 打开当前文件搜索 | `ctrl-shift-f` | `buffer_search::Deploy` |
| 执行终端相关操作 | `ctrl-shift-l` | `terminal::Clear` |
| 窗格：关闭Active Item | `ctrl-shift-w` | `pane::CloseActiveItem` |
| 执行终端相关操作 | `up` | `terminal::SendKeystroke`; 参数 `["up"]` |
| 执行终端相关操作 | `pageup` | `terminal::SendKeystroke`; 参数 `["pageup"]` |
| 执行终端相关操作 | `down` | `terminal::SendKeystroke`; 参数 `["down"]` |
| 执行终端相关操作 | `pagedown` | `terminal::SendKeystroke`; 参数 `["pagedown"]` |
| 执行终端相关操作 | `escape` | `terminal::SendKeystroke`; 参数 `["escape"]` |
| 执行终端相关操作 | `enter` | `terminal::SendKeystroke`; 参数 `["enter"]` |
| 执行终端相关操作 | `shift-pageup` | `terminal::ScrollPageUp` |
| 执行终端相关操作 | `shift-pagedown` | `terminal::ScrollPageDown` |
| 执行终端相关操作 | `shift-up` | `terminal::ScrollLineUp` |
| 执行终端相关操作 | `shift-down` | `terminal::ScrollLineDown` |
| 执行终端相关操作 | `shift-home` | `terminal::ScrollToTop` |
| 执行终端相关操作 | `shift-end` | `terminal::ScrollToBottom` |
| 执行终端相关操作 | `ctrl-shift-space` | `terminal::ToggleViMode` |
| 执行终端相关操作 | `ctrl-shift-r` | `terminal::RerunTask` |
| 执行终端相关操作 | `ctrl-alt-r` | `terminal::RerunTask` |
| 执行终端相关操作 | `alt-t` | `terminal::RerunTask` |
| 向右拆分窗格 | `ctrl-shift-5` | `pane::SplitRight` |
| Agent/AI：添加Selection To Thread | `ctrl-shift-.` | `agent::AddSelectionToThread` |

## `MarkdownPreview`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`102`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Markdown：执行 Scroll Page Up | `pageup` | `markdown::ScrollPageUp` |
| Markdown：执行 Scroll Page Down | `pagedown` | `markdown::ScrollPageDown` |
| Markdown：执行 Scroll Up | `up` | `markdown::ScrollUp` |
| Markdown：执行 Scroll Down | `down` | `markdown::ScrollDown` |
| Markdown：执行 Scroll Up By Item | `alt-up` | `markdown::ScrollUpByItem` |
| Markdown：执行 Scroll Down By Item | `alt-down` | `markdown::ScrollDownByItem` |
| Markdown：执行 Scroll To Top | `ctrl-home` | `markdown::ScrollToTop` |
| Markdown：执行 Scroll To Bottom | `ctrl-end` | `markdown::ScrollToBottom` |
| 打开当前文件搜索 | `find` | `buffer_search::Deploy` |
| 打开当前文件搜索 | `ctrl-f` | `buffer_search::Deploy` |

## `KeymapEditor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`103`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 聚焦搜索输入框 | `ctrl-f` | `search::FocusSearch` |
| keymap editor：切换Keystroke Search | `alt-f` | `keymap_editor::ToggleKeystrokeSearch` |
| keymap editor：切换Conflict Filter | `alt-c` | `keymap_editor::ToggleConflictFilter` |
| keymap editor：执行 Edit Binding | `enter` | `keymap_editor::EditBinding` |
| keymap editor：执行 Create Binding | `alt-enter` | `keymap_editor::CreateBinding` |
| keymap editor：打开Create Keybinding Modal | `ctrl-k` | `keymap_editor::OpenCreateKeybindingModal` |
| keymap editor：复制Action | `ctrl-c` | `keymap_editor::CopyAction` |
| keymap editor：复制Context | `ctrl-shift-c` | `keymap_editor::CopyContext` |
| keymap editor：显示Matching Keybinds | `ctrl-t` | `keymap_editor::ShowMatchingKeybinds` |
| Zed：打开Keymap File | `ctrl-e` | `zed::OpenKeymapFile` |

## `GitBranchSelector || (GitBranchSelector > Picker > Editor)`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`114`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| branch picker：删除Branch | `ctrl-shift-backspace` | `branch_picker::DeleteBranch` |
| branch picker：执行 Force Delete Branch | `ctrl-alt-shift-backspace` | `branch_picker::ForceDeleteBranch` |
| branch picker：执行 Filter Remotes | `ctrl-shift-i` | `branch_picker::FilterRemotes` |

## `GitPicker`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`117`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| git picker：执行 Activate Branches Tab | `alt-1` | `git_picker::ActivateBranchesTab` |
| git picker：执行 Activate Stash Tab | `alt-2` | `git_picker::ActivateStashTab` |

## `WorktreePicker || (WorktreePicker > Picker > Editor)`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`118`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| worktree picker：删除Worktree | `ctrl-shift-backspace` | `worktree_picker::DeleteWorktree` |
| worktree picker：执行 Force Delete Worktree | `ctrl-alt-shift-backspace` | `worktree_picker::ForceDeleteWorktree` |

## `GitGraphSearchBar > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`123`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| git graph：聚焦Next Tab Stop | `tab` | `git_graph::FocusNextTabStop` |
| git graph：聚焦Previous Tab Stop | `shift-tab` | `git_graph::FocusPreviousTabStop` |

