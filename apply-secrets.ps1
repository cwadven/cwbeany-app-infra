param(
    [Parameter(Mandatory=$true)]
    [string]$NAMESPACE
)

Write-Host "Applying secrets to namespace: $NAMESPACE"

# NAMESPACE 에서 - 뒤에 있는 글자 가져오기
$ENVIRONMENT = $NAMESPACE.Split('-')[1]

# Django 민감 정보 Secret 적용
kubectl apply -f k8s/overlays/$ENVIRONMENT/secret/django-secret.yaml -n $NAMESPACE

# Google 서비스 계정 Secret 적용
kubectl apply -f k8s/overlays/$ENVIRONMENT/secret/google-service-account-secret.yaml -n $NAMESPACE

# MySQL 비밀번호 Secret 적용
kubectl apply -f k8s/overlays/$ENVIRONMENT/secret/mysql-secret.yaml -n $NAMESPACE

# MySQL-Exporter 비밀번호 Secret 적용
kubectl apply -f k8s/overlays/$ENVIRONMENT/secret/mysqld-exporter-secret.yaml -n $NAMESPACE

# Redis Secret 적용
kubectl apply -f k8s/overlays/$ENVIRONMENT/secret/redis-secret.yaml -n $NAMESPACE

# Elasticsearch Secret 적용
kubectl apply -f k8s/overlays/$ENVIRONMENT/secret/elasticsearch-secret.yaml -n $NAMESPACE

Write-Host "Secrets applied successfully to namespace $NAMESPACE" 