GDB（GNU Debugger）是 Linux/UNIX 平台下最核心的底层调试工具。编写教材级别的 GDB 手册，需要涵盖从**启动**、**断点生命周期**、**执行控制**、**堆栈分析**、**内存/数据检查**到**多线程与底层汇编调试**的完整体系。

以下按模块梳理核心指令，附带长短参数、语法逻辑、注释与实战用例。

---

## 1. GDB 启动与调试会话管理

### 启动命令与常用参数

在 Shell 中启动 GDB 时支持多种参数以应对不同场景（普通调试、Core Dump 剖析、Attach 在线进程）。

* **语法**: `gdb [参数] [可执行程序] [Core文件|PID]`
* **常用长/短参数**:
* `-q`, `--quiet`, `--silent`: 静默启动，不打印版本和版权信息。
* `-tui`: 启动 GDB 内置的 Text User Interface（文本图形化界面），可直接分屏显示源码。
* `-p <PID>`, `--pid=<PID>`: 附加（Attach）到一个正在运行的进程进行调试。
* `-c <file>`, `--core=<file>`: 指定 Core Dump 转储文件进行事后剖析。
* `-x <file>`, `--command=<file>`: 启动后自动执行指定的 GDB 脚本文件。
* `-args <exec> [args...]`: 向被调试程序直接传递命令行参数。



```bash
# 1. 静默模式附加到 PID 为 1234 的进程
gdb -q -p 1234

# 2. 调试可执行程序并直接传入程序参数 -a -b 100
gdb --args ./my_server -a -b 100

# 3. 事后调试：结合可执行文件与崩溃生成的 core 文件
gdb ./my_server core.1234

```

### 会话内管理子命令

* `file <filename>`: 加载/替换当前调试的可执行文件及符号表。
* `attach <PID>`: 挂载到运行中的进程。
* `detach`: 脱离当前进程（被挂载进程会继续正常运行）。
* `kill`: 终止正在运行的子进程。
* `quit` (简写 `q`): 退出 GDB 会话。

---

## 2. 断点与监控（Breakpoints, Watchpoints, Catchpoints）

断点机制是 GDB 控制流程的核心，包含常规代码断点、硬件观察点和系统事件捕获点。

### 2.1 `break` (简写 `b`) - 设置断点

* **语法**: `break [位置] [if 条件]`
* **位置指定方式**:
* 行号：`b 42`（当前文件第 42 行），`b main.c:42`（指定文件行号）。
* 函数名：`b calculate_sum`，`b ClassName::method`（C++ 成员函数）。
* 内存地址：`b *0x004005d6`（汇编级断点）。
* 条件断点：`b 45 if i == 10`。


* **临时断点 `tbreak` (简写 `tb`)**: 触发一次后自动删除。
* **正则断点 `rbreak**`: 批量匹配函数名，如 `rbreak ^test_` 给所有以 `test_` 开头的函数下断点。

```gdb
# 在 main 函数入口设置断点
(gdb) b main

# 在 worker.cpp 的第 88 行设置条件断点，当 count > 1000 时触发
(gdb) b worker.cpp:88 if count > 1000

# 在特定函数入口设置单次临时断点
(gdb) tb init_system

```

### 2.2 `watch` / `rwatch` / `awatch` - 观察点（硬件/软件监控）

监控某块内存或变量的变化，利用 CPU 调试寄存器（如 x86 的 DR0-DR7）实现无侵入监控。

* `watch <expr>`: 当表达式/变量值被写入（修改）时中断。
* `rwatch <expr>`: 当变量**被读取**时中断（需硬件支持）。
* `awatch <expr>`: 当变量被读或写（访问）时中断。

```gdb
# 监控全局变量 g_status 何时被篡改
(gdb) watch g_status

# 监控指针指向的内存区域（16 字节大小）何时被修改
(gdb) watch *(int[4]*)0x7fffffffe000

```

### 2.3 `catch` - 捕获系统事件

* `catch throw`: 捕获 C++ 异常抛出瞬间。
* `catch catch`: 捕获 C++ 异常被捕获的瞬间。
* `catch syscall [name|num]`: 捕获系统调用（如 `catch syscall open`）。
* `catch fork` / `catch exec`: 捕获多进程派生或程序执行事件。

```gdb
# 在程序抛出任何未处理的 C++ 异常时立刻停下
(gdb) catch throw

```

### 2.4 断点管理命令

