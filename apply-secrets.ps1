# 네임스페이스 설정
$NAMESPACE = "cwbeany"

# Django 민감 정보 Secret 적용
kubectl apply -f k8s/base/django/secret.yaml -n $NAMESPACE

# Google 서비스 계정 Secret 적용
kubectl apply -f k8s/base/django/google-service-account-secret.yaml -n $NAMESPACE

# MySQL 비밀번호 Secret 적용
kubectl apply -f k8s/base/mysql/secret.yaml -n $NAMESPACE

# MySQL-Exporter 비밀번호 Secret 적용
kubectl apply -f k8s/base/mysqld-exporter/secret.yaml -n $NAMESPACE

# Elasticsearch Secret 적용
kubectl apply -f k8s/base/elasticsearch/secret.yaml -n $NAMESPACE

Write-Host "Secrets applied successfully to namespace $NAMESPACE" 