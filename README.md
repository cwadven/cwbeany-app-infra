# How to use

## 1. Create namespace for application & argocd

```bash
kubectl create namespace cwbeany
kubectl create namespace argocd
```

## 2. Set argocd

```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl apply -f k8s/argocd-nodeport.yaml
kubectl apply -f k8s/argocd-rbac.yaml
kubectl apply -f k8s/apps/cwbeany.yaml -n argocd
```

## 3. Set Application

```bash
kubectl apply -k k8s/base -n cwbeany
```

## 4. Set secrets

You have to create secret.yaml file in each services

```
django/secret.yaml
django/google-service-account-secret.yaml
mysql/secret.yaml
mysqld-exporter/secret.yaml
elasticsearch/secret.yaml
```

Example
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysqld-exporter-secret
  namespace: cwbeany
type: Opaque
stringData:
  DATA_SOURCE_NAME: "user:userpassword@tcp(mysql:3306)/"
```

## 5. Add secret from local

```
powershell -ExecutionPolicy Bypass -File .\apply-secrets.ps1
```

## 6. ArgoCD Login

https://localhost:30999/

ID is "admin"

Password Getting

```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | ForEach-Object { [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($_)) }
```

# Extra

## How to now Pod info

```bash
kubectl get pods -n cwbeany -l app=django
```

## Get inside to pod

```bash
kubectl exec -it django-cron-66f79cd876-69tgs -n cwbeany -- bash
```

## Grafana Login

http://localhost:30301/
