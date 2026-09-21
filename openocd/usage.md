OpenOCD（Open On-Chip Debugger）的底层命令架构基于 Jim-Tcl 解释器，其指令集按照执行生命周期、硬件拓扑及操作对象严格分层。

---

## 一、 OpenOCD 基础架构与命令分类逻辑

OpenOCD 的命令执行可分为两个主要阶段：

1. **配置阶段（Configuration Stage）**：在执行 `init` 之前生效，用于声明调试探针、总线时钟、扫描链（TAP）与目标核心（Target）。
2. **运行阶段（Execution Stage）**：在执行 `init` 之后生效，用于控制 CPU 执行流、访问内存寄存器、操作 Flash 以及运行断点系统。

OpenOCD 支持三类主要调用界面：

* **命令行选项**：启动进程时传递给 binary 的参数。
* **Telnet 交互界面**（默认端口 `4444`）：用于开发人员实时调试与单步下发指令。
* **GDB 接口**（默认端口 `3333`）：用于驱动标准 GDB Client。通过 `monitor <command>` 前缀可将所有 OpenOCD 内部命令穿透传递。

---

## 二、 命令行启动参数（Command-line Options）

OpenOCD 可执行程序在终端启动时的参数标准格式如下：

### 选项定义与参数全解

* `-f <filename>` 或 `--file <filename>`
* **参数**：`<filename>` 脚本路径（支持相对/绝对路径，或 OpenOCD 搜索路径内的文件）。
* **释义**：指定启动时要执行的配置文件。若指定多个 `-f`，按从左往右的顺序加载。


* `-s <directory>` 或 `--search <directory>`
* **参数**：`<directory>` 搜索目录。
* **释义**：添加查找 scripts/target/interface 等 `.cfg` 文件的搜索路径。


* `-c <command>` 或 `--command <command>`
* **参数**：`<command>` Jim-Tcl 指令字符串。
* **释义**：在解析配置过程中就地执行一段 Tcl 命令。可传入多次。


* `-d[level]` 或 `--debug=[level]`
* **参数**：`level` 取值为 `0`（Error）、`1`（Warning）、`2`（Info，默认）、`3`（Debug）、`4`（Developer verbose）。
* **释义**：设置输出日志的详细等级。


* `-l <filename>` 或 `--log_output <filename>`
* **参数**：`<filename>` 日志保存文件路径。
* **释义**：将控制台 stdout/stderr 日志重定向到指定文件。



### 示例

```bash
# 场景：指定调试器接口为 CMSIS-DAP，目标为 STM32F4，搜索自定义库路径，并在启动完成后直接擦写固件
openocd \
  -s /opt/custom_openocd/scripts \
  -f interface/cmsis-dap.cfg \
  -f target/stm32f4x.cfg \
  -c "transport select swd" \
  -c "adapter speed 4000" \
  -c "init" \
  -c "reset halt" \
  -c "program build/firmware.elf verify reset exit"

```

---

## 三、 核心指令体系详解（按功能领域）

### 1. 通用系统与生命周期管理

#### `init`

* **完整语法**：`init`
* **参数**：无。
* **作用阶段**：配置阶段 $\rightarrow$ 运行阶段过渡。
* **注释**：结束配置状态，初始化硬件探测总线（JTAG TAP 枚举 / SWD 连接建立），验证 IDCODE，挂载 target。
* **示例**：
```tcl
# 手动触发硬件连接建立
init

```



#### `shutdown`

* **完整语法**：`shutdown`
* **参数**：无。
* **作用阶段**：运行阶段。
* **注释**：关闭所有打开的调试器接口、释放 target 状态并退出 OpenOCD 进程（返回码 0）。
* **示例**：
```tcl
# 自动化脚本末尾执行退出
shutdown

```



#### `sleep <ms> [busy]`

* **完整语法**：`sleep <milliseconds> [busy]`
* **参数**：
* `<milliseconds>`：等待毫秒数。
* `busy`（可选）：采用忙等待（Busy wait）而非 yield/sleep 阻塞。用于对微秒/毫秒时序极其严格的外部复位电平操作。


* **注释**：延迟执行后续脚本。
* **示例**：
```tcl
# 释放硬件复位脚后等待外设供电与 PLL 稳定 100 毫秒
sleep 100

```



---

### 2. 调试探针与物理层配置（Adapter & Transport）

#### `adapter speed <frequency_khz>`

