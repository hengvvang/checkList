下面用一个**完全假定存在的 STM32 + ST-Link 环境**，系统介绍 OpenOCD。你不需要现在拥有硬件；先理解流程，之后把假设中的型号、接口和文件替换成自己的实际设备即可。

整个实验环境假定为：

| 项目 | 假设值 |
|---|---|
| 操作系统 | Windows 10/11 |
| 调试器 | ST-Link V2 |
| 目标芯片 | STM32F103C8T6 |
| 调试接口 | SWD |
| OpenOCD | 0.12.x |
| 编译器 | Arm GNU Toolchain |
| GDB | `arm-none-eabi-gdb` |
| 工程目录 | `C:\openocd-lab` |
| 固件文件 | `C:\openocd-lab\build\app.elf` |

---

# 1. OpenOCD 是什么

OpenOCD 全称是 **Open On-Chip Debugger**，作用是通过调试器访问微控制器内部的调试接口。

它通常位于下面这条链路中：

```text
GDB / IDE
    |
    | TCP 3333
    v
OpenOCD
    |
    | USB
    v
ST-Link / J-Link / CMSIS-DAP
    |
    | SWD / JTAG
    v
STM32 芯片
```

OpenOCD 主要负责：

1. 识别调试器；
2. 连接目标芯片；
3. 通过 SWD 或 JTAG 访问芯片；
4. 擦除 Flash；
5. 写入固件；
6. 读取寄存器和内存；
7. 控制 CPU 运行、暂停、单步；
8. 为 GDB 提供远程调试服务；
9. 提供 Telnet 命令行；
10. 执行自动化脚本。

OpenOCD 本身不是编译器，也不是 GDB。

它们的分工是：

| 工具 | 作用 |
|---|---|
| GCC | 编译 C/C++ 代码 |
| Linker | 生成 ELF、HEX、BIN |
| OpenOCD | 连接芯片、烧录、控制调试器 |
| GDB | 设置断点、查看变量、单步调试 |
| IDE | 组织和调用上述工具 |

---

# 2. 先建立几个重要概念

## 2.1 SWD 和 JTAG

STM32 常见的调试接口有两种。

### SWD

SWD 是 ARM 的两线调试接口，常见信号为：

```text
SWDIO
SWCLK
GND
VTref
NRST，可选
```

优点：

- 引脚少；
- STM32 使用非常普遍；
- ST-Link 默认经常使用 SWD。

### JTAG

JTAG 使用更多信号：

```text
TCK
TMS
TDI
TDO
nTRST
GND
VTref
```

JTAG 除了调试 CPU，还常用于边界扫描和多器件级联。

本教程使用：

```text
ST-Link V2 + SWD + STM32F103
```

---

## 2.2 调试器和目标芯片

ST-Link 不是目标芯片，它是一个 USB 调试器。

```text
电脑 USB
  |
  v
ST-Link
  |
  | SWD
  v
STM32
```

OpenOCD 同时需要知道两件事：

1. 使用什么**调试器接口配置**；
2. 连接什么**目标芯片配置**。

因此命令通常有两个配置文件：

```text
-f interface/stlink.cfg
-f target/stm32f1x.cfg
```

前者描述 ST-Link，后者描述 STM32F1 系列。

---

## 2.3 OpenOCD 的三个端口

OpenOCD 默认会监听三个 TCP 端口。

| 端口 | 用途 |
|---|---|
| 3333 | GDB 调试端口 |
| 4444 | Telnet 命令端口 |
| 6666 | TCL 命令端口 |

最常用的是：

```text
3333：GDB 使用
4444：Telnet 使用
6666：自动化脚本使用
```

---

# 3. 安装软件

## 3.1 安装 OpenOCD

在 Windows 上安装 OpenOCD 后，假定目录为：

```text
C:\OpenOCD
```

应当能看到类似目录：

```text
C:\OpenOCD\bin
C:\OpenOCD\share\openocd\scripts
```

其中：

```text
C:\OpenOCD\bin\openocd.exe
```

