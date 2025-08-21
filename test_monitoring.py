# -*- coding: utf-8 -*-
"""
测试文件监控功能
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from main import MeituanDataCollector
import time
import threading

def test_monitoring():
    """测试文件监控功能"""
    print("=== 测试文件监控功能 ===")
    
    # 创建采集器实例（不启动GUI）
    collector = MeituanDataCollector()
    
    # 设置文件路径
    file1 = r"D:\ailun\xiaochengxumeituan.txt"
    file2 = r"D:\ailun\xiaochengxumeituan01.txt"
    
    collector.file1_var.set(file1)
    collector.file2_var.set(file2)
    
    print(f"监控文件1: {file1}")
    print(f"监控文件2: {file2}")
    print(f"文件1存在: {os.path.exists(file1)}")
    print(f"文件2存在: {os.path.exists(file2)}")
    
    if not os.path.exists(file1) or not os.path.exists(file2):
        print("数据文件不存在，无法测试监控")
        return
    
    try:
        print("\n1. 启动文件监控...")
        collector.start_monitoring()
        
        print("\n2. 监控已启动，等待文件变化...")
        print("   提示：您可以修改第二份文档来测试监控功能")
        print("   程序将等待20秒...")
        
        # 等待20秒检测文件变化
        for i in range(20):
            time.sleep(1)
            if i % 5 == 0:
                print(f"   等待中... ({i}/20秒)")
        
        print("\n3. 停止文件监控...")
        collector.stop_monitoring()
        
        print("\n=== 监控测试完成 ===")
        print("如果您在测试期间修改了第二份文档，应该会看到检测消息")
        
    except Exception as e:
        print(f"监控测试失败: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # 确保清理资源
        if collector.is_monitoring:
            collector.stop_monitoring()

if __name__ == "__main__":
    test_monitoring()