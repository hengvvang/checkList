from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZED = ROOT / "zed"
KEYMAPS = ZED / "keymaps"

ACTION_DESCRIPTIONS: list[tuple[str, str]] = [
    ("menu::SelectFirst", "选择菜单/列表中的第一项"),
    ("menu::SelectLast", "选择菜单/列表中的最后一项"),
    ("menu::SelectNext", "选择菜单/列表中的下一项"),
    ("menu::SelectPrevious", "选择菜单/列表中的上一项"),
    ("menu::Confirm", "确认当前菜单/列表选择"),
    ("menu::SecondaryConfirm", "执行当前选择的次级确认操作"),
    ("menu::Cancel", "取消菜单/关闭当前弹出层"),
    ("menu::Restart", "重启/重新运行当前菜单流程"),
    ("menu::SelectChild", "进入子菜单或展开当前项"),
    ("menu::SelectParent", "返回父菜单或收起当前项"),
    ("picker::ConfirmInput", "确认 Picker 输入内容"),
    ("picker::ToggleActionsMenu", "打开或关闭 Picker 操作菜单"),
    ("picker::TogglePreview", "切换 Picker 预览区域"),
    ("picker::SetPreviewRight", "将 Picker 预览放到右侧"),
    ("picker::SetPreviewBelow", "将 Picker 预览放到底部"),
    ("picker::SetPreviewHidden", "隐藏 Picker 预览"),
    ("workspace::CloseWindow", "关闭当前窗口"),
    ("workspace::ToggleZoom", "切换工作区缩放/聚焦显示"),
    ("workspace::OpenFiles", "打开文件"),
    ("workspace::Open", "打开项目/文件入口"),
    ("workspace::NewWindow", "新建窗口"),
    ("workspace::NewFile", "新建文件"),
    ("workspace::NewTerminal", "新建终端"),
    ("workspace::SaveAll", "保存所有文件"),
    ("workspace::Save", "保存当前文件"),
    ("workspace::SaveAs", "当前文件另存为"),
    ("workspace::CloseActiveItem", "关闭当前标签/项目"),
    ("workspace::CloseAll", "关闭全部项目"),
    ("workspace::CloseOther", "关闭其它项目"),
    ("workspace::ActivatePaneLeft", "切换焦点到左侧窗格"),
    ("workspace::ActivatePaneRight", "切换焦点到右侧窗格"),
    ("workspace::ActivatePaneUp", "切换焦点到上方窗格"),
    ("workspace::ActivatePaneDown", "切换焦点到下方窗格"),
    ("workspace::Toggle", "切换工作区功能"),
    ("zed::IncreaseBufferFontSize", "增大编辑器字体大小"),
    ("zed::DecreaseBufferFontSize", "减小编辑器字体大小"),
    ("zed::ResetBufferFontSize", "重置编辑器字体大小"),
    ("zed::OpenSettingsFile", "打开设置 JSON 文件"),
    ("zed::OpenSettings", "打开设置界面"),
    ("zed::OpenKeymap", "打开快捷键配置"),
    ("zed::Quit", "退出 Zed"),
    ("zed::ToggleFullScreen", "切换全屏"),
    ("debugger::Start", "开始调试"),
    ("debugger::Stop", "停止调试"),
    ("debugger::RerunSession", "重新运行调试会话"),
    ("debugger::Pause", "暂停调试"),
    ("debugger::StepOver", "调试时单步跳过"),
    ("debugger::StepInto", "调试时单步进入"),
    ("debugger::StepOut", "调试时单步跳出"),
    ("debugger::ToggleBreakpoint", "切换断点"),
    ("edit_prediction::ToggleMenu", "切换编辑预测菜单"),
    ("editor::DisplayCursorNames", "显示协作光标名称"),
    ("editor::Cancel", "取消当前编辑器操作"),
    ("editor::Backspace", "向前删除字符"),
    ("editor::Delete", "向后删除字符"),
    ("editor::Tab", "插入缩进或跳到下一个输入位置"),
    ("editor::Backtab", "反向缩进或跳到上一个输入位置"),
    ("editor::Rewrap", "重新换行/重排当前段落"),
    ("editor::DeleteToPreviousWordStart", "删除到上一个单词开头"),
    ("editor::DeleteToNextWordEnd", "删除到下一个单词结尾"),
    ("editor::Cut", "剪切选区或当前行"),
    ("editor::Copy", "复制选区或当前行"),
    ("editor::Paste", "粘贴剪贴板内容"),
    ("editor::Undo", "撤销上一步编辑"),
    ("editor::Redo", "重做被撤销的编辑"),
    ("editor::MoveUp", "光标上移"),
    ("editor::MoveDown", "光标下移"),
    ("editor::MoveLeft", "光标左移"),
    ("editor::MoveRight", "光标右移"),
    ("editor::LineUp", "向上滚动一行"),
    ("editor::LineDown", "向下滚动一行"),
    ("editor::MovePageUp", "向上翻页移动光标"),
    ("editor::MovePageDown", "向下翻页移动光标"),
    ("editor::PageUp", "向上翻页"),
    ("editor::PageDown", "向下翻页"),
    ("editor::SelectPageUp", "向上翻页并扩展选区"),
    ("editor::SelectPageDown", "向下翻页并扩展选区"),
    ("editor::MoveToBeginningOfLine", "移动到行首"),
    ("editor::MoveToEndOfLine", "移动到行尾"),
    ("editor::MoveToPreviousWordStart", "移动到上一个单词开头"),
    ("editor::MoveToNextWordEnd", "移动到下一个单词结尾"),
    ("editor::MoveToBeginning", "移动到文件开头"),
    ("editor::MoveToEnd", "移动到文件末尾"),
    ("editor::SelectUp", "向上扩展选区"),
    ("editor::SelectDown", "向下扩展选区"),
    ("editor::SelectLeft", "向左扩展选区"),
    ("editor::SelectRight", "向右扩展选区"),
    ("editor::SelectToPreviousWordStart", "扩展选区到上一个单词开头"),
    ("editor::SelectToNextWordEnd", "扩展选区到下一个单词结尾"),
    ("editor::SelectToBeginning", "扩展选区到文件开头"),
    ("editor::SelectToEnd", "扩展选区到文件末尾"),
    ("editor::SelectToBeginningOfLine", "扩展选区到行首"),
    ("editor::SelectToEndOfLine", "扩展选区到行尾"),
    ("editor::SelectAll", "全选当前编辑器内容"),
    ("editor::SelectLine", "选中当前行"),
    ("editor::Format", "格式化代码"),
    ("editor::OrganizeImports", "整理导入语句"),
    ("editor::ShowCharacterPalette", "打开字符选择面板"),
    ("editor::ToggleLineNumbers", "显示/隐藏行号"),
    ("editor::ToggleSelectedDiffHunks", "折叠/展开选中的 diff hunk"),
    ("editor::ExpandAllDiffHunks", "展开所有 diff hunk"),
    ("editor::ShowSignatureHelp", "显示函数签名帮助"),
    ("editor::OpenContextMenu", "打开编辑器上下文菜单"),
    ("editor::ToggleBreakpoint", "切换当前行断点"),
    ("editor::EditLogBreakpoint", "编辑日志断点"),
    ("editor::NewlineBelow", "在下方新建一行"),
    ("editor::NewlineAbove", "在上方新建一行"),
    ("editor::Newline", "插入换行"),
    ("editor::ToggleSoftWrap", "切换自动换行"),
    ("editor::OpenSelectionsInMultibuffer", "在多缓冲区中打开选区"),
    ("editor::ShowCompletions", "显示代码补全"),
    ("editor::ToggleCodeActions", "打开代码操作/快速修复菜单"),
    ("editor::GoToDefinition", "跳转到定义"),
    ("editor::GoToDeclaration", "跳转到声明"),
    ("editor::GoToTypeDefinition", "跳转到类型定义"),
    ("editor::GoToImplementation", "跳转到实现"),
    ("editor::FindAllReferences", "查找所有引用"),
    ("editor::Rename", "重命名符号"),
    ("editor::Hover", "显示悬停信息"),
    ("editor::BlameHover", "显示 Git blame 悬停信息"),
    ("editor::GoToDiagnostic", "跳转到下一个诊断"),
    ("editor::GoToPreviousDiagnostic", "跳转到上一个诊断"),
    ("editor::GoToPreviousChange", "跳转到上一处变更"),
    ("editor::GoToNextChange", "跳转到下一处变更"),
    ("editor::OpenUrl", "打开光标处链接"),
    ("editor::OpenSelectedFilename", "打开选中的文件名"),
    ("editor::SelectNext", "选择下一个匹配项/添加下一个选择"),
    ("editor::SelectPrevious", "选择上一个匹配项/添加上一个选择"),
    ("editor::SelectAllMatches", "选择所有匹配项"),
    ("editor::SelectLargerSyntaxNode", "扩大语法节点选区"),
    ("editor::SelectSmallerSyntaxNode", "缩小语法节点选区"),
    ("editor::OpenExcerpts", "打开当前搜索摘录/引用摘录"),
    ("editor::FoldAll", "折叠所有代码块"),
    ("editor::UnfoldAll", "展开所有代码块"),
    ("editor::ToggleFold", "切换当前代码块折叠"),
    ("editor::Fold", "折叠当前代码块"),
    ("editor::Unfold", "展开当前代码块"),
    ("editor::FoldRecursive", "递归折叠当前代码块"),
    ("editor::UnfoldRecursive", "递归展开当前代码块"),
    ("git::Blame", "打开 Git blame"),
    ("git::OpenModifiedFiles", "打开已修改文件列表"),
    ("git::ReviewDiff", "查看 Git diff"),
    ("git::Restore", "还原 Git 变更"),
    ("git::StageAndNext", "暂存当前变更并跳到下一处"),
    ("git::UnstageAndNext", "取消暂存当前变更并跳到下一处"),
    ("git_panel::ToggleFocus", "切换 Git 面板焦点"),
    ("terminal_panel::Toggle", "显示/隐藏终端面板"),
    ("terminal::", "执行终端相关操作"),
    ("project_panel::ToggleFocus", "切换项目文件面板焦点"),
    ("project_panel::Open", "打开项目面板选中项"),
    ("project_panel::NewFile", "在项目面板中新建文件"),
    ("project_panel::NewDirectory", "在项目面板中新建目录"),
    ("project_panel::Cut", "剪切项目面板选中项"),
    ("project_panel::Copy", "复制项目面板选中项"),
    ("project_panel::Paste", "粘贴到项目面板"),
    ("project_panel::Delete", "删除项目面板选中项"),
    ("project_panel::Rename", "重命名项目面板选中项"),
    ("project_panel::Collapse", "折叠项目面板条目"),
    ("project_panel::Expand", "展开项目面板条目"),
    ("file_finder::Toggle", "打开/关闭文件快速查找"),
    ("file_finder::SelectPrevious", "文件查找中选择上一个结果"),
    ("text_finder::ToProjectSearch", "从文本查找切换到项目搜索"),
    ("buffer_search::DeployReplace", "打开当前文件替换"),
    ("buffer_search::Deploy", "打开当前文件搜索"),
    ("buffer_search::Dismiss", "关闭当前文件搜索"),
    ("search::SelectNextMatch", "跳到下一个搜索结果"),
    ("search::SelectPreviousMatch", "跳到上一个搜索结果"),
    ("search::SelectAllMatches", "选中所有搜索结果"),
    ("search::FocusSearch", "聚焦搜索输入框"),
    ("search::ToggleReplace", "显示/隐藏替换输入框"),
    ("search::ToggleSelection", "切换搜索选区范围"),
    ("project_search::DeployReplace", "打开项目替换"),
    ("project_search::Deploy", "打开项目搜索"),
    ("outline::Toggle", "打开/关闭文件符号大纲"),
    ("project_symbols::Toggle", "打开/关闭项目符号搜索"),
    ("command_palette::Toggle", "打开/关闭命令面板"),
    ("theme_selector::Toggle", "打开主题选择器"),
    ("language_selector::Toggle", "打开语言模式选择器"),
    ("agent::ToggleFocus", "切换 Agent/AI 面板焦点"),
    ("agent_panel::ToggleFocus", "切换 Agent 面板焦点"),
    ("agent::NewThread", "新建 Agent 对话线程"),
    ("agent::KeepAll", "保留所有 Agent 生成的变更"),
    ("agent::RejectAll", "拒绝所有 Agent 生成的变更"),
    ("agent::Keep", "保留 Agent 生成的当前变更"),
    ("agent::Reject", "拒绝 Agent 生成的当前变更"),
    ("agent::OpenAgentDiff", "打开 Agent diff 视图"),
    ("assistant::InlineAssist", "打开行内 AI 助手"),
    ("markdown::CopyAsMarkdown", "按 Markdown 格式复制"),
    ("markdown::Copy", "复制 Markdown 内容"),
    ("pane::SplitRight", "向右拆分窗格"),
    ("pane::SplitLeft", "向左拆分窗格"),
    ("pane::SplitDown", "向下拆分窗格"),
    ("pane::SplitUp", "向上拆分窗格"),
    ("pane::GoBack", "导航后退"),
    ("pane::GoForward", "导航前进"),
    ("pane::DeploySearch", "在窗格中打开搜索"),
    ("pane::GoToOlderTag", "跳转到更早的标签位置"),
    ("lsp_tool::ToggleMenu", "打开/关闭 LSP 工具菜单"),
    ("vim::Left", "Vim：向左移动"),
    ("vim::Right", "Vim：向右移动"),
    ("vim::Up", "Vim：向上移动"),
    ("vim::Down", "Vim：向下移动"),
    ("vim::WrappingLeft", "Vim：向左移动，必要时换到上一行"),
    ("vim::WrappingRight", "Vim：向右移动，必要时换到下一行"),
    ("vim::NextLineStart", "Vim：移动到下一行行首"),
    ("vim::PreviousLineStart", "Vim：移动到上一行行首"),
    ("vim::Tab", "Vim：执行 Tab 跳转/补全导航"),
    ("vim::EndOfLine", "Vim：移动到行尾"),
    ("vim::StartOfLine", "Vim：移动到行首"),
    ("vim::FirstNonWhitespace", "Vim：移动到行首第一个非空字符"),
    ("vim::StartOfLineDownward", "Vim：按行移动并到行首"),
    ("vim::EndOfLineDownward", "Vim：按行移动并到行尾"),
    ("vim::EndOfDocument", "Vim：移动到文档末尾"),
    ("vim::StartOfDocument", "Vim：移动到文档开头"),
    ("vim::StartOfParagraph", "Vim：移动到段落开头"),
    ("vim::EndOfParagraph", "Vim：移动到段落结尾"),
    ("vim::SentenceBackward", "Vim：移动到上一句"),
    ("vim::SentenceForward", "Vim：移动到下一句"),
    ("vim::GoToColumn", "Vim：跳转到指定列"),
    ("vim::NextWordStart", "Vim：移动到下一个单词开头"),
    ("vim::NextWordEnd", "Vim：移动到下一个单词结尾"),
    ("vim::PreviousWordStart", "Vim：移动到上一个单词开头"),
    ("vim::PreviousWordEnd", "Vim：移动到上一个单词结尾"),
    ("vim::Search", "Vim：打开搜索"),
    ("vim::MoveToNextMatch", "Vim：跳到下一个搜索匹配"),
    ("vim::MoveToPreviousMatch", "Vim：跳到上一个搜索匹配"),
    ("vim::MoveToNext", "Vim：跳到下一个匹配/目标"),
    ("vim::MoveToPrevious", "Vim：跳到上一个匹配/目标"),
    ("vim::Matching", "Vim：跳转到匹配的括号/结构"),
    ("vim::PushFindForward", "Vim：输入字符并向前查找"),
    ("vim::PushFindBackward", "Vim：输入字符并向后查找"),
    ("vim::PushMark", "Vim：设置 mark 标记"),
    ("vim::PushJump", "Vim：跳转到 mark 标记"),
    ("vim::RepeatFindReversed", "Vim：反向重复上次字符查找"),
    ("vim::RepeatFind", "Vim：重复上次字符查找"),
    ("vim::SwitchToNormalMode", "Vim：切回普通模式"),
    ("vim::NormalBefore", "Vim：退出插入/可视状态并回到普通模式"),
    ("vim::ToggleVisualLine", "Vim：切换行可视模式"),
    ("vim::ToggleVisualBlock", "Vim：切换块可视模式"),
    ("vim::ToggleVisual", "Vim：切换字符可视模式"),
    ("vim::ToggleReplace", "Vim：切换替换模式"),
    ("vim::ShowLocation", "Vim：显示当前位置"),
    ("vim::PageDown", "Vim：向下翻页"),
    ("vim::PageUp", "Vim：向上翻页"),
    ("vim::ScrollDown", "Vim：向下滚动半屏"),
    ("vim::ScrollUp", "Vim：向上滚动半屏"),
    ("vim::LineDown", "Vim：屏幕向下滚动一行"),
    ("vim::LineUp", "Vim：屏幕向上滚动一行"),
    ("vim::PushReplaceWithRegister", "Vim：准备使用寄存器内容替换"),
    ("vim::SelectNextMatch", "Vim：选择下一个匹配项"),
    ("vim::SelectPreviousMatch", "Vim：选择上一个匹配项"),
    ("vim::SelectNext", "Vim：添加/选择下一个相同文本"),
    ("vim::SelectPrevious", "Vim：添加/选择上一个相同文本"),
    ("vim::RestoreVisualSelection", "Vim：恢复上次可视选区"),
    ("vim::InsertAtPrevious", "Vim：跳到上次插入位置"),
    ("vim::ChangeListNewer", "Vim：跳到更新的变更位置"),
    ("vim::ChangeListOlder", "Vim：跳到更早的变更位置"),
    ("vim::WindowTop", "Vim：移动到窗口顶部"),
    ("vim::WindowMiddle", "Vim：移动到窗口中部"),
    ("vim::WindowBottom", "Vim：移动到窗口底部"),
    ("vim::ScrollCursorCenter", "Vim：将光标行滚动到窗口中央"),
    ("vim::ScrollCursorTop", "Vim：将光标行滚动到窗口顶部"),
    ("vim::ScrollCursorBottom", "Vim：将光标行滚动到窗口底部"),
    ("vim::PushObject", "Vim：选择/指定文本对象"),
    ("vim::PushOperator", "Vim：进入操作符等待状态"),
    ("vim::SwitchToInsertMode", "Vim：进入插入模式"),
    ("vim::SwitchToReplaceMode", "Vim：进入替换模式"),
    ("vim::Literal", "Vim：插入 literal 控制字符"),
    ("vim::Undo", "Vim：撤销"),
    ("vim::Redo", "Vim：重做"),
    ("vim::Paste", "Vim：粘贴"),
    ("vim::Yank", "Vim：复制/yank"),
    ("vim::Delete", "Vim：删除"),
    ("vim::Change", "Vim：修改并进入插入"),
    ("vim::Indent", "Vim：增加缩进"),
    ("vim::Outdent", "Vim：减少缩进"),
    ("vim::JoinLines", "Vim：合并行"),
    ("vim::OpenDefaultKeymap", "Vim：打开默认 Vim keymap"),
    ("null", "取消/屏蔽该快捷键在当前上下文中的默认行为"),
]

