以下是 Zed 编辑器 Windows 平台**默认 VS Code 键位方案**中，所有需要分步触发的**序列快捷键（Chord）**，均来自官方 `default-windows.json` 键位定义，格式统一为「前缀组合 + 后续按键」，操作方式为：先按下前缀组合并松开，再按下后续按键；若后续按键仍带 Ctrl，可保持 Ctrl 不松开直接按。

---

### 一、Ctrl+K 前缀（最核心的通用序列组）
这是 Zed 中数量最多的序列前缀，覆盖界面、编辑、分屏、折叠等全场景。

#### 全局与工作区
| 快捷键 | 对应命令 | 功能说明 |
|--------|----------|----------|
| `Ctrl+K Ctrl+S` | `zed::OpenKeymap` | 打开快捷键配置文件 |
| `Ctrl+K Ctrl+T` | `theme_selector::Toggle` | 打开主题选择器 |
| `Ctrl+K Ctrl+Shift+T` | `theme::ToggleMode` | 一键切换明暗主题模式 |
| `Ctrl+K Ctrl+O` | `workspace::Open` | 打开文件/文件夹对话框 |
| `Ctrl+K Ctrl+Shift+S` | `workspace::SaveWithoutFormat` | 保存当前文件但跳过自动格式化 |
| `Ctrl+K S` | `workspace::SaveAll` | 保存所有已打开的文件 |
| `Ctrl+K M` | `language_selector::Toggle` | 打开当前文件的语言模式选择器 |
| `Ctrl+K N` | `encoding_selector::Toggle` | 打开文件编码选择器 |
| `Ctrl+K Ctrl+W` | `workspace::CloseAllItemsAndPanes` | 关闭所有标签页与分屏窗格 |
| `Ctrl+K W` | `pane::CloseAllItems` | 关闭当前窗格内的所有标签页 |
| `Ctrl+K E` | `pane::CloseItemsToTheLeft` | 关闭当前标签左侧的所有标签 |
| `Ctrl+K T` | `pane::CloseItemsToTheRight` | 关闭当前标签右侧的所有标签 |
| `Ctrl+K U` | `pane::CloseCleanItems` | 批量关闭所有无修改的已保存标签 |
| `Ctrl+K Shift+Enter` | `pane::TogglePinTab` | 固定/取消固定当前标签页 |
| `Ctrl+K R` | `editor::RevealInFileManager` | 在资源管理器中显示当前文件 |
| `Ctrl+K P` | `editor::CopyPath` | 复制当前文件的完整绝对路径 |
| `Ctrl+K Ctrl+Shift+C` | `workspace::CopyRelativePath` | 复制当前文件的项目相对路径 |
| `Ctrl+K Ctrl+Shift+F` | `project_panel::NewSearchInDirectory` | 在选中目录内开启全局搜索 |

