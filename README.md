# JICC ���~�귽�W���t��
python -m pytest tests/ -v


�@�Ӱ�� FastAPI + React ���{�N�� ERP �t�ΡA�M�����p���~�]�p�A���ѧ��㪺�~�Ⱥ޲z�ѨM��סC

##  �\��S��

### �֤߼Ҷ�
- **�Τ�޲z** - ���㪺�Τ�{�һP�v������t��
- **�]�Ⱥ޲z** - ���J/��X�O���B�o���޲z�B�]�ȳ���
- **�w�s�޲z** - ���~�޲z�B�w�s�i�X�B�����Ӻ޲z
- **�P��޲z** - �Ȥ�޲z�B�q��޲z�B������t��
- **���ʺ޲z** - �����Ӻ޲z�B���ʬy�{�B�I�ں޲z
- **������R** - �h���׼ƾڤ��R�P�i���Ƴ���

### �޳N�S��
- **�{�N�Ƭ[�c** - FastAPI + React + TypeScript
- **�T�����]�p** - ����h�]�ƳX��
- **��ɼƾ�** - WebSocket �����ɧ�s
- **�w���i�a** - JWT �{�ҡB�ƾڥ[�K�B�v������
- **�����X�i** - �Ҷ��Ƴ]�p�B�L�A�Ȭ[�c�ǳ�

##  �t�έn�D

### �}�o����
- Python 3.9+
- Node.js 18+
- PostgreSQL 14+ (�Ͳ�����)
- Redis 6+ (�w�s)
- Git

### �Ͳ�����
- Docker & Docker Compose
- Kubernetes (�i��)
- Nginx (�ϦV�N�z)

##  �ֳt�}�l

### 1. �J������
```bash
git clone <repository-url>
cd ji_erp
```

### 2. ��ݳ]�m
```bash
# �Ыص�������
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# �w�˨̿�
pip install -r requirements.txt

# ��l�Ƽƾڮw
python init_db.py

# �Ұʫ�ݪA��
python main.py
```

### 3. �e�ݳ]�m
```bash
cd frontend
npm install
npm start
```

### 4. �X�ݨt��
- ��� API: http://localhost:8000
- �e������: http://localhost:3000
- API ����: http://localhost:8000/docs

##  ���ձb��

| ���� | �Τ�W | �K�X | �v�� |
|------|--------|------|------|
| �޲z�� | admin | admin123 | �����v�� |
| �]�� | finance | finance123 | �]�ȼҶ� |
| �w�s | inventory | inv123 | �w�s�Ҷ� |
| �P�� | sales | sales123 | �P��Ҷ� |

##  ���ص��c

```
ji_erp/
 backend/                 # ��ݥN�X
    app/
       api/            # API ����
       core/           # �֤߰t�m
       models/         # �ƾڼҫ�
       schemas/        # Pydantic �Ҧ�
       services/       # �~���޿�
       utils/          # �u����
    tests/              # ���դ��
    requirements.txt    # Python �̿�
 frontend/               # �e�ݥN�X
    src/
       components/     # React �ե�
       pages/          # �����ե�
       hooks/          # �۩w�q Hooks
       services/       # API �A��
       store/          # ���A�޲z
       utils/          # �u����
    package.json
 docs/                   # ���ؤ���
 docker/                 # Docker �t�m
 .cursorrules           # Cursor AI �W�h
 context.md             # ���ؤW�U��
 README.md              # ���ػ���
```

##  �}�o���n

### �N�X�W�d
- **Python**: ��` PEP 8 �W�d
- **TypeScript**: �ϥ��Y��Ҧ�
- **Git**: �ϥ� Conventional Commits
- **����**: �O�� 80%+ �����л\�v

### �}�o�y�{
1. �Ыإ\�����
2. ��{�\��ýs�g����
3. ����N�X�óЫ� PR
4. �N�X�f�d
5. �X�֨�D����

### �����ܶq
```bash
# ��������ܶq
DATABASE_URL=postgresql://user:password@localhost/ji_erp
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30

# �e�������ܶq
REACT_APP_API_URL=http://localhost:8000
REACT_APP_WS_URL=ws://localhost:8000/ws
```

##  API ����

### �{�Һ��I
- `POST /api/auth/login` - �Τ�n�J
- `POST /api/auth/logout` - �Τ�n�X
- `POST /api/auth/refresh` - ��s Token

### �Τ�޲z
- `GET /api/users` - ����Τ�C��
- `POST /api/users` - �ЫإΤ�
- `PUT /api/users/{id}` - ��s�Τ�
- `DELETE /api/users/{id}` - �R���Τ�

### �]�Ⱥ޲z
- `GET /api/transactions` - �������O��
- `POST /api/transactions` - �Ыإ��
- `GET /api/reports/financial` - �]�ȳ���

�Բ� API ���ɽгX��: http://localhost:8000/docs

##  ���p

### Docker ���p
```bash
# �c�بñҰʩҦ��A��
docker-compose up -d

# �d�ݪA�Ȫ��A
docker-compose ps

# �d�ݤ�x
docker-compose logs -f
```

### �Ͳ����ҳ��p
```bash
# �ϥ� Kubernetes
kubectl apply -f k8s/

# �Ψϥ� Docker Swarm
docker stack deploy -c docker-compose.prod.yml ji-erp
```

##  ����

### �B�����
```bash
# ��ݴ���
cd backend
pytest

# �e�ݴ���
cd frontend
npm test

# �ݨ�ݴ���
npm run test:e2e
```

### �����л\�v
```bash
# ����л\�v
pytest --cov=app tests/

# �e���л\�v
npm run test:coverage
```

##  �ʯ�ʱ�

### �ʱ�����
- API �T���ɶ�
- �ƾڮw�d�ߩʯ�
- ���s�ϥα��p
- ���~�v�έp

### ��x�޲z
- ���Τ�x
- ���~��x
- �X�ݤ�x
- �f�p��x

##  �^�m���n

1. Fork ����
2. �Ыإ\����� (`git checkout -b feature/AmazingFeature`)
3. ������ (`git commit -m 'Add some AmazingFeature'`)
4. ���e����� (`git push origin feature/AmazingFeature`)
5. �Ы� Pull Request

##  ��s��x

### v1.0.0 (2024-01-01)
- ��l�����o��
- ��¦�Τ�޲z�\��
- ²�檺�]�ȰO���\��

### v1.1.0 (�p����)
- �w�s�޲z�Ҷ�
- �Ȥ����Y�޲z
- ��¦����\��

##  �\�i��

�����رĥ� MIT �\�i�� - �d�� [LICENSE](LICENSE) ���F�ѸԱ�

##  ���

- ����: [���ؤ���](docs/)
- ���D���X: [GitHub Issues](https://github.com/your-repo/ji-erp/issues)
- �Q��: [GitHub Discussions](https://github.com/your-repo/ji-erp/discussions)

##  �P��

�P�©Ҧ����o�Ӷ��ذ��X�^�m���}�o�̡I

---

**�`�N**: �o�O�@�ӾǲߩM�}�o�������ءA�ФŦb�Ͳ����Ҥ��ϥΥ��g�R�����ժ��\��C