VERB_MAP = {
    "Toggle": "切换",
    "Open": "打开",
    "Close": "关闭",
    "Select": "选择",
    "Move": "移动",
    "GoTo": "跳转到",
    "Show": "显示",
    "Hide": "隐藏",
    "Focus": "聚焦",
    "Add": "添加",
    "Remove": "移除",
    "Delete": "删除",
    "Copy": "复制",
    "Cut": "剪切",
    "Paste": "粘贴",
    "Save": "保存",
    "New": "新建",
    "Rename": "重命名",
    "Find": "查找",
    "Accept": "接受",
    "Reject": "拒绝",
    "Keep": "保留",
    "Stage": "暂存",
    "Unstage": "取消暂存",
    "Expand": "展开",
    "Collapse": "折叠",
    "Fold": "折叠",
    "Unfold": "展开",
    "Run": "运行",
    "Restart": "重启",
    "Start": "开始",
    "Stop": "停止",
    "Pause": "暂停",
}

NAMESPACE_MAP = {
    "editor": "编辑器",
    "workspace": "工作区",
    "pane": "窗格",
    "menu": "菜单",
    "picker": "选择器",
    "project_panel": "项目面板",
    "project_search": "项目搜索",
    "buffer_search": "文件内搜索",
    "search": "搜索",
    "file_finder": "文件查找",
    "text_finder": "文本查找",
    "terminal": "终端",
    "terminal_panel": "终端面板",
    "git": "Git",
    "git_panel": "Git 面板",
    "debugger": "调试器",
    "agent": "Agent/AI",
    "agent_panel": "Agent 面板",
    "assistant": "AI 助手",
    "vim": "Vim",
    "zed": "Zed",
    "markdown": "Markdown",
    "outline": "大纲",
    "project_symbols": "项目符号",
    "command_palette": "命令面板",
}


