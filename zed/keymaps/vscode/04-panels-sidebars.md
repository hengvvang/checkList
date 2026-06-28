# VS Code 默认布局：侧边栏与面板

包含 ProjectPanel、OutlinePanel、通知、频道、线程侧栏、协作面板等面板/侧边栏上下文快捷键。


## `ThreadsSidebar`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`46`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| agents sidebar：新建Thread In Group | `ctrl-n` | `agents_sidebar::NewThreadInGroup` |
| 返回父菜单或收起当前项 | `left` | `menu::SelectParent` |
| 进入子菜单或展开当前项 | `right` | `menu::SelectChild` |
| 确认当前菜单/列表选择 | `enter` | `menu::Confirm` |
| agents sidebar：聚焦Sidebar Filter | `ctrl-f` | `agents_sidebar::FocusSidebarFilter` |
| agents sidebar：切换Thread History | `ctrl-g` | `agents_sidebar::ToggleThreadHistory` |
| Agent/AI：执行 Archive Selected Thread | `shift-backspace` | `agent::ArchiveSelectedThread` |
| Agent/AI：移除Selected Thread | `ctrl-backspace` | `agent::RemoveSelectedThread` |
| agents sidebar：切换Thread Switcher | `ctrl-tab` | `agents_sidebar::ToggleThreadSwitcher` |
| agents sidebar：切换Thread Switcher | `ctrl-shift-tab` | `agents_sidebar::ToggleThreadSwitcher`; 参数 `[{"select_last":true}]` |

## `ThreadSwitcher`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`48`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| agents sidebar：切换Thread Switcher | `ctrl-tab` | `agents_sidebar::ToggleThreadSwitcher` |
| agents sidebar：切换Thread Switcher | `ctrl-shift-tab` | `agents_sidebar::ToggleThreadSwitcher`; 参数 `[{"select_last":true}]` |

## `ProjectPanel && not_editing`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`69`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 打开项目面板选中项 | `space` | `project_panel::Open` |

## `ChannelModal`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`84`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| channel modal：切换Mode | `tab` | `channel_modal::ToggleMode` |

