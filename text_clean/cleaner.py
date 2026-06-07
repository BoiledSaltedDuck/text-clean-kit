#!/usr/bin/env python3
"""
text-clean-kit - 文本文件清洗处理工具
功能：批量清洗文本文件（去重行、去空行、去首尾空格、统一换行符、正则替换）
用法：text-clean [输入文件/目录] [操作] [输出目录(可选)]
      text-clean ./data/ dedup ./output/
      text-clean messy.txt trim
"""
import sys
import re
from pathlib import Path

OPERATIONS = {
    "trim": "去除每行首尾空白",
    "dedup": "去除重复行（保留首次出现）",
    "dedup-consecutive": "去除连续重复行",
    "strip-blank": "删除空行和仅含空白字符的行",
    "normalize-newline": "统一换行符为 LF (\\n)",
    "remove-bom": "移除 UTF-8 BOM 头",
    "lowercase": "转为小写",
    "uppercase": "转为大写",
}

def process_text(content, operation):
    """对文本内容执行指定操作"""
    if operation == "trim":
        lines = content.splitlines(True)
        lines = [line.rstrip('\n\r').strip() + '\n' for line in lines]
        return ''.join(lines)

    elif operation == "dedup":
        seen = set()
        result = []
        for line in content.splitlines(True):
            stripped = line.rstrip('\n\r')
            if stripped not in seen:
                seen.add(stripped)
                result.append(line)
        return ''.join(result)

    elif operation == "dedup-consecutive":
        result = []
        prev = None
        for line in content.splitlines(True):
            stripped = line.rstrip('\n\r')
            if stripped != prev:
                prev = stripped
                result.append(line)
        return ''.join(result)

    elif operation == "strip-blank":
        lines = content.splitlines(True)
        lines = [l for l in lines if l.strip()]
        return ''.join(lines)

    elif operation == "normalize-newline":
        return content.replace('\r\n', '\n').replace('\r', '\n')

    elif operation == "remove-bom":
        return content.lstrip('\ufeff')

    elif operation == "lowercase":
        return content.lower()

    elif operation == "uppercase":
        return content.upper()

    else:
        raise ValueError(f"不支持的操作: {operation}")


def process_file(input_file, operation, output_file=None):
    """处理单个文件"""
    try:
        with open(input_file, 'rb') as f:
            raw = f.read()

        # 检测编码
        try:
            content = raw.decode('utf-8')
        except UnicodeDecodeError:
            try:
                content = raw.decode('gbk')
            except UnicodeDecodeError:
                try:
                    content = raw.decode('latin-1')
                except:
                    print(f"  ✗ {input_file.name}: 无法解码文件")
                    return False

        result = process_text(content, operation)

        if output_file is None:
            output_file = input_file

        with open(output_file, 'w', encoding='utf-8', newline='\n') as f:
            f.write(result)

        original_size = len(raw)
        new_size = len(result.encode('utf-8'))
        saved = original_size - new_size
        print(f"  ✓ {input_file.name} ({original_size}→{new_size} bytes, {'+' if saved < 0 else ''}{saved})")
        return True

    except Exception as e:
        print(f"  ✗ {input_file.name}: {e}")
        return False


def process_path(path, operation, output_dir=None):
    """处理文件或目录"""
    p = Path(path)

    if p.is_file():
        if output_dir:
            out_path = Path(output_dir) / p.name
            out_path.parent.mkdir(parents=True, exist_ok=True)
        else:
            out_path = None
        return process_file(p, operation, out_path)

    elif p.is_dir():
        text_exts = {'.txt', '.csv', '.md', '.log', '.json', '.xml', '.yaml', '.yml', '.ini', '.cfg', '.conf', '.bat', '.sh', '.py', '.js', '.html', '.css'}
        files = []
        for ext in text_exts:
            files.extend(list(p.glob(f"*{ext}")))
        files.sort()

        if not files:
            print(f"错误：目录 {path} 中没有找到文本文件")
            return False

        print(f"找到 {len(files)} 个文本文件")

        success = 0
        for f in files:
            if output_dir:
                out_path = Path(output_dir) / f.name
                out_path.parent.mkdir(parents=True, exist_ok=True)
            else:
                out_path = None

            if process_file(f, operation, out_path):
                success += 1

        print(f"\n完成！成功处理 {success}/{len(files)} 个文件")
        return success > 0

    else:
        print(f"错误：路径 {path} 不存在")
        return False


def _show_promotion():
    print("\n" + "=" * 55)
    print("  🔧 text-clean-kit - 文本文件清洗处理工具")
    print("  📦 pip install text-clean-kit")
    print("  ☕ 如果帮到了您，欢迎打赏支持:")
    print("     USDT(TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa")
    print("  ⭐ https://github.com/BoiledSaltedDuck/text-clean-kit")
    print("=" * 55)


def main():
    if len(sys.argv) < 3:
        print("用法: text-clean [输入文件/目录] [操作] [输出目录(可选)]")
        print("示例: text-clean ./data/ dedup ./output/")
        print("      text-clean messy.txt trim")
        print("      text-clean ./logs/ strip-blank")
        print()
        print("支持的操作:")
        for op, desc in OPERATIONS.items():
            print(f"  {op:22s} {desc}")
        sys.exit(1)

    input_path = sys.argv[1]
    operation = sys.argv[2]

    if operation not in OPERATIONS:
        print(f"错误：不支持的操作 '{operation}'")
        print("支持的操作:", ", ".join(OPERATIONS.keys()))
        sys.exit(1)

    output_dir = sys.argv[3] if len(sys.argv) > 3 else None

    success = process_path(input_path, operation, output_dir)
    if success:
        _show_promotion()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
