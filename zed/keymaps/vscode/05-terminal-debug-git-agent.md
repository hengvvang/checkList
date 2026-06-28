# VS Code 默认布局：终端、调试、Git 与 Agent/AI

包含 Terminal、Debugger、Git、Agent/AI、ACP thread、edit prediction、LSP tool 等现代工作流快捷键。


## `Editor && !agent_diff`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`11`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 还原 Git 变更 | `ctrl-k ctrl-r` | `git::Restore` |
| 暂存当前变更并跳到下一处 | `alt-y` | `git::StageAndNext` |
| 取消暂存当前变更并跳到下一处 | `shift-alt-y` | `git::UnstageAndNext` |

## `Editor && editor_agent_diff`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`12`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 保留 Agent 生成的当前变更 | `alt-y` | `agent::Keep` |
| 保留 Agent 生成的当前变更 | `ctrl-alt-y` | `agent::Keep` |
| 拒绝 Agent 生成的当前变更 | `ctrl-alt-z` | `agent::Reject` |
| 保留所有 Agent 生成的变更 | `shift-alt-y` | `agent::KeepAll` |
| 拒绝所有 Agent 生成的变更 | `shift-alt-z` | `agent::RejectAll` |
| 打开 Agent diff 视图 | `ctrl-shift-r` | `agent::OpenAgentDiff` |
## `AgentDiff`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`13`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 保留 Agent 生成的当前变更 | `alt-y` | `agent::Keep` |
| 保留 Agent 生成的当前变更 | `ctrl-alt-y` | `agent::Keep` |
| 拒绝 Agent 生成的当前变更 | `ctrl-alt-z` | `agent::Reject` |
| 保留所有 Agent 生成的变更 | `shift-alt-y` | `agent::KeepAll` |
| 拒绝所有 Agent 生成的变更 | `shift-alt-z` | `agent::RejectAll` |

## `AgentPanel`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`14`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 新建 Agent 对话线程 | `ctrl-n` | `agent::NewThread` |
| Agent/AI：打开Settings | `shift-alt-c` | `agent::OpenSettings` |
| Agent/AI：切换Options Menu | `shift-alt-i` | `agent::ToggleOptionsMenu` |
| Agent/AI：切换New Thread Menu | `ctrl-shift-alt-n` | `agent::ToggleNewThreadMenu` |
| 切换项目文件面板焦点 | `ctrl-shift-e` | `project_panel::ToggleFocus` |
| agents sidebar：切换Thread Switcher | `ctrl-tab` | `agents_sidebar::ToggleThreadSwitcher` |
| agents sidebar：切换Thread Switcher | `ctrl-shift-tab` | `agents_sidebar::ToggleThreadSwitcher`; 参数 `[{"select_last":true}]` |

## `AgentPanel > Markdown`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`15`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 按 Markdown 格式复制 | `ctrl-c` | `markdown::CopyAsMarkdown` |

## `AgentFeedbackMessageEditor > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`16`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |
| 确认当前菜单/列表选择 | `enter` | `menu::Confirm` |
| 插入换行 | `alt-enter` | `editor::Newline` |

## `AcpThread > ModeSelector`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`17`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 确认当前菜单/列表选择 | `ctrl-enter` | `menu::Confirm` |