是主程序。

配置文件通常位于：

```text
C:\OpenOCD\share\openocd\scripts
```

里面常见目录包括：

```text
interface
target
board
config
```

例如：

```text
interface\stlink.cfg
target\stm32f1x.cfg
```

---

## 3.2 安装 Arm GNU Toolchain

安装 Arm GNU Toolchain 后，假定 GDB 位于：

```text
C:\ArmGNU\bin\arm-none-eabi-gdb.exe
```

你需要确保下面两个目录加入 Windows 的 `PATH`：

```text
C:\OpenOCD\bin
C:\ArmGNU\bin
```

打开新的 PowerShell，验证版本：

```powershell
openocd --version
```

再验证 GDB：

```powershell
arm-none-eabi-gdb --version
```

这里的命令由你自己执行。

如果提示“不是内部或外部命令”，通常是：

- 没有安装；
- `PATH` 没有配置；
- 当前终端是在修改 `PATH` 之前打开的；
- 使用了错误的安装目录。

---

# 4. 设计实验目录

请在你自己的电脑上创建以下目录：

```text
C:\openocd-lab
C:\openocd-lab\config
C:\openocd-lab\build
C:\openocd-lab\scripts
C:\openocd-lab\logs
```

最终结构如下：

```text
C:\openocd-lab
├── config
├── build
├── scripts
└── logs
```

后续假定：

```text
C:\openocd-lab\build\app.elf
C:\openocd-lab\build\app.hex
C:\openocd-lab\build\app.bin
```

这三个文件分别代表：

| 文件 | 说明 |
|---|---|
| ELF | 带符号信息，最适合 GDB 调试 |
| HEX | 带地址信息，适合烧录 |
| BIN | 裸二进制，需要额外指定烧录地址 |

---

# 5. 第一个 OpenOCD 配置文件

创建文件：

```text
C:\openocd-lab\config\stm32f103-stlink.cfg
```

内容如下：

```tcl
source [find interface/stlink.cfg]

transport select hla_swd

source [find target/stm32f1x.cfg]

reset_config srst_only srst_nogate connect_assert_srst
adapter speed 4000
```

逐行解释：

```tcl
source [find interface/stlink.cfg]
```

加载 ST-Link 接口配置。

```tcl
transport select hla_swd
```

选择 SWD 调试协议。

这里的 `hla` 是 High-Level Adapter，ST-Link 的常见 OpenOCD 驱动模式。

```tcl
source [find target/stm32f1x.cfg]
```

加载 STM32F1 系列目标芯片配置。

```tcl
reset_config srst_only srst_nogate connect_assert_srst
```

配置复位行为：

- `srst` 表示系统复位；
- `connect_assert_srst` 表示在复位期间尝试连接目标；
- 对于运行异常或读保护状态的芯片，复位连接有时更可靠。

```tcl
adapter speed 4000
```

设置调试时钟为 4000 kHz。

如果连接不稳定，可以降低为：

```tcl
adapter speed 1000
```

甚至：

```tcl
adapter speed 100
```

速度越低，通常越容易连接长线、供电不稳定或启动较慢的目标。

---

# 6. 启动 OpenOCD 服务器

打开 PowerShell，进入实验目录：

```powershell
Set-Location C:\openocd-lab
```

启动 OpenOCD：

```powershell
openocd -f .\config\stm32f103-stlink.cfg
```

正常情况下，OpenOCD 会持续运行，不会立即返回命令提示符。

你应该看到类似信息：

```text
Open On-Chip Debugger 0.12.x
Info : auto-selecting first available session transport "hla_swd"
Info : The selected transport took over low-level target control
Info : clock speed 4000 kHz
Info : STLINK V2JxxSxx
Info : Target voltage: 3.3xxx V
Info : [stm32f1x.cpu] Cortex-M3 r2p1 processor detected
Info : [stm32f1x.cpu] hardware has 6 breakpoints, 4 watchpoints
Info : gdb server for stm32f1x.cpu on 3333
Info : Listening on port 3333 for gdb connections
```

