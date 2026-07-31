# zed quickshort

## dock
ctrl + shift + y
ctrl + b   / ctrl + alt + b  
ctrl + j   / ctrl + alt  + j  

### ptf
> 'ptf' -->  xxx panel: toggle focus

- project panel
  - pptf
  - E    //   S   //  H  // L
  - ctrl + shift + e

- debug panel
  - dptf
  - D
  - ctrl + shift + d

- git panel
  - gptf
  - G
  - ctrl + shift + g

- collaboration panel
  - cptf
  - C
  - ctrl + shift + c

- outline panel
  - optf
  - ctrl + shfit + b

- terminal panel
  - tptf
  - T
  - ctrl + `             // 打开 term
  - ctrl + shfit + `     // 新建
  - ctrl + shift + space  // 编辑模式进入vim mode
  
  
  
## windows

### new pane
ctrl + w  n  
ctrl + w  v  
ctrl + w  s  

### close pane
ctrl + w  q 
space + w  + q

### focus pane
ctrl + w  h  
ctrl + w  j  
ctrl + w  k  
ctrl + w  l  

### move pane
ctrl + w  H    //   `ctrl + w  shift + h`  
ctrl + w  J    //   `ctrl + w  shift + j`  
ctrl + w  K    //   `ctrl + w  shift + k`  
ctrl + w  L    //   `ctrl + w  shift + l`  

### open in explorer
ctrl + k r

### language selector
ctrl + k m

### markdown preview
ctrl + k v
ctrl + shift + v

### code fold

#### flod
- ctrl + shift [
- zc

// 递归折叠
- ctrl + k ctrl + [  
- zC      //    `z + shitf + c`

#### expend
- ctrl + shift + ]
- zo

// 递归展开
- ctrl + k ctrl + ]  
- zO      //   `z + shift + o`

#### switch code fold status
- ctrl + k ctrl + l
- za

#### flod all
- ctrl + k ctrl + 0
- zM   //    `z + shift + m`

#### expend all
- ctrl + k ctrl + j
- zR   //    `z + shift + r `


### search 
- 向后搜索
   /
   g /
- 向前搜索
   ?

#### 重复搜索操作
n 

#### 反向搜索操作
N

### theme 
ctrl + k ctrl + t
ctrl + k ctrl + shift + t

### keybinds
ctrl + k ctrl + s

### switch tab
alt + 1~9


### coding
ctrl + g


### 代码重构与编辑 (Refactoring & Code
Actions)

