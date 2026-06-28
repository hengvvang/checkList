# 来源、加载逻辑与统计口径

抽取时使用的 Zed 源码 commit：`afaef857b987d924c5ec09265a83feb030283f48`。

## 为什么默认 VS Code 布局只取 Windows 默认 keymap

- 官方文档 `docs/src/key-bindings.md` 写明 `base_keymap` 支持 `VS Code (default)`，并指向各平台默认 keymap 文件。
- `crates/settings/src/base_keymap_setting.rs` 中 `BaseKeymap::VSCode` 是默认值。
- 同一文件的 `BaseKeymap::asset_path()` 对 `VSCode` 返回 `None`，说明 VS Code 布局没有额外覆盖资产文件。
- 当前环境是 Windows，所以 `crates/settings/src/settings.rs` 选择 `DEFAULT_KEYMAP_PATH = "keymaps/default-windows.json"`。

## 运行时加载顺序

见 `crates/zed/src/zed.rs::load_default_keymap`：

1. `assets/keymaps/default-windows.json`
2. base keymap 额外文件；VS Code 为 `None`，所以无额外文件
3. `assets/keymaps/vim.json`，仅 `vim_mode` 或 `helix_mode` 开启时加载
4. `assets/keymaps/specific-overrides.json`，非 macOS 平台加载，且在内置默认/base/vim 后加载，冲突时优先级更高

## 未纳入默认 VS Code 表的文件

- `initial.json`：用户 keymap 初始模板。
- `storybook.json`：Storybook/组件预览用途。
- `linux/atom.json`、`linux/jetbrains.json`、`linux/sublime_text.json`、`linux/emacs.json`、`linux/cursor.json` 等：其它 base keymap，不属于默认 VS Code 布局。
- macOS 目录下对应布局：不是当前 Windows 平台默认。

## 表格说明

- `context` 为空时在文档中标为 `全局 / 无 context`。
- `context` 使用 Zed keymap 语法，如 `&&`、`||`、`!`、`>`。
- `ctrl-k ctrl-s` 这类写法表示 key sequence：先按前一组键，再按后一组键。
- 表格中的 Action 与参数完全来自源 keymap，不人工猜测中文动作名。
