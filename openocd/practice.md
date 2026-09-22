如果你说的“opencode 文件”是指 **OpenOCD 配置文件和脚本文件**，那么它们本质上都是 **Tcl 脚本**。常见扩展名是：

```text
.cfg
.tcl
```

OpenOCD 文件的主要作用是描述：

```text
使用什么调试器
使用 SWD 还是 JTAG
连接什么芯片
调试速度是多少
如何复位
如何烧录
如何自动化执行命令
```

下面通过多个完整例子介绍。

---

# 1. OpenOCD 文件的基本工作方式

最简单的启动命令：

```powershell
openocd -f .\config\stm32f103.cfg
```

OpenOCD 会：

1. 读取 `stm32f103.cfg`；
2. 按文件中的顺序执行 Tcl 命令；
3. 加载调试器配置；
4. 加载目标芯片配置；
5. 初始化目标；
6. 启动 GDB、Telnet 和 Tcl 服务。

配置文件可以理解为：

```text
OpenOCD 启动说明书
```

一个典型配置文件：

```tcl
source [find interface/stlink.cfg]

transport select hla_swd

source [find target/stm32f1x.cfg]

adapter speed 4000
reset_config srst_only srst_nogate connect_assert_srst
```

---

# 2. 第一个最小配置文件

创建：

```text
C:\openocd-lab\config\stm32f103.cfg
```

内容：

```tcl
source [find interface/stlink.cfg]
source [find target/stm32f1x.cfg]
```

启动：

```powershell
openocd -f .\config\stm32f103.cfg
```

这个文件做了两件事：

```tcl
source [find interface/stlink.cfg]
```

加载 ST-Link 配置。

```tcl
source [find target/stm32f1x.cfg]
```

加载 STM32F1 目标芯片配置。

这是最简单的“调试器 + 目标芯片”组合。

---

# 3. `source`：加载其他文件

## 3.1 使用官方配置文件

```tcl
source [find interface/stlink.cfg]
source [find target/stm32f1x.cfg]
```

`source` 的作用是执行另一个 Tcl 文件。

```tcl
source 文件路径
```

`[find ...]` 会让 OpenOCD 在脚本搜索目录中查找文件。

例如：

```tcl
[find interface/stlink.cfg]
```

通常会在类似目录中查找：

```text
C:\OpenOCD\share\openocd\scripts\interface\stlink.cfg
```

---

## 3.2 加载自己的文件

目录结构：

```text
C:\openocd-lab
├── config
│   ├── interface.cfg
│   ├── target.cfg
│   └── main.cfg
└── scripts
    └── common.cfg
```

`main.cfg`：

```tcl
source [find config/interface.cfg]
source [find config/target.cfg]
source [find scripts/common.cfg]
```

启动：

```powershell
openocd -s C:\openocd-lab -f .\config\main.cfg
```

这里：

```powershell
-s C:\openocd-lab
```

表示把这个目录加入 OpenOCD 的脚本搜索路径。

---

## 3.3 直接使用相对路径

也可以这样写：

```tcl
source ../scripts/common.cfg
```

但相对路径容易受到当前工作目录影响。更稳定的方式是：

```tcl
source [find scripts/common.cfg]
```

配合：

```powershell
-s C:\openocd-lab
```

---

# 4. `interface` 文件：描述调试器

## 4.1 ST-Link

```tcl
source [find interface/stlink.cfg]
```

有些版本也可以使用更具体的文件：

```tcl
source [find interface/stlink-v2.cfg]
```

具体文件名取决于 OpenOCD 版本。

典型完整配置：

```tcl
source [find interface/stlink.cfg]

transport select hla_swd

adapter speed 4000
```

---

## 4.2 CMSIS-DAP

假设使用 CMSIS-DAP 调试器：

```tcl
source [find interface/cmsis-dap.cfg]

transport select swd

adapter speed 1000
```

与 ST-Link 的差别主要是接口配置：

```tcl
interface/stlink.cfg
```

