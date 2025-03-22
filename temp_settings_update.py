import os

# 기존 코드 대신 아래 코드로 변경
SERVER_ENV = os.environ.get('SERVER_ENV', 'Local')
if SERVER_ENV == 'K8s':
    # Kubernetes 환경에서는 마운트된 파일 경로 사용
    GOOGLE_SERVICE_ACCOUNT_FILE = '/app/secrets/google_service_account_file.json'
else:
    # 로컬 개발 환경에서는 기존 경로 사용
    GOOGLE_SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'google_service_account_file.json')

GOOGLE_API_SCOPES = [
    'https://www.googleapis.com/auth/drive',
] 