#### 分屏与窗格导航
| 快捷键 | 对应命令 | 功能说明 |
|--------|----------|----------|
| `Ctrl+K Ctrl+\` | `pane::SplitDown` | 水平向下拆分窗格 |
| `Ctrl+K Ctrl+←` | `workspace::ActivatePaneLeft` | 聚焦左侧分屏窗格 |
| `Ctrl+K Ctrl+→` | `workspace::ActivatePaneRight` | 聚焦右侧分屏窗格 |
| `Ctrl+K Ctrl+↑` | `workspace::ActivatePaneUp` | 聚焦上方分屏窗格 |
| `Ctrl+K Ctrl+↓` | `workspace::ActivatePaneDown` | 聚焦下方分屏窗格 |
| `Ctrl+K Shift+←` | `workspace::SwapPaneLeft` | 与左侧窗格交换位置 |
| `Ctrl+K Shift+→` | `workspace::SwapPaneRight` | 与右侧窗格交换位置 |
| `Ctrl+K Shift+↑` | `workspace::SwapPaneUp` | 与上方窗格交换位置 |
| `Ctrl+K Shift+↓` | `workspace::SwapPaneDown` | 与下方窗格交换位置 |
| `Ctrl+K ↑` | `pane::SplitUp` | 向上拆分窗格（Atom 风格） |
| `Ctrl+K ↓` | `pane::SplitDown` | 向下拆分窗格 |
| `Ctrl+K ←` | `pane::SplitLeft` | 向左拆分窗格 |
| `Ctrl+K →` | `pane::SplitRight` | 向右拆分窗格 |

#### 编辑器编辑与代码智能
| 快捷键 | 对应命令 | 功能说明 |
|--------|----------|----------|
| `Ctrl+K Ctrl+D` | `editor::SelectNext` | 跳过当前匹配项，选中下一个相同内容 |
| `Ctrl+K Ctrl+I` | `editor::Hover` | 显示当前符号的悬停提示文档 |
| `Ctrl+K Ctrl+B` | `editor::BlameHover` | 悬停显示当前行的 Git 提交信息 |
| `Ctrl+K Ctrl+F` | `editor::FormatSelections` | 仅格式化选中的代码片段 |
| `Ctrl+K Ctrl+C` | `editor::ToggleComments` | 切换行注释 |
| `Ctrl+K Ctrl+/` | `editor::ToggleBlockComments` | 切换块注释 |
| `Ctrl+K Ctrl+Q` / `Ctrl+K Q` | `editor::Rewrap` | 按换行宽度自动重排文本 |
| `Ctrl+K Ctrl+Z` / `Ctrl+K Z` | `editor::ToggleSoftWrap` | 切换编辑器软换行 |
| `Ctrl+K Ctrl+R` | `git::Restore` | 恢复当前行的 Git 变更 |

#### 代码折叠
| 快捷键 | 对应命令 | 功能说明 |
|--------|----------|----------|
| `Ctrl+K Ctrl+L` | `editor::ToggleFold` | 切换当前代码块的折叠状态 |
| `Ctrl+K Ctrl+[` | `editor::FoldRecursive` | 递归折叠当前块及所有子代码块 |
| `Ctrl+K Ctrl+]` | `editor::UnfoldRecursive` | 递归展开当前块及所有子代码块 |
| `Ctrl+K Ctrl+0` | `editor::FoldAll` | 折叠文档内所有代码块 |
| `Ctrl+K Ctrl+J` | `editor::UnfoldAll` | 展开文档内所有代码块 |
| `Ctrl+K Ctrl+1` ~ `Ctrl+K Ctrl+9` | `editor::FoldAtLevel_1` ~ `FoldAtLevel_9` | 按指定层级折叠代码 |

#### 特定文件预览
| 快捷键 | 对应命令 | 功能说明 |
|--------|----------|----------|
| `Ctrl+K V` | `markdown::OpenPreviewToTheSide` / `svg::OpenPreviewToTheSide` | Markdown / SVG 文件在侧边打开预览<br>（你提到的 `Ctrl+W V` 是记忆偏差，实际为 `Ctrl+K V`） |

---

### 二、Ctrl+G 前缀（Git 面板内生效）
仅在 Git 面板聚焦时可用，用于快速执行版本控制操作。
| 快捷键 | 对应命令 | 功能说明 |
|--------|----------|----------|
| `Ctrl+G Ctrl+G` | `git::Fetch` | 从远程仓库拉取更新（Fetch） |
| `Ctrl+G ↑` | `git::Push` | 推送到远程仓库 |
| `Ctrl+G ↓` | `git::Pull` | 从远程拉取并合并 |
| `Ctrl+G Shift+↓` | `git::PullRebase` | 以变基方式拉取更新 |
| `Ctrl+G Shift+↑` | `git::ForcePush` | 强制推送到远程仓库 |
| `Ctrl+G D` | `git::Diff` | 查看文件差异 |
| `Ctrl+G Backspace` | `git::RestoreTrackedFiles` | 恢复已跟踪文件的全部变更 |
| `Ctrl+G Shift+Backspace` | `git::TrashUntrackedFiles` | 删除所有未跟踪的文件 |

---

### 三、Alt+G 前缀（编辑器内 Git 快捷操作）
在编辑器普通编辑状态下即可触发，无需切换到 Git 面板。
| 快捷键 | 对应命令 | 功能说明 |
|--------|----------|----------|
| `Alt+G B` | `git::Blame` | 打开当前文件的 Git 责备视图 |
| `Alt+G M` | `git::OpenModifiedFiles` | 一键打开所有已修改的文件 |
| `Alt+G R` | `git::ReviewDiff` | 审查当前文件的 Git 变更差异 |

---

### 四、其他零散序列快捷键
| 快捷键 | 对应命令 | 功能说明 |
|--------|----------|----------|
| `Ctrl+M Ctrl+M` | `toolchain::AddToolchain` | 连续两次 Ctrl+M，添加开发工具链 |
| `Escape Escape Escape` | `keystroke_input::StopRecording` | 快捷键录制模式下，连续三次 Esc 停止录制 |
