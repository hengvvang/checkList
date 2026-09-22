set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR arm)

set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)
set(CMAKE_OBJCOPY arm-none-eabi-objcopy)
set(CMAKE_SIZE arm-none-eabi-size)

set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)

set(MCPU cortex-m3)
set(MFLOAT_ABI soft)

set(CMAKE_C_FLAGS
    "-mcpu=${MCPU} -mthumb -mfloat-abi=${MFLOAT_ABI} \
    -ffunction-sections -fdata-sections \
    -Wall -Wextra"
)

set(CMAKE_ASM_FLAGS
    "-mcpu=${MCPU} -mthumb -mfloat-abi=${MFLOAT_ABI}"
)

set(CMAKE_EXE_LINKER_FLAGS
    "-mcpu=${MCPU} -mthumb -mfloat-abi=${MFLOAT_ABI} \
    -T${CMAKE_SOURCE_DIR}/app/linker/STM32F103C8Tx_FLASH.ld \
    -Wl,--gc-sections \
    -Wl,-Map=${CMAKE_BINARY_DIR}/TempController.map \
    --specs=nosys.specs \
    --specs=nano.specs"
)
