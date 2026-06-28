from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEYMAPS = ROOT / "zed" / "keymaps"

ACTION_DESCRIPTIONS = {
    "workspace::ToggleWorktreeSecurity": "切换工作区信任/安全状态",
    "workspace::SendKeystrokes": "发送一组预定义按键序列",
    "pane::ActivateNextItem": "切换到下一个标签页/项目",
    "pane::ActivatePreviousItem": "切换到上一个标签页/项目",
    "pane::ActivateLastItem": "切换到最后一个标签页/项目",
    "pane::ActivateItem": "切换到指定标签页/项目",
    "pane::CloseActiveItem": "关闭当前标签页/项目",
    "pane::AlternateFile": "切换到备用文件",
    "editor::ScrollCursorTop": "将光标所在行滚动到窗口顶部",
    "editor::ScrollCursorCenter": "将光标所在行滚动到窗口中央",
    "editor::ScrollCursorBottom": "将光标所在行滚动到窗口底部",
    "editor::ToggleFoldRecursive": "递归切换当前代码块折叠",
    "editor::UnfoldLines": "展开当前行所在折叠区域",
    "editor::FoldSelectedRanges": "折叠选中的范围",
    "editor::GoToDefinitionSplit": "在分屏中跳转到定义",
    "editor::GoToTypeDefinitionSplit": "在分屏中跳转到类型定义",
    "editor::OpenExcerptsSplit": "在分屏中打开摘录/搜索结果",
    "editor::GoToHunk": "跳转到下一个 Git hunk",
    "editor::GoToPreviousHunk": "跳转到上一个 Git hunk",
    "editor::SignatureHelpPrevious": "切换到上一个函数签名提示",
    "editor::SignatureHelpNext": "切换到下一个函数签名提示",
    "git::ToggleStaged": "切换当前变更的暂存状态",
    "notebook::NotebookMoveDown": "Notebook：向下移动单元格焦点",
    "notebook::NotebookMoveUp": "Notebook：向上移动单元格焦点",
    "notebook::EnterCommandMode": "Notebook：进入命令模式",
    "vim::Tab": "Vim：执行 Tab 导航/补全跳转",
    "vim::Enter": "Vim：确认当前等待中的操作",
    "vim::MiddleOfLine": "Vim：移动到当前行中间",
    "vim::ToggleRecord": "Vim：开始或停止录制宏",
    "vim::ReplayLastRecording": "Vim：回放上一次宏录制",
    "vim::PushReplayRegister": "Vim：选择寄存器并回放宏",
    "vim::ColumnRight": "Vim：向右横向滚动一列",
    "vim::ColumnLeft": "Vim：向左横向滚动一列",
    "vim::HalfPageRight": "Vim：向右横向滚动半屏",
    "vim::HalfPageLeft": "Vim：向左横向滚动半屏",
    "vim::Number": "Vim：输入计数数字",
    "vim::CountCommand": "Vim：用计数打开命令行范围",
    "vim::GoToPercentage": "Vim：按百分比跳转到文件位置",
    "vim::Repeat": "Vim：重复上一次编辑命令",
    "vim::InsertBefore": "Vim：在光标前进入插入模式",
    "vim::InsertAfter": "Vim：在光标后进入插入模式",
    "vim::PushChange": "Vim：进入 change 操作符等待状态",
    "vim::ChangeToEndOfLine": "Vim：修改从光标到行尾的内容",
    "vim::PushDelete": "Vim：进入 delete 操作符等待状态",
    "vim::DeleteRight": "Vim：删除光标右侧/当前字符",
    "vim::DeleteLeft": "Vim：删除光标左侧字符",
    "vim::JoinLinesNoWhitespace": "Vim：合并行且不插入额外空格",
    "vim::PushYank": "Vim：进入 yank 复制操作符等待状态",
    "vim::YankLine": "Vim：复制当前行",
    "vim::Increment": "Vim：递增光标处数字",
    "vim::Decrement": "Vim：递减光标处数字",
    "vim::PushIndent": "Vim：进入增加缩进操作符等待状态",
    "vim::PushOutdent": "Vim：进入减少缩进操作符等待状态",
    "vim::PushAutoIndent": "Vim：进入自动缩进操作符等待状态",
    "vim::PushShellCommand": "Vim：进入 shell 命令过滤操作符等待状态",
    "vim::PushLowercase": "Vim：进入转小写操作符等待状态",
    "vim::PushUppercase": "Vim：进入转大写操作符等待状态",
    "vim::PushOppositeCase": "Vim：进入大小写反转操作符等待状态",
    "vim::PushRot13": "Vim：进入 ROT13 转换操作符等待状态",
    "vim::PushRewrap": "Vim：进入文本重排操作符等待状态",
    "vim::PushToggleComments": "Vim：进入行注释切换操作符等待状态",
    "vim::PushToggleBlockComments": "Vim：进入块注释切换操作符等待状态",
    "vim::ClearOperators": "Vim：取消当前操作符等待状态",
    "vim::PushDigraph": "Vim：输入 digraph 字符",
    "vim::PushLiteral": "Vim：输入 literal 控制字符",
    "vim::Word": "Vim 文本对象：单词",
    "vim::Tag": "Vim 文本对象：HTML/XML 标签",
    "vim::Sentence": "Vim 文本对象：句子",
    "vim::Paragraph": "Vim 文本对象：段落",
    "vim::Quotes": "Vim 文本对象：单引号内容",
    "vim::BackQuotes": "Vim 文本对象：反引号内容",
    "vim::DoubleQuotes": "Vim 文本对象：双引号内容",
    "vim::MiniQuotes": "Vim 文本对象：mini.ai 风格引号内容",
    "vim::VerticalBars": "Vim 文本对象：竖线包围内容",
    "vim::Parentheses": "Vim 文本对象：圆括号内容",
    "vim::SquareBrackets": "Vim 文本对象：方括号内容",
    "vim::CurlyBrackets": "Vim 文本对象：花括号内容",
    "vim::AngleBrackets": "Vim 文本对象：尖括号内容",
    "vim::Argument": "Vim 文本对象：参数/列表项",
    "vim::IndentObj": "Vim 文本对象：当前缩进块",
    "vim::Method": "Vim 文本对象：函数/方法",
    "vim::Class": "Vim 文本对象：类/定义块",
    "vim::EntireFile": "Vim 文本对象：整个文件",
    "vim::PushHelixSurroundAdd": "Helix/Vim：添加 surrounding 包围符",
    "vim::PushHelixSurroundReplace": "Helix/Vim：替换 surrounding 包围符",
    "vim::PushHelixSurroundDelete": "Helix/Vim：删除 surrounding 包围符",
    "vim::NextSectionStart": "Vim：跳到下一节开头",
    "vim::NextSectionEnd": "Vim：跳到下一节结尾",
    "vim::PreviousSectionStart": "Vim：跳到上一节开头",
    "vim::PreviousSectionEnd": "Vim：跳到上一节结尾",
    "vim::NextComment": "Vim：跳到下一条注释",
    "vim::PreviousComment": "Vim：跳到上一条注释",
    "vim::NextLesserIndent": "Vim：跳到下一个更浅缩进位置",
    "vim::NextGreaterIndent": "Vim：跳到下一个更深缩进位置",
    "vim::NextSameIndent": "Vim：跳到下一个相同缩进位置",
    "vim::PreviousLesserIndent": "Vim：跳到上一个更浅缩进位置",
    "vim::PreviousGreaterIndent": "Vim：跳到上一个更深缩进位置",
    "vim::PreviousSameIndent": "Vim：跳到上一个相同缩进位置",
    "vim::InsertEmptyLineBelow": "Vim：在下方插入空行",
    "vim::InsertEmptyLineAbove": "Vim：在上方插入空行",
    "vim::CurrentLine": "Vim：把当前行作为操作目标",
    "vim::Exchange": "Vim：执行 exchange 交换操作",
    "vim::PushChangeSurrounds": "Vim：进入修改 surrounding 包围符状态",
    "vim::PushDeleteSurrounds": "Vim：进入删除 surrounding 包围符状态",
    "vim::PushForcedMotion": "Vim：强制按 motion 执行当前操作符",
}