换成：

```tcl
interface/cmsis-dap.cfg
```

---

## 4.3 J-Link

假设使用 SEGGER J-Link：

```tcl
source [find interface/jlink.cfg]

transport select swd

adapter speed 4000
```

调试器不同，通常只需要替换接口文件，目标芯片文件仍然可以保持不变。

---

## 4.4 不使用官方 interface 文件

某些情况下可以直接指定适配器驱动：

```tcl
adapter driver cmsis-dap
transport select swd
adapter speed 1000
```

或者：

```tcl
adapter driver jlink
transport select swd
adapter speed 4000
```

实际可用驱动取决于你的 OpenOCD 构建版本。

初学时建议优先使用：

```tcl
source [find interface/stlink.cfg]
```

而不是手动拆开配置。

---

# 5. `target` 文件：描述目标芯片

## 5.1 STM32F1

```tcl
source [find target/stm32f1x.cfg]
```

适用于常见的 STM32F1 系列。

## 5.2 STM32F4

```tcl
source [find target/stm32f4x.cfg]
```

## 5.3 STM32F7

```tcl
source [find target/stm32f7x.cfg]
```

## 5.4 STM32H7

```tcl
source [find target/stm32h7x.cfg]
```

## 5.5 nRF52

```tcl
source [find target/nrf52.cfg]
```

## 5.6 RP2040

```tcl
source [find target/rp2040.cfg]
```

目标文件会定义：

- CPU 类型；
- Flash 驱动；
- RAM 地址；
- Flash 地址；
- 复位方式；
- 芯片识别逻辑；
- 调试寄存器；
- 擦除算法；
- 目标对象名称。

---

# 6. 标准配置文件的完整写法

创建：

```text
C:\openocd-lab\config\stm32f103-stlink.cfg
```

内容：

```tcl
source [find interface/stlink.cfg]

transport select hla_swd

adapter speed 4000

source [find target/stm32f1x.cfg]

reset_config srst_only srst_nogate connect_assert_srst
```

逐行解释：

```tcl
source [find interface/stlink.cfg]
```

选择 ST-Link。

```tcl
transport select hla_swd
```

选择 SWD 协议。

```tcl
adapter speed 4000
```

设置调试速度为 4000 kHz。

```tcl
source [find target/stm32f1x.cfg]
```

选择 STM32F1 目标配置。

```tcl
reset_config srst_only srst_nogate connect_assert_srst
```

指定复位策略。

---

# 7. `adapter speed`：配置调试速度

```tcl
adapter speed 4000
```

单位通常是 kHz。

常见值：

```tcl
adapter speed 4000
adapter speed 2000
adapter speed 1000
adapter speed 100
```

高速适合：

```tcl
adapter speed 4000
```

连接不稳定时：

```tcl
adapter speed 1000
```

目标刚上电、线路较长、供电不稳或芯片状态异常时：

```tcl
adapter speed 100
```

可以为不同环境创建不同配置。

高速版本：

```text
C:\openocd-lab\config\stm32f103-fast.cfg
```

```tcl
source [find interface/stlink.cfg]
transport select hla_swd
adapter speed 4000
source [find target/stm32f1x.cfg]
```

低速版本：

```text
C:\openocd-lab\config\stm32f103-safe.cfg
```

```tcl
source [find interface/stlink.cfg]
transport select hla_swd
adapter speed 100
source [find target/stm32f1x.cfg]
```

启动低速版本：

```powershell
openocd -f .\config\stm32f103-safe.cfg
```

---

# 8. `reset_config`：配置复位方式

示例：

```tcl
reset_config srst_only srst_nogate connect_assert_srst
```

常见关键词：

| 关键词 | 含义 |
|---|---|
| `srst_only` | 只有系统复位线 |
| `trst_only` | 只有测试复位线 |
| `srst_nogate` | 调试逻辑不受系统复位门控影响 |
| `connect_assert_srst` | 连接时保持复位有效 |
| `combined` | SRST 和 TRST 组合使用 |
| `separate` | SRST 和 TRST 分开使用 |