* **完整语法**：`adapter speed <frequency_khz>`
* **参数**：`<frequency_khz>`：传输时钟频率，单位为 kHz。
* **注释**：设置 JTAG TCK 或 SWD SWCLK 的物理频率。低速用于复位连接建立阶段，高速用于固件下载。
* **示例**：
```tcl
# 设置通信时钟为 2 MHz
adapter speed 2000

```



#### `transport select <transport_name>`

* **完整语法**：`transport select [transport_name]`
* **参数**：`<transport_name>` 支持的值包括 `jtag`、`swd`、`dapdirect_swd` 等（取决于探针驱动能力）。
* **注释**：如果不带参数，则返回当前生效的传输协议；带参数则配置物理层走线协议（仅配置阶段可用）。
* **示例**：
```tcl
transport select swd

```



#### `adapter srst delay <ms>` / `adapter srst pulse_width <ms>`

* **完整语法**：
* `adapter srst delay <ms>`
* `adapter srst pulse_width <ms>`


* **参数**：`<ms>` 时间（毫秒）。
* **注释**：
* `pulse_width`：驱动 nSRST 引脚拉低的持续脉宽。
* `delay`：释放 nSRST 引脚后，探针等待目标芯片完成 boot 的延时。


* **示例**：
```tcl
adapter srst pulse_width 100
adapter srst delay 50

```



---

### 3. 目标控制与状态机（Target Execution Control）

#### `poll [on|off]`

* **完整语法**：`poll [on|off]`
* **参数**：`on` 打开周期性轮询；`off` 关闭；缺省输出当前轮询状态与 Target 状态。
* **注释**：OpenOCD 默认后台每隔几十毫秒轮询一次 Target 核心状态（Running / Halted）。
* **示例**：
```tcl
poll
# 输出: background polling: on, target: stm32f4x.cpu - state: halted

```



#### `halt [ms]`

* **完整语法**：`halt [timeout_ms]`
* **参数**：`timeout_ms`（可选）：等待 CPU 中断挂起的最大超时时间（毫秒）。
* **注释**：向 CPU 发送 debug halt 请求，使其停止运行并停在当前 PC 处。
* **示例**：
```tcl
halt 1000

```



#### `resume [address]`

* **完整语法**：`resume [address]`
* **参数**：`address`（可选）：16 进制或十进制地址。缺省时从当前 Program Counter 处继续执行；给定参数则强行跳转到该地址恢复执行。
* **注释**：恢复目标 CPU 的全速运行。
* **示例**：
```tcl
resume
# 或从引导向量处强行恢复
resume 0x08000000

```



#### `step [address]`

* **完整语法**：`step [address]`
* **参数**：`address`（可选）：单步起点地址。缺省时执行当前 PC 对应的一条汇编指令。
* **注释**：单步执行（Instruction-level single step）。执行后 Target 会立即重新进入 Halt 状态。
* **示例**：
```tcl
step

```



#### `reset [run|halt|init]`

* **完整语法**：`reset [run|halt|init]`
* **参数**：
* `run`：复位后直接运行代码，不挂起。
* `halt`：复位并在第 1 条指令（Reset Vector）处挂起 CPU。
* `init`：复位、挂起，并执行该芯片 target 脚本中注册的 `reset-init` 钩子函数（通常用于初始化 PLL、关闭看门狗、配置外设 RAM）。


* **注释**：核心复位控制命令。
* **示例**：
```tcl
reset init

```



#### `wait_halt [ms]`

* **完整语法**：`wait_halt [timeout_ms]`
* **参数**：`timeout_ms`（可选，默认 5000 毫秒）。
* **注释**：阻塞等待目标 CPU 变为 Halted 状态。常用于自动化脚本中确保前序动作已完成。
* **示例**：
```tcl
reset halt
wait_halt 2000

```



---

### 4. 内存与外设寄存器读写（Memory Access）

数据宽度定义对应关系：`8位 (b/byte)`，`16位 (h/halfword)`，`32位 (w/word)`，`64位 (d/doubleword)`。

#### 读内存：`md<b|h|w|d> <address> [count]`

* **完整语法**：
* `mdb <addr> [count]` （读 8-bit）
* `mdh <addr> [count]` （读 16-bit）
* `mdw <addr> [count]` （读 32-bit）
* `mdd <addr> [count]` （读 64-bit）


* **参数**：
* `<address>`：物理或总线起始地址。
* `[count]`：连续读取的单元个数（缺省为 1）。


