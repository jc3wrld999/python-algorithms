## 그래프

<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221830878-8f08d5e7-05ff-48b8-bbc2-b2fb36ca5829.png)

</div>
- 선형 구조: 자료가 순서를 가지고 연속되어 있음
- 비선형 구조: 선형 구조에 해당하지 않는 자료구조


그래프는 정점(vertes)과 간선(edge)으로 이루어진 자료구조이다.

<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221831330-8c7b2b59-3985-4fae-8064-40922e3249bc.png)

</div>


- vertex: 자료, 상태 등 뭔가를 담고 있음, 노드라고도 함
- edge: 정점 간의 관계를 나타냄 방향이 있을 수도 있고 없을 수도 있음 방향이 있으면 반대로 이동 못함
- 경로: 어떤 정점에서 간선을 통해 다른 정점으로 이동할 수 있는데 다른 정점으로 가기 위해 거치는 모든 정점
- 사이클: 어떤 정점에서 시작하여 자기 자신으로 돌아오는 경로

## 트리

<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221832033-ddbb1167-fcf5-4b1f-8c86-1b3ac38db340.png)

![image](https://user-images.githubusercontent.com/61821641/221829505-2ee52b63-e6cf-4046-866b-c31bae63cf55.png)

</div>


트리는 그래프의 특수한 형태이다. 
- 트리의 간선들은 모두 방향을 가진다.
- 어떤 정점을 가리키는 정점의 최대 개수는 1개이다.
- 어떤 정점에서 다른 정점으로 이동할 수 있는 경로는 1개이다.
- 사이클을 갖지 않는다.
- 루트 노드: 다른 어떠한 정점도 가리키지 않는 정점을 루트 노드라고 한다.
- 리프 노드: 가리키는 정점이 없는 정점들을 리프 노드라고 한다.
- 깊이: 루트 노드로부터의 거리
- 트리는 계층적 구조이다.
- 운영체제에서 파일을 분류하기 위해 사용하는 디렉토리는 트리의 대표적인 예시이다.

<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221833830-afd33095-0b55-43ee-9bf7-a2779ddc8da6.png)
</div>
- 이진트리
    - 각 정점들이 자식 노드를 최대 2개까지만 갖는 트리를 이진 트리라고 한다.
    - 이진 탐색 트리 등 유용하게 활용되는 트리 중에는 대부분 이진 트리를 응용한 것이 많다.

<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221834264-dee93875-47ab-42de-bfc6-05f49f00f837.png)
</div>

- 포화 이진 트리
    - 리프 노드를 제외한 모든 정점이 항상 자식을 2개씩 가지면서 모든 리프 노드의 깊이가 동일한 트리
    - 포화 이진 트리의 높이를 h라고 할때 정점의 개수는 항상 $2^h - 1$개이다.

<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221834812-b168470e-4b3f-4499-ab3a-8ae07d18225c.png)
</div>

- 완전 이진 트리
    - 마지막 깊이를 제외하고 모든 정점이 완전히 채워져있으며 마지막 깊이의 정점들은 가능한 한 왼쪽에 있는 트리
    - 포화이진 트리에서 마지막 깊이의 정점이 오른쪽에서부터 일부 제거된 트리라고 볼 수 있다.
    - 완전 이진 트리의 높이가 h일 때 정점의 개수는 $2^{h-1}$개 이상 $2^h-1$개 이하이다.
    - 배열로 표현 가능

<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221837138-63253c39-7f0f-44d7-9cc1-e7a63091565f.png)

![image](https://user-images.githubusercontent.com/61821641/221837434-e564d250-2000-49fd-92cb-376cfe212eb6.png)
<div>


<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221836048-8440af8c-4150-492d-bdfa-9e24a18e327d.png)
<div>

- 정 이진 트리
    - 정 이진 트리는 리프 노드를 제외한 모든 노드들이 두 개의 자식 노드를 갖고 있는 이진 트리
    - 모든 정점이 0개 또는 2개의 자식의 노드를 갖는다.

### 트리 순회하기

<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221838599-771f763b-ac7f-470b-8a4c-8ebe6bf27c0d.png)

![image](https://user-images.githubusercontent.com/61821641/221838848-4bd9736b-09ad-4180-852f-ec1180b752a7.png)

![image](https://user-images.githubusercontent.com/61821641/221838930-c8b785bf-cbfc-48b7-8255-ba207d1fa3ba.png)
<div>

- DFS(깊이 우선 탐색)
    - 전위 순회: 루트 > 왼쪽 서브트리 > 오른쪽 서브트리
    - 중위 순회: 왼쪽 서브트리 > 루트 > 오른쪽 서브트리
    - 후위 순회: 왼쪽 서브트리 > 오른쪽 서브트리 > 루트
    - 재귀 회출을 사용하는 알고리즘이다.
    - 재귀 호출은 스택의 특성을 이용하므로 스택을 이용한다고 볼 수 있다.
    - DFS의 세가지 방법은 정점을 언제 방문하는지에 따라 순서가 달라지며 재귀 호출을 이용한다는 기본적인 개념 자체는 동일하다. 
    - 전체 트리를 순회하기 위해 서브트리를 순회한다. > 순회를 위해 순회한다. > 재귀

<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221840807-b758994d-486d-4124-8ad5-ca2739cb7c9f.png)

</div>

<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221839083-477df388-42bc-4dca-972a-889b5efe12bd.png)


</div>

- BFS(너비 우선 탐색)
    - 큐 자료구조를 이용하여 구현
    - 현재 정점과 이웃한 정점일 수록 먼저 방문해야하기 때문에 FIFO구조인 큐를 이용해야 한다.

<div style = "width:300px;">

![image](https://user-images.githubusercontent.com/61821641/221841986-cbfc4640-681d-4017-ba01-c9b5e2f410fa.png)

</div>

```python
push(1) # [1]
pop(1) push(2, 3) # [2, 3]
pop(2) push(4, 5) # [3, 4, 5]
pop(3) push(6, 7) # [4, 5, 6, 7]
pop(4, 5, 6, 7)
```
