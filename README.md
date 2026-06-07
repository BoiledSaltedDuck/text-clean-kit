# text-clean-kit 文本文件清洗处理工具

[![PyPI version](https://img.shields.io/pypi/v/text-clean-kit)](https://pypi.org/project/text-clean-kit/)
[![Downloads](https://img.shields.io/pypi/dm/text-clean-kit)](https://pypi.org/project/text-clean-kit/)
[![License](https://img.shields.io/pypi/l/text-clean-kit)](https://github.com/BoiledSaltedDuck/text-clean-kit/blob/main/LICENSE)

## 安装

```bash
pip install text-clean-kit
```

## 用法

```bash
# 去除文件每行首尾空格
text-clean messy.txt trim

# 去除重复行
text-clean ./data/ dedup

# 删除空行
text-clean ./logs/ strip-blank

# 统一换行符为 LF
text-clean ./scripts/ normalize-newline
```

## 支持的操作

| 操作 | 说明 |
|------|------|
| `trim` | 去除每行首尾空白 |
| `dedup` | 去除重复行（保留首次出现） |
| `dedup-consecutive` | 去除连续重复行 |
| `strip-blank` | 删除空行和仅含空白字符的行 |
| `normalize-newline` | 统一换行符为 LF (\\n) |
| `remove-bom` | 移除 UTF-8 BOM 头 |
| `lowercase` | 转为小写 |
| `uppercase` | 转为大写 |

## 特点

- 支持单个文件或整个目录批量处理
- 自动检测 UTF-8/GBK/Latin-1 编码
- 支持就地修改或输出到新目录
- 纯 Python，零依赖
- 兼容 Windows/Linux/Mac

## 支持

如果 text-clean-kit 帮到了您，欢迎打赏支持：

```
USDT (TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa
```

您的支持是开源项目持续发展的动力 ❤️