* **注释**：Memory Display。用于检查外设寄存器（如 RCC、GPIO）或 SRAM/Flash 区域的内容。
* **示例**：
```tcl
# 读取 STM32 RCC_CR 寄存器 (32-bit, 地址 0x40023800)
mdw 0x40023800 1

# 从内存 0x20000000 连续 dump 16 个字节 (8-bit)
mdb 0x20000000 16

```



#### 写内存：`mw<b|h|w|d> <address> <value> [count]`

* **完整语法**：
* `mwb <addr> <val> [count]`
* `mwh <addr> <val> [count]`
* `mww <addr> <val> [count]`
* `mwd <addr> <val> [count]`


* **参数**：
* `<addr>`：目的起始地址。
* `<val>`：待写入数值。
* `[count]`：连续写入的次数（缺省为 1）。


* **注释**：Memory Write。常用于使能时钟外设、喂狗或在 RAM 中修改变量。
* **示例**：
```tcl
# 向外设控制寄存器写入 32 位控制字
mww 0x40023830 0x00000001

# 将 0x20000100 处的 32 字节区域全部填 0xAA (8-bit 写入 32 次)
mwb 0x20000100 0xAA 32

```



#### 内存块转储与加载：`dump_image` 与 `load_image`

* **完整语法**：
* `dump_image <filename> <address> <size>`
* `load_image <filename> <address> [bin|ihex|elf|s19]`


* **参数**：
* `filename`：本地存储文件路径。
* `address`：内存物理地址。
* `size`：转储的字节总量。
* 镜像格式参数（`bin`、`ihex`、`elf`、`s19`）：缺省通常由后缀自动推导。


* **注释**：
* `dump_image`：将目标芯片内存数据导出到 Host 磁盘文件。
* `load_image`：将 Host 本地二进制或 ELF 数据直接写入芯片 RAM（不调用 Flash 擦写算法，若目标地址是 Flash 则会失败）。


* **示例**：
```tcl
# 提取 128KB 固件备份到本地
dump_image backup_flash.bin 0x08000000 0x20000

# 加载一段测试程序到 SRAM 运行
load_image sram_runner.bin 0x20000000 bin

```



---

### 5. 断点与观察点管理（Breakpoint & Watchpoint）

#### `bp <address> <length> [hw]`

* **完整语法**：`bp <address> <length> [hw]`
* **参数**：
* `<address>`：断点指令地址。
* `<length>`：指令长度（ARM 为 4，Thumb 为 2）。
* `hw`（可选）：指定强制使用硬件断点单元（如 ARM Cortex-M 的 FPB）。在 Flash 中执行代码必须使用 `hw`。


* **注释**：设置断点。
* **示例**：
```tcl
# 在 Flash 代码段 0x08000456 处打硬件断点 (Thumb 模式长度为 2)
bp 0x08000456 2 hw

```



#### `rbp <address>`

* **完整语法**：`rbp <address>`
* **参数**：`<address>` 已设置断点的地址。
* **注释**：Remove Breakpoint。移除指定地址处的断点。
* **示例**：
```tcl
rbp 0x08000456

```



#### `wp [address length (r|w|a) [value [mask]]]`

* **完整语法**：`wp [address length (r|w|a) [value [mask]]]`
* **参数**：
* `address`：监视的变量地址。
* `length`：长度（通常 1、2、4）。
* 访问属性：`r`（读监视）、`w`（写监视）、`a`（读写访问监视 Access）。
* `value` 与 `mask`（可选）：当写入特定值且匹配 mask 时才触发挂起。


* **注释**：设置硬件数据断点（利用 DWT 单元）。无参调用时打印所有观察点。
* **示例**：
```tcl
# 当全局变量地址 0x20000080 发生 4 字节写入时停机
wp 0x20000080 4 w

```



#### `rwp <address>`

* **完整语法**：`rwp <address>`
* **参数**：`<address>` 观察点地址。
* **注释**：移除观察点。
* **示例**：
```tcl
rwp 0x20000080

```



---

### 6. Flash 烧录与保护机制（Flash Subsystem）

#### `flash banks` / `flash list`

* **完整语法**：`flash banks` 或 `flash list`
* **参数**：无。
* **注释**：列出当前系统探测到的所有可用 Flash 存储体（Banks）及其基地址、大小、总线宽度与驱动名称。
* **示例**：
```tcl
flash banks
# 输出: #0: stm32f4x at 0x08000000, size 0x00100000, buswidth 0, chipwidth 0

```



