#!/usr/bin/env python3
"""
自動化測試運行腳本
"""
import subprocess
import sys
import os

def run_tests():
    """運行所有測試"""
    print("🧪 開始運行自動化測試...")
    
    # 確保在正確的目錄
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 運行測試
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "tests/", 
        "-v", 
        "--tb=short",
        "--cov=app",
        "--cov-report=html",
        "--cov-report=term"
    ], capture_output=True, text=True)
    
    print("測試輸出:")
    print(result.stdout)
    
    if result.stderr:
        print("錯誤輸出:")
        print(result.stderr)
    
    return result.returncode == 0

def run_linting():
    """運行代碼檢查"""
    print("🔍 開始運行代碼檢查...")
    
    # 運行 flake8
    flake8_result = subprocess.run([
        sys.executable, "-m", "flake8", 
        "app/", 
        "--max-line-length=88",
        "--exclude=__pycache__"
    ], capture_output=True, text=True)
    
    if flake8_result.stdout:
        print("Flake8 輸出:")
        print(flake8_result.stdout)
    
    return flake8_result.returncode == 0

def main():
    """主函數"""
    print("�� JI ERP MVC 自動化測試流程")
    print("=" * 50)
    
    # 運行代碼檢查
    lint_success = run_linting()
    if not lint_success:
        print("❌ 代碼檢查失敗")
        return False
    
    print("✅ 代碼檢查通過")
    
    # 運行測試
    test_success = run_tests()
    if not test_success:
        print("❌ 測試失敗")
        return False
    
    print("✅ 所有測試通過")
    print("🎉 自動化測試流程完成！")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)