* `info breakpoints` (简写 `i b`): 查看所有断点、观察点的编号、类型、命中次数、启用状态。
* `enable [breakpoints] [delete|once] <nums...>`: 启用断点（`once` 为触发一次后禁用；`delete` 为触发后删除）。
* `disable [breakpoints] <nums...>`: 禁用断点（保留配置但不生效）。
* `delete [breakpoints] <nums...>` (简写 `d`): 删除指定断点；不带参数则删除全部。
* `condition <num> [expr]`: 为已存在的断点追加或清除条件（省略 expr 为清除）。
* `ignore <num> <count>`: 忽略指定断点接下来的 `count` 次命中。
* `commands <num>`: 设定命中该断点时自动执行的 GDB 批处理命令。

```gdb
# 为断点 2 设置命中自动化：打印变量后自动继续运行
(gdb) commands 2
> silent
> printf "Current idx: %d, value: %s\n", idx, ptr->name
> continue
> end

```

---

## 3. 程序执行控制（Execution Flow）

控制断点停下后的程序行进方向。

| 命令 | 简写 | 含义 | 行为说明 |
| --- | --- | --- | --- |
| `run [args]` | `r` | 运行程序 | 从头启动被调试程序，可传入运行参数（如 `r -v -f test.txt`）。 |
| `continue [N]` | `c` | 继续执行 | 恢复运行直到下一个断点；`c 5` 表示忽略此断点接下来的 4 次触发。 |
| `step [N]` | `s` | 单步步入（Step Into） | 进入当前行的子函数内部。支持源码行步进。 |
| `next [N]` | `n` | 单步步过（Step Over） | 将子函数调用作为单行执行完毕，不进入内部。 |
| `stepi [N]` | `si` | 汇编单步步入 | 按照单条机器指令步入。 |
| `nexti [N]` | `ni` | 汇编单步步过 | 按照单条机器指令步过（如执行一条 `call` 指令不跟踪内部）。 |
| `finish` | `fin` | 退出函数 | 运行至当前函数返回，并打印返回值。 |
| `until [loc]` | `u` | 运行至指定行/跳出循环 | 在循环体内使用 `until` 可以直接单步直到跳出当前循环体。 |
| `return [expr]` | - | 强制提前返回 | 不执行函数剩余指令，直接弹出当前帧并可选返回指定值。 |
| `jump <loc>` | `j` | 强制跳转PC指针 | 强行将指令计数器移动至指定行或地址（慎用，可能破坏栈平衡）。 |

```gdb
# 步入函数内部
(gdb) s

# 连续执行 3 条汇编指令
(gdb) ni 3

# 直接结束当前函数运行并获取返回值
(gdb) finish

```

---

## 4. 堆栈回溯与调用帧切换（Call Stack）

在程序崩溃或命中端点时，检查调用栈是定位问题的关键手段。

* `backtrace [full] [N]` (简写 `bt`):
* `bt`: 打印当前线程完整的调用栈。
* `bt full`: 打印调用栈的同时输出每个栈帧内的局部变量。
* `bt 5`: 只打印最内层（最顶层）5 层调用。
* `bt -5`: 只打印最外层（最底层）5 层调用。


* `frame [N]` (简写 `f`): 切换到指定编号的栈帧（0 为当前发生处，数字越大越向外层调用层推进）。
* `up [N]` / `down [N]`: 向外层（调用者）/ 内层（被调用者）移动 N 个栈帧。
* `info frame` (简写 `i f`): 打印当前栈帧详细信息（PC 指针、寄存器备份位置、栈基地址、局部变量起始偏移）。
* `info args`: 查看当前栈帧的入参。
* `info locals`: 查看当前栈帧所有的局部变量值。

```gdb
# 查看当前崩溃的完整堆栈和每一帧的局部变量
(gdb) bt full

# 切换到外层调用者（假设为 frame 2）以检查其上下文
(gdb) f 2

# 打印该函数接收的参数值
(gdb) info args

```

---

## 5. 数据检查、输出与内存审查

### 5.1 `print` (简写 `p`) - 表达式与数据输出

* **语法**: `print [/格式] <表达式>`
* **格式控制符 (`/F`)**:
* `/x`: 十六进制
* `/d`: 有符号十进制
* `/u`: 无符号十进制
* `/o`: 八进制
* `/t` 或 `/b`: 二进制
* `/c`: 字符
* `/f`: 浮点数
* `/s`: 字符串


* **类型转换与动态数组切片**:
* `p (char*)ptr`: 强制指针转换。
* `p *array@10`: 打印从 `array` 指针开始的连续 10 个元素（动态数组打印利器）。



```gdb
# 以 16 进制打印变量 status
(gdb) p /x status

# 打印动态分配数组的前 8 个元素
(gdb) p *buf@8

# 调用类方法或 C 库函数（会实际在目标进程中执行一次）
(gdb) p strlen(my_string)

```

### 5.2 `x` (Examine) - 检查底层物理/虚拟内存

