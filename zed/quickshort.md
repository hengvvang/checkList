### 一、全局与工作区基础操作
- 打开命令面板：`Ctrl+Shift+P` → `command_palette::Toggle`
- 快速搜索并打开文件：`Ctrl+P` → `file_finder::Toggle`
- 打开图形化设置界面：`Ctrl+,` → `zed::OpenSettings`
- 打开设置 JSON 配置文件：`Ctrl+Alt+,` → `zed::OpenSettingsFile`
- 打开快捷键配置文件：`Ctrl+K Ctrl+S` → `zed::OpenKeymap`
- 新建编辑器窗口：`Ctrl+Shift+N` → `workspace::NewWindow`
- 关闭当前窗口：`Ctrl+Shift+W` → `workspace::CloseWindow`
- 新建空白文件：`Ctrl+N` → `workspace::NewFile`
- 保存当前文件：`Ctrl+S` → `workspace::Save`
- 文件另存为：`Ctrl+Shift+S` → `workspace::SaveAs`
- 保存所有已打开文件：`Ctrl+Alt+S` → `workspace::SaveAll`
- 关闭当前标签页：`Ctrl+W` → `pane::CloseActiveItem`
- 恢复最近关闭的标签页：`Ctrl+Shift+T` → `pane::ReopenClosedItem`
- 切换到下一个标签页：`Ctrl+Tab` → `pane::ActivateNextItem`
- 切换到上一个标签页：`Ctrl+Shift+Tab` → `pane::ActivatePrevItem`
- 快速跳转到第 1-9 个标签页：`Alt+1~9` → `pane::ActivateItem1` ~ `pane::ActivateItem9`
- 切换全屏显示：`F11` → `workspace::ToggleFullscreen`
- 退出 Zed 程序：`Ctrl+Q` → `workspace::Quit`
- 打开主题选择器：`Ctrl+K Ctrl+T` → `theme_selector::Toggle`
- 打开当前文件语言模式选择器：`Ctrl+K M` → `language_selector::Toggle`
- 切换基础键位方案：无默认快捷键 → `zed::ToggleBaseKeymapSelector`
- 切换禅模式（隐藏所有面板，专注编辑）：无默认快捷键 → `workspace::ToggleZenMode`

### 二、编辑器基础编辑
- 复制选中内容（无选中则复制整行）：`Ctrl+C` → `editor::Copy`
- 剪切选中内容（无选中则剪切整行）：`Ctrl+X` → `editor::Cut`
- 粘贴剪贴板内容：`Ctrl+V` → `editor::Paste`
- 全选文档内容：`Ctrl+A` → `editor::SelectAll`
- 撤销上一步操作：`Ctrl+Z` → `editor::Undo`
- 重做撤销的操作：`Ctrl+Y` → `editor::Redo`
- 删除当前整行：`Ctrl+Shift+K` → `editor::DeleteLine`
- 向下复制当前行：`Alt+Shift+↓` → `editor::DuplicateLineDown`
- 向上复制当前行：`Alt+Shift+↑` → `editor::DuplicateLineUp`
- 向下移动当前行：`Alt+↓` → `editor::MoveLineDown`
- 向上移动当前行：`Alt+↑` → `editor::MoveLineUp`
- 在当前行下方插入新行：`Ctrl+Enter` → `editor::NewlineBelow`
- 在当前行上方插入新行：`Ctrl+Shift+Enter` → `editor::NewlineAbove`
- 增加行缩进：`Ctrl+]` → `editor::Indent`
- 减少行缩进：`Ctrl+[` → `editor::Outdent`
- 切换行注释：`Ctrl+/` → `editor::ToggleComments`
- 切换块注释：`Alt+Shift+A` → `editor::ToggleBlockComments`
- 剪切光标位置到行尾的内容：`Ctrl+K` → `editor::CutToEndOfLine`
- 格式化当前文档：`Alt+Shift+F` → `editor::Format`
- 自动整理导入语句：`Alt+Shift+O` → `editor::OrganizeImports`
- 触发代码补全弹窗：`Ctrl+Space` → `editor::ToggleCompletions`

