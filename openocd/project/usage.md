这个项目的完整流程是：

```text
准备工具
  ↓
检查项目文件
  ↓
CMake 配置
  ↓
交叉编译
  ↓
生成 ELF / HEX / BIN
  ↓
检查地址和大小
  ↓
连接 ST-Link 与 STM32
  ↓
OpenOCD 识别芯片
  ↓
擦除并烧录
  ↓
校验并复位运行
  ↓
GDB 断点调试
```

当前项目是第一阶段：**没有 Bootloader，程序从 `0x08000000` 运行，功能是让 PC13 LED 每 500 ms 翻转一次。**

---

# 1. 认识项目中的文件

项目目录：

```text
C:\Users\hengvvang\Desktop\work\project
```

## 应用代码

```text
app\src\main.c
```

负责：

- 打开 GPIOC 时钟；
- 配置 PC13；
- 配置 SysTick；
- 循环翻转 LED。

## 启动文件

```text
app\src\startup_stm32f103xb.s
```

芯片复位后，执行顺序不是直接进入 `main()`，而是：

```text
读取初始栈指针
  ↓
读取 Reset_Handler
  ↓
初始化 .data
  ↓
清零 .bss
  ↓
调用 main()
```

启动文件中这两项位于向量表最前面：

```asm
.word _estack
.word Reset_Handler
```

## 链接脚本

```text
app\linker\STM32F103C8Tx_FLASH.ld
```

定义：

```text
Flash：0x08000000，64 KB
RAM：  0x20000000，20 KB
```

并规定：

```text
代码放入 Flash
全局变量放入 RAM
栈顶位于 RAM 末尾
```

## CMake 文件

```text
CMakeLists.txt
toolchain-arm-none-eabi.cmake
```

负责告诉构建系统：

- 使用哪个编译器；
- 目标 CPU 是 Cortex-M3；
- 使用哪个链接脚本；
- 编译哪些源文件；
- 如何生成 ELF、HEX、BIN。

## OpenOCD 文件

```text
openocd\board-stm32f103-stlink.cfg
```

描述硬件连接：

```text
ST-Link
SWD
STM32F1
调试速度
复位方式
```

```text
openocd\flash.cfg
```

描述一次性烧录：

```text
初始化
复位
擦除
烧录
校验
复位运行
退出
```

```text
openocd\debug.cfg
```

描述调试服务器：

```text
启动 OpenOCD
暂停目标
监听 GDB 3333 端口
监听 Telnet 4444 端口
持续运行
```

---

# 2. 准备工具

假定已经安装：

```text
CMake
Ninja
Arm GNU Toolchain
OpenOCD
```

打开 PowerShell，执行：

```powershell
arm-none-eabi-gcc --version
```

检查编译器。

```powershell
arm-none-eabi-gdb --version
```

检查 GDB。

```powershell
cmake --version
```

检查 CMake。

```powershell
ninja --version
```

检查 Ninja。

```powershell
openocd --version
```

检查 OpenOCD。

如果某个命令提示找不到，通常是工具没有安装，或者对应目录没有加入 `PATH`。

常见需要加入 `PATH` 的目录类似：

```text
C:\Program Files\Arm GNU Toolchain arm-none-eabi\...\bin
C:\OpenOCD\bin
```

具体路径以你的实际安装位置为准。

---

# 3. 进入项目目录

执行：

```powershell
Set-Location C:\Users\hengvvang\Desktop\work\project
```

确认当前目录：

```powershell
Get-Location
```

查看项目文件：

```powershell
Get-ChildItem -Recurse
```

你应该看到：

```text
app
openocd
CMakeLists.txt
toolchain-arm-none-eabi.cmake
README.md
```

---

# 4. 配置 CMake

执行：

```powershell
cmake `
  -S . `
  -B .\build `
  -G Ninja `
  -DCMAKE_TOOLCHAIN_FILE=.\toolchain-arm-none-eabi.cmake `
  -DCMAKE_BUILD_TYPE=Debug