GENERAL_PREFIXES = [
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
    ("workspace::CloseWindow", "关闭当前窗口"),
    ("workspace::OpenFiles", "打开文件"),
    ("workspace::Open", "打开项目/文件入口"),
    ("workspace::", "执行工作区操作"),
    ("zed::IncreaseBufferFontSize", "增大编辑器字体大小"),
    ("zed::DecreaseBufferFontSize", "减小编辑器字体大小"),
    ("zed::ResetBufferFontSize", "重置编辑器字体大小"),
    ("zed::OpenSettingsFile", "打开设置 JSON 文件"),
    ("zed::Quit", "退出 Zed"),
    ("zed::ToggleFullScreen", "切换全屏"),
    ("debugger::StepOver", "调试时单步跳过"),
    ("debugger::StepInto", "调试时单步进入"),
    ("debugger::StepOut", "调试时单步跳出"),
    ("debugger::", "执行调试器操作"),
    ("lsp_tool::ToggleMenu", "打开/关闭 LSP 工具菜单"),
    ("editor::Cancel", "取消当前编辑器操作"),
    ("editor::Backspace", "向前删除字符"),
    ("editor::DeleteToPreviousWordStart", "删除到上一个单词开头"),
    ("editor::DeleteToNextWordEnd", "删除到下一个单词结尾"),
    ("editor::Delete", "向后删除字符"),
    ("editor::Cut", "剪切选区或当前行"),
    ("editor::Copy", "复制选区或当前行"),
    ("editor::Paste", "粘贴剪贴板内容"),
    ("editor::Undo", "撤销上一步编辑"),
    ("editor::Redo", "重做被撤销的编辑"),
    ("editor::MoveUp", "光标上移"),
    ("editor::MoveDown", "光标下移"),
    ("editor::MoveLeft", "光标左移"),
    ("editor::MoveRight", "光标右移"),
    ("editor::MoveToBeginningOfLine", "移动到行首"),
    ("editor::MoveToEndOfLine", "移动到行尾"),
    ("editor::MoveToBeginning", "移动到文件开头"),
    ("editor::MoveToEnd", "移动到文件末尾"),
    ("editor::SelectAll", "全选当前编辑器内容"),
    ("editor::SelectLine", "选中当前行"),
    ("editor::Format", "格式化代码"),
    ("editor::OrganizeImports", "整理导入语句"),
    ("editor::GoToDefinition", "跳转到定义"),
    ("editor::GoToDeclaration", "跳转到声明"),
    ("editor::GoToTypeDefinition", "跳转到类型定义"),
    ("editor::GoToImplementation", "跳转到实现"),
    ("editor::FindAllReferences", "查找所有引用"),
    ("editor::Rename", "重命名符号"),
    ("editor::Hover", "显示悬停信息"),
    ("editor::GoToDiagnostic", "跳转到下一个诊断"),
    ("editor::GoToPreviousDiagnostic", "跳转到上一个诊断"),
    ("editor::SelectSmallerSyntaxNode", "缩小语法节点选区"),
    ("editor::SelectLargerSyntaxNode", "扩大语法节点选区"),
    ("editor::ToggleSelectedDiffHunks", "折叠/展开选中的 diff hunk"),
    ("editor::FoldAll", "折叠所有代码块"),
    ("editor::UnfoldAll", "展开所有代码块"),
    ("editor::ToggleFold", "切换当前代码块折叠"),
    ("editor::FoldRecursive", "递归折叠当前代码块"),
    ("editor::UnfoldRecursive", "递归展开当前代码块"),
    ("editor::Fold", "折叠当前代码块"),
    ("editor::Unfold", "展开当前代码块"),
    ("git::Restore", "还原 Git 变更"),
    ("git::StageAndNext", "暂存当前变更并跳到下一处"),
    ("git::UnstageAndNext", "取消暂存当前变更并跳到下一处"),
    ("git::", "执行 Git 操作"),
    ("pane::SplitRight", "向右拆分窗格"),
    ("pane::SplitLeft", "向左拆分窗格"),
    ("pane::SplitDown", "向下拆分窗格"),
    ("pane::SplitUp", "向上拆分窗格"),
    ("pane::GoBack", "导航后退"),
    ("pane::GoForward", "导航前进"),
    ("pane::DeploySearch", "在窗格中打开搜索"),
    ("pane::", "执行窗格操作"),
    ("file_finder::SelectPrevious", "文件查找中选择上一个结果"),
    ("file_finder::", "执行文件查找操作"),
    ("text_finder::ToProjectSearch", "从文本查找切换到项目搜索"),
    ("buffer_search::DeployReplace", "打开当前文件替换"),
    ("buffer_search::Deploy", "打开当前文件搜索"),
    ("search::SelectNextMatch", "跳到下一个搜索结果"),
    ("search::SelectPreviousMatch", "跳到上一个搜索结果"),
    ("project_search::", "执行项目搜索操作"),
    ("outline::Toggle", "打开/关闭文件符号大纲"),
    ("project_symbols::Toggle", "打开/关闭项目符号搜索"),
    ("command_palette::Toggle", "打开/关闭命令面板"),
    ("agent::", "执行 Agent/AI 操作"),
    ("assistant::InlineAssist", "打开行内 AI 助手"),
    ("terminal::", "执行终端操作"),
    ("terminal_panel::", "执行终端面板操作"),
    ("project_panel::", "执行项目面板操作"),
    ("vim::Left", "Vim：向左移动"),
    ("vim::Right", "Vim：向右移动"),
    ("vim::Up", "Vim：向上移动"),
    ("vim::Down", "Vim：向下移动"),
    ("vim::WrappingLeft", "Vim：向左移动，必要时换到上一行"),
    ("vim::WrappingRight", "Vim：向右移动，必要时换到下一行"),
    ("vim::NextLineStart", "Vim：移动到下一行行首"),
    ("vim::PreviousLineStart", "Vim：移动到上一行行首"),
    ("vim::EndOfLine", "Vim：移动到行尾"),
    ("vim::StartOfLine", "Vim：移动到行首"),
    ("vim::FirstNonWhitespace", "Vim：移动到行首第一个非空字符"),
    ("vim::EndOfDocument", "Vim：移动到文档末尾"),
    ("vim::StartOfDocument", "Vim：移动到文档开头"),
    ("vim::Search", "Vim：打开搜索"),
    ("vim::Matching", "Vim：跳转到匹配的括号/结构"),
    ("vim::SwitchToNormalMode", "Vim：切回普通模式"),
    ("vim::NormalBefore", "Vim：退出当前模式并回到普通模式"),
    ("vim::ToggleVisualBlock", "Vim：切换块可视模式"),
    ("vim::ToggleVisualLine", "Vim：切换行可视模式"),
    ("vim::ToggleVisual", "Vim：切换字符可视模式"),
    ("vim::", "执行 Vim 操作"),
    ("null", "取消/屏蔽该快捷键在当前上下文中的默认行为"),
]

