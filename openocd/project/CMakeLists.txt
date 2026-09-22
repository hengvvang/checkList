cmake_minimum_required(VERSION 3.20)

project(TempController C ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_executable(${PROJECT_NAME}
    app/src/main.c
    app/src/startup_stm32f103xb.s
)

target_include_directories(${PROJECT_NAME}
    PRIVATE
        app/include
)

target_compile_options(${PROJECT_NAME}
    PRIVATE
        $<$<COMPILE_LANGUAGE:C>:-Og>
        $<$<COMPILE_LANGUAGE:C>:-g3>
)

set_target_properties(${PROJECT_NAME}
    PROPERTIES
        SUFFIX ".elf"
)

add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
    COMMAND ${CMAKE_OBJCOPY}
        -O ihex
        $<TARGET_FILE:${PROJECT_NAME}>
        ${CMAKE_CURRENT_BINARY_DIR}/TempController.hex

    COMMAND ${CMAKE_OBJCOPY}
        -O binary
        $<TARGET_FILE:${PROJECT_NAME}>
        ${CMAKE_CURRENT_BINARY_DIR}/TempController.bin

    COMMAND ${CMAKE_SIZE}
        $<TARGET_FILE:${PROJECT_NAME}>

    COMMENT "Generating ELF, HEX and BIN files"
)