```

这条命令还没有编译程序，它主要完成配置。

参数含义：

```text
-S .
```

源码目录是当前目录。

```text
-B .\build
```

把构建中间文件和输出放在 `build` 目录。

```text
-G Ninja
```

使用 Ninja 构建系统。

```text
-DCMAKE_TOOLCHAIN_FILE=...
```

使用 ARM 交叉编译配置。

```text
-DCMAKE_BUILD_TYPE=Debug
```

生成适合调试的版本。

Debug 版本使用：

```text
-Og
-g3
```

其中：

- `-Og`：适度优化，保留较好的调试体验；
- `-g3`：生成较完整的调试信息。

---

# 5. 编译项目

执行：

```powershell
cmake --build .\build
```

CMake 会调用类似下面的工具：

```text
arm-none-eabi-gcc
arm-none-eabi-gcc -c
arm-none-eabi-objcopy
arm-none-eabi-size
```

编译过程大致是：

```text
main.c
    ↓
main.c.obj
```

```text
startup_stm32f103xb.s
    ↓
startup_stm32f103xb.s.obj
```

然后链接：

```text
main.c.obj
startup_stm32f103xb.s.obj
链接脚本
    ↓
TempController.elf
```

最后转换：

```text
TempController.elf
    ├── TempController.hex
    └── TempController.bin
```

编译完成后查看：

```powershell
Get-ChildItem .\build
```

应该包含：

```text
TempController.elf
TempController.hex
TempController.bin
TempController.map
```

---

# 6. 理解三种固件文件

## 6.1 ELF

```text
build\TempController.elf
```

ELF 包含：

- 程序代码；
- 内存地址；
- 函数名；
- 变量名；
- 源代码行号；
- 调试信息。

因此 GDB 使用它：

```powershell
arm-none-eabi-gdb .\build\TempController.elf
```

ELF 是最完整的文件。

## 6.2 HEX

```text
build\TempController.hex
```

HEX 包含：

- 程序数据；
- 目标地址；
- 校验信息。

OpenOCD 烧录 HEX 时通常不需要额外指定地址：

```tcl
program firmware.hex verify
```

因为地址已经写在 HEX 文件中。

## 6.3 BIN

```text
build\TempController.bin
```

BIN 只是连续字节，没有地址信息。

所以烧录 BIN 时必须指定地址：

```tcl
program firmware.bin 0x08000000 verify
```

当前程序的正确 Flash 起始地址是：

```text
0x08000000
```

---

# 7. 检查程序大小和地址

查看程序大小：

```powershell
arm-none-eabi-size .\build\TempController.elf
```

输出大致包含：

```text
text
data
bss
dec
hex
```

含义：

| 字段 | 含义 |
|---|---|
| `text` | 代码和只读内容 |
| `data` | 有初始值的全局变量 |
| `bss` | 无初始值的全局变量 |
| `dec` | 总大小，十进制 |
| `hex` | 总大小，十六进制 |

检查关键符号：

```powershell
arm-none-eabi-nm .\build\TempController.elf |
  Select-String "Reset_Handler|main|_estack"