这些输出非常重要。

## 6.1 常见输出含义

### `Target voltage`

```text
Target voltage: 3.3xxx V
```

表示 ST-Link 检测到了目标板电压。

这不一定代表目标芯片工作正常，但通常说明：

- 目标板已供电；
- ST-Link 的电压参考线连接正确；
- 电气连接至少部分正常。

### `Cortex-M3`

STM32F103 使用 Cortex-M3 内核。

### `hardware has 6 breakpoints`

表示硬件断点资源数量。

### `hardware has 4 watchpoints`

表示硬件观察点资源数量。

### `Listening on port 3333`

表示 GDB 可以连接：

```text
localhost:3333
```

---

# 7. 通过 Telnet 操作 OpenOCD

保持 OpenOCD 窗口运行。

另开一个 PowerShell，执行：

```powershell
telnet localhost 4444
```

Windows 可能默认没有启用 Telnet 客户端。如果提示找不到 `telnet`，可以在“启用或关闭 Windows 功能”中启用 Telnet Client。

连接成功后，会进入 OpenOCD 命令行。

你可以执行：

```text
help
```

查看命令帮助。

查看目标状态：

```text
targets
```

暂停 CPU：

```text
halt
```

查看 CPU 状态：

```text
targets
```

继续运行：

```text
resume
```

复位并暂停：

```text
reset halt
```

复位并运行：

```text
reset run
```

退出 OpenOCD：

```text
shutdown
```

注意：

- `shutdown` 是 OpenOCD 命令；
- 它不是 PowerShell 命令；
- Telnet 窗口中输入的命令和 PowerShell 中输入的命令不同。

---

# 8. 查看芯片信息

## 8.1 查看 Flash 信息

在 Telnet 中执行：

```text
flash info 0
```

可能看到：

```text
#0 : stm32f1x.flash
  stm32f1x.flash bank 0
  size 64kbytes
  buswidth 0
  chip_width 0
  pagesize 1024
```

这里可以了解：

- Flash 总容量；
- 页大小；
- Flash bank；
- 擦除组织方式。

STM32F103C8 常见 Flash 容量是 64 KB，但具体芯片和仿制型号可能不同，不能只根据型号字母推断。

---

## 8.2 查看 CPU 寄存器

暂停 CPU 后执行：

```text
reg
```

可以查看寄存器。

常见寄存器包括：

| 寄存器 | 作用 |
|---|---|
| `r0` - `r12` | 通用寄存器 |
| `sp` | 栈指针 |
| `lr` | 返回地址寄存器 |
| `pc` | 程序计数器 |
| `xPSR` | 程序状态寄存器 |
| `msp` | 主栈指针 |
| `psp` | 进程栈指针 |
| `primask` | 中断屏蔽状态 |
| `control` | 当前线程控制状态 |

查看单个寄存器：

```text
reg pc
```

---

## 8.3 读取内存

OpenOCD 读取内存的基本格式是：

```text
mdw 地址 数量
```

例如读取 Flash 起始地址：

```text
mdw 0x08000000 4
```

`mdw` 中的 `w` 表示 word，通常是 32 位。

常用命令：

| 命令 | 宽度 |
|---|---|
| `mdb` | byte，8 位 |
| `mdh` | halfword，16 位 |
| `mdw` | word，32 位 |

读取 SRAM 起始区域：

```text
mdw 0x20000000 4
```

读取外设寄存器：

```text
mdw 0x40021000 4
```

写入内存：

```text
mww 地址 数据
```

例如：

```text
mww 0x20000000 0x12345678
```

注意：随意写外设寄存器可能导致：

- 时钟改变；
- GPIO 状态改变；
- 中断异常；
- 外设停止工作；
- 系统锁死。

不熟悉寄存器定义时，优先使用只读命令。

---

# 9. 使用 OpenOCD 烧录 ELF 文件

确保 OpenOCD 已经在一个窗口中运行。

在另一个 PowerShell 中执行：

