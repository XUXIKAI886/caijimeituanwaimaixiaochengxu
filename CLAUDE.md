# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个呈尚策划美团外卖数据工具，使用Python和tkinter构建的桌面应用程序。主要功能包括解析美团数据文件、自动下载产品图片、生成Excel报告，并支持文件变化监控。

> **⚠️ 重要声明：仅供公司内部测试使用，禁止商用**

## 常用开发命令

### 环境设置
```bash
# 安装依赖
pip install -r requirements.txt

# 或手动安装核心依赖
pip install requests aiohttp openpyxl pillow watchdog aiofiles
```

### 程序运行
```bash
# 标准启动方式
python main.py

# 使用批处理文件启动（Windows）
启动程序.bat

# 运行特定测试文件
python test_simple_start.py
python test_collection.py
python analyze_first_file.py
```

### 调试和测试
```bash
# 运行完整系统测试
python test_complete_system.py

# 测试文件监控功能
python test_auto_monitoring.py

# 调试数据解析
python debug_parsing.py

# 分析数据文件结构
python analyze_first_file.py
```

## 核心架构

### 主要组件

#### 1. MeituanDataCollector (main.py)
- **核心类**：主程序入口，管理整个应用程序的生命周期
- **GUI组件**：使用tkinter构建用户界面，包括文件选择、进度显示、日志输出
- **文件监控**：集成watchdog库实现文件变化监控，支持自动数据更新
- **异步图片下载**：使用aiohttp实现并发图片下载

#### 2. FileChangeHandler (main.py:29-65)
- **文件监控器**：继承FileSystemEventHandler，监控指定数据文件的变化
- **防抖机制**：避免频繁触发处理，设置3秒防抖时间
- **双文件监控**：同时监控两个数据文件的修改事件

#### 3. 数据处理流程
- **第一阶段**：解析店铺分类文件 (`xiaochengxumeituan.txt`)
- **第二阶段**：解析产品数据文件 (`xiaochengxumeituan01.txt`)
- **第三阶段**：合并数据，异步下载产品图片
- **第四阶段**：生成Excel报告，包含产品信息和图片链接

### 数据文件架构

#### 预期数据结构
```
数据文件位置: D:\ailun\
├── xiaochengxumeituan.txt     # 店铺分类和基础产品数据
└── xiaochengxumeituan01.txt   # 更新的产品数据

输出文件结构:
├── 输出文件\
│   ├── 产品图片\              # 下载的产品图片
│   └── 美团外卖数据报告_时间戳.xlsx
└── 采集日志.log               # 程序运行日志
```

#### JSON数据格式
- **分类数据**：`data.food_spu_tags` 包含产品分类信息
- **产品数据**：`data.food_spu_tags[].spus` 包含具体产品信息
- **关键字段**：`name`(产品名)、`price`(价格)、`picture`(图片URL)、`spec`(规格)

### 关键特性

#### 异步处理
- 使用`asyncio`和`aiohttp`进行并发图片下载
- 多线程处理避免UI阻塞，主线程负责界面更新

#### 文件监控机制
- 实时监控数据文件变化，自动触发数据重新处理
- 支持手动启动/停止监控功能

#### 错误处理
- 完整的日志记录系统，支持文件和界面双重输出
- 异常处理覆盖文件读取、网络请求、Excel生成等环节

### 测试文件说明

- `test_simple_start.py`: 基础GUI测试，验证界面启动
- `test_collection.py`: 数据采集功能测试
- `test_auto_monitoring.py`: 文件监控功能测试
- `analyze_first_file.py`: 数据文件结构分析工具
- `debug_parsing.py`: 数据解析调试工具

## 开发注意事项

### 文件路径配置
- 默认数据文件路径：`D:\ailun\`
- 所有路径处理使用`pathlib.Path`或`os.path`确保跨平台兼容性
- 图片下载路径：`输出文件/产品图片/`

### 依赖管理
- 核心依赖：`requests`、`aiohttp`、`openpyxl`、`pillow`、`watchdog`
- GUI依赖：`tkinter`（Python标准库）
- 日志处理：`logging`（Python标准库）

### 编码规范
- 所有Python文件使用UTF-8编码
- 中文字符处理确保编码正确性
- 异常处理包含详细的中文错误信息