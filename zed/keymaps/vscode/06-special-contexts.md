# VS Code 默认布局：其它特殊上下文

包含未归入前面模块的特殊 UI、扩展、Notebook、任务、协作或功能上下文。仍然全部来自 Windows 默认 keymap 源文件。


## `Editor && extension == md`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`40`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Markdown：打开Preview To The Side | `ctrl-k v` | `markdown::OpenPreviewToTheSide` |
| Markdown：打开Preview | `ctrl-shift-v` | `markdown::OpenPreview` |

## `Editor && extension == svg`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`41`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| svg：打开Preview To The Side | `ctrl-k v` | `svg::OpenPreviewToTheSide` |
| svg：打开Preview | `ctrl-shift-v` | `svg::OpenPreview` |

## `Editor && renaming`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`52`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：执行 Confirm Rename | `enter` | `editor::ConfirmRename` |

## `Editor && showing_completions`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`53`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：执行 Confirm Completion | `enter` | `editor::ConfirmCompletion` |
| 编辑器：执行 Confirm Completion Replace | `shift-enter` | `editor::ConfirmCompletionReplace` |
| 编辑器：执行 Compose Completion | `tab` | `editor::ComposeCompletion` |

## `Editor && in_snippet && has_next_tabstop && !showing_completions`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`54`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：执行 Next Snippet Tabstop | `tab` | `editor::NextSnippetTabstop` |

## `Editor && in_snippet && has_previous_tabstop && !showing_completions`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`55`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：执行 Previous Snippet Tabstop | `shift-tab` | `editor::PreviousSnippetTabstop` |

## `Editor && showing_code_actions`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`58`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：执行 Confirm Code Action | `enter` | `editor::ConfirmCodeAction` |

## `Editor && (showing_code_actions || showing_completions)`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`59`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：执行 Context Menu Previous | `ctrl-p` | `editor::ContextMenuPrevious` |
| 编辑器：执行 Context Menu Previous | `up` | `editor::ContextMenuPrevious` |
| 编辑器：执行 Context Menu Next | `ctrl-n` | `editor::ContextMenuNext` |
| 编辑器：执行 Context Menu Next | `down` | `editor::ContextMenuNext` |
| 编辑器：执行 Context Menu First | `pageup` | `editor::ContextMenuFirst` |
| 编辑器：执行 Context Menu Last | `pagedown` | `editor::ContextMenuLast` |

## `Editor && showing_signature_help && !showing_completions`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`60`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 编辑器：执行 Signature Help Previous | `up` | `editor::SignatureHelpPrevious` |
| 编辑器：执行 Signature Help Next | `down` | `editor::SignatureHelpNext` |

## `Prompt`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`65`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 选择菜单/列表中的上一项 | `left` | `menu::SelectPrevious` |
| 选择菜单/列表中的下一项 | `right` | `menu::SelectNext` |
| 选择菜单/列表中的上一项 | `h` | `menu::SelectPrevious` |
| 选择菜单/列表中的下一项 | `l` | `menu::SelectNext` |

## `AskPass > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`76`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 确认当前菜单/列表选择 | `enter` | `menu::Confirm` |

## `VariableList`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`79`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| variable list：折叠Selected Entry | `left` | `variable_list::CollapseSelectedEntry` |
| variable list：展开Selected Entry | `right` | `variable_list::ExpandSelectedEntry` |
| variable list：执行 Edit Variable | `enter` | `variable_list::EditVariable` |
| variable list：复制Variable Value | `ctrl-c` | `variable_list::CopyVariableValue` |
| variable list：复制Variable Name | `ctrl-alt-c` | `variable_list::CopyVariableName` |
| variable list：移除Watch | `delete` | `variable_list::RemoveWatch` |
| variable list：移除Watch | `backspace` | `variable_list::RemoveWatch` |
| variable list：添加Watch | `alt-enter` | `variable_list::AddWatch` |

## `ToolchainSelector`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`87`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| toolchain：添加Toolchain | `ctrl-shift-a` | `toolchain::AddToolchain` |

## `ZedPredictModal`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`95`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |

## `ConfigureContextServerModal > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`96`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |
| 插入换行 | `enter` | `editor::Newline` |
| 确认当前菜单/列表选择 | `ctrl-enter` | `menu::Confirm` |

## `ContextServerToolsModal`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`97`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |

## `OnboardingAiConfigurationModal`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`98`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |

## `Diagnostics`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`99`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| diagnostics：切换Diagnostics Refresh | `ctrl-r` | `diagnostics::ToggleDiagnosticsRefresh` |

## `KeystrokeInput`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`104`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| keystroke input：开始Recording | `enter` | `keystroke_input::StartRecording` |
| keystroke input：停止Recording | `escape escape escape` | `keystroke_input::StopRecording` |
| keystroke input：执行 Clear Keystrokes | `delete` | `keystroke_input::ClearKeystrokes` |

## `KeybindEditorModal`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`105`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 确认当前菜单/列表选择 | `ctrl-enter` | `menu::Confirm` |
| 取消菜单/关闭当前弹出层 | `escape` | `menu::Cancel` |

## `KeybindEditorModal > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`106`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 选择菜单/列表中的上一项 | `up` | `menu::SelectPrevious` |
| 选择菜单/列表中的下一项 | `down` | `menu::SelectNext` |