```powershell
openocd `
  -f .\config\stm32f103-stlink.cfg `
  -c "program .\build\app.elf verify reset exit"
```

PowerShell 的反引号 `` ` `` 表示命令换行。

也可以写成一行：

```powershell
openocd -f .\config\stm32f103-stlink.cfg -c "program .\build\app.elf verify reset exit"
```

这条命令的含义是：

```text
program       烧录文件
.\build\app.elf
verify        烧录后校验
reset         复位目标芯片
exit          完成后退出 OpenOCD
```

这是最常用的自动烧录形式。

---

## 9.1 烧录 HEX

```powershell
openocd -f .\config\stm32f103-stlink.cfg -c "program .\build\app.hex verify reset exit"
```

HEX 文件已经包含地址信息，因此不需要指定地址。

---

## 9.2 烧录 BIN

BIN 文件不包含地址信息，所以必须指定地址：

```powershell
openocd -f .\config\stm32f103-stlink.cfg -c "program .\build\app.bin 0x08000000 verify reset exit"
```

STM32 通常从以下地址映射 Flash：

```text
0x08000000
```

如果你的 Bootloader 占用了前面一部分空间，例如应用程序从 `0x08004000` 开始，则命令应改为：

```powershell
openocd -f .\config\stm32f103-stlink.cfg -c "program .\build\app.bin 0x08004000 verify reset exit"
```

BIN 烧录时地址错误是非常常见的问题。

---

# 10. 擦除 Flash

## 10.1 擦除所有 Flash

```powershell
openocd -f .\config\stm32f103-stlink.cfg -c "init; reset halt; flash erase_sector 0 0 last; reset run; shutdown"
```

这条命令的结构是：

```text
init
reset halt
flash erase_sector 0 0 last
reset run
shutdown
```

其中：

```text
flash erase_sector 0 0 last
```

表示：

- Flash bank 为 `0`；
- 从第 `0` 个扇区开始；
- 擦除到 `last`。

实际扇区组织依目标芯片配置而定。

---

## 10.2 mass erase

某些目标支持：

```text
stm32f1x mass_erase 0
```

完整命令：

```powershell
openocd -f .\config\stm32f103-stlink.cfg -c "init; reset halt; stm32f1x mass_erase 0; shutdown"
```

这会擦除整个 Flash，包括：

- 用户程序；
- Bootloader；
- 配置数据；
- 可能的校准数据。

不要把 mass erase 当成普通烧录前的必需步骤。

---

# 11. 使用 GDB 调试

## 11.1 启动 OpenOCD

启动：

```powershell
openocd -f .\config\stm32f103-stlink.cfg
```

保持窗口不关闭。

---

## 11.2 启动 GDB

另开 PowerShell：

```powershell
Set-Location C:\openocd-lab
arm-none-eabi-gdb .\build\app.elf
```

进入 GDB 后，连接 OpenOCD：

```text
target extended-remote localhost:3333
```

复位并暂停：

```text
monitor reset halt
```

查看当前寄存器：

```text
info registers
```

继续运行：

```text
continue
```

暂停程序：

```text
interrupt
```

设置 `main` 函数断点：

```text
break main
```

重新复位：

```text
monitor reset halt
```

运行到断点：

```text
continue
```

单步执行一行源码：

```text
next
```

进入函数：

```text
step
```

执行一条汇编指令：

```text
 stepi
