# quick input
## ptf
> 'ptf' --> panel toggle focus

- pptf 
  - project
  
- dptf
  - debug
  
- tptf
  - terminal
  
- gptf
  - git
  
- cptf
  - collabration

- optf
  - outline

## windows

### new pane

ctrl + w  v
ctrl + w  s

### focus pane
ctrl + w  h
ctrl + w  j
ctrl + w  K
ctrl + w  l

### move pane
ctrl + w  H
ctrl + w  J
ctrl + w  K
ctrl + w  L


### other
ctrl + w q close 
ctrl + k r explorer

### code fold
ctrl + k ctrl + l

ctrl + k ctrl + [
ctrl + k ctrl + ]

ctrl + k ctrl + 0
ctrl + k ctrl + j

### search 
space /

### theme 
ctrl + k ctrl + t
ctrl + k ctrl + shift + t


ctrl + k ctrl + s

### switch tab
alt + 1~9


### coding

ctrl + g

  ### 三、 代码重构与编辑 (Refactoring & Code
  Actions)

  •  g .  或  g r a : 触发代码动作 (Code Actions) /
  快速修复 (Quick Fix)，非常适合修复 Rust
  编译报错！
  •  g h  或  shift-k : 查看悬浮文档提示 (Hover,
  editor)
  •  g B : 查看当前行的 Git Blame 悬浮历史提交信息
  ( editor::BlameHover )
  •  g r n  或  c d : 重命名当前光标处的变量/符号
  (Rename)
  •  g c : 切换单行或选中行的注释 (normal.rs)
  •  g b : 切换块注释 (
  vim::PushToggleBlockComments )
  
  ### 四、 Vim 环绕字符与文本对象 (Surround & Text
  Objects)

  Zed 原生实现了类似  vim-surround
  的操作，用于快速处理括号、引号：

  •  y s <motion> <char> : 添加环绕字符。例如：
      •  y s w "  (用双引号包围当前单词)
      •  y s a ) [
      (用中括号包围包括小括号的整个表达式块)
  •  d s <char> : 删除环绕的某个字符。例如：
      •  d s "  (删除双引号)
  •  c s <old_char> <new_char> :
  更改环绕字符。例如：
      •  c s " '  (把外侧的双引号改成单引号)


  此外，Zed 支持非常强悍的代码专用文本对象 (Text
  Objects)：

  •  i a  /  a a : 选中参数 (Argument)
  块，对修改函数参数极其有用。
  •  i f  /  a f : 选中整个函数/方法 (Method) 体。
  •  i c  /  a c : 选中整个类 (Class) 定义。
  •  i e  /  a e : 选中整个文件内容 (Entire file)。


  ### 8. 项目面板文件树快捷键 (Project Panel - netrw 兼容模式)

  当光标在左侧文件面板 (Project Panel) 中时，Zed 允许使用经典的 netrw/Vim
  风格键位。

   快捷键    │ 绑定 Action                     │ 详细说明
  ───────────┼─────────────────────────────────┼──────────────────────────────────
    %        │  project_panel::NewFile         │ 在当前目录下新建文件
    d        │  project_panel::NewDirectory    │ 在当前目录下新建文件夹
    h  /  l  │  CollapseSelectedEntry  /       │ 折叠/展开选中的文件夹目录
             │ ExpandSelectedEntry             │
    v        │  project_panel::OpenSplitVertica│ 将选中文件在垂直分屏中打开
             │ l                               │
    o        │  project_panel::OpenSplitHorizon│ 将选中文件在水平分屏中打开
             │ tal                             │
    shift-d  │  project_panel::Delete          │ 删除选中的文件/文件夹
    shift-r  │  project_panel::Rename          │ 对选中的文件/文件夹进行重命名
    x        │  project_panel::RevealInFileMana│ 在系统资源管理器（Windows 的
             │ ger                             │ File Explorer）中显示选中的文件
    escape   │  vim::ToggleProjectPanelFocus   │ 移开焦点，将光标放回主编辑器中


  ### 6. Vim 环绕字符 (Surround) 与进阶文本对象

  Zed 原生支持强大的  vim-surround
  操作。利用这些组合，您可以极其优雅地增删改括号和引号，以及选中语义化的代码块。

  #### A. 环绕操作 (Surround)

   快捷模式                 │ 对应 Action              │ 详细说明
  ──────────────────────────┼──────────────────────────┼──────────────────────────
    y s <motion> <char>     │  vim::PushAddSurrounds   │ 给指定运动范围内的内容添
                            │                          │ 加环绕字符
    d s <char>              │  vim::PushDeleteSurrounds│ 删除指定的环绕字符
                            │                          │
    c s <old_char>          │  vim::PushChangeSurrounds│ 修改指定的环绕字符为新字
   <new_char>               │                          │ 符

  #### B. 进阶文本对象 (Text Objects)

  搭配  c  (Change),  d  (Delete),  y  (Yank),  v  (Visual)
  等算子使用，可操作极具编程语言语义的范围。

   文本对象键 │ 对应操作范围                │ 说明
  ────────────┼─────────────────────────────┼─────────────────────────────────────
    a         │ 参数 (Argument)             │ 代表函数定义或调用中的某个参数（含
              │                             │ 逗号）
    f         │ 方法/函数 (Method/Function) │ 代表整个函数的代码块范围
    c         │ 类/结构体 (Class/Struct)    │ 代表整个类/结构体的代码块范围
    e         │ 整个文件 (Entire File)      │ 代表当前文件的全部内容
    q         │ 任意引号 (Quotes)           │ 智能识别最近的单/双/反引号并作为范
              │                             │ 围

  #### 💡 实际使用示例 (以 Rust 代码为例)

    // 初始代码状态
    let value = format_name(first_name, last_name);

  1. 替换函数参数：光标移动到  first_name  上，按下  c i a  (Change Inner
  Argument)。
      • 结果： first_name  被删除且进入插入模式：
       let value = format_name(|, last_name);
  2. 给参数加双引号：退出到 Normal 模式，光标在  last_name  上，按下  y s i a "
  (Yank Surround Inner Argument with  " ).
      • 结果：
       let value = format_name(first_name, "last_name");
  3. 更改单双引号：光标在  last_name  内，按下  c s " '  (Change Surround  "  to
  ' ).
      • 结果：
       let value = format_name(first_name, 'last_name');
  4. 删除外围引号：按下  d s '  (Delete Surround  ' ).
      • 结果：回到无引号状态。


  ### 1. 如何启用 Vim 模式
  
    在您的 Zed 配置文件  settings.json （可以通过命令面板  Ctrl-Shift-P  并搜索
    open settings  打开）中添加：
  
      {
        "vim_mode": true
      }
      ──────
    ### 2. LSP 代码导航快捷键 (Normal 模式)
  
    Zed 将 Vim
    的跳转指令与内置语言服务器（LSP）进行了绑定，用于在代码符号、定义和引用之间穿梭
    。
  
     快捷键                   │ 绑定 Action              │ 详细说明
    ──────────────────────────┼──────────────────────────┼──────────────────────────
      g d  或  Ctrl-]         │ editor           │ 跳转到当前光标处符号的定
                              │                          │ 义位置
      Ctrl-w d  或  Ctrl-w ]  │  editor::GoToDefinitionSp│ 在分屏中打开并跳转到定义
                              │ lit                      │ 位置
      g shift-d               │  editor::GoToDeclaration │ 跳转到当前光标处符号的声
                              │                          │ 明位置
      g y                     │  editor::GoToTypeDefiniti│ 跳转到当前光标处符号的类
                              │ on                       │ 型定义位置
      g r i  或  g shift-i    │  editor::GoToImplementati│ 跳转到当前接口/Trait
                              │ on                       │ 的具体实现位置
      g r r  或  g shift-a    │  editor::FindAllReference│ 查找当前符号的所有引用（
                              │ s                        │ 会在侧边弹出引用列表）
      g s  或  g shift-o      │ outline           │ 切换/打开当前文件的大纲
                              │                          │ 面板 (Outline Panel)
      g shift-s               │ project_symbols           │ 全局模糊搜索项目中的所有
                              │                          │ 符号 (Project Symbols)
      Ctrl-o  /  Ctrl-i       │  pane::GoBack  /         │ 在您的编辑光标跳转历史中
                              │ pane::GoForward          │ 后退/前进
      Ctrl-^                  │  pane::AlternateFile     │ 在最近使用的两个文件（缓
                              │                          │ 冲区）之间快速交替切换
  
    #### 💡 实际使用示例
  
    • 查找并分屏看结构体定义：光标移动到  MyStruct  上，按下  Ctrl-w d 。Zed
    会在右侧分屏打开  MyStruct  定义所在的文件，左侧当前文件依然保留，方便对比阅读。
    • 寻找当前方法的所有调用者：光标移动到方法名上，按下  g r r
    ，右侧会列出项目内所有调用此方法的行，回车可直接跳转。
    ──────
    ### 3. 代码重构与基础编辑快捷键 (Normal 模式)
  
    在阅读和修改 Zed 源码时，用于批处理、重构和快速重命名的组合键。
  
     快捷键             │ 绑定 Action                 │ 详细说明
    ────────────────────┼─────────────────────────────┼─────────────────────────────
      g r n             │  editor::Rename             │ 重命名当前符号，会自动更新
                        │                             │ 所有引用此符号的文件
      c d               │  editor::Rename             │ 重命名当前符号（Zed 专属
                        │                             │ Vim-operator 快捷方式）
      g .  或  g r a    │  editor::ToggleCodeActions  │ 打开 Code Actions 菜单（即
                        │                             │ Quick Fix 快速修复补丁）
      g h  或  shift-k  │ editor              │ 显示当前符号的 LSP
                        │                             │ 悬浮文档说明 (Hover)
      g B               │  editor::BlameHover         │ 显示当前行的 Git Blame
                        │                             │ 详细悬浮提示（作者、提交哈
                        │                             │ 希、时间）
      g c               │ vim              │ 切换所选行或当前行的单行注
                        │                             │ 释状态
      g b               │  vim::PushToggleBlockComment│ 切换所选行或当前行的块注释
                        │ s                           │ ( /* ... */ ) 状态
      z a               │  editor::ToggleFold         │ 折叠/展开当前代码块
  
    #### 💡 实际使用示例
  
    • 修改变量名：光标在  user_id  变量上，输入  c d ，此时 Zed
    会弹出重命名输入框，输入新名字  account_id  并回车，全项目内所有  user_id
    会同步更改。
    • 修复 Rust 编译器报错：当某一行出现红波浪线报错时，光标移到其上，按下  g .
    。Zed 会弹出 LSP 自动修复建议（例如自动引入未导入的库），选择后即可秒级修复。
    ──────
    ### 4. 报错诊断与 Git 差异导航快捷键 (Normal 模式)
  
    专为日常开发中“修改-编译-排错”循环设计的强绑定。
  
     快捷键            │ 绑定 Action                 │ 详细说明
    ───────────────────┼─────────────────────────────┼──────────────────────────────
      ] d  或  g ]     │ editor              │ 跳转到文件中的下一个报错/警
                       │                             │ 告/诊断位置
     **`editor │ 跳转到文件中的上一个报错/警 │
                       │ 告/诊断位置                 │
      ] c              │  editor::GoToHunk           │ 跳转到当前文件的下一个 Git
                       │                             │ 修改块 (Hunk)
      [ c              │  editor::GoToPreviousHunk   │ 跳转到当前文件的上一个 Git
                       │                             │ 修改块
      d o              │  editor::ToggleSelectedDiffH│ 展开/折叠显示当前 Git
                       │ unks                        │ 修改块与 HEAD
                       │                             │ 版本的内联差异对比
      d p              │  git::Restore               │ 丢弃当前 Git
                       │                             │ 修改块的所有改动，恢复到
                       │                             │ HEAD 状态
      d u              │  git::StageAndNext          │ 将当前 Git 修改块加入暂存区
                       │                             │ (Stage)
                       │                             │ 并自动跳到下一个修改块
  
    #### 💡 实际使用示例
  
    • 遍历并暂存代码改动：做完一波小修改后，按下  [ c  跳到文件第一个修改处。按下  d
    o  确认改动无误，再按下  d u
    。这会自动暂存当前改动，并直接飞到下一个修改位置，无需频繁使用终端执行  git add
    。
    ──────
    ### 5. 窗口分屏与面板切换快捷键
  
    在编写和阅读复杂项目代码时，合理排布视口非常重要。
  
     快捷键                   │ 绑定 Action              │ 详细说明
    ──────────────────────────┼──────────────────────────┼──────────────────────────
      ctrl-w v  或  ctrl-w    │  pane::SplitVertical     │ 向右垂直分屏
     ctrl-v                   │                          │
      ctrl-w s  或  ctrl-w    │  pane::SplitHorizontal   │ 向下水平分屏
     ctrl-s                   │                          │
      ctrl-w h / j / k / l    │  workspace::ActivatePaneL│ 将焦点移动到 左/下/上/右
                              │ eft / Down / Up / Right  │ 侧的分屏
      ctrl-w shift-h / j / k  │  workspace::MovePaneLeft │ 将当前分屏整体移动到最左
     / l                      │ / Down / Up / Right      │ /最下/最上/最右边
      ctrl-w =                │  vim::ResetPaneSizes     │ 重置所有分屏的尺寸，使其
                              │                          │ 平均等宽/等高
      ctrl-w _                │  vim::MaximizePane       │ 最大化当前激活的分屏（收
                              │                          │ 起其他分屏）
      ctrl-w c  或  ctrl-w q  │  pane::CloseActiveItem   │ 关闭当前激活的标签页/分
                              │                          │ 屏
      g t  /  g shift-t       │  vim::GoToTab  /         │ 切换到下一个/上一个标签
                              │ vim::GoToPreviousTab     │ 页 (Tab)
    ──────
    ### 6. Vim 环绕字符 (Surround) 与进阶文本对象
  
    Zed 原生支持强大的  vim-surround
    操作。利用这些组合，您可以极其优雅地增删改括号和引号，以及选中语义化的代码块。
  
    #### A. 环绕操作 (Surround)
  
     快捷模式                 │ 对应 Action              │ 详细说明
    ──────────────────────────┼──────────────────────────┼──────────────────────────
      y s <motion> <char>     │  vim::PushAddSurrounds   │ 给指定运动范围内的内容添
                              │                          │ 加环绕字符
      d s <char>              │  vim::PushDeleteSurrounds│ 删除指定的环绕字符
                              │                          │
      c s <old_char>          │  vim::PushChangeSurrounds│ 修改指定的环绕字符为新字
     <new_char>               │                          │ 符
  
    #### B. 进阶文本对象 (Text Objects)
  
    搭配  c  (Change),  d  (Delete),  y  (Yank),  v  (Visual)
    等算子使用，可操作极具编程语言语义的范围。
  
     文本对象键 │ 对应操作范围                │ 说明
    ────────────┼─────────────────────────────┼─────────────────────────────────────
      a         │ 参数 (Argument)             │ 代表函数定义或调用中的某个参数（含
                │                             │ 逗号）
      f         │ 方法/函数 (Method/Function) │ 代表整个函数的代码块范围
      c         │ 类/结构体 (Class/Struct)    │ 代表整个类/结构体的代码块范围
      e         │ 整个文件 (Entire File)      │ 代表当前文件的全部内容
      q         │ 任意引号 (Quotes)           │ 智能识别最近的单/双/反引号并作为范
                │                             │ 围
  
    #### 💡 实际使用示例 (以 Rust 代码为例)
  
      // 初始代码状态
      let value = format_name(first_name, last_name);
  
    1. 替换函数参数：光标移动到  first_name  上，按下  c i a  (Change Inner
    Argument)。
        • 结果： first_name  被删除且进入插入模式：
         let value = format_name(|, last_name);
    2. 给参数加双引号：退出到 Normal 模式，光标在  last_name  上，按下  y s i a "
    (Yank Surround Inner Argument with  " ).
        • 结果：
         let value = format_name(first_name, "last_name");
    3. 更改单双引号：光标在  last_name  内，按下  c s " '  (Change Surround  "  to
    ' ).
        • 结果：
         let value = format_name(first_name, 'last_name');
    4. 删除外围引号：按下  d s '  (Delete Surround  ' ).
        • 结果：回到无引号状态。
  
    ──────
    ### 7. 插入模式下 Zed 智能快捷键 (Insert 模式)
  
    在插入模式下，Zed 提供了专属的 AI 生成和编辑提示操作。
  
     快捷键          │ 绑定 Action		│ 详细说明
    ─────────────────┼────────────────────────────┼─────────────────────────────────
      Ctrl-x Ctrl-a  │ assistant             │ 唤起 Inline AI
                     │				│ 助手输入框，输入自然语言即可在
                     │				│ 光标处生成/重写代码
      Ctrl-x Ctrl-c  │  editor::ShowEditPrediction│ 显示当前位置的 AI 内联编辑预测
                     │  				│ (AI Edit Prediction)
      Ctrl-x Ctrl-o  │  editor::ShowCompletions   │ 强制展开 LSP 的补全下拉菜单
      Ctrl-x Ctrl-l  │  editor::ToggleCodeActions │ 在插入模式下快速展开 Code
                     │				│ Actions 菜单
    ──────
    ### 8. 项目面板文件树快捷键 (Project Panel - netrw 兼容模式)
  
    当光标在左侧文件面板 (Project Panel) 中时，Zed 允许使用经典的 netrw/Vim
    风格键位。
  
     快捷键    │ 绑定 Action                     │ 详细说明
    ───────────┼─────────────────────────────────┼──────────────────────────────────
      %        │  project_panel::NewFile         │ 在当前目录下新建文件
      d        │  project_panel::NewDirectory    │ 在当前目录下新建文件夹
      h  /  l  │  CollapseSelectedEntry  /       │ 折叠/展开选中的文件夹目录
               │ ExpandSelectedEntry             │
      v        │  project_panel::OpenSplitVertica│ 将选中文件在垂直分屏中打开
               │ l                               │
      o        │  project_panel::OpenSplitHorizon│ 将选中文件在水平分屏中打开
               │ tal                             │
      shift-d  │  project_panel::Delete          │ 删除选中的文件/文件夹
      shift-r  │  project_panel::Rename          │ 对选中的文件/文件夹进行重命名
      x        │  project_panel::RevealInFileMana│ 在系统资源管理器（Windows 的
               │ ger                             │ File Explorer）中显示选中的文件
      escape   │  vim::ToggleProjectPanelFocus   │ 移开焦点，将光标放回主编辑器中
