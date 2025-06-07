# How to use

## 1. Create namespace for application & argocd

```bash
kubectl create namespace cwbeany
kubectl create namespace argocd
kubectl create namespace argo-rollouts
```

## 2. Set argocd

```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl apply -f k8s/argocd-nodeport.yaml
kubectl apply -f k8s/argocd-rbac.yaml
kubectl apply -f k8s/apps/cwbeany.yaml -n argocd
```

## 3. Set argocd rollouts

```bash
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml
```

## 4. Set Application

```bash
kubectl apply -k k8s/base -n cwbeany
```

## 5. Set secrets

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

## 6. Add secret from local

```
powershell -ExecutionPolicy Bypass -File .\apply-secrets.ps1
```

## 7. ArgoCD Login

https://localhost:30999/

ID is "admin"

Password Getting

```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | ForEach-Object { [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($_)) }
```

# Extra

## How to update code

Go to code repository and build and push to dockerhub

1. build with tag

```shell
docker build -t <dockerhub_username>/<repository_name>:<GENTERATED_TAG> .
```

2. push with tag

```shell
docker push <dockerhub_username>/<repository_name>:<GENTERATED_TAG>
```

3. Change .yaml files to image tag

k8s/base/django/xxxx-deployment.yaml file of containers `image:` should be change

4. Go to argocd web and sync or wait

## How to reapply kubectl

```
kubectl apply -k k8s/base
```


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