```

应当看到：

```text
Reset_Handler 位于 0x08000000 附近
main 位于 Flash 区域
_estack 位于 0x20005000
```

因为：

```text
RAM 起始地址 = 0x20000000
RAM 大小 = 20 KB = 0x5000
RAM 结束地址 = 0x20005000
```

查看 ELF 段：

```powershell
arm-none-eabi-readelf -S .\build\TempController.elf
```

重点确认代码段位于：

```text
0x08000000
```

---

# 8. 当前项目在没有硬件时能做什么

没有硬件时，你可以完成：

```text
CMake 配置
交叉编译
生成 ELF
生成 HEX
生成 BIN
查看程序大小
查看符号地址
查看链接布局
检查 OpenOCD 配置文件
```

没有硬件时，不能真正验证：

```text
ST-Link 是否被识别
目标电压
SWD 通信
STM32 芯片 ID
Flash 擦除
Flash 写入
实际 LED 是否闪烁
GDB 是否能停在 main
```

因此当前的正确学习顺序是：

```text
先完成构建
再理解输出文件
以后有硬件时再执行 OpenOCD
```

---

# 9. 有硬件后的连接方式

假定硬件为：

```text
ST-Link V2
STM32F103C8T6
```

SWD 连接：

| ST-Link | STM32 |
|---|---|
| SWDIO | SWDIO |
| SWCLK | SWCLK |
| GND | GND |
| VTref | 目标板 3.3 V |
| NRST | NRST，可选但推荐 |

注意：

- ST-Link 和目标板必须共地；
- VTref 用于检测目标电平；
- 目标芯片必须供电；
- SWDIO 和 SWCLK 不能接反；
- 没有目标电压时，OpenOCD 通常无法正常连接。

---

# 10. 第一次只检查硬件

不要第一次就烧录。先启动 OpenOCD 服务器。

进入项目目录：

```powershell
Set-Location C:\Users\hengvvang\Desktop\work\project
```

执行：

```powershell
openocd -s . -f .\openocd\debug.cfg
```

参数：

```text
-s .
```

把当前项目目录加入 OpenOCD 脚本搜索路径。

```text
-f .\openocd\debug.cfg
```

加载调试服务器配置。

正常情况下会看到类似：

```text
STLINK
Target voltage: 3.3xxx V
Cortex-M3 processor detected
hardware has breakpoints
Listening on port 3333 for gdb connections
```

重点检查：

```text
ST-Link 是否识别
Target voltage 是否正常
目标是否识别为 Cortex-M3
端口 3333 是否监听
```

不要关闭这个 OpenOCD 窗口。

---

# 11. 使用 Telnet 检查目标

另开一个 PowerShell：

```powershell
telnet localhost 4444
```

如果 Windows 没有 Telnet 客户端，需要先启用 Telnet Client。

进入 OpenOCD Telnet 后执行：

```text
targets
```

查看目标。

```text
reset halt
```

复位并暂停 CPU。

```text
flash info 0
```

查看 Flash 信息。

```text
reg
```

查看 CPU 寄存器。

```text
mdw 0x08000000 8
```

读取 Flash 起始处的向量表。

向量表前两个值理论上应当是：

```text
初始栈指针
Reset_Handler 地址
```

初始栈指针应接近：

```text
0x20005000
```

Reset_Handler 应接近：

```text
0x08000000
```

这一步是验证“程序是否被正确烧录”的基础。

---

# 12. 烧录项目

确认目标硬件能够识别后，执行：

```powershell
openocd -s . -f .\openocd\flash.cfg
```

`flash.cfg` 的流程是：

```tcl
init
```

初始化 OpenOCD 和目标芯片。

```tcl
reset halt
```

复位并暂停 CPU。

```tcl
flash erase_sector 0 0 last
```

擦除整个 Flash。

```tcl
program ...TempController.hex verify
```

烧录 HEX 并校验。

```tcl
reset run
```

复位并运行。

```tcl
shutdown
```

退出 OpenOCD。

生产或开发过程中，OpenOCD 输出中的重点是：

```text
Programming Finished
verified
```

如果出现校验失败，不要直接重复烧录，应检查：

- 固件地址；
- 芯片型号配置；
- 调试速度；
- 目标电源；
- Flash 保护；
- SWD 连接；
- 是否有其他程序占用 ST-Link。

---

# 13. 烧录后程序如何运行

芯片复位后：

```text
0x08000000
```

被当作向量表起始地址。

向量表中的第一个 word：

```text
_estack
```

被加载为栈指针。

第二个 word：

```text
Reset_Handler
```

被加载为程序入口。

随后启动代码：

```text
复制 .data
清零 .bss
调用 main()
```

`main()` 中：

```c
led_init();
systick_init();
```

完成初始化后进入无限循环：

```c
while (1) {
    led_toggle();
    delay_ms(500);
}
```

因此 LED 每约 500 ms 翻转一次。

如果 LED 不闪烁，可能不是程序完全没有运行，还可能是：

- LED 实际接在其他引脚；
- LED 是低电平点亮；
- 板子的系统时钟不是假定值；
- 芯片型号不是 STM32F103；
- PC13 没有连接板载 LED；
- 烧录成功但硬件供电或复位异常。

---

# 14. 使用 GDB 调试

先启动 OpenOCD：

```powershell
openocd -s . -f .\openocd\debug.cfg
```

保持运行。

另开 PowerShell：

```powershell
arm-none-eabi-gdb .\build\TempController.elf
```

进入 GDB 后：

```text
target extended-remote localhost:3333
```

连接到 OpenOCD 的 GDB 端口。

```text
monitor reset halt
```

通过 OpenOCD 复位并暂停目标。

```text
break main
```

在 `main()` 设置断点。

```text
continue
```

继续运行，程序应停在 `main()`。

查看源代码：

```text
list
```

单步执行：

```text
next
```

进入函数：

```text
step
```

查看寄存器：

```text
info registers
```

查看程序计数器：

```text
print/x $pc
```

查看栈指针：

```text
print/x $sp
```

查看调用栈：

```text
backtrace
```

查看内存：

```text
x/8wx 0x08000000
```

查看 GPIOC 输出寄存器：

```text
x/wx 0x4001100C
```

继续运行：

```text
continue
```

退出 GDB：

```text
quit
```

这里的职责关系是：

```text
GDB：设置断点、单步、查看变量
OpenOCD：接收 GDB 命令
ST-Link：传输调试命令
STM32：执行、暂停和返回状态
```

---

# 15. 开发流程和生产流程的区别

## 开发流程

开发时通常是：

```text
修改代码
  ↓