| 快捷键 | 绑定 Action | 详细说明 |
| :--- | :--- | :--- |
| `g .` 或 `g r a` | `editor::ToggleCodeActions` | 触发代码动作（Code Actions）或快速修复（Quick Fix），非常适合修复 Rust 编译报错 |
| `g h` 或 `Shift-k` | `editor` | 查看悬浮文档提示（Hover） |
| `g B` | `editor::BlameHover` | 查看当前行的 Git Blame 悬浮历史提交信息 |
| `g r n` 或 `c d` | `editor::Rename` | 重命名当前光标处的变量或符号 |
| `g c` | `normal.rs` | 切换当前行或选中行的单行注释 |
| `g b` | `vim::PushToggleBlockComments` | 切换块注释 |
  
  
### 添加环绕字符
-  y s <motion> <char> : 
  - 例如：
      -  y s w "       // (用双引号包围当前单词)
      -  y s a ) [    // (用中括号包围包括小括号的整个表达式块)
      
### 更改环绕字符
-  c s <old_char> <new_char> :
  - 例如：
      -  c s " '  (把外侧的双引号改成单引号)
      
### 删除环绕的某个字符
-  d s <char> : 
  - 例如：
      -  d s "  (删除双引号)

-  i a  /  a a : 选中参数 (Argument)
块，对修改函数参数极其有用。
-  i f  /  a f : 选中整个函数/方法 (Method) 体。
-  i c  /  a c : 选中整个类 (Class) 定义。
-  i e  /  a e : 选中整个文件内容 (Entire file)。


### 8. 项目面板文件树快捷键 (Project Panel - netrw 兼容模式)

| 快捷键 | 绑定 Action | 详细说明 |
| :---: | :--- | :--- |
| `%` | `project_panel::NewFile` | 在当前目录下新建文件 |
| `d` | `project_panel::NewDirectory` | 在当前目录下新建文件夹 |
| `h` / `l` | `project_panel::CollapseSelectedEntry` / `project_panel::ExpandSelectedEntry` | 折叠/展开选中的文件夹目录 |
| `v` | `project_panel::OpenSplitVertical` | 将选中文件在垂直分屏中打开 |
| `o` | `project_panel::OpenSplitHorizontal` | 将选中文件在水平分屏中打开 |
| `shift-d` | `project_panel::Delete` | 删除选中的文件/文件夹 |
| `shift-r` | `project_panel::Rename` | 对选中的文件/文件夹进行重命名 |
| `x` | `project_panel::RevealInFileManager` | 在系统资源管理器（Windows 的 File Explorer）中显示选中的文件 |
| `escape` | `vim::ToggleProjectPanelFocus` | 移开焦点，将光标放回主编辑器中 |



  #### B. 进阶文本对象 (Text Objects)

  搭配  c  (Change),  d  (Delete),  y  (Yank),  v  (Visual)
  等算子使用，可操作极具编程语言语义的范围。

   | 文本对象键 | 对应操作范围 | 说明 |
   | :---: | :--- | :--- |
   | `a` | 参数 (Argument) | 代表函数定义或调用中的某个参数（含逗号） |
   | `f` | 方法/函数 (Method/Function) | 代表整个函数的代码块范围 |
   | `c` | 类/结构体 (Class/Struct) | 代表整个类/结构体的代码块范围 |
   | `e` | 整个文件 (Entire File) | 代表当前文件的全部内容 |
   | `q` | 任意引号 (Quotes) | 智能识别最近的单引号、双引号或反引号并将其作为范围 |



### 2. LSP 代码导航快捷键 (Normal 模式)
  
| 快捷键 | 绑定 Action | 详细说明 |
| :--- | :--- | :--- |
| `g d` 或 `Ctrl-]` | `editor::GoToDefinition` | 跳转到当前光标处符号的定义位置 |
| `Ctrl-w d` 或 `Ctrl-w ]` | `editor::GoToDefinitionSplit` | 在分屏中打开并跳转到定义位置 |
| `g shift-d` | `editor::GoToDeclaration` | 跳转到当前光标处符号的声明位置 |
| `g y` | `editor::GoToTypeDefinition` | 跳转到当前光标处符号的类型定义位置 |
| `g r i` 或 `g shift-i` | `editor::GoToImplementation` | 跳转到当前接口/Trait 的具体实现位置 |
| `g r r` 或 `g shift-a` | `editor::FindAllReferences` | 查找当前符号的所有引用（会在侧边弹出引用列表） |
| `g s` 或 `g shift-o` | `outline` | 切换/打开当前文件的大纲面板 (Outline Panel) |
| `g shift-s` | `project_symbols` | 全局模糊搜索项目中的所有符号 (Project Symbols) |
| `Ctrl-o` / `Ctrl-i` | `pane::GoBack` / `pane::GoForward` | 在编辑光标跳转历史中后退/前进 |
| `Ctrl-^` | `pane::AlternateFile` | 在最近使用的两个文件（缓冲区）之间快速交替切换 |

### 3. 代码重构与基础编辑快捷键 (Normal 模式)

| 快捷键 | 绑定 Action | 详细说明 |
| :--- | :--- | :--- |
| `g r n` | `editor::Rename` | 重命名当前符号，并自动更新所有引用该符号的文件 |
| `c d` | `editor::Rename` | 重命名当前符号（Zed 专属 Vim operator 快捷方式） |
| `g .` 或 `g r a` | `editor::ToggleCodeActions` | 打开 Code Actions 菜单（即 Quick Fix 快速修复补丁） |
| `g h` 或 `Shift-k` | `editor` | 显示当前符号的 LSP 悬浮文档说明（Hover） |
| `g B` | `editor::BlameHover` | 显示当前行的 Git Blame 详细悬浮提示（作者、提交哈希、时间） |
| `g c` | `vim` | 切换所选行或当前行的单行注释状态 |
| `g b` | `vim::PushToggleBlockComments` | 切换所选行或当前行的块注释（`/* ... */`）状态 |
| `z a` | `editor::ToggleFold` | 折叠或展开当前代码块 |

### 4. 报错诊断与 Git 差异导航快捷键 (Normal 模式)

| 快捷键 | 绑定 Action | 详细说明 |
| :---: | :--- | :--- |
| `] d` 或 `g ]` | `editor::GoToDiagnostic` | 跳转到文件中的下一个报错、警告或诊断位置 |
| `[ d` 或 `g [` | `editor::GoToPreviousDiagnostic` | 跳转到文件中的上一个报错、警告或诊断位置 |
| `] c` | `editor::GoToHunk` | 跳转到当前文件的下一个 Git 修改块 (Hunk) |
| `[ c` | `editor::GoToPreviousHunk` | 跳转到当前文件的上一个 Git 修改块 |
| `d o` | `editor::ToggleSelectedDiffHunks` | 展开或折叠当前 Git 修改块与 HEAD 版本的内联差异对比 |
| `d p` | `git::Restore` | 丢弃当前 Git 修改块的所有改动，恢复到 HEAD 状态 |
| `d u` | `git::StageAndNext` | 将当前 Git 修改块加入暂存区 (Stage)，并自动跳到下一个修改块 |

### 5. 窗口分屏与面板切换快捷键

在编写和阅读复杂项目代码时，合理排布视口非常重要。

  | 快捷键 | 绑定 Action | 详细说明 |
  | :--- | :--- | :--- |
  | `Ctrl-w v` 或 `Ctrl-w Ctrl-v` | `pane::SplitVertical` | 向右垂直分屏 |
  | `Ctrl-w s` 或 `Ctrl-w Ctrl-s` | `pane::SplitHorizontal` | 向下水平分屏 |
  | `Ctrl-w h / j / k / l` | `workspace::ActivatePaneLeft / Down / Up / Right` | 将焦点移动到左/下/上/右侧的分屏 |
  | `Ctrl-w Shift-h / j / k / l` | `workspace::MovePaneLeft / Down / Up / Right` | 将当前分屏整体移动到最左/最下/最上/最右边 |
  | `Ctrl-w =` | `vim::ResetPaneSizes` | 重置所有分屏的尺寸，使其平均等宽/等高 |
  | `Ctrl-w _` | `vim::MaximizePane` | 最大化当前激活的分屏（收起其他分屏） |
  | `Ctrl-w c` 或 `Ctrl-w q` | `pane::CloseActiveItem` | 关闭当前激活的标签页/分屏 |
  | `g t` / `g Shift-t` | `vim::GoToTab` / `vim::GoToPreviousTab` | 切换到下一个/上一个标签页 (Tab) |


### 7. 插入模式下 Zed 智能快捷键 (Insert 模式)

| 快捷键 | 绑定 Action | 详细说明 |
|---|---|---|
| `Ctrl-x Ctrl-a` | `assistant` | 唤起 Inline AI 助手输入框，输入自然语言即可在光标处生成/重写代码 |
| `Ctrl-x Ctrl-c` | `editor::ShowEditPrediction` | 显示当前位置的 AI 内联编辑预测 (AI Edit Prediction) |
| `Ctrl-x Ctrl-o` | `editor::ShowCompletions` | 强制展开 LSP 的补全下拉菜单 |
| `Ctrl-x Ctrl-l` | `editor::ToggleCodeActions` | 在插入模式下快速展开 Code Actions 菜单 |
    
### g xx
g s   / gO 当前文件
g S       //整个项目

上/下一个方法
[ m    
] m

选中
[ x
] x

d o
d O

## 范围选区
v / d / c / y
### 函数参数
ia
aa

### 函数
if
af

### 类
ic
ac

### 标签
it
at

### 注释
igc
agc

###
vii
vai

via
vaa

## 多光标
- 下一个重复项增加光标
gl

- 上一个重复项增加光标
gL

- visual mode
  - 在选中内容行尾增加光标（真正的行尾，也包括行尾的空字符）
    - gA
  - 在选中内容行首第一个非空字符前面)增加光标
  - gI
- 跳过最后的光标
  - g shift .
- 往前跳  
  - g shfit ,

## 替换操作  vim-exchange 操作
- 在一个单词上点击cxaw，在另一行上点击cxaw，两个单词互换
- cxaw
- 在一行上点击cxx，在另一行上点击cxx，两行互换
  - cxx
- 在某一行使用cxaf， 然后在某一行使用cxx，函数位置替换

- cxip

- cxc 取消交换标记

跳转
- w 下一个单词开头
- ge 上一个单词结尾


- b 单词结尾
- e 单词开头
包括后面的字符
- B
- E