### 三、光标与多选操作
- 移动光标到行首：`Home` → `editor::MoveToBeginningOfLine`
- 移动光标到行尾：`End` → `editor::MoveToEndOfLine`
- 移动光标到文档开头：`Ctrl+Home` → `editor::MoveToBeginning`
- 移动光标到文档结尾：`Ctrl+End` → `editor::MoveToEnd`
- 按单词向右移动光标：`Ctrl+→` → `editor::MoveToNextWordEnd`
- 按单词向左移动光标：`Ctrl+←` → `editor::MoveToPreviousWordStart`
- 向下翻一页：`PageDown` → `editor::PageDown`
- 向上翻一页：`PageUp` → `editor::PageUp`
- 选中下一个相同内容并创建多光标：`Ctrl+D` → `editor::SelectNext`
- 选中所有匹配内容并创建多光标：`Ctrl+Shift+L` → `editor::SelectAllMatches`
- 在上方一行添加多光标：`Alt+Shift+↑` → `editor::AddCursorAbove`
- 在下方一行添加多光标：`Alt+Shift+↓` → `editor::AddCursorBelow`
- 扩大语法节点选择范围：`Ctrl+Shift+→` → `editor::SelectLargerSyntaxNode`
- 缩小语法节点选择范围：`Ctrl+Shift+←` → `editor::SelectSmallerSyntaxNode`
- 选中括号/分隔符内的全部内容：`Ctrl+Shift+Space` → `editor::SelectInsideDelimiters`

### 四、代码智能与导航（LSP 功能）
- 跳转到符号定义：`F12` → `editor::GoToDefinition`
- 分屏打开符号定义：`Ctrl+K F12` → `editor::GoToDefinitionSplit`
- 查找所有引用位置：`Shift+F12` → `editor::FindAllReferences`
- 跳转到接口/方法实现：`Ctrl+F12` → `editor::GoToImplementation`
- 跳转到类型定义：`Ctrl+Shift+F12` → `editor::GoToTypeDefinition`
- 重命名符号：`F2` → `editor::Rename`
- 打开代码操作/快速修复菜单：`Ctrl+.` → `editor::ToggleCodeActions`
- 显示当前符号悬停提示：`Ctrl+K Ctrl+I` → `editor::Hover`
- 跳转到指定行号：`Ctrl+G` → `editor::GoToLine`
- 当前文件内符号跳转（大纲视图）：`Ctrl+Shift+O` → `outline_view::Toggle`
- 整个项目内全局符号跳转：`Ctrl+T` → `project_symbols::Toggle`
- 跳转到下一个诊断错误：`F8` → `editor::GoToNextDiagnostic`
- 跳转到上一个诊断错误：`Shift+F8` → `editor::GoToPreviousDiagnostic`
- 跳转到下一处 Git 代码变更：`Ctrl+Shift+]` → `editor::GoToNextChange`
- 跳转到上一处 Git 代码变更：`Ctrl+Shift+[` → `editor::GoToPreviousChange`
- 重启当前文件的语言服务器：无默认快捷键 → `editor::RestartLanguageServer`

### 五、搜索与替换
- 当前文件内文本搜索：`Ctrl+F` → `buffer_search::Deploy`
- 当前文件内文本替换：`Ctrl+H` → `buffer_search::DeployReplace`
- 项目内全局文本搜索：`Ctrl+Shift+F` → `project_search::Deploy`
- 项目内全局文本替换：`Ctrl+Shift+H` → `project_search::DeployReplace`
- 跳转到下一个匹配项（搜索框激活时）：`Enter` → `buffer_search::NextMatch`
- 跳转到上一个匹配项（搜索框激活时）：`Shift+Enter` → `buffer_search::PreviousMatch`

### 六、侧边栏与面板操作
- 切换项目文件侧边栏显隐：`Ctrl+B` → `project_panel::ToggleFocus`
- 聚焦并激活项目文件侧边栏：`Ctrl+Shift+E` → `project_panel::ToggleFocus`
- 切换底部终端面板显隐：`Ctrl+`` → `terminal_panel::Toggle`
- 新建终端实例：`Ctrl+Shift+`` → `workspace::NewTerminal`
- 切换诊断/问题面板显隐：`Ctrl+Shift+M` → `diagnostics_panel::Toggle`
- 切换底部停靠面板整体显隐：`Ctrl+J` → `workspace::ToggleBottomDock`
- 切换 AI 助手面板：`Ctrl+?` → `agent_panel::ToggleFocus`
- 切换 Git 版本控制面板：`Ctrl+Shift+G` → `git_panel::ToggleFocus`
- 切换扩展市场面板：`Ctrl+Shift+X` → `extensions_panel::ToggleFocus`