如果固件一启动就进入低功耗或重新配置调试引脚，可以尝试：

```tcl
reset_config srst_only srst_nogate connect_assert_srst
```

但前提是目标板确实连接了 NRST。

如果没有连接 NRST，不要盲目使用依赖硬件复位线的配置。

---

# 9. 在配置文件中执行 OpenOCD 命令

配置文件不仅能“配置”，也能执行命令。

例如：

```tcl
init
reset halt
targets
reg
shutdown
```

但是注意：如果你把 `shutdown` 放在主配置文件里，OpenOCD 会启动后立刻退出。

因此，以下文件适合作为一次性脚本：

```text
inspect.cfg
```

```tcl
source [find interface/stlink.cfg]
transport select hla_swd
source [find target/stm32f1x.cfg]

init
reset halt
targets
reg
flash info 0
shutdown
```

执行：

```powershell
openocd -f .\config\inspect.cfg
```

执行顺序是：

```text
加载 ST-Link
加载 STM32F1
初始化
复位并暂停
显示目标
显示寄存器
显示 Flash 信息
退出
```

---

# 10. 用 `-c` 传入命令

不创建脚本文件，也可以从命令行传入命令：

```powershell
openocd `
  -f .\config\stm32f103-stlink.cfg `
  -c "init" `
  -c "reset halt" `
  -c "flash info 0" `
  -c "shutdown"
```

也可以合并：

```powershell
openocd `
  -f .\config\stm32f103-stlink.cfg `
  -c "init; reset halt; flash info 0; shutdown"
```

这两种方式效果类似。

单独的 `-c` 更容易阅读：

```powershell
-c "init"
-c "reset halt"
-c "flash info 0"
-c "shutdown"
```

复杂操作建议使用 `.cfg` 或 `.tcl` 文件。

---

# 11. 烧录脚本示例

## 11.1 烧录 ELF

创建：

```text
C:\openocd-lab\scripts\flash-elf.cfg
```

内容：

```tcl
source [find config/stm32f103-stlink.cfg]

init
reset halt

program C:/openocd-lab/build/app.elf verify

reset run
shutdown
```

运行：

```powershell
openocd `
  -s C:\openocd-lab `
  -f .\scripts\flash-elf.cfg
```

这里：

```tcl
program C:/openocd-lab/build/app.elf verify
```

表示：

1. 烧录 ELF；
2. 烧录后校验。

---

## 11.2 烧录 HEX

```tcl
source [find config/stm32f103-stlink.cfg]

init
reset halt

program C:/openocd-lab/build/app.hex verify

reset run
shutdown
```

HEX 文件包含地址信息，所以不需要额外写地址。

---

## 11.3 烧录 BIN

```tcl
source [find config/stm32f103-stlink.cfg]

init
reset halt

program C:/openocd-lab/build/app.bin 0x08000000 verify

reset run
shutdown
```

BIN 不包含地址，所以必须指定：

```text
0x08000000
```

如果应用程序从 `0x08004000` 开始：

```tcl
program C:/openocd-lab/build/app.bin 0x08004000 verify
```

---

## 11.4 烧录后复位并暂停

```tcl
source [find config/stm32f103-stlink.cfg]

init
reset halt

program C:/openocd-lab/build/app.elf verify

reset halt
shutdown
```

与 `reset run` 的差异：

```tcl
reset run
```

烧录后运行程序。

```tcl
reset halt
```

烧录后停在复位状态，方便随后连接 GDB。

---

# 12. 擦除脚本示例

## 12.1 擦除指定 Flash 区域

```tcl
source [find config/stm32f103-stlink.cfg]

init
reset halt

flash erase_sector 0 0 last