def split_camel(name: str) -> str:
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    name = name.replace("_", " ").replace("-", " ")
    return " ".join(name.split())


def generic_description(action: str) -> str:
    if action == "null":
        return "取消/屏蔽该快捷键在当前上下文中的默认行为"
    if "::" not in action:
        return f"执行 `{action}`"
    namespace, name = action.split("::", 1)
    area = NAMESPACE_MAP.get(namespace, namespace.replace("_", " "))
    for verb, zh in sorted(VERB_MAP.items(), key=lambda x: -len(x[0])):
        if name.startswith(verb):
            rest = split_camel(name[len(verb) :]).strip()
            return f"{area}：{zh}{rest or '操作'}"
    return f"{area}：执行 {split_camel(name)}"


def extract_action(action_cell: str) -> str:
    cell = action_cell.strip()
    m = re.match(r"`([^`]+)`", cell)
    if m:
        return m.group(1)
    if cell.startswith("``"):
        m = re.match(r"`+\s*(.*?)\s*`+", cell)
        if m:
            return m.group(1)
    return cell.split(";", 1)[0].strip()


def description_for(action_cell: str) -> str:
    action = extract_action(action_cell)
    for prefix, desc in ACTION_DESCRIPTIONS:
        if action == prefix or (prefix.endswith("::") and action.startswith(prefix)):
            return desc
    return generic_description(action)


