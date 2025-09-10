from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import sqlite3

app = FastAPI(title='JI ERP 最簡版')

def get_db():
    conn = sqlite3.connect('ji_erp.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get('/', response_class=HTMLResponse)
async def read_index():
    return HTMLResponse(content='''
<!DOCTYPE html>
<html>
<head>
    <title>JI ERP 最簡版</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        .container { max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
        h1 { color: #333; text-align: center; }
        input { width: 100%; padding: 10px; margin: 5px 0; border: 1px solid #ddd; border-radius: 5px; }
        button { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
        .message { margin-top: 20px; padding: 10px; border-radius: 5px; }
        .success { background: #d4edda; color: #155724; }
        .error { background: #f8d7da; color: #721c24; }
        .dashboard { display: none; }
        .stat-card { background: #f8f9fa; padding: 20px; margin: 10px; border-radius: 5px; text-align: center; display: inline-block; min-width: 150px; }
    </style>
</head>
<body>
    <div class="container">
        <h1> JI ERP 最簡版系統</h1>
        
        <div id="login-form">
            <h2>用戶登入</h2>
            <form id="loginForm">
                <input type="text" id="username" placeholder="用戶名" required>
                <input type="password" id="password" placeholder="密碼" required>
                <button type="submit">登入</button>
            </form>
            <div id="message"></div>
        </div>
        
        <div id="dashboard" class="dashboard">
            <h2>歡迎使用 JI ERP 系統！</h2>
            <div class="stats">
                <div class="stat-card">
                    <h3>總收入</h3>
                    <p id="total-income"></p>
                </div>
                <div class="stat-card">
                    <h3>總支出</h3>
                    <p id="total-expense"></p>
                </div>
                <div class="stat-card">
                    <h3>淨利潤</h3>
                    <p id="net-profit"></p>
                </div>
            </div>
            <div style="margin-top: 30px;">
                <h3>最近交易</h3>
                <div id="transactions-list"></div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('loginForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            try {
                const response = await fetch('/api/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: username=&password=
                });
                
                const result = await response.json();
                
                if (result.success) {
                    document.getElementById('login-form').style.display = 'none';
                    document.getElementById('dashboard').style.display = 'block';
                    loadDashboard();
                } else {
                    document.getElementById('message').innerHTML = '<div class="error">' + result.message + '</div>';
                }
            } catch (error) {
                document.getElementById('message').innerHTML = '<div class="error">登入失敗，請重試</div>';
            }
        });
        
        async function loadDashboard() {
            try {
                const response = await fetch('/api/transactions');
                const result = await response.json();
                
                if (result.success) {
                    const transactions = result.data;
                    let totalIncome = 0;
                    let totalExpense = 0;
                    
                    transactions.forEach(t => {
                        if (t.type === 'income') {
                            totalIncome += parseFloat(t.amount);
                        } else {
                            totalExpense += parseFloat(t.amount);
                        }
                    });
                    
                    document.getElementById('total-income').textContent = '$' + totalIncome.toLocaleString();
                    document.getElementById('total-expense').textContent = '$' + totalExpense.toLocaleString();
                    document.getElementById('net-profit').textContent = '$' + (totalIncome - totalExpense).toLocaleString();
                    
                    const listHtml = transactions.map(t => 
                        '<div style="padding: 10px; border-bottom: 1px solid #eee;">' +
                        '<strong>' + (t.type === 'income' ? '收入' : '支出') + '</strong> - ' +
                        '$' + parseFloat(t.amount).toLocaleString() + ' - ' +
                        (t.description || '無描述') + ' - ' +
                        (t.category || '無分類') +
                        '</div>'
                    ).join('');
                    
                    document.getElementById('transactions-list').innerHTML = listHtml || '<div>暫無交易記錄</div>';
                }
            } catch (error) {
                console.error('載入數據失敗:', error);
            }
        }
    </script>
</body>
</html>
    ''')

@app.post('/api/login')
async def login(username: str = Form(...), password: str = Form(...)):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return {'success': True, 'message': '登入成功', 'user': dict(user)}
    else:
        return {'success': False, 'message': '用戶名或密碼錯誤'}

@app.get('/api/transactions')
async def get_transactions():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions ORDER BY created_at DESC')
    transactions = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {'success': True, 'data': transactions}

if __name__ == '__main__':
    import uvicorn
    print(' 啟動 JI ERP 最簡版服務器...')
    print(' 訪問地址: http://localhost:8000')
    print(' 測試帳號: admin/admin123 或 user1/user123')
    uvicorn.run(app, host='0.0.0.0', port=8000)