shutdown
```

含义：

```text
Flash bank 0
从第 0 个扇区开始
擦除到最后一个扇区
```

不同芯片的扇区含义不同。不要把 STM32F1 的页组织方式直接套到 STM32F4、STM32H7 上。

---

## 12.2 mass erase

```tcl
source [find config/stm32f103-stlink.cfg]

init
reset halt

stm32f1x mass_erase 0

shutdown
```

注意：

```text
mass erase 会擦除整个用户 Flash
```

可能包括：

- Bootloader；
- 应用程序；
- 配置数据；
- 校准参数。

---

# 13. 查看信息脚本

创建：

```text
inspect.cfg
```

```tcl
source [find config/stm32f103-stlink.cfg]

init
reset halt

puts "=== Target information ==="
targets

puts "=== Registers ==="
reg

puts "=== Flash information ==="
flash info 0

puts "=== Vector table ==="
mdw 0x08000000 8

shutdown
```

这里新增了：

```tcl
puts "文本"
```

`puts` 用于打印信息。

执行：

```powershell
openocd -s C:\openocd-lab -f .\scripts\inspect.cfg
```

输出会被分成几个区域，更容易阅读。

---

# 14. `puts` 和变量

Tcl 支持变量。

```tcl
set flash_start 0x08000000
set vector_words 8

puts "Flash start: $flash_start"
mdw $flash_start $vector_words
```

这里：

```tcl
set flash_start 0x08000000
```

创建变量。

```tcl
$flash_start
```

读取变量。

完整示例：

```tcl
source [find config/stm32f103-stlink.cfg]

set flash_address 0x08000000
set inspect_count 8

init
reset halt

puts "Reading vector table at $flash_address"
mdw $flash_address $inspect_count

shutdown
```

---

# 15. 使用命令行变量

OpenOCD 可以通过 `-c` 传递 Tcl 变量。

脚本：

```text
flash-variable.cfg
```

```tcl
source [find config/stm32f103-stlink.cfg]

init
reset halt

program $firmware_path $firmware_address verify

reset run
shutdown
```

启动：

```powershell
openocd `
  -s C:\openocd-lab `
  -f .\scripts\flash-variable.cfg `
  -c "set firmware_path C:/openocd-lab/build/app.bin" `
  -c "set firmware_address 0x08000000"
```

这里的关键是：

```tcl
set firmware_path ...
set firmware_address ...
```

必须在脚本使用变量之前执行。

更简单的写法是把变量放在前面：

```tcl
set firmware_path C:/openocd-lab/build/app.elf

source [find config/stm32f103-stlink.cfg]

init
reset halt
program $firmware_path verify
reset run
shutdown
```

---

# 16. `if`：根据条件执行

Tcl 支持条件判断。

```tcl
set do_reset 1

if {$do_reset} {
    reset halt
}
```

再例如：

```tcl
set speed 1000

if {$speed < 1000} {
    puts "Debug speed is low"
} else {
    puts "Debug speed is normal"
}
```

常用比较：

```tcl
if {$value == 1} {
    puts "value is one"
}
```

```tcl
if {$value != 0} {
    puts "value is not zero"
}
```

```tcl
if {$speed >= 4000} {
    puts "High speed mode"
}
```

---

# 17. `proc`：定义自己的命令

Tcl 可以定义函数，称为 `proc`。

```tcl
proc halt_and_inspect {} {
    reset halt
    reg
    flash info 0
}
```

使用：

```tcl
halt_and_inspect
```

完整示例：

```tcl
source [find config/stm32f103-stlink.cfg]

proc inspect_target {} {
    puts "Halting target..."
    reset halt

    puts "Target list:"
    targets

    puts "Registers:"
    reg

    puts "Flash:"
    flash info 0
}

init
inspect_target
shutdown
```

这样可以把重复操作封装起来。

---

# 18. 带参数的 `proc`

```tcl
proc read_memory {address count} {
    puts "Reading $count words at $address"
    mdw $address $count
}
```

调用：

```tcl
read_memory 0x08000000 8
```

完整示例：

```tcl
source [find config/stm32f103-stlink.cfg]