NS = {
    "editor": "编辑器",
    "workspace": "工作区",
    "pane": "窗格",
    "menu": "菜单",
    "picker": "选择器",
    "project_panel": "项目面板",
    "terminal": "终端",
    "git": "Git",
    "vim": "Vim",
    "notebook": "Notebook",
}

VERB = {
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

TOKEN = {
    "Active": "当前",
    "Item": "项目",
    "Next": "下一个",
    "Previous": "上一个",
    "Last": "最后一个",
    "First": "第一个",
    "Definition": "定义",
    "Type": "类型",
    "Split": "分屏",
    "Hunk": "Git hunk",
    "Lines": "行",
    "Line": "行",
    "Selected": "选中",
    "Ranges": "范围",
    "Range": "范围",
    "Cursor": "光标",
    "Top": "顶部",
    "Center": "中央",
    "Bottom": "底部",
    "Recursive": "递归",
    "Current": "当前",
    "Word": "单词",
    "File": "文件",
    "Files": "文件",
    "Search": "搜索",
    "Replace": "替换",
    "Completion": "补全",
    "Completions": "补全",
    "Signature": "签名",
    "Help": "帮助",
    "Mode": "模式",
    "Command": "命令",
    "Comments": "注释",
    "Block": "块",
    "Indent": "缩进",
    "Outdent": "反缩进",
    "Uppercase": "大写",
    "Lowercase": "小写",
}


def split_words(name: str) -> list[str]:
    return re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name).replace("_", " ").split()


