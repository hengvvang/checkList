# TempController

这是一个面向 STM32F103C8T6 的最小裸机项目，使用：

- Arm GNU Toolchain
- CMake
- Ninja
- OpenOCD
- ST-Link
- SWD

当前阶段的目标是：

1. 编译一个不依赖 HAL 的 Cortex-M3 程序；
2. 生成 ELF、HEX、BIN 文件；
3. 使用 OpenOCD 烧录；
4. 使用 GDB 连接并调试；
5. 让 PC13 上的 LED 每 500 ms 翻转一次。

当前 Flash 布局：

```text
Flash: 0x08000000 - 0x0800FFFF, 64 KiB
RAM:   0x20000000 - 0x20004FFF, 20 KiB
```

当前还没有加入 Bootloader。后续会把应用迁移到 `0x08004000`，
并增加生产配置区。

## 构建

在项目根目录执行：

```powershell
cmake -S . -B .\build -G Ninja `
  -DCMAKE_TOOLCHAIN_FILE=.\toolchain-arm-none-eabi.cmake `
  -DCMAKE_BUILD_TYPE=Debug

cmake --build .\build
```

预期生成：

```text
build\TempController.elf
build\TempController.hex
build\TempController.bin
build\TempController.map
```

## OpenOCD 烧录

确保硬件已经连接后，在项目根目录执行：

```powershell
openocd -s . -f .\openocd\flash.cfg
```

## OpenOCD 调试服务器

```powershell
openocd -s . -f .\openocd\debug.cfg
```

另一个终端启动 GDB：

```powershell
arm-none-eabi-gdb .\build\TempController.elf
```

在 GDB 中执行：

```text
target extended-remote localhost:3333
monitor reset halt
break main
continue
```