### 七、分屏与窗格操作
- 垂直向右拆分窗格：`Ctrl+\` → `pane::SplitRight`
- 水平向下拆分窗格：`Ctrl+K Ctrl+\` → `pane::SplitDown`
- 关闭当前分屏窗格：`Ctrl+W` → `pane::ClosePane`
- 聚焦左侧窗格：`Ctrl+K ←` → `workspace::ActivatePaneLeft`
- 聚焦右侧窗格：`Ctrl+K →` → `workspace::ActivatePaneRight`
- 聚焦上方窗格：`Ctrl+K ↑` → `workspace::ActivatePaneUp`
- 聚焦下方窗格：`Ctrl+K ↓` → `workspace::ActivatePaneDown`

### 八、代码折叠
- 折叠当前代码块：`Ctrl+Shift+[` → `editor::Fold`
- 展开当前代码块：`Ctrl+Shift+]` → `editor::Unfold`
- 折叠所有代码块：`Ctrl+K Ctrl+0` → `editor::FoldAll`
- 展开所有代码块：`Ctrl+K Ctrl+J` → `editor::UnfoldAll`
- 递归折叠当前块及所有子块：`Ctrl+K Ctrl+[` → `editor::FoldRecursively`
- 递归展开当前块及所有子块：`Ctrl+K Ctrl+]` → `editor::UnfoldRecursively`

### 九、调试功能
- 开始/继续调试：`F5` → `debugger::Resume`
- 停止调试：`Shift+F5` → `debugger::Stop`
- 单步跳过（不进入函数内部）：`F7` → `debugger::StepOver`
- 单步进入函数内部：`Ctrl+F11` → `debugger::StepInto`
- 单步退出当前函数：`Shift+F11` → `debugger::StepOut`
- 切换当前行断点：`F9` → `editor::ToggleBreakpoint`

### 十、Git 版本控制
- 打开代码提交界面：`Ctrl+G C` → `git::Commit`
- 推送到远程仓库：`Ctrl+G P` → `git::Push`
- 从远程仓库拉取更新：`Ctrl+G U` → `git::Pull`
- 以变基方式拉取更新：`Ctrl+G Shift+↓` → `git::PullRebase`
- 强制推送到远程仓库：`Ctrl+G Shift+↑` → `git::ForcePush`
- 切换行内 Git 责备信息：无默认快捷键 → `editor::ToggleInlineBlame`

### 十一、无默认快捷键的常用命令（仅命令面板调用）
以下命令无出厂绑定，可在命令面板中搜索执行，也可自行添加到快捷键配置：
- 文本大小写转换：`editor::ConvertToUpperCase`（转大写）、`editor::ConvertToLowerCase`（转小写）、`editor::ConvertToOppositeCase`（大小写反转）
- 命名风格转换：`editor::ConvertToSnakeCase`（蛇形命名）、`editor::ConvertToKebabCase`（短横线命名）、`editor::ConvertToUpperCamelCase`（大驼峰）、`editor::ConvertToLowerCamelCase`（小驼峰）
- 编解码工具：`editor::ConvertToBase64`（Base64 编码）、`editor::ConvertFromBase64`（Base64 解码）
- 插入工具：`editor::InsertUuidV4`（插入 UUID v4）、`editor::InsertUuidV7`（插入 UUID v7）
- 行操作：`editor::ReverseLines`（反转行顺序）、`editor::ShuffleLines`（随机打乱行）、`editor::JoinLines`（合并选中行）
- 文件操作：`editor::ReloadFile`（重载当前文件）、`editor::RevealInFileManager`（在资源管理器中显示）
- 界面缩放：`workspace::IncreaseZoom`（放大）、`workspace::DecreaseZoom`（缩小）、`workspace::ResetZoom`（重置缩放）