## `AcpThread > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`21`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Agent/AI：执行 Scroll Output Page Up | `ctrl-alt-pageup` | `agent::ScrollOutputPageUp` |
| Agent/AI：执行 Scroll Output Page Down | `ctrl-alt-pagedown` | `agent::ScrollOutputPageDown` |
| Agent/AI：执行 Scroll Output To Top | `ctrl-alt-home` | `agent::ScrollOutputToTop` |
| Agent/AI：执行 Scroll Output To Bottom | `ctrl-alt-end` | `agent::ScrollOutputToBottom` |
| Agent/AI：执行 Scroll Output Line Up | `ctrl-alt-up` | `agent::ScrollOutputLineUp` |
| Agent/AI：执行 Scroll Output Line Down | `ctrl-alt-down` | `agent::ScrollOutputLineDown` |
| Agent/AI：执行 Scroll Output To Previous Message | `ctrl-alt-shift-pageup` | `agent::ScrollOutputToPreviousMessage` |
| Agent/AI：执行 Scroll Output To Next Message | `ctrl-alt-shift-pagedown` | `agent::ScrollOutputToNextMessage` |
| 打开 Agent diff 视图 | `ctrl-shift-r` | `agent::OpenAgentDiff` |
| Git：执行 Diff | `ctrl-shift-d` | `git::Diff` |
| 保留所有 Agent 生成的变更 | `shift-alt-y` | `agent::KeepAll` |
| 拒绝所有 Agent 生成的变更 | `shift-alt-z` | `agent::RejectAll` |
| Agent/AI：执行 Undo Last Reject | `shift-alt-u` | `agent::UndoLastReject` |
| Agent/AI：执行 Chat With Follow | `ctrl-enter` | `agent::ChatWithFollow` |
| Agent/AI：执行 Send Immediately | `ctrl-shift-enter` | `agent::SendImmediately` |
| Agent/AI：执行 Send Next Queued Message | `ctrl-shift-alt-enter` | `agent::SendNextQueuedMessage` |
| Agent/AI：移除First Queued Message | `ctrl-shift-backspace` | `agent::RemoveFirstQueuedMessage` |
| Agent/AI：执行 Edit First Queued Message | `ctrl-alt-e` | `agent::EditFirstQueuedMessage` |
| Agent/AI：切换Steer First Queued Message | `ctrl-alt-s` | `agent::ToggleSteerFirstQueuedMessage` |
| Agent/AI：执行 Clear Message Queue | `ctrl-alt-backspace` | `agent::ClearMessageQueue` |
| Agent/AI：粘贴Raw | `ctrl-shift-v` | `agent::PasteRaw` |
| Agent/AI：切换Profile Selector | `ctrl-i` | `agent::ToggleProfileSelector` |
| Agent/AI：执行 Cycle Mode Selector | `shift-tab` | `agent::CycleModeSelector` |
| Agent/AI：执行 Cycle Favorite Models | `alt-tab` | `agent::CycleFavoriteModels` |
| Agent/AI：执行 Cycle Favorite Models | `alt-l` | `agent::CycleFavoriteModels` |
| Agent/AI：打开Add Context Menu | `ctrl-;` | `agent::OpenAddContextMenu` |
| Agent/AI：切换Thinking Mode | `ctrl-alt-k` | `agent::ToggleThinkingMode` |
| Agent/AI：切换Thinking Effort Menu | `ctrl-alt-'` | `agent::ToggleThinkingEffortMenu` |
| Agent/AI：执行 Cycle Thinking Effort | `ctrl-'` | `agent::CycleThinkingEffort` |
| Agent/AI：切换Fast Mode | `ctrl-alt-.` | `agent::ToggleFastMode` |

## `AcpThread > Editor && start_of_input`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`22`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Agent/AI：执行 Scroll Output Page Up | `pageup` | `agent::ScrollOutputPageUp` |
| Agent/AI：执行 Scroll Output Page Up | `ctrl-pageup` | `agent::ScrollOutputPageUp` |
| Agent/AI：执行 Scroll Output To Top | `ctrl-home` | `agent::ScrollOutputToTop` |

## `AcpThread > Editor && end_of_input`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`23`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Agent/AI：执行 Scroll Output Page Down | `pagedown` | `agent::ScrollOutputPageDown` |
| Agent/AI：执行 Scroll Output Page Down | `ctrl-pagedown` | `agent::ScrollOutputPageDown` |
| Agent/AI：执行 Scroll Output To Bottom | `ctrl-end` | `agent::ScrollOutputToBottom` |

## `AcpThread > Editor && mode == full`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`24`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 打开当前搜索摘录/引用摘录 | `alt-enter` | `editor::OpenExcerpts` |

## `AcpThread > Editor && !use_modifier_to_send`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`25`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Agent/AI：执行 Chat | `enter` | `agent::Chat` |