def zh_words(name: str) -> str:
    return "".join(TOKEN.get(w, w) for w in split_words(name))


def extract_action(action_cell: str) -> str:
    m = re.search(r"`([^`]+)`", action_cell.strip())
    return m.group(1) if m else action_cell.strip().split(";", 1)[0]


def describe(action_cell: str) -> str:
    action = extract_action(action_cell)
    if action in ACTION_DESCRIPTIONS:
        return ACTION_DESCRIPTIONS[action]
    for prefix, desc in GENERAL_PREFIXES:
        if action == prefix or (prefix.endswith("::") and action.startswith(prefix)):
            return desc
    if "::" in action:
        ns, name = action.split("::", 1)
        area = NS.get(ns, ns.replace("_", " "))
        for verb in sorted(VERB, key=len, reverse=True):
            if name.startswith(verb):
                return f"{area}：{VERB[verb]}{zh_words(name[len(verb) :]) or '操作'}"
        return f"{area}：{zh_words(name)}"
    return f"执行 `{action}`"


def split_table_row(line: str) -> list[str] | None:
    if not line.startswith("|"):
        return None
    cells: list[str] = []
    cur: list[str] = []
    in_code = False
    tick_len = 0
    i = 1
    while i < len(line):
        ch = line[i]
        if ch == "`":
            j = i
            while j < len(line) and line[j] == "`":
                j += 1
            ticks = j - i
            if not in_code:
                in_code = True
                tick_len = ticks
            elif ticks == tick_len:
                in_code = False
                tick_len = 0
            cur.append(line[i:j])
            i = j
            continue
        if ch == "|" and not in_code and (i == 0 or line[i - 1] != "\\"):
            cells.append("".join(cur).strip())
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    # If the row ended with a delimiter, the last collected cell is empty; ignore it.
    if cur:
        cells.append("".join(cur).strip())
    return cells