```

查看当前源代码位置：

```text
list
```

查看当前调用栈：

```text
backtrace
```

查看局部变量：

```text
info locals
```

查看变量：

```text
print variable_name
```

查看变量地址：

```text
print &variable_name
```

查看内存：

```text
x/16wx 0x20000000
```

含义：

```text
x       examine，检查内存
16      读取 16 个单位
w       每个单位 32 位
x       使用十六进制显示
```

删除断点：

```text
delete
```

查看断点：

```text
info breakpoints
```

退出 GDB：

```text
quit
```

---

## 11.3 GDB 中的 `monitor`

GDB 自己不理解 OpenOCD 的所有命令，因此使用：

```text
monitor 命令
```

把命令转发给 OpenOCD。

例如：

```text
monitor reset halt
```

```text
monitor flash info 0
```

```text
monitor mdw 0x08000000 4
```

```text
monitor halt
```

```text
monitor resume
```

---

# 12. GDB 加载固件

如果 ELF 已经编译完成，可以让 GDB 直接烧录：

```text
target extended-remote localhost:3333
monitor reset halt
load
monitor reset halt
```

`load` 会根据 ELF 文件中的段地址烧录程序。

完整过程通常是：

```text
arm-none-eabi-gdb .\build\app.elf
```

进入 GDB 后：

```text
target extended-remote localhost:3333
monitor reset halt
load
break main
continue
```

对比两种烧录方式：

| 方式 | 适合场景 |
|---|---|
| OpenOCD `program` | 自动烧录、脚本、生产流程 |
| GDB `load` | 烧录后立即调试 |
| IDE 调试按钮 | 日常开发 |

---

# 13. 理解 ELF、HEX 和 BIN

## ELF

ELF 通常包含：

- 代码；
- 数据；
- 地址；
- 调试符号；
- 源代码行号；
- 函数名；
- 变量信息。

因此最适合：

```text
GDB 调试
断点
查看变量
源码单步
```

## HEX

Intel HEX 文件是文本格式，包含：

- 数据；
- 地址；
- 校验信息。

适合烧录工具使用。

## BIN

BIN 只是连续的原始字节流：

```text
字节 0
字节 1
字节 2
...
```

它不知道自己应该被放到什么地址，所以烧录时必须显式指定地址。

---

# 14. 复位方式

OpenOCD 中常见命令：

```text
reset halt
```

复位后暂停。

```text
reset run
```

复位后运行。

```text
reset init
```

复位并执行初始化。

```text
halt
```

暂停 CPU。

```text
resume
```

继续执行。

不同复位类型可能包括：

- 软件复位；
- SYSRESETREQ；
- 看门狗复位；
- NRST 外部复位；
- 上电复位；
- 复位时连接。

如果芯片一启动就关闭调试接口、进入低功耗或配置错误，普通连接可能失败，可以尝试在配置文件中使用：

```tcl
reset_config srst_only srst_nogate connect_assert_srst
```

如果目标板没有连接 NRST，某些复位策略可能不可用。

---

# 15. 断点和观察点

## 15.1 断点

断点分为：

### 硬件断点

由 Cortex-M 的调试硬件实现。

优点：

- 可以在 Flash 中断点；
- 不修改程序代码。

缺点：

- 数量有限。

查看断点资源通常可以看到类似：

```text
6 hardware breakpoints
```

### 软件断点

GDB 修改 RAM 中的代码或通过其他方式实现。

在微控制器 Flash 上，软件断点通常不如硬件断点方便。

---

## 15.2 观察点

观察点用于监视变量或内存被访问。

GDB 示例：

```text
watch counter
```

表示变量写入时暂停。

```text
rwatch counter
```

表示变量读取时暂停。

```text
awatch counter
```

表示读取或写入时暂停。

观察点同样受到硬件资源限制。

---

# 16. 调试优化问题

如果编译时启用了较高优化，例如：

```text
-O2
```

或：

```text
-O3
```

可能出现：

- 变量显示为 `<optimized out>`；
- 单步跳跃；
- 源码行和汇编顺序不一致；
- 函数被内联；
- 断点位置不稳定。

调试版本通常使用：

```text
-Og -g3
```

或者：

```text
-O0 -g3
```

推荐：

```text
-Og -g3
```

因为它在保留较好调试体验的同时，不会完全放弃优化。

---

# 17. 查看启动向量表

Cortex-M 芯片通常从 Flash 起始位置读取向量表。

STM32F1 的 Flash 通常从：

```text
0x08000000
```

开始。

向量表前两个 word 通常是：

```text
0x08000000：初始栈指针
0x08000004：Reset_Handler 地址
```

读取：

```text
mdw 0x08000000 8
```

理论上：

- 第一个值应该像一个 SRAM 地址，例如 `0x2000xxxx`；
- 第二个值应该像一个 Flash 地址，例如 `0x0800xxxx`；
- Cortex-M 函数地址最低位通常为 `1`，表示 Thumb 状态。

如果向量表明显不正确，可能说明：

- 没有成功烧录；
- 烧录地址错误；
- 链接脚本错误；
- 启动文件错误；
- Bootloader 跳转地址错误。

---

# 18. Bootloader 场景

假定 Flash 布局如下：

```text
0x08000000 - 0x08003FFF    Bootloader
0x08004000 - 结束          Application
```

那么应用程序不能继续按照 `0x08000000` 链接。

应用程序的链接地址应设置为：

```text
0x08004000
```

烧录 BIN：

```powershell
openocd -f .\config\stm32f103-stlink.cfg -c "program .\build\app.bin 0x08004000 verify reset exit"
```

烧录 HEX 或 ELF 时，地址通常已经包含在文件内部：

```powershell
openocd -f .\config\stm32f103-stlink.cfg -c "program .\build\app.hex verify reset exit"
```

但是，文件中的地址必须和链接脚本一致。

Bootloader 跳转到应用程序时，通常还需要处理：

1. 设置主栈指针；
2. 设置向量表偏移；
3. 关闭或清理中断；
4. 跳转到应用程序复位处理函数。

在 STM32F1 上，向量表偏移通常涉及：

```text
SCB->VTOR
```

---

# 19. 保护机制

STM32 常见保护概念：

## Readout Protection

读保护会限制调试器读取 Flash。

表现可能包括：

- 无法读取 Flash；
- 连接后目标状态异常；
- 需要 mass erase 才能恢复；
- 芯片连接成功但无法正常调试。

关闭读保护通常会擦除 Flash。

不要在没有备份的情况下尝试解除保护。

## Write Protection

写保护会阻止某些 Flash 页被修改。

表现可能包括：

- 烧录失败；
- 擦除失败；
- 校验失败；
- 某些区域无法写入。

## Option Bytes

Option Bytes 用于配置：

- 读保护；
- 写保护；
- 看门狗模式；
- Brown-out 级别；
- Boot 配置；
- 复位行为。

Option Bytes 操作必须非常谨慎，因为错误配置可能导致：

- 芯片无法正常启动；
- 调试连接困难；
- 自动复位；
- 需要完整擦除恢复。

---

# 20. 记录日志

可以把 OpenOCD 输出保存到日志：

```powershell
openocd `
  -f .\config\stm32f103-stlink.cfg `
  -l .\logs\openocd.log
