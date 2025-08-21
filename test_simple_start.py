# -*- coding: utf-8 -*-
"""
测试简单启动，找出弹窗问题
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

import tkinter as tk
from tkinter import ttk
import threading
import time

def simple_test():
    """简单测试程序启动"""
    print("创建简单测试窗口...")
    
    root = tk.Tk()
    root.title("简单测试")
    root.geometry("400x300")
    
    # 添加一些基本组件
    ttk.Label(root, text="测试窗口", font=("微软雅黑", 12)).pack(pady=20)
    
    def test_button():
        print("按钮被点击")
    
    ttk.Button(root, text="测试按钮", command=test_button).pack(pady=10)
    
    print("窗口创建完成，启动主循环...")
    root.mainloop()
    print("程序退出")

def test_with_monitoring():
    """测试包含监控功能的简化版本"""
    print("测试监控功能...")
    
    from main import MeituanDataCollector
    
    print("创建MeituanDataCollector实例...")
    collector = MeituanDataCollector()
    
    print("准备启动程序...")
    # 不调用run方法，直接启动mainloop
    collector.root.mainloop()
    print("程序退出")

if __name__ == "__main__":
    print("=== 启动测试 ===")
    print("1. 简单窗口测试")
    
    # 先测试简单窗口
    #simple_test()
    
    print("\n2. 监控功能测试")
    test_with_monitoring()