#### `flash probe <bank_id>`

* **完整语法**：`flash probe <bank_id>`
* **参数**：`<bank_id>` 存储体编号，通常首个为 0。
* **注释**：主动向芯片 Flash 控制器读取参数（如 Flash 大小寄存器），动态配置扇区拓扑。
* **示例**：
```tcl
flash probe 0

```



#### `flash erase_sector <bank_id> <first_sector> <last_sector>`

* **完整语法**：`flash erase_sector <bank_id> <first> <last>`
* **参数**：
* `<bank_id>`：目标 Flash Bank（如 0）。
* `<first>`：起始扇区索引（从 0 开始）。
* `<last>`：结束扇区索引；部分平台支持 `last` 关键字代表最后一个扇区。


* **注释**：物理擦除指定范围内的 Flash 扇区。
* **示例**：
```tcl
# 擦除 Bank 0 的扇区 0 到扇区 3
flash erase_sector 0 0 3

```



#### `flash erase_check <bank_id>`

* **完整语法**：`flash erase_check <bank_id>`
* **参数**：`<bank_id>` 存储体编号。
* **注释**：通过 Target 端驻留代码快速检查指定 Bank 的所有扇区是否已经全为 `0xFF`。
* **示例**：
```tcl
flash erase_check 0

```



#### `flash protect <bank_id> <first_sector> <last_sector> <on|off>`

* **完整语法**：`flash protect <bank_id> <first> <last> <on|off>`
* **参数**：
* `on`：使能写保护/读保护。
* `off`：清除保护。


* **注释**：修改选项字节或保护控制位（注意：解除写保护在部分 MCU 上会触发全片全擦除）。
* **示例**：
```tcl
# 解除 Bank 0 扇区 0 到 11 的写保护
flash protect 0 0 11 off

```



#### `program <filename> [pre-verify] [verify] [reset] [exit] [offset]`

* **完整语法**：`program <filename> [args...]`
* **参数**：
* `<filename>`：待烧录文件路径（支持 `.bin`、`.hex`、`.elf`）。
* `pre-verify`（可选）：烧录前校验。
* `verify`（可选）：烧录后逐字节校验。
* `reset`（可选）：烧录校验完成后自动执行硬件复位。
* `exit`（可选）：流程结束直接自动断开并退出 OpenOCD 进程。
* `offset`（可选）：若文件为 raw binary (`.bin`)，需提供物理基地址（如 `0x08000000`）。HEX/ELF 文件内置重定位地址，无需指定。


* **注释**：综合复合指令，其内部依次执行 `reset init` $\rightarrow$ `flash write_image erase` $\rightarrow$ `verify_image` $\rightarrow$ `reset run`。
* **示例**：
```tcl
# 产线最常用的单行全自动化刷机指令
program app.elf verify reset exit

# 烧录纯二进制文件
program app.bin verify reset 0x08000000 exit

```



---

## 四、 工业级生产实战场景

### 场景 1：工厂产线自动化无头烧录与防呆闭环

在工业批量生产环境中，烧录工位需要通过 Linux Shell 脚本驱动 OpenOCD 完成“连接-解除芯片保护-整片擦除-烧录-校验-重锁保护-复位”的完整闭环，并通过命令返回值确定良率。

```bash
#!/usr/bin/env bash
set -e

FIRMWARE_FILE="production_v2.4.0.hex"
SERIAL_PROBE="CMSIS-DAP-SN-20260901"

echo "==== 1. 开始烧录作业 ===="

openocd \
  -f interface/cmsis-dap.cfg \
  -c "cmsis_dap_serial $SERIAL_PROBE" \
  -f target/stm32f4x.cfg \
  -c "adapter speed 10000" \
  -c "init" \
  -c "reset init" \
  -c "echo \">>> 清除潜在写保护\"" \
  -c "stm32f2x unlock 0" \
  -c "reset init" \
  -c "echo \">>> 烧写固件与双重校验\"" \
  -c "flash write_image erase $FIRMWARE_FILE" \
  -c "verify_image $FIRMWARE_FILE" \
  -c "echo \">>> 锁定芯片读保护(RDP Level 1)\"" \
  -c "stm32f2x lock 0" \
  -c "reset run" \
  -c "shutdown"

if [ $? -eq 0 ]; then
    echo "==== 结果: 烧录成功 (PASS) ===="
    exit 0
else
    echo "==== 结果: 烧录失败 (FAIL) ===="
    exit 1
fi

```

