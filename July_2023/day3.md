# Topic3. Container
### 1. ECR/Image
- Immutable 설정이 무엇이고 왜 사용해야 하는지 정리하세요.
- 1.0.1, 1.0.2 tag를 가진 이미지 두 개가 존재 한다면 두 이미지는 서로 다른 이미지인지, 아닐 수 있다면 왜 그런지 정리하세요.
- 컨테이너로 된 어플리케이션 배포 중 Docker hub의 rate limit 이슈로 인해 배포가 중단되었을 경우 해결할 수 있는 방법을 제시해 보세요.
- 1111 AWS account에 ECR repository 하나를 생성하였고, 2222 AWS account의 EKS에서 해당 이미지를 사용하고자 할 때 어떤 설정을 해야 이미지를 가져갈 수 있는지 정리하고 실제로 구성해 보세요.
- 컨테이너 배포 중 `exec /bin/sh: exec format error` 라는 에러가 발생할 때 어떤 문제 때문에 해당 에러가 발생하고 어떻게 해결할 수 있는지 정리해 보세요. 

### 2. EKS
- Pod, Daemonset, Ingress 등 K8s의 주요 object는 무엇이 있는지 정리해 보세요.
- EKS cluster가 인터넷 엑세스가 불가능한 환경에서 운영될 수 있는 방법을 정리하고, 실제 해당 방법으로 Cluster를 구성해 보세요.
- Pod 마다 Security Group을 가질 수 있도록 구성해 보세요.
- AWS LB Controller와 External DNS가 어떤 역할을 하는지 정리하세요.
- ingress 두 개가 하나의 ALB에 매핑 되도록 설정해 보세요. Path 라우팅을 통해 /foo/* 는 foo Pod로, /bar/*는 bar Pod로 라우팅 되어야 합니다.
  ```
      - foo ingress - foo service - foo pod
  ALB
      - bar ingress - bar service - bar pod
  ```
- Karpenter가 cluster-autoscaler 보다 어떤 점이 더 좋은지 정리하고, Karpenter를 직접 구성해 foo Pod가 실행될 수 있는 Node를 생성해 보세요.
- IRSA가 무엇인지 정리하고 실제 Pod가 IAM role로 assume 하는 구성을 해보세요.
- 50개의 MSA app들이 300대의 EC2에서 돌고 있는 서비스가 있고, 각 app의 로깅 포맷이 현재 모두 다른 상황이다. EC2 환경에서 EKS 환경으로 마이그레이션 하고자 했을 때 로깅 아키텍처에 대해 설계해 보고 왜 그렇게 디자인하였는지 정리해 보세요.

### 3. ECS
- Cluster, Task definition, Task, Service의 개념에 대해 정리하세요.
- EC2 대신 Fargate를 사용하였을 때의 장/단점에 대해 정리해 보세요.
- Firelens가 무엇인지와 왜 사용하는지 정리해 보세요.
- Service Mesh와 Service Discovery가 무엇인지, ECS에서 사용 가능한 Service Mesh는 어떤 것이 있는지 정리하고 직접 구성해 보세요.
- ECS로 Stateful 한 서비스를 운영하고자 했을 때 설계 시 어떤 점을 고려해야 하는지 정리해 보세요.