编译
  ↓
OpenOCD 烧录
  ↓
GDB 调试
  ↓
查看变量和寄存器
  ↓
继续修改
```

常用文件：

```text
TempController.elf
openocd\debug.cfg
```

## 生产流程

生产时通常是：

```text
确认产品型号
  ↓
确认固件版本
  ↓
检查调试器和目标板
  ↓
擦除
  ↓
烧录
  ↓
校验
  ↓
读取芯片信息
  ↓
硬件功能测试
  ↓
记录 PASS/FAIL
```

生产不应直接使用开发时的临时文件，而应该使用：

```text
版本固定的 HEX
版本固定的配置
版本固定的烧录脚本
生产日志
```

---

# 16. 以后加入 Bootloader 后会怎样

当前链接脚本：

```ld
FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 64K
```

以后加入 Bootloader 后，Application 链接脚本需要改为：

```ld
FLASH (rx) : ORIGIN = 0x08004000, LENGTH = 44K
```

同时 Application 的向量表也会位于：

```text
0x08004000
```

新的启动关系：

```text
复位
  ↓
0x08000000 Bootloader
  ↓
检查升级条件
  ↓
跳转到 0x08004000
  ↓
Application Reset_Handler
  ↓
main()
```

这时不能只把当前 `.bin` 烧到 `0x08004000`，因为当前程序是按照：

```text
0x08000000
```

链接的。

必须一起修改：

```text
链接脚本
向量表
Bootloader 跳转逻辑
OpenOCD 烧录文件
```

---

# 17. 当前推荐的实际操作顺序

你现在可以按照下面顺序操作：

## 第一步：检查文件

```powershell
Set-Location C:\Users\hengvvang\Desktop\work\project
Get-ChildItem -Recurse
```

## 第二步：检查工具

```powershell
arm-none-eabi-gcc --version
arm-none-eabi-gdb --version
cmake --version
ninja --version
openocd --version
```

## 第三步：配置项目

```powershell
cmake `
  -S . `
  -B .\build `
  -G Ninja `
  -DCMAKE_TOOLCHAIN_FILE=.\toolchain-arm-none-eabi.cmake `
  -DCMAKE_BUILD_TYPE=Debug
```

## 第四步：编译

```powershell
cmake --build .\build
```

## 第五步：检查输出

```powershell
Get-ChildItem .\build
```

## 第六步：检查程序大小

```powershell
arm-none-eabi-size .\build\TempController.elf
```

## 第七步：如果没有硬件，到此停止

你可以继续分析：

```text
ELF
HEX
BIN
MAP
链接地址
符号地址
```

## 第八步：以后有硬件，再启动 OpenOCD

```powershell
openocd -s . -f .\openocd\debug.cfg
```

## 第九步：确认硬件识别后再烧录

```powershell
openocd -s . -f .\openocd\flash.cfg
```

## 第十步：使用 GDB 调试

```powershell
arm-none-eabi-gdb .\build\TempController.elf
```

---

# 18. 当前项目的核心理解

这个项目中最重要的关系是：

```text
链接脚本决定地址
编译器生成机器码
ELF 保存代码和调试信息
HEX 保存带地址的烧录数据
OpenOCD 访问芯片并烧录
GDB 通过 OpenOCD 调试
```

用一句话概括：

> **CMake 负责构建，链接脚本负责布局，ELF/HEX/BIN 负责承载固件，OpenOCD 负责访问和烧录芯片，GDB 负责调试。**

当前项目先完成“单一 Application”流程。等你熟悉：

```text
构建 → 检查 → 烧录 → 调试
```

再把它扩展为真正的生产项目：

```text
Bootloader
Application
配置区
产品序列号
芯片唯一 ID
生产测试
烧录日志
```
