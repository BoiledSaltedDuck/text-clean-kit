# text-clean-kit 文本文件清洗处理工具

[![PyPI version](https://img.shields.io/pypi/v/text-clean-kit)](https://pypi.org/project/text-clean-kit/)
[![Downloads](https://img.shields.io/pypi/dm/text-clean-kit)](https://pypi.org/project/text-clean-kit/)
[![License](https://img.shields.io/pypi/l/text-clean-kit)](https://github.com/BoiledSaltedDuck/text-clean-kit/blob/main/LICENSE)

> **Office Tools Kit 系列** — 用AI写代码，用工具提效。一行命令搞定日常办公与开发杂务。

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

## 🧰 Office Tools Kit 系列工具

本工具属于 **Office Tools Kit 系列**，同类工具推荐：

| 工具 | 功能 | 安装 |
|------|------|------|
| [office-tools-kit](https://pypi.org/project/office-tools-kit/) | Excel合并拆分、PDF合并 | `pip install office-tools-kit` |
| [file-org-kit](https://pypi.org/project/file-org-kit/) | 文件智能分类整理 | `pip install file-org-kit` |
| [img-convert-kit](https://pypi.org/project/img-convert-kit/) | 图片格式批量转换 | `pip install img-convert-kit` |
| [img-resize-kit](https://pypi.org/project/img-resize-kit/) | 图片批量缩放与压缩 | `pip install img-resize-kit` |
| [json-tool-kit](https://pypi.org/project/json-tool-kit/) | JSON 文件处理 | `pip install json-tool-kit` |
| [markdown-kit](https://pypi.org/project/markdown-kit/) | Markdown 文档辅助 | `pip install markdown-kit` |
| [qr-code-kit](https://pypi.org/project/qr-code-kit/) | 二维码生成与解析 | `pip install qr-code-kit` |
| [text-clean-kit](https://pypi.org/project/text-clean-kit/) | 文本文件清洗处理 | `pip install text-clean-kit` |
| [unit-convert-kit](https://pypi.org/project/unit-convert-kit/) | 单位换算 | `pip install unit-convert-kit` |

> 📚 更多工具请访问 [BoiledSaltedDuck 工具主页](https://boiledsaltedduck.github.io/)

## 支持

如果 text-clean-kit 帮到了您，欢迎打赏支持：

```
USDT (TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa
```

您的支持是开源项目持续发展的动力 ❤️
