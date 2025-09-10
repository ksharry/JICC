from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# 創建 FastAPI 應用
app = FastAPI(
    title='JI ERP',
    version='1.0.0',
    debug=True
)

# 主頁面
@app.get('/', response_class=HTMLResponse)
async def read_index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>JI ERP</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>JI ERP 系統</h1>
        <p>系統正在重構中...</p>
        <p>新的模組化架構正在開發中</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    import uvicorn
    print(' 啟動 JI ERP 服務器...')
    print(' 訪問地址: http://localhost:8000')
    uvicorn.run(app, host='0.0.0.0', port=8000)