def repair_file(path: Path) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    in_keymap_table = False
    skip_alignment = False
    for line in lines:
        if line.strip() == "| # | 快捷键 / key sequence | Action / 参数 |":
            out.append("| 功能说明 | 快捷键 / key sequence | Action / 参数 |")
            in_keymap_table = True
            skip_alignment = True
            continue
        if (
            in_keymap_table
            and skip_alignment
            and re.match(r"^\|\s*:?-{3,}:?\s*\|", line)
        ):
            out.append("|---|---|---|")
            skip_alignment = False
            continue
        if in_keymap_table:
            if not line.startswith("|") or line.strip() == "":
                in_keymap_table = False
                out.append(line)
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 3 and cells[0].isdigit():
                key = cells[1]
                action = "|".join(cells[2:]).strip()
                desc = description_for(action)
                out.append(f"| {desc} | {key} | {action} |")
                continue
        out.append(line)
    text = "\n".join(out) + "\n"
    text = re.sub(r"\n- 来源 section 数：\d+\n- 快捷键绑定数：\d+\n", "\n", text)
    path.write_text(text, encoding="utf-8")


def repair_all_md() -> None:
    path = ZED / "all.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "- keymap 绑定总数：1730 条\n- 额外 Vim `:` 命令行命令：79 条\n",
        "- 内容组织：按功能场景拆分模块，每个快捷键表第一列直接说明功能。\n",
    )
    text = re.sub(
        r"\| 模块 \| 文件 \| section 数 \| 绑定/命令数 \|\n\|---\|---\|---:\|---:\|\n",
        "| 模块 | 文件 | 说明 |\n|---|---|---|\n",
        text,
    )
    replacements = {
        "| 来源、加载逻辑与统计口径 | [`keymaps/reference/source-and-loading-logic.md`](keymaps/reference/source-and-loading-logic.md) | 0 | 0 |": "| 来源、加载逻辑与统计口径 | [`keymaps/reference/source-and-loading-logic.md`](keymaps/reference/source-and-loading-logic.md) | 说明为什么这些文件属于默认 VS Code/Vim 快捷键范围。 |",
        "| VS Code 默认布局：全局、菜单与编辑器基础 | [`keymaps/vscode/01-global-editor.md`](keymaps/vscode/01-global-editor.md) | 14 | 201 |": "| VS Code 默认布局：全局、菜单与编辑器基础 | [`keymaps/vscode/01-global-editor.md`](keymaps/vscode/01-global-editor.md) | 全局命令、菜单、基础编辑、移动、选择、格式化等。 |",
        "| VS Code 默认布局：工作区、窗格、标签与窗口 | [`keymaps/vscode/02-workspace-panes-tabs.md`](keymaps/vscode/02-workspace-panes-tabs.md) | 16 | 129 |": "| VS Code 默认布局：工作区、窗格、标签与窗口 | [`keymaps/vscode/02-workspace-panes-tabs.md`](keymaps/vscode/02-workspace-panes-tabs.md) | 窗口、标签页、分屏、窗格焦点与工作区级操作。 |",
        "| VS Code 默认布局：搜索、替换、Picker 与命令入口 | [`keymaps/vscode/03-search-pickers-command.md`](keymaps/vscode/03-search-pickers-command.md) | 29 | 266 |": "| VS Code 默认布局：搜索、替换、Picker 与命令入口 | [`keymaps/vscode/03-search-pickers-command.md`](keymaps/vscode/03-search-pickers-command.md) | 文件查找、文本搜索、替换、命令面板、符号跳转等。 |",
        "| VS Code 默认布局：侧边栏与面板 | [`keymaps/vscode/04-panels-sidebars.md`](keymaps/vscode/04-panels-sidebars.md) | 4 | 14 |": "| VS Code 默认布局：侧边栏与面板 | [`keymaps/vscode/04-panels-sidebars.md`](keymaps/vscode/04-panels-sidebars.md) | 项目、侧栏、通知、协作等面板类操作。 |",
        "| VS Code 默认布局：终端、调试、Git 与 Agent/AI | [`keymaps/vscode/05-terminal-debug-git-agent.md`](keymaps/vscode/05-terminal-debug-git-agent.md) | 33 | 137 |": "| VS Code 默认布局：终端、调试、Git 与 Agent/AI | [`keymaps/vscode/05-terminal-debug-git-agent.md`](keymaps/vscode/05-terminal-debug-git-agent.md) | 终端、调试、Git、AI/Agent、LSP 工具相关快捷键。 |",
        "| VS Code 默认布局：其它特殊上下文 | [`keymaps/vscode/06-special-contexts.md`](keymaps/vscode/06-special-contexts.md) | 29 | 96 |": "| VS Code 默认布局：其它特殊上下文 | [`keymaps/vscode/06-special-contexts.md`](keymaps/vscode/06-special-contexts.md) | Notebook、任务、扩展、特殊 UI 状态等上下文。 |",
        "| VS Code 默认布局：specific overrides 高优先级覆盖 | [`keymaps/vscode/07-specific-overrides.md`](keymaps/vscode/07-specific-overrides.md) | 4 | 15 |": "| VS Code 默认布局：specific overrides 高优先级覆盖 | [`keymaps/vscode/07-specific-overrides.md`](keymaps/vscode/07-specific-overrides.md) | 默认加载链路最后应用的内置覆盖快捷键。 |",
        "| Vim mode：Normal/VimControl 移动、导航与 Zed 语义跳转 | [`keymaps/vim/01-normal-motion-navigation.md`](keymaps/vim/01-normal-motion-navigation.md) | 7 | 220 |": "| Vim mode：Normal/VimControl 移动、导航与 Zed 语义跳转 | [`keymaps/vim/01-normal-motion-navigation.md`](keymaps/vim/01-normal-motion-navigation.md) | 普通模式移动、搜索、跳转、LSP、诊断和滚动。 |",
        "| Vim mode：操作符、文本对象、surround 与 exchange | [`keymaps/vim/02-operators-textobjects-surround.md`](keymaps/vim/02-operators-textobjects-surround.md) | 23 | 104 |": "| Vim mode：操作符、文本对象、surround 与 exchange | [`keymaps/vim/02-operators-textobjects-surround.md`](keymaps/vim/02-operators-textobjects-surround.md) | 操作符、文本对象、surround、exchange 等组合命令。 |",
        "| Vim mode：Insert、Visual、Replace、Literal 与输入相关模式 | [`keymaps/vim/03-insert-visual-replace-literal.md`](keymaps/vim/03-insert-visual-replace-literal.md) | 6 | 161 |": "| Vim mode：Insert、Visual、Replace、Literal 与输入相关模式 | [`keymaps/vim/03-insert-visual-replace-literal.md`](keymaps/vim/03-insert-visual-replace-literal.md) | 插入、可视、替换、literal 输入等模式快捷键。 |",
        "| Vim mode：窗口、窗格、项目面板、终端与侧栏 | [`keymaps/vim/04-window-project-terminal-panels.md`](keymaps/vim/04-window-project-terminal-panels.md) | 8 | 244 |": "| Vim mode：窗口、窗格、项目面板、终端与侧栏 | [`keymaps/vim/04-window-project-terminal-panels.md`](keymaps/vim/04-window-project-terminal-panels.md) | Vim 风格窗格、项目面板、终端、侧栏导航。 |",
        "| Vim mode：Helix 兼容与特殊集成 | [`keymaps/vim/05-helix-and-special-integrations.md`](keymaps/vim/05-helix-and-special-integrations.md) | 4 | 53 |": "| Vim mode：Helix 兼容与特殊集成 | [`keymaps/vim/05-helix-and-special-integrations.md`](keymaps/vim/05-helix-and-special-integrations.md) | Helix 兼容层和特殊集成上下文。 |",
        "| Vim mode：其它上下文 | [`keymaps/vim/07-other-vim-contexts.md`](keymaps/vim/07-other-vim-contexts.md) | 16 | 90 |": "| Vim mode：其它上下文 | [`keymaps/vim/07-other-vim-contexts.md`](keymaps/vim/07-other-vim-contexts.md) | 未归入前面分类的 Vim 上下文快捷键。 |",
        "| Vim mode：命令行 `:` 命令 | [`keymaps/vim/06-command-line.md`](keymaps/vim/06-command-line.md) | 1 | 79 |": "| Vim mode：命令行 `:` 命令 | [`keymaps/vim/06-command-line.md`](keymaps/vim/06-command-line.md) | Vim 命令行命令说明，不是 JSON keymap 按键表。 |",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace(
        "- 每个模块保留原始 `context`、源文件、section 编号、快捷键序列、Action 和参数，便于回到源码核对。",
        "- 每个模块保留原始 `context`、源文件、section 编号、快捷键序列、Action 和参数，并在第一列直接说明快捷键功能。",
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for path in KEYMAPS.rglob("*.md"):
        if path.name == "06-command-line.md":
            continue
        repair_file(path)
    repair_all_md()


if __name__ == "__main__":
    main()
