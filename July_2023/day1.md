# Topic 1. Network and Security
### 1. VPC
- Internet G/W, Egress-only internet G/W, NAT G/W의 개념과 차이를 정리하세요.
- VPC peering의 개념에 대해 정리하세요.
- 두 개의 VPC를 peering으로 연결할 때 다른 VPC의 DNS private zone의 주소를 쿼리 할 수 있는 방법에 대해 조사하고 직접 구성해 보세요.
- DX 사용 시 하나의 DX G/W 당 연결 가능한 Virtual private G/W는 hard limit으로 인해 20개 이상 직접 추가를 할 수 없습니다. 20개 이상 연결을 추가할 수 있는 다른 방법을 생각해 보세요.
- VPC Endpoint와 Private Link에 대해서 정리하세요.

### 2. CloudFront
- CDN의 개념에 대해 정리해 보세요.
- Client -> CloudFront -> EC2(Backend)로 request가 들어올 때 EC2에서 Client의 IP를 알 수 있는 방법은 어떤 것이 있는지 조사하세요.
- CloudFront가 S3에 있는 static asset을 캐싱 하고 있고 방금 S3의 파일들이 배포가 일어났을 때, 각 edge로 즉시 캐시 파일을 업데이트할 수 있는 방법은 무엇이 있는지 정리하세요.
- Client -> CloudFront -> ALB -> EC2 로된 아키텍쳐가 있고 www.sample.io 라는 도메인으로 https를 사용하기를 원할 때, 인증서 설정을 해야 할 부분은 어디인지와 왜 해당 모듈에 설정을 하고 다른 모듈에는 설정을 하지 않아도 되는지 정리하세요.
- CORS 가 무엇인지와 CloudFront에서 CORS와 관련된 옵션이 무엇이 있는지 정리하고 실제 CORS와 관련된 구성을 해보세요.
- CloudFront에서 backend에서 준 정보에 추가로 http response header에 정보를 추가하는 방법은 어떤 것이 있는지 정리하세요.

### 3. LB
- Target Group에서 draining time(deregistration)을 사용하는 이유가 무엇인지 정리하세요.
- ALB의 80 port로 들어온 트레픽을 다시 443 port로 들어올 수 있도록 구성해 보세요.
- ALB를 거친 request는 EC2에서 확인 시 클라이언트 IP가 ALB의 주소로 확인 되지만, NLB를 거친 request는 실제 request를 쏜 클라이언트의 IP로 확인됩니다. 두 LB의 통신 방식을 비교하고 왜 이런 현상이 나타 나는지 정리하세요.
- ALB의 Stickiness가 어떤 문제 때문에 사용하는지와, 해당 문제를 Stickiness option을 사용하지 않고 다른 기능이나 아키텍쳐적으로 해결할 수 있는 방법이 어떤것이 있는지 정리하세요.

### 4. IAM
- AWS IAM user, role, policy에 대한 차이를 정리하세요.
- 보안에서 인증과 인가에 대한 개념을 정리하세요.
- AWS IAM identity providers가 무엇인지와 사용되는 사례를 정리하세요.
- User01, user02, user03 IAM user와 dev, ops라는 IAM role을 생성하고, user01은 dev role만 assume 가능하도록 하고 user02, user03은 ops라는 role만 assume 할 수 있도록 구성해 보세요.
- EKS의 Pod에서 curl http://169.254.169.254 호출이 실패한다면 어떤 이유 때문에 이런 현상이 나타날 수 있는지 생각해 보세요.

### 5. WAF/Shield
- WAF와 Shield의 차이에 대해 정리하세요.
- AWS WAF의 WCU가 무엇인지 정리하세요.
- 한 IP에서 5분~~1분~~ 동안 50~~10~~번 이상 요청 시 차단하는 AWS WAF를 구성을 해보세요.
  만약 50을 사용할 수 없다면 AWS Quotas를 같이 알아보고 관련된 quota의 최소값이 얼마인지와 50으로 설정이 불가능한 이유가 무엇인지도 알아보세요. 알아본 후 50대신 조절 가능한 최소 값을 설정하여 WAF 문제를 풀면됩니다.
- log4shell을 막는 AWS WAF를 구성해 보세요.