proc read_region {address count} {
    reset halt
    mdw $address $count
}

init
read_region 0x08000000 8
read_region 0x20000000 8
shutdown
```

---

# 19. `foreach`：批量读取多个地址

```tcl
source [find config/stm32f103-stlink.cfg]

init
reset halt

foreach address {
    0x08000000
    0x08000004
    0x20000000
    0x40021000
} {
    puts "Reading $address"
    mdw $address 1
}

shutdown
```

这适合批量检查：

- 向量表；
- 外设寄存器；
- 配置地址；
- 芯片唯一 ID。

例如 STM32 常见唯一 ID 地址可能位于某个系统存储区，但具体地址要查对应芯片参考手册，不能盲目套用。

---

# 20. `while`：循环等待状态

Tcl 可以循环检查寄存器：

```tcl
set count 0

while {$count < 5} {
    mdw 0x20000000 1
    incr count
}
```

`incr` 用于变量加一：

```tcl
incr count
```

增加指定数值：

```tcl
incr count 2
```

不过，OpenOCD 脚本中的循环如果没有等待机制，可能执行得非常快。实际项目里应谨慎使用无限循环。

---

# 21. 事件回调：`reset-init`

OpenOCD 支持在特定事件发生时自动执行命令。

例如：

```tcl
$_TARGETNAME configure -event reset-init {
    puts "Reset initialization event"
    adapter speed 1000
}
```

这段配置的含义是：

```text
每次目标完成 reset-init 事件时
执行大括号内的命令
```

更实际的例子：

```tcl
$_TARGETNAME configure -event reset-init {
    puts "Running reset initialization"
    halt
}
```

注意：

```tcl
$_TARGETNAME
```

通常由目标芯片配置文件定义。

不同芯片的目标名称可能不同，例如：

```text
stm32f1x.cpu
```

不要在未加载目标配置之前使用它。

---

# 22. 常见事件类型

不同 OpenOCD 版本和目标配置支持的事件有所差异，常见事件包括：

```tcl
reset-start
reset-init
reset-end
examine-start
examine-end
halted
resumed
gdb-attach
gdb-detach
gdb-start
gdb-end
```

示例：

```tcl
$_TARGETNAME configure -event examine-end {
    puts "Target examination completed"
}
```

```tcl
$_TARGETNAME configure -event reset-start {
    puts "Reset is starting"
}
```

```tcl
$_TARGETNAME configure -event reset-end {
    puts "Reset completed"
}
```

使用事件的好处是：不需要每次在命令行手动重复执行初始化步骤。

---

# 23. GDB 相关配置

可以为 GDB 连接事件添加处理逻辑：

```tcl
$_TARGETNAME configure -event gdb-attach {
    puts "GDB attached"
}
```

```tcl
$_TARGETNAME configure -event gdb-detach {
    puts "GDB detached"
}
```

例如，GDB 连接时自动暂停：

```tcl
$_TARGETNAME configure -event gdb-attach {
    halt
}
```

但要注意：某些 IDE 本身也会执行复位和暂停操作，重复配置可能导致行为与 IDE 预期不同。

---

# 24. 自定义目标配置的基本结构

通常不建议初学时完全手写芯片目标文件，但理解结构很重要。

一个简化目标配置可能类似：

```tcl
set CHIPNAME stm32f103
set CPU cortex-m3

source [find target/swj-dp.tcl]

swj_newdap $CHIPNAME cpu -irlen 4

set DAPID 0x1ba01477

dap create $CHIPNAME.dap -chain-position $CHIPNAME.cpu

target create $CHIPNAME.cpu cortex_m \
    -endian little \
    -dap $CHIPNAME.dap

flash bank $CHIPNAME.flash stm32f1x \
    0x08000000 0x00010000 0 0 \
    $CHIPNAME.cpu