## `AcpThread > Editor && use_modifier_to_send`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`26`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Agent/AI：执行 Chat | `ctrl-enter` | `agent::Chat` |
| 插入换行 | `enter` | `editor::Newline` |

## `ThreadHistory`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`27`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Agent/AI：移除Selected Thread | `backspace` | `agent::RemoveSelectedThread` |

## `ThreadsArchiveView`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`28`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Agent/AI：执行 Archive Selected Thread | `shift-backspace` | `agent::ArchiveSelectedThread` |

## `Workspace && debugger_running`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`44`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消/屏蔽该快捷键在当前上下文中的默认行为 | `f5` | `null` |

## `Workspace && debugger_stopped`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`45`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 调试器：执行 Continue | `f5` | `debugger::Continue` |

## `Editor && edit_prediction`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`56`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：接受Edit Prediction | `alt-tab` | `editor::AcceptEditPrediction` |
| 编辑器：接受Edit Prediction | `alt-l` | `editor::AcceptEditPrediction` |
| 编辑器：接受Next Word Edit Prediction | `alt-k` | `editor::AcceptNextWordEditPrediction` |
| 编辑器：接受Next Line Edit Prediction | `alt-j` | `editor::AcceptNextLineEditPrediction` |

## `Editor && edit_prediction && edit_prediction_mode == eager && !showing_completions`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`57`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：接受Edit Prediction | `tab` | `editor::AcceptEditPrediction` |

## `!Terminal`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`62`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| collab panel：切换Focus | `ctrl-shift-c` | `collab_panel::ToggleFocus` |

## `InlineAssistant`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`64`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Agent/AI：执行 Cycle Previous Inline Assist | `ctrl-[` | `agent::CyclePreviousInlineAssist` |
| Agent/AI：执行 Cycle Next Inline Assist | `ctrl-]` | `agent::CycleNextInlineAssist` |
| inline assistant：执行 Thumbs Up Result | `ctrl-shift-enter` | `inline_assistant::ThumbsUpResult` |
| inline assistant：执行 Thumbs Down Result | `ctrl-shift-delete` | `inline_assistant::ThumbsDownResult` |

## `GitPanel`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`70`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Git 面板：执行 Activate Changes Tab | `ctrl-1` | `git_panel::ActivateChangesTab` |
| Git 面板：执行 Activate History Tab | `ctrl-2` | `git_panel::ActivateHistoryTab` |

## `GitPanel && ChangesList && !GitBranchSelector`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`71`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Git 面板：执行 Previous Entry | `up` | `git_panel::PreviousEntry` |
| Git 面板：执行 Next Entry | `down` | `git_panel::NextEntry` |
| Git 面板：折叠Selected Entry | `left` | `git_panel::CollapseSelectedEntry` |
| Git 面板：展开Selected Entry | `right` | `git_panel::ExpandSelectedEntry` |
| 确认当前菜单/列表选择 | `enter` | `menu::Confirm` |
| Git：暂存File | `alt-y` | `git::StageFile` |
| Git：取消暂存File | `shift-alt-y` | `git::UnstageFile` |
| Git：切换Staged | `space` | `git::ToggleStaged` |
| Git：暂存Range | `shift-space` | `git::StageRange` |
| Git 面板：聚焦Editor | `tab` | `git_panel::FocusEditor` |
| Git 面板：聚焦Editor | `shift-tab` | `git_panel::FocusEditor` |
| 切换 Git 面板焦点 | `escape` | `git_panel::ToggleFocus` |
| 执行当前选择的次级确认操作 | `alt-enter` | `menu::SecondaryConfirm` |
| Git：执行 Restore File | `delete` | `git::RestoreFile`; 参数 `[{"skip_prompt":false}]` |
| Git：执行 Restore File | `backspace` | `git::RestoreFile`; 参数 `[{"skip_prompt":false}]` |
| Git：执行 Restore File | `shift-delete` | `git::RestoreFile`; 参数 `[{"skip_prompt":false}]` |
| Git：执行 Restore File | `ctrl-backspace` | `git::RestoreFile`; 参数 `[{"skip_prompt":false}]` |
| Git：执行 Restore File | `ctrl-delete` | `git::RestoreFile`; 参数 `[{"skip_prompt":false}]` |

