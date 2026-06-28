# VS Code 默认布局：specific overrides 高优先级覆盖

这些绑定来自 `specific-overrides.json`。源码注释说明它在默认/base/vim 之后、用户 keymap 之前加载，因此在内置绑定中优先级最高。


## `Picker > Editor`

- 源文件：`assets/keymaps/specific-overrides.json`
- Section：`1`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 打开或关闭 Picker 操作菜单 | `ctrl-shift-a` | `picker::ToggleActionsMenu` |

## `(Picker && with_preview) > Editor`

- 源文件：`assets/keymaps/specific-overrides.json`
- Section：`2`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 切换 Picker 预览区域 | `ctrl-alt-p` | `picker::TogglePreview` |
| 将 Picker 预览放到右侧 | `ctrl-alt-right` | `picker::SetPreviewRight` |
| 将 Picker 预览放到底部 | `ctrl-alt-down` | `picker::SetPreviewBelow` |
| 隐藏 Picker 预览 | `ctrl-alt-up` | `picker::SetPreviewHidden` |

## `FileFinder || (FileFinder > Picker > Editor) || (FileFinder > Picker > menu)`

- 源文件：`assets/keymaps/specific-overrides.json`
- Section：`3`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 文件查找中选择上一个结果 | `ctrl-shift-p` | `file_finder::SelectPrevious` |
| 向下拆分窗格 | `ctrl-j` | `pane::SplitDown` |
| 向上拆分窗格 | `ctrl-k` | `pane::SplitUp` |
| 向左拆分窗格 | `ctrl-h` | `pane::SplitLeft` |
| 向右拆分窗格 | `ctrl-l` | `pane::SplitRight` |

## `TextFinder || (TextFinder > Picker > Editor) || (TextFinder > Picker > menu)`

- 源文件：`assets/keymaps/specific-overrides.json`
- Section：`4`

| 功能说明 | 快捷键 / key sequence | Action / 参数 |
|---|---|---|
| 从文本查找切换到项目搜索 | `ctrl-alt-f` | `text_finder::ToProjectSearch` |
| 向下拆分窗格 | `ctrl-j` | `pane::SplitDown` |
| 向上拆分窗格 | `ctrl-k` | `pane::SplitUp` |
| 向左拆分窗格 | `ctrl-h` | `pane::SplitLeft` |
| 向右拆分窗格 | `ctrl-l` | `pane::SplitRight` |