```

这里涉及：

```text
DAP
DP
AP
target
flash bank
```

对于初学者，建议先使用：

```tcl
source [find target/stm32f1x.cfg]
```

只有在以下情况下才考虑自定义：

- 芯片是新型号；
- 官方目标文件不支持；
- 使用特殊 Flash；
- 需要修改复位行为；
- 需要自定义内存映射。

---

# 25. 多目标配置

有些硬件链路上可能有多个调试目标，例如 JTAG 链。

概念上可能如下：

```tcl
jtag newtap chip0 cpu -irlen 4 -expected-id 0x12345678
jtag newtap chip1 cpu -irlen 4 -expected-id 0x87654321
```

然后分别创建目标：

```tcl
target create chip0.cpu cortex_m -chain-position chip0.cpu
target create chip1.cpu cortex_m -chain-position chip1.cpu
```

查看目标：

```text
targets
```

你可能看到：

```text
0* chip0.cpu
1  chip1.cpu
```

操作指定目标：

```text
targets chip0.cpu
halt
```

多个目标主要出现在：

- JTAG 链；
- 多核芯片；
- FPGA + MCU；
- 调试桥接器件。

SWD 通常是一对一连接，因此一般不会这样配置。

---

# 26. 自定义 Flash Bank

OpenOCD 通过 `flash bank` 描述 Flash。

概念形式：

```tcl
flash bank 名称 驱动 地址 大小 总线宽度 芯片宽度 目标
```

示例：

```tcl
flash bank myflash stm32f1x \
    0x08000000 \
    0x00010000 \
    0 0 \
    stm32f103.cpu
```

参数含义：

```text
myflash       Flash bank 名称
stm32f1x      Flash 驱动
0x08000000    Flash 起始地址
0x00010000    Flash 大小
0             总线宽度
0             芯片宽度
stm32f103.cpu 目标对象
```

具体目标文件通常已经完成了这项工作，所以不需要重复定义。

---

# 27. 文件路径问题

## 27.1 PowerShell 路径

PowerShell 中通常写：

```powershell
C:\openocd-lab\build\app.elf
```

相对路径：

```powershell
.\build\app.elf
```

## 27.2 Tcl 路径

Tcl 中推荐使用正斜杠：

```tcl
C:/openocd-lab/build/app.elf
```

例如：

```tcl
program C:/openocd-lab/build/app.elf verify
```

也可以使用反斜杠，但需要注意转义问题：

```tcl
program C:\\openocd-lab\\build\\app.elf verify
```

因此在 OpenOCD Tcl 文件中，推荐：

```tcl
C:/openocd-lab/build/app.elf
```

---

# 28. 文件中的注释

Tcl 单行注释使用 `#`：

```tcl
# Load ST-Link configuration
source [find interface/stlink.cfg]

# Select SWD transport
transport select hla_swd
```

注释适合说明：

- 为什么使用低速；
- 为什么使用特殊复位配置；
- BIN 文件的烧录地址；
- Bootloader 的内存布局；
- 某个事件处理的原因。

不要把普通注释写成实际命令。

---

# 29. 花括号和引号的区别

以下两种写法常见：

```tcl
if {$value == 1} {
    puts "enabled"
}
```

```tcl
-c "program C:/openocd-lab/build/app.elf verify"
```

大致理解：

- 双引号允许变量替换；
- 花括号通常抑制内部替换，并用于代码块；
- PowerShell 本身也有引号规则。

例如：

```tcl
set file C:/openocd-lab/build/app.elf
program $file verify
```

通常可以正常替换变量。

---

# 30. 配置文件和脚本文件如何分工

推荐这样组织：

```text
C:\openocd-lab
├── config
│   ├── interface-stlink.cfg
│   ├── target-stm32f103.cfg
│   └── board-stm32f103.cfg
├── scripts
│   ├── flash.cfg
│   ├── erase.cfg
│   ├── inspect.cfg
│   └── debug-init.cfg
├── build
│   └── app.elf
└── logs
```

## `interface-stlink.cfg`

```tcl
source [find interface/stlink.cfg]
transport select hla_swd
adapter speed 4000
```

