@echo off
echo 呈尚策划 美团外卖数据工具
echo ========================
echo 仅供公司内部测试使用，禁止商用
echo ========================

echo 检查Python依赖...
pip install -r requirements.txt

echo.
echo 启动程序...
python main.py

pause