## `Onboarding`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`107`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| Zed：执行 Increase Ui Font Size | `ctrl-=` | `zed::IncreaseUiFontSize`; 参数 `[{"persist":false}]` |
| Zed：执行 Increase Ui Font Size | `ctrl-+` | `zed::IncreaseUiFontSize`; 参数 `[{"persist":false}]` |
| Zed：执行 Decrease Ui Font Size | `ctrl--` | `zed::DecreaseUiFontSize`; 参数 `[{"persist":false}]` |
| Zed：执行 Reset Ui Font Size | `ctrl-0` | `zed::ResetUiFontSize`; 参数 `[{"persist":false}]` |
| onboarding：执行 Finish | `ctrl-enter` | `onboarding::Finish` |
| onboarding：执行 Sign In | `alt-shift-l` | `onboarding::SignIn` |
| onboarding：打开Account | `shift-alt-a` | `onboarding::OpenAccount` |

## `!SettingsWindow`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`109`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 打开设置界面 | `ctrl-,` | `zed::OpenSettings` |

## `SettingsWindow > NavigationMenu`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`112`；`use_key_equivalents`: `true`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| settings editor：聚焦Previous Nav Entry | `up` | `settings_editor::FocusPreviousNavEntry` |
| settings editor：聚焦Previous Nav Entry | `shift-tab` | `settings_editor::FocusPreviousNavEntry` |
| settings editor：聚焦Next Nav Entry | `down` | `settings_editor::FocusNextNavEntry` |
| settings editor：聚焦Next Nav Entry | `tab` | `settings_editor::FocusNextNavEntry` |
| settings editor：展开Nav Entry | `right` | `settings_editor::ExpandNavEntry` |
| settings editor：折叠Nav Entry | `left` | `settings_editor::CollapseNavEntry` |
| settings editor：聚焦Previous Root Nav Entry | `pageup` | `settings_editor::FocusPreviousRootNavEntry` |
| settings editor：聚焦Next Root Nav Entry | `pagedown` | `settings_editor::FocusNextRootNavEntry` |
| settings editor：聚焦First Nav Entry | `home` | `settings_editor::FocusFirstNavEntry` |
| settings editor：聚焦Last Nav Entry | `end` | `settings_editor::FocusLastNavEntry` |

## `EditPredictionContext > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`113`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| dev：执行 Edit Prediction Context Go Back | `alt-left` | `dev::EditPredictionContextGoBack` |
| dev：执行 Edit Prediction Context Go Forward | `alt-right` | `dev::EditPredictionContextGoForward` |

## `ImageViewer`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`115`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| image viewer：执行 Zoom In | `ctrl-=` | `image_viewer::ZoomIn` |
| image viewer：执行 Zoom In | `ctrl-+` | `image_viewer::ZoomIn` |
| image viewer：执行 Zoom Out | `ctrl--` | `image_viewer::ZoomOut` |
| image viewer：执行 Reset Zoom | `ctrl-0` | `image_viewer::ResetZoom` |
| image viewer：执行 Zoom To Actual Size | `ctrl-1` | `image_viewer::ZoomToActualSize` |
| 编辑器：执行 Reveal In File Manager | `ctrl-k r` | `editor::RevealInFileManager` |
| image viewer：执行 Fit To View | `ctrl-shift-0` | `image_viewer::FitToView` |

## `NotebookEditor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`119`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| notebook：运行And Advance | `shift-enter` | `notebook::RunAndAdvance` |
| notebook：运行操作 | `ctrl-enter` | `notebook::Run` |
| notebook：运行All | `ctrl-shift-enter` | `notebook::RunAll` |
| notebook：移动Cell Up | `alt-up` | `notebook::MoveCellUp` |
| notebook：移动Cell Down | `alt-down` | `notebook::MoveCellDown` |
| notebook：添加Code Block | `ctrl-m` | `notebook::AddCodeBlock` |
| notebook：添加Markdown Block | `ctrl-shift-m` | `notebook::AddMarkdownBlock` |
| notebook：重启Kernel | `ctrl-shift-r` | `notebook::RestartKernel` |
| notebook：执行 Interrupt Kernel | `ctrl-c` | `notebook::InterruptKernel` |

## `NotebookEditor && notebook_mode == command`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`120`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| notebook：执行 Enter Edit Mode | `enter` | `notebook::EnterEditMode` |
| 选择菜单/列表中的下一项 | `down` | `menu::SelectNext` |
| 选择菜单/列表中的上一项 | `up` | `menu::SelectPrevious` |

## `NotebookEditor > Editor`

- 源文件：`assets/keymaps/default-windows.json`
- Section：`121`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 插入换行 | `enter` | `editor::Newline` |
| notebook：运行And Advance | `shift-enter` | `notebook::RunAndAdvance` |
| notebook：运行操作 | `ctrl-enter` | `notebook::Run` |
| notebook：运行All | `ctrl-shift-enter` | `notebook::RunAll` |
| notebook：移动Cell Up | `alt-up` | `notebook::MoveCellUp` |
| notebook：移动Cell Down | `alt-down` | `notebook::MoveCellDown` |
| notebook：添加Code Block | `ctrl-m` | `notebook::AddCodeBlock` |
| notebook：添加Markdown Block | `ctrl-shift-m` | `notebook::AddMarkdownBlock` |
| notebook：重启Kernel | `ctrl-shift-r` | `notebook::RestartKernel` |
| notebook：执行 Enter Command Mode | `escape` | `notebook::EnterCommandMode` |