```

也可以增加调试级别：

```powershell
openocd `
  -d3 `
  -f .\config\stm32f103-stlink.cfg `
  -l .\logs\openocd-debug.log
```

日志级别通常从低到高：

```text
-d0
-d1
-d2
-d3
-d4
-d5
```

常用：

```text
-d3
```

调试连接失败时，重点查看：

- 是否识别 ST-Link；
- 目标电压是否存在；
- 传输协议是否正确；
- 目标芯片 ID 是否识别；
- reset 配置是否冲突；
- SWD 时钟是否过高。

---

# 21. 用命令行自动完成烧录

可以创建文件：

```text
C:\openocd-lab\scripts\flash.tcl
```

内容：

```tcl
adapter speed 4000

init
reset halt

flash info 0

program C:/openocd-lab/build/app.elf verify

reset run
shutdown
```

然后执行：

```powershell
openocd `
  -f .\config\stm32f103-stlink.cfg `
  -s .\scripts `
  -f .\scripts\flash.tcl
```

注意 Tcl 路径中通常使用正斜杠：

```tcl
C:/openocd-lab/build/app.elf
```

而 PowerShell 路径通常使用反斜杠：

```powershell
C:\openocd-lab\build\app.elf
```

也可以不写绝对路径，使用：

```tcl
program build/app.elf verify
```

但这依赖 OpenOCD 当前工作目录和搜索路径，初学阶段使用绝对路径更容易排错。

---

# 22. 用 OpenOCD 的 TCL 端口

OpenOCD 默认监听：

```text
localhost:6666
```

可以用 Tcl 客户端发送命令。

例如使用 PowerShell 建立 TCP 连接：

```powershell
$client = New-Object System.Net.Sockets.TcpClient("localhost", 6666)
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$reader = New-Object System.IO.StreamReader($stream)