---

### 场景 2：现场设备死锁（HardFault/Watchdog）无侵入式现场还原

当设备死机挂死在现场时，绝不能直接复位，否则所有的调用栈和崩溃现场都会被销毁。工程师需在不复位 CPU（No-Reset Attach）的前提下切入并排查：

1. **终端接入**：
```bash
openocd -f interface/jlink.cfg -c "transport select swd" -f target/stm32f4x.cfg -c "reset_config none"

```


2. **通过 Telnet 提取关键寄存器与异常现场**：
```tcl
$ telnet localhost 4444

# 1. 强制中止核心（无复位挂起）
> halt
target halted due to debug-request, current mode: Handler HardFault
xPSR: 0x21000003 pc: 0x08001a44 msp: 0x2001ffb0

# 2. 读取当前核心通用寄存器组
> reg
===== arm v7m registers
(0) r0 (/32): 0x00000000
(1) r1 (/32): 0x40021000
...
(13) sp (/32): 0x2001ffb0
(14) lr (/32): 0xfffffff9   <-- 确认异常前使用的是 MSP 栈
(15) pc (/32): 0x08001a44

# 3. 查看 Cortex-M 的可配置故障状态寄存器 (CFSR, 地址 0xE000ED28)
> mdw 0xE000ED28 1
0xe000ed28: 0x00010000      <-- BIT16 = 1 (UNDEFINSTR: 执行了未定义指令)

# 4. Dump 崩溃时刻的 MSP 栈内存 (向上提取 64 字节)
> mdw 0x2001ffb0 16

# 5. 将整个 128KB 运行态 RAM 完整导出，留存现场离线定位
> dump_image core_ram_dump.bin 0x20000000 0x20000
dumped 131072 bytes in 0.420100s (304.689 KiB/s)

```



---

### 场景 3：产线唯一序列号（UID）与 MAC 地址批量注入

很多设备需要出厂烧录一个单独的序列号或加密密钥到特定的保留 Flash/OTP 扇区中，不需要重新编译完整二进制：

```bash
# 目标：向 OTP/保留扇区地址 0x080E0000 写入动态 MAC 地址 (00:80:E1:22:33:44) 与 64位 设备编号
DEVICE_SN_HIGH=0x20260921
DEVICE_SN_LOW=0x00000001
MAC_WORD1=0x8000
MAC_WORD2=0x443322E1

openocd \
  -f interface/cmsis-dap.cfg \
  -f target/stm32f4x.cfg \
  -c "init" \
  -c "reset init" \
  -c "echo \">>> 准备写入单板参数...\"" \
  -c "mww 0x20000000 $DEVICE_SN_HIGH" \
  -c "mww 0x20000004 $DEVICE_SN_LOW" \
  -c "mww 0x20000008 $MAC_WORD1" \
  -c "mww 0x2000000C $MAC_WORD2" \
  -c "flash write_sector 0 11 11" \
  -c "echo \">>> 校验写入数据...\"" \
  -c "mdw 0x080E0000 4" \
  -c "reset run" \
  -c "shutdown"

```

---

## 五、 常用命令对照速查

| 指令类别 | 命令格式 | 典型用途 | 破坏性/只读 |
| --- | --- | --- | --- |
| **状态流转** | `halt` / `resume [addr]` | 暂停 / 恢复处理器执行 | 运行态控制 |
| **复位控制** | `reset [run|halt|init]` | 芯片级复位，`init` 可执行配置钩子 | 重置硬件 |
| **单步执行** | `step [addr]` | 指令级单步推进 | 运行态控制 |
| **寄存器** | `reg [name [val]]` | 检视或覆盖通用/控制寄存器 | 覆盖写时有风险 |
| **数据读取** | `mdw <addr> [count]` | 读取 32-bit 外设/内存值 | 只读 |
| **数据写入** | `mww <addr> <val> [count]` | 修改 32-bit 外设/内存值 | 破坏性写 |
| **全自动刷机** | `program <file> [args]` | 组合执行擦、写、校验、复位 | 覆盖固件 |
| **镜像导出** | `dump_image <file> <addr> <size>` | 导出 Flash/RAM 物理内存镜像 | 只读 |
| **断点操作** | `bp <addr> <len> [hw]` | 打入代码断点（Flash 须选 hw） | 调试拦截 |
| **数据断点** | `wp <addr> <len> (r|w|a)` | 数据写/读监视 | 调试拦截 |
