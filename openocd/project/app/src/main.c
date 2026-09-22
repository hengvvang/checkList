#include <stdint.h>

#define RCC_BASE        0x40021000UL
#define GPIOC_BASE      0x40011000UL
#define SYSTICK_BASE    0xE000E010UL

#define RCC_APB2ENR     (*(volatile uint32_t *)(RCC_BASE + 0x18UL))

#define GPIOC_CRH       (*(volatile uint32_t *)(GPIOC_BASE + 0x04UL))
#define GPIOC_ODR       (*(volatile uint32_t *)(GPIOC_BASE + 0x0CUL))

#define SYSTICK_CTRL    (*(volatile uint32_t *)(SYSTICK_BASE + 0x00UL))
#define SYSTICK_LOAD    (*(volatile uint32_t *)(SYSTICK_BASE + 0x04UL))
#define SYSTICK_VAL     (*(volatile uint32_t *)(SYSTICK_BASE + 0x08UL))

#define RCC_APB2ENR_IOPCEN (1UL << 4)
#define GPIOC_PIN13        (1UL << 13)

#define SYSTICK_CTRL_ENABLE    (1UL << 0)
#define SYSTICK_CTRL_CLKSOURCE (1UL << 2)
#define SYSTICK_CTRL_COUNTFLAG (1UL << 16)

static void systick_init(void)
{
    /*
     * 复位后的 STM32F103 默认系统时钟为 8 MHz。
     * 8,000,000 / 1000 - 1 = 7999，因此每次溢出约为 1 ms。
     */
    SYSTICK_LOAD = 8000UL - 1UL;
    SYSTICK_VAL = 0;
    SYSTICK_CTRL = SYSTICK_CTRL_ENABLE | SYSTICK_CTRL_CLKSOURCE;
}

static void delay_ms(uint32_t milliseconds)
{
    while (milliseconds > 0U) {
        while ((SYSTICK_CTRL & SYSTICK_CTRL_COUNTFLAG) == 0U) {
        }

        milliseconds--;
    }
}

static void led_init(void)
{
    /*
     * 常见 STM32F103 最小系统板的 LED 接在 PC13。
     * PC13 位于 GPIOC_CRH 的 [23:20] 位段。
     */
    RCC_APB2ENR |= RCC_APB2ENR_IOPCEN;

    GPIOC_CRH &= ~(0xFUL << 20);
    GPIOC_CRH |= (0x2UL << 20);

    GPIOC_ODR |= GPIOC_PIN13;
}

static void led_toggle(void)
{
    GPIOC_ODR ^= GPIOC_PIN13;
}

int main(void)
{
    led_init();
    systick_init();

    while (1) {
        led_toggle();
        delay_ms(500);
    }
}