$writer.WriteLine("reset halt")
$writer.Flush()

$reader.ReadLine()

$client.Close()
```

这个例子展示了自动化原理：

```text
脚本
  |
  | TCP 6666
  v
OpenOCD TCL 服务
```

实际自动化时，通常直接使用 OpenOCD 的 `-c` 参数或 Tcl 配置文件，除非你需要从其他程序动态控制调试器。

---

# 23. 常见错误和排查顺序

## 23.1 找不到 OpenOCD

错误类似：

```text
openocd is not recognized
```

检查：

```powershell
Get-Command openocd
```

如果没有结果：

- 检查 OpenOCD 是否安装；
- 检查 `C:\OpenOCD\bin` 是否加入 PATH；
- 关闭并重新打开 PowerShell。

也可以直接使用绝对路径：

```powershell
C:\OpenOCD\bin\openocd.exe --version
```

---

## 23.2 找不到配置文件

错误类似：

```text
Can't find interface/stlink.cfg
```

这通常表示 OpenOCD 没有找到 scripts 目录。

可以显式指定脚本搜索路径：

```powershell
openocd `
  -s C:\OpenOCD\share\openocd\scripts `
  -f .\config\stm32f103-stlink.cfg
```

---

## 23.3 无法打开 ST-Link

可能原因：

- USB 驱动未安装；
- ST-Link 被其他程序占用；
- ST-Link 固件过旧；
- 使用了错误的接口配置；
- USB 线只有充电功能；
- Windows 设备管理器没有识别设备。

排查方向：

1. 查看设备管理器；
2. 关闭 STM32CubeProgrammer；
3. 关闭其他 IDE 调试会话；
4. 重新插拔调试器；
5. 检查 ST-Link 驱动；
6. 尝试另一个 USB 接口。

---

## 23.4 `Target voltage: 0.000000`

通常表示：

- 目标板没有供电；
- VTref 没有连接；
- GND 没有连接；
- 调试器和目标板电平不匹配；
- 目标板电源开关关闭。

ST-Link 的 VTref 不是简单的“给目标板供电线”，它主要用于让调试器知道目标电平。

---

## 23.5 无法识别目标芯片

可能原因：

- SWDIO 和 SWCLK 接反；
- GND 没连接；
- 目标芯片没有供电；
- SWD 时钟太快；
- 芯片正在运行低功耗状态；
- 复位线配置不正确；
- 芯片启用了读保护；
- 固件重配置了 SWD 引脚。

先降低速度：

```tcl
adapter speed 1000
```

仍然失败时：

```tcl
adapter speed 100
```

然后尝试：

```text
reset halt
```

或者使用带复位连接的配置。

---

## 23.6 GDB 连接不上 3333

确认 OpenOCD 正在运行，并且输出中包含：

```text
Listening on port 3333 for gdb connections
```

检查端口：

```powershell
Test-NetConnection localhost -Port 3333
```

如果端口没有监听：

- OpenOCD 已经退出；
- 配置文件有错误；
- 目标初始化失败；
- 端口被其他程序占用。

---

## 23.7 `program` 后校验失败

可能原因：

- Flash 写保护；
- 文件链接地址错误；
- 目标芯片型号配置错误；
- 电源不稳定；
- 调试速度过高；
- Flash 擦除没有完成；
- ELF/BIN 地址错误。

优先尝试：

```tcl
adapter speed 1000
```

并确认：

```text
flash info 0
```

以及 ELF 的段地址。

---

# 24. 推荐的第一次完整实验

假定你已经安装好了软件，并且目标硬件真的连接好了。

## 第一步：确认工具

```powershell
openocd --version
```

```powershell
arm-none-eabi-gdb --version
```

## 第二步：进入实验目录

```powershell
Set-Location C:\openocd-lab
```

## 第三步：启动 OpenOCD

```powershell
openocd -f .\config\stm32f103-stlink.cfg
```

保持这个窗口运行。

## 第四步：打开 Telnet

```powershell
telnet localhost 4444
```

## 第五步：查看目标

```text
targets
```

## 第六步：复位并暂停

```text
reset halt
```

## 第七步：查看芯片信息

```text
flash info 0
```

## 第八步：查看向量表

```text
mdw 0x08000000 8
```

## 第九步：退出 Telnet

```text
shutdown
```

如果不想关闭 OpenOCD，也可以直接断开 Telnet 客户端；如果执行 `shutdown`，OpenOCD 会停止。

## 第十步：烧录 ELF

```powershell
openocd -f .\config\stm32f103-stlink.cfg -c "program .\build\app.elf verify reset exit"
```

## 第十一步：重新启动 OpenOCD

```powershell
openocd -f .\config\stm32f103-stlink.cfg
```

## 第十二步：启动 GDB

```powershell
arm-none-eabi-gdb .\build\app.elf
```

在 GDB 中执行：

```text
target extended-remote localhost:3333
```

```text
monitor reset halt
```

```text
break main
```

```text
continue
```

如果程序确实包含 `main`，GDB 应该在 `main` 处停下来。

然后练习：

```text
info registers
```

```text
backtrace
```

```text
list
```

```text
next
```

```text
continue
```

---

# 25. 最常用命令速查表

## OpenOCD 启动

```powershell
openocd -f .\config\stm32f103-stlink.cfg
```

## 自动烧录

```powershell
openocd -f .\config\stm32f103-stlink.cfg -c "program .\build\app.elf verify reset exit"
```

## 烧录 BIN

```powershell
openocd -f .\config\stm32f103-stlink.cfg -c "program .\build\app.bin 0x08000000 verify reset exit"
```

## Telnet 连接

```powershell
telnet localhost 4444
```

## 查看目标

```text
targets
```

## 复位并暂停

```text
reset halt
```

## 继续运行

```text
resume
```

## 暂停 CPU

```text
halt
```

## 查看 Flash

```text
flash info 0
```

## 查看寄存器

```text
reg
```

## 查看内存

```text
mdw 0x08000000 4
```

## 启动 GDB

```powershell
arm-none-eabi-gdb .\build\app.elf
```

## GDB 连接

```text
target extended-remote localhost:3333
```

## GDB 复位

```text
monitor reset halt
```

## GDB 烧录

```text
load
```

## 设置断点

```text
break main
```

## 继续执行

```text
continue
```

## 单步

```text
next
```

## 查看调用栈

```text
backtrace
```

## 查看寄存器

```text
info registers
```

## 查看断点

```text
info breakpoints
```

---

# 26. 建议的学习顺序

按以下顺序学习最容易建立完整概念：

1. 理解 SWD、JTAG、调试器和目标芯片；
2. 安装 OpenOCD 和 Arm GDB；
3. 学会通过配置文件启动 OpenOCD；
4. 学会使用 Telnet；
5. 学会 `targets`、`halt`、`resume`、`reset halt`；
6. 学会查看寄存器和内存；
7. 学会烧录 ELF、HEX、BIN；
8. 理解链接地址和 Flash 地址；
9. 学会用 GDB 连接 OpenOCD；
10. 学会断点、单步、查看变量；
11. 学习 Bootloader 和向量表；
12. 学习读保护、写保护和 Option Bytes；
13. 最后再学习 Tcl 自动化和 IDE 集成。

最重要的一条经验是：

```text
先确认 OpenOCD 能识别调试器，
再确认能识别目标芯片，
再确认能 halt，
再烧录，
最后使用 GDB 调试。
```