* **语法**: `x /[数量][格式][单体尺寸] <内存地址/指针>`
* **单体尺寸 (Size)**:
* `b`: 1 字节（byte）
* `h`: 2 字节（halfword）
* `w`: 4 字节（word，默认）
* `g`: 8 字节（giant word）


* **格式符 (Format)**: 与 `print` 类似，常见有 `x`(hex), `d`(decimal), `s`(string), `i`(instruction 机器指令)。

```gdb
# 从当前 PC 寄存器开始，反汇编接下来的 5 条指令
(gdb) x /5i $pc

# 从 0x7fffffffe100 处，以十六进制格式读取 16 个 4 字节（word）的连续内存
(gdb) x /16xw 0x7fffffffe100

# 读取指定内存中以 NULL 结尾的字符串
(gdb) x /s 0x402010

```

### 5.3 `display` - 自动刷新显示

在每次执行停下（如每次 `step` 或 `next`）后自动打印指定表达式。

* `display <expr>`: 添加自动显示项。
* `info display`: 查看所有自动显示编号。
* `undisplay <nums...>`: 删除自动显示。
* `disable/enable display <nums...>`: 禁用/启用。

---

## 6. 多线程与多进程调试

现代后端应用普遍多线程/多进程，GDB 提供了对线程的感知与控制能力。

### 6.1 多线程（Thread）

* `info threads`: 列出当前进程所有线程（ID、LWP 核心线程号、当前停留在哪个函数）。
* `thread <ID>` (简写 `t <ID>`): 切换调试上下文到指定编号的线程。
* `thread apply <ID-list|all> <command>`: 批量在多个线程或所有线程上执行同一条 GDB 指令。
* `set scheduler-locking [off|on|step]`:
* `off`: 默认模式，单步调试当前线程时，其他线程也并发运行。
* `on`: 锁定调度器，只有当前被调试的线程会运行，其余线程暂停（排查死锁与并发竞争的核心配置）。
* `step`: 单步（`step`/`next`）调试时锁定其他线程，使用 `continue` 时恢复并发。



```gdb
# 打印所有线程当前的堆栈信息（定位死锁时必用）
(gdb) thread apply all bt

# 开启调度器锁定，避免单步时其它线程跑偏干扰现场
(gdb) set scheduler-locking on

```

### 6.2 多进程派生（Fork）

* `set follow-fork-mode [parent|child]`: 设置在程序发生 `fork()` 后，GDB 继续跟踪父进程还是跟踪新派生的子进程。
* `set detach-on-fork [on|off]`:
* `on`: （默认）只跟踪被选中的分支，另一个分支脱离 GDB 继续运行。
* `off`: 两个分支均被 GDB 挂起接管，使用 `info inferiors` 切换调试目标。



```gdb
# 设置 fork 后由 GDB 跟踪子进程
(gdb) set follow-fork-mode child
(gdb) set detach-on-fork off

```

---

## 7. 底层汇编与寄存器

针对崩溃（如 SIGSEGV）没有符号表（Release 模式）时的汇编级分析。

* `info registers` (简写 `i r`): 打印所有通用寄存器（rax, rbx, rip, rsp 等）的当前值。
* `info registers <reg_name>`: 查看单个寄存器，如 `i r rsp`。
* `print $rax`: 直接读取寄存器值并参与计算。
* `set $rax = 0`: 运行时直接修改寄存器数值。
* `disassemble [location]` (简写 `disas`):
* `disas`: 反汇编当前执行函数。
* `disas /m <func>`: 将源代码与汇编指令混合交织打印（需调试符号）。
* `disas /r <func>`: 反汇编同时打印 Hex 机器指令字节（Raw bytes）。
* `disas 0x400500, 0x400550`: 反汇编指定内存区间。



```gdb
# 源码与汇编交替展示当前 main 函数
(gdb) disas /m main

# 查看栈指针寄存器的十六进制值
(gdb) p /x $rsp

```

---

## 8. GDB 调试辅助与持久化配置

* `set print pretty on`: 结构体、C++ STL 容器（如 `std::vector`, `std::map`）自动美化换行缩进打印。
* `set pagination off`: 禁用分页输出（防止大输出量时不断弹出 `--Type <RET> for more, q to quit--`），适合保存日志。
* `set logging on` / `set logging off`: 开启/关闭将控制台的所有会话输出同步记录至 `gdb.txt`。
* `source <script.py|script.gdb>`: 加载外部自定义 GDB 自动化脚本或 Python 扩展脚本。
* `~/.gdbinit`: GDB 启动时自动读取的配置文件，可将通用设置放入其中：

```text
# 示例 ~/.gdbinit 推荐配置
set print pretty on
set print object on
set print static-members on
set pagination off
set history save on
set history size 10000

```