## `target-stm32f103.cfg`

```tcl
source [find target/stm32f1x.cfg]
reset_config srst_only srst_nogate connect_assert_srst
```

## `board-stm32f103.cfg`

```tcl
source [find config/interface-stlink.cfg]
source [find config/target-stm32f103.cfg]
```

## `flash.cfg`

```tcl
source [find config/board-stm32f103.cfg]

init
reset halt
program C:/openocd-lab/build/app.elf verify
reset run
shutdown
```

这种拆分方式的好处是：

```text
调试器配置可以复用
目标配置可以复用
板级配置负责组合
操作脚本负责烧录或检查
```

---

# 31. 一个完整的项目配置

## 文件一：板级配置

```text
config/board-stm32f103.cfg
```

```tcl
source [find interface/stlink.cfg]

transport select hla_swd

adapter speed 4000

source [find target/stm32f1x.cfg]

reset_config srst_only srst_nogate connect_assert_srst
```

## 文件二：启动服务器

```text
scripts/server.cfg
```

```tcl
source [find config/board-stm32f103.cfg]
```

运行：

```powershell
openocd -s C:\openocd-lab -f .\scripts\server.cfg
```

这个脚本不会执行 `shutdown`，因此 OpenOCD 会持续运行。

## 文件三：烧录

```text
scripts/flash.cfg
```

```tcl
source [find config/board-stm32f103.cfg]

init
reset halt
program C:/openocd-lab/build/app.elf verify
reset run
shutdown
```

运行：

```powershell
openocd -s C:\openocd-lab -f .\scripts\flash.cfg
```

## 文件四：检查目标

```text
scripts/inspect.cfg
```

```tcl
source [find config/board-stm32f103.cfg]

init
reset halt

puts "=== Targets ==="
targets

puts "=== Registers ==="
reg

puts "=== Flash ==="
flash info 0

puts "=== Vector table ==="
mdw 0x08000000 8

shutdown
```

运行：

```powershell
openocd -s C:\openocd-lab -f .\scripts\inspect.cfg
```

---

# 32. 使用日志配置文件

可以在启动命令中指定日志文件：

```powershell
openocd `
  -s C:\openocd-lab `
  -f .\config\board-stm32f103.cfg `
  -l C:\openocd-lab\logs\openocd.log
```

增加调试日志：

```powershell
openocd `
  -d3 `
  -s C:\openocd-lab `
  -f .\config\board-stm32f103.cfg `
  -l C:\openocd-lab\logs\openocd-debug.log
```

也可以在脚本中打印自定义阶段：

```tcl
puts "Loading board configuration"
source [find config/board-stm32f103.cfg]

puts "Starting initialization"
init

puts "Halting target"
reset halt

puts "Programming firmware"
program C:/openocd-lab/build/app.elf verify

puts "Finished"
reset run
shutdown
```

---

# 33. GDB 事件和自动初始化示例

```tcl
source [find config/board-stm32f103.cfg]

$_TARGETNAME configure -event gdb-attach {
    puts "GDB has attached"
    reset halt
}

$_TARGETNAME configure -event gdb-detach {
    puts "GDB has detached"
}
```

启动：

```powershell
openocd -s C:\openocd-lab -f .\scripts\gdb-events.cfg
```

然后在另一个窗口中启动 GDB：

```powershell
arm-none-eabi-gdb .\build\app.elf
```

连接：

```text
target extended-remote localhost:3333
```

OpenOCD 会触发：

```text
GDB has attached
```

---

# 34. 通过 Telnet 执行配置中的自定义命令

配置文件：

```tcl
source [find config/board-stm32f103.cfg]

proc show_vector_table {} {
    reset halt
    mdw 0x08000000 8
}

proc show_basic_info {} {
    targets
    reg
    flash info 0
}