## `GitCommit > Editor && mode == auto_height`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`73`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |
| 插入换行 | `enter` | `editor::Newline` |
| Git：执行 Commit | `ctrl-enter` | `git::Commit` |
| Git：执行 Amend | `ctrl-shift-enter` | `git::Amend` |
| Git：执行 Generate Commit Message | `alt-l` | `git::GenerateCommitMessage` |

## `GitDiff > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`75`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Git：执行 Commit | `ctrl-enter` | `git::Commit` |
| Git：执行 Amend | `ctrl-shift-enter` | `git::Amend` |
| Git：暂存All | `ctrl-space` | `git::StageAll` |
| Git：取消暂存All | `ctrl-shift-space` | `git::UnstageAll` |
| Git：执行 Restore And Next | `ctrl-k ctrl-r` | `git::RestoreAndNext` |

## `CommitEditor > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`77`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Git 面板：聚焦Changes | `escape` | `git_panel::FocusChanges` |
| Git 面板：聚焦Changes | `tab` | `git_panel::FocusChanges` |
| Git 面板：聚焦Changes | `shift-tab` | `git_panel::FocusChanges` |
| 插入换行 | `enter` | `editor::Newline` |
| Git：执行 Commit | `ctrl-enter` | `git::Commit` |
| Git：执行 Amend | `ctrl-shift-enter` | `git::Amend` |
| Git 面板：聚焦Changes | `alt-up` | `git_panel::FocusChanges` |
| Git：执行 Generate Commit Message | `alt-l` | `git::GenerateCommitMessage` |
| Git：展开Commit Editor | `shift-escape` | `git::ExpandCommitEditor` |
| Git：切换Fill Commit Editor | `alt-shift-escape` | `git::ToggleFillCommitEditor` |

## `BreakpointList`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`80`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 调试器：切换Enable Breakpoint | `space` | `debugger::ToggleEnableBreakpoint` |
| 调试器：执行 Unset Breakpoint | `backspace` | `debugger::UnsetBreakpoint` |
| 调试器：执行 Previous Breakpoint Property | `left` | `debugger::PreviousBreakpointProperty` |
| 调试器：执行 Next Breakpoint Property | `right` | `debugger::NextBreakpointProperty` |

## `AgentPanel > Terminal`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`93`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 新建 Agent 对话线程 | `ctrl-n` | `agent::NewThread` |

## `Terminal && selection`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`94`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 执行终端相关操作 | `ctrl-c` | `terminal::Copy` |

## `DebugConsole > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`100`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 确认当前菜单/列表选择 | `enter` | `menu::Confirm` |
| console：执行 Watch Expression | `alt-enter` | `console::WatchExpression` |

## `StashDiff > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`111`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Git：执行 Apply Current Stash | `ctrl-space` | `git::ApplyCurrentStash` |
| Git：执行 Pop Current Stash | `ctrl-shift-space` | `git::PopCurrentStash` |
| Git：执行 Drop Current Stash | `ctrl-shift-backspace` | `git::DropCurrentStash` |

## `RunModal`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`116`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| new process modal：执行 Activate Task Tab | `alt-1` | `new_process_modal::ActivateTaskTab` |
| new process modal：执行 Activate Debug Tab | `alt-2` | `new_process_modal::ActivateDebugTab` |
| new process modal：执行 Activate Attach Tab | `alt-3` | `new_process_modal::ActivateAttachTab` |
| new process modal：执行 Activate Launch Tab | `alt-4` | `new_process_modal::ActivateLaunchTab` |

## `GitGraph`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`122`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| git graph：聚焦Next Tab Stop | `tab` | `git_graph::FocusNextTabStop` |
| git graph：聚焦Previous Tab Stop | `shift-tab` | `git_graph::FocusPreviousTabStop` |
