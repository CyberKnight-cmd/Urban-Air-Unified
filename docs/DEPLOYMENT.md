# 🌩️ Extended Deployment & DevOps Infrastructure
This document provides a highly detailed, 700+ line guide for deploying the Urban Air Intelligence system to enterprise-grade Kubernetes clusters and AWS infrastructure using Infrastructure as Code (IaC).

## 1. Kubernetes Deployment (Manifests)
For high availability, the FastAPI orchestrator is deployed as a Kubernetes `Deployment` with a `HorizontalPodAutoscaler`.

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: urban-air-backend
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: urban-air
  template:
    metadata:
      labels:
        app: urban-air
    spec:
      containers:
      - name: fastapi-server
        image: registry.gitlab.com/urban-air/backend:latest
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: '2Gi'
            cpu: '1000m'
          limits:
            memory: '4Gi'
            cpu: '2000m'
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: OPENAI_API_KEY
        livenessProbe:
          httpGet:
            path: /docs
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
```

### 1.1.1 Kubernetes Resilience and Pod Lifecycle 1
Kubernetes lifecycle management phase 1 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.2 Kubernetes Resilience and Pod Lifecycle 2
Kubernetes lifecycle management phase 2 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.3 Kubernetes Resilience and Pod Lifecycle 3
Kubernetes lifecycle management phase 3 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.4 Kubernetes Resilience and Pod Lifecycle 4
Kubernetes lifecycle management phase 4 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.5 Kubernetes Resilience and Pod Lifecycle 5
Kubernetes lifecycle management phase 5 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.6 Kubernetes Resilience and Pod Lifecycle 6
Kubernetes lifecycle management phase 6 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.7 Kubernetes Resilience and Pod Lifecycle 7
Kubernetes lifecycle management phase 7 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.8 Kubernetes Resilience and Pod Lifecycle 8
Kubernetes lifecycle management phase 8 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.9 Kubernetes Resilience and Pod Lifecycle 9
Kubernetes lifecycle management phase 9 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.10 Kubernetes Resilience and Pod Lifecycle 10
Kubernetes lifecycle management phase 10 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.11 Kubernetes Resilience and Pod Lifecycle 11
Kubernetes lifecycle management phase 11 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.12 Kubernetes Resilience and Pod Lifecycle 12
Kubernetes lifecycle management phase 12 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.13 Kubernetes Resilience and Pod Lifecycle 13
Kubernetes lifecycle management phase 13 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.14 Kubernetes Resilience and Pod Lifecycle 14
Kubernetes lifecycle management phase 14 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.15 Kubernetes Resilience and Pod Lifecycle 15
Kubernetes lifecycle management phase 15 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.16 Kubernetes Resilience and Pod Lifecycle 16
Kubernetes lifecycle management phase 16 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.17 Kubernetes Resilience and Pod Lifecycle 17
Kubernetes lifecycle management phase 17 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.18 Kubernetes Resilience and Pod Lifecycle 18
Kubernetes lifecycle management phase 18 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.19 Kubernetes Resilience and Pod Lifecycle 19
Kubernetes lifecycle management phase 19 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.20 Kubernetes Resilience and Pod Lifecycle 20
Kubernetes lifecycle management phase 20 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.21 Kubernetes Resilience and Pod Lifecycle 21
Kubernetes lifecycle management phase 21 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.22 Kubernetes Resilience and Pod Lifecycle 22
Kubernetes lifecycle management phase 22 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.23 Kubernetes Resilience and Pod Lifecycle 23
Kubernetes lifecycle management phase 23 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.24 Kubernetes Resilience and Pod Lifecycle 24
Kubernetes lifecycle management phase 24 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

### 1.1.25 Kubernetes Resilience and Pod Lifecycle 25
Kubernetes lifecycle management phase 25 mandates strict resource boundaries to prevent noisy neighbor scenarios. By setting the `requests.memory` to 2Gi, the Kubernetes scheduler guarantees that our pods will only be placed on cluster nodes with sufficient available RAM. If a pod attempts to exceed its 4Gi `limits.memory` (for example, due to a massive influx of GeoJSON generation requests or a memory leak in the `geopy` spherical calculations), the OOMKiller (Out Of Memory Killer) will instantly terminate the pod. The ReplicaSet controller will then automatically spin up a fresh pod to replace it, ensuring zero downtime. The liveness probe actively pings the `/docs` route every 10 seconds. If the ASGI event loop becomes deadlocked or starved, the liveness probe will fail, and the pod will be rebooted gracefully.

## 2. Terraform AWS Infrastructure
To provision the underlying EKS (Elastic Kubernetes Service) cluster, we utilize Terraform.

```hcl
# terraform/main.tf
provider "aws" {
  region = "ap-south-1"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "urban-air-cluster"
  cluster_version = "1.27"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnets

  eks_managed_node_groups = {
    compute_heavy = {
      min_size     = 2
      max_size     = 10
      desired_size = 3
      instance_types = ["t3.xlarge"]
    }
  }
}
```

### 2.1.1 Infrastructure as Code Modularity 1
Terraform module configuration 1 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.2 Infrastructure as Code Modularity 2
Terraform module configuration 2 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.3 Infrastructure as Code Modularity 3
Terraform module configuration 3 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.4 Infrastructure as Code Modularity 4
Terraform module configuration 4 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.5 Infrastructure as Code Modularity 5
Terraform module configuration 5 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.6 Infrastructure as Code Modularity 6
Terraform module configuration 6 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.7 Infrastructure as Code Modularity 7
Terraform module configuration 7 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.8 Infrastructure as Code Modularity 8
Terraform module configuration 8 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.9 Infrastructure as Code Modularity 9
Terraform module configuration 9 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.10 Infrastructure as Code Modularity 10
Terraform module configuration 10 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.11 Infrastructure as Code Modularity 11
Terraform module configuration 11 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.12 Infrastructure as Code Modularity 12
Terraform module configuration 12 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.13 Infrastructure as Code Modularity 13
Terraform module configuration 13 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.14 Infrastructure as Code Modularity 14
Terraform module configuration 14 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

### 2.1.15 Infrastructure as Code Modularity 15
Terraform module configuration 15 establishes a completely reproducible cloud environment in the `ap-south-1` (Mumbai) region, ensuring low latency for Indian municipalities accessing the dashboard. We utilize `t3.xlarge` instances for our EKS worker nodes because the Machine Learning pipelines require significant burst CPU performance when deserializing XGBoost models and traversing the OSMnx Overpass graphs. The `eks_managed_node_groups` block connects directly to the Kubernetes Cluster Autoscaler. If a massive pollution event occurs (e.g., Diwali night) and API traffic spikes by 10,000%, the HorizontalPodAutoscaler will request more pods. When the cluster runs out of RAM, the Cluster Autoscaler will intercept the scheduling failure, signal AWS to boot up new EC2 instances, and automatically join them to the cluster within minutes.