init
```

启动：

```powershell
openocd -s C:\openocd-lab -f .\scripts\interactive.cfg
```

另开窗口：

```powershell
telnet localhost 4444
```

在 Telnet 中执行：

```text
show_vector_table
```

再执行：

```text
show_basic_info
```

这样可以把常用命令封装成自己的 OpenOCD 命令。

---

# 35. 常见错误写法

## 错误一：只加载 interface，不加载 target

```tcl
source [find interface/stlink.cfg]
```

这只能识别调试器，不能完整配置 STM32 目标。

通常还需要：

```tcl
source [find target/stm32f1x.cfg]
```

---

## 错误二：BIN 烧录不指定地址

错误或风险较高：

```tcl
program C:/openocd-lab/build/app.bin verify
```

正确：

```tcl
program C:/openocd-lab/build/app.bin 0x08000000 verify
```

---

## 错误三：服务器配置里写了 `shutdown`

```tcl
source [find config/board-stm32f103.cfg]
shutdown
```

这样 OpenOCD 会启动后立即关闭，不适合作为 GDB 服务器配置。

---

## 错误四：在未加载目标配置前使用目标名称

```tcl
$_TARGETNAME configure -event reset-init {
    halt
}

source [find target/stm32f1x.cfg]
```

顺序错误。

应当先加载目标：

```tcl
source [find target/stm32f1x.cfg]

$_TARGETNAME configure -event reset-init {
    halt
}
```

---

## 错误五：路径含空格却不处理

例如：

```text
C:\Users\Test User\firmware\app.elf
```

可以在 Tcl 中使用正斜杠并加引号：

```tcl
program "C:/Users/Test User/firmware/app.elf" verify
```

---

# 36. 最推荐的三类文件

实际使用时，可以先掌握这三类。

## 类型一：服务器配置

```tcl
source [find interface/stlink.cfg]
transport select hla_swd
adapter speed 4000
source [find target/stm32f1x.cfg]
```

用途：

```text
启动 OpenOCD，等待 GDB 或 Telnet 连接
```

## 类型二：一次性烧录脚本

```tcl
source [find config/board-stm32f103.cfg]

init
reset halt
program C:/openocd-lab/build/app.elf verify
reset run
shutdown
```

用途：

```text
自动烧录并退出
```

## 类型三：诊断脚本

```tcl
source [find config/board-stm32f103.cfg]

init
reset halt
targets
reg
flash info 0
mdw 0x08000000 8
shutdown
```

用途：

```text
诊断调试器、芯片、寄存器和 Flash
```

---

# 37. 最后用一个类比理解

可以把 OpenOCD 文件分成四层：

```text
interface 文件
    ↓
target 文件
    ↓
board 文件
    ↓
operation 脚本
```

对应关系：

```text
interface：我用什么调试器？
target：我要连接什么芯片？
board：这个具体开发板如何连接和复位？
operation：这次我要烧录、擦除还是检查？
```

例如：

```text
interface/stlink.cfg
```

回答：

```text
使用 ST-Link
```

```text
target/stm32f1x.cfg
```

回答：

```text
目标是 STM32F1
```

```text
board-stm32f103.cfg
```

回答：

```text
这个板子用 SWD，调试速度 4000 kHz，复位方式是什么
```

```text
flash.cfg
```

回答：

```text
烧录哪个文件，校验后是否复位并退出
```

掌握下面这个模板，就能读懂大多数 OpenOCD 配置：

```tcl
# 1. 调试器
source [find interface/stlink.cfg]

# 2. 协议
transport select hla_swd

# 3. 调试速度
adapter speed 4000

# 4. 目标芯片
source [find target/stm32f1x.cfg]

# 5. 复位方式
reset_config srst_only srst_nogate connect_assert_srst

# 6. 后续操作
init
reset halt
program C:/openocd-lab/build/app.elf verify
reset run
shutdown
```

核心规律就是：

```text
source：加载配置
set：设置变量
puts：打印信息
if：条件判断
proc：定义命令
init：初始化
reset：复位
program：烧录
shutdown：退出
```