def escape_cell(cell: str) -> str:
    # Markdown table separators must be escaped, even inside code spans in many renderers.
    out = []
    in_code = False
    tick_len = 0
    i = 0
    while i < len(cell):
        if cell[i] == "`":
            j = i
            while j < len(cell) and cell[j] == "`":
                j += 1
            ticks = j - i
            if not in_code:
                in_code = True
                tick_len = ticks
            elif ticks == tick_len:
                in_code = False
                tick_len = 0
            out.append(cell[i:j])
            i = j
            continue
        if cell[i] == "|" and (i == 0 or cell[i - 1] != "\\"):
            out.append("\\|")
        else:
            out.append(cell[i])
        i += 1
    return "".join(out)


def repair_file(path: Path) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    in_table = False
    for line in lines:
        if line.strip() == "| 功能说明 | 快捷键 / key sequence | Action / 参数 |":
            in_table = True
            out.append(line)
            continue
        if in_table and line.strip() == "|---|---|---|":
            out.append(line)
            continue
        if in_table:
            if not line.startswith("|") or not line.strip():
                in_table = False
                out.append(line)
                continue
            cells = split_table_row(line)
            if cells and len(cells) >= 3:
                key = escape_cell(cells[1])
                action = escape_cell(cells[2])
                out.append(f"| {describe(cells[2])} | {key} | {action} |")
                continue
        out.append(line)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> None:
    for path in KEYMAPS.rglob("*.md"):
        if path.name != "06-command-line.md" and "reference" not in path.parts:
            repair_file(path)


if __name__ == "__main__":
    main()
