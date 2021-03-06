# FIFA_Online_4_Player_Evalution_Analysis
평소 피파온라인 4 게임을 즐겨하면서 팀을 새로 구성하고 선수를 구매할 때 피파온라인 4 인벤을 보고 유저들의 평가를 보고 추천을 받는 것을 조금 더 수월하게 추천을 얻기 위해
피파온라인4 인벤에 선수에 대한 평가 댓글을 가져와서 해당 댓글이 긍정인지 부정인지를 판별하는 감정분석 모델 ( Update 22.06.14 )
## 데이터 수집 
- [OPEN API 사용](https://developers.nexon.com/fifaonline4)
  - 피파온라인4 시즌의 고유 아이디와 시즌이름을 제공받아 Season.csv에 저장
  - 피파온라인4 선수들의 고유 아이디와 시즌 아이디, 선수이름을 제공받아 Player.csv에 저장
  - 피파온라인4 인벤에서 사용하는 시즌 고유 아이디가 다른 2개의 시즌은 피파온라인4 인벤에 맞춰 수정
- [데이터 크롤링](https://fifaonline4.inven.co.kr/dataninfo/rate/)
  - 피파온라인4 OPEN API를 이용해서 가져온 Player.csv를 이용해서 크롤링을 진행
  - 피파온라인4 인벤 선수평가 페이지에서 모든 시즌의 선수들의 댓글 긁어옴
## 데이터 전처리
- 생각했던것과는 다르게 쓸모없는 댓글들이 많아 최대한 줄이기 위해 불용어를 선정해 불용어가 포함되어 있는 댓글들은 사전에 제거 
- ex) "쪽지", "판매", "팔아", "사요", "카톡", "가격", "ㅋㅋㅋㅋㅋ", "신규", "팝니", "삽니", "연락" 등등
- 프로젝트 구상과정에서는 감정분석에 영향을 줄거라고 생각했던 별점 Column 제거
- 부정(0), 긍정(1), 쓸모없는 댓글(2)으로 직접 라벨링 ( ICON 시즌 약 16,000개 )
## 데이터 모델링
- Konlpy와 NLTK를 사용해서 한글 형태소를 분리하고 토큰화 진행
- LSTM 모델을 사용해서 한글 감정분석 진행 ( Update 22.06.14 )
- 다중분류모델 (3가지)
## 결과
- ~총 5가지 결과를 출력~
  - ~매우추천~
  - ~추천~
  - ~긍정적 검토~
  - ~비추천~
  - ~업데이트 예정 데이터 -> 추후 데이터가 없습니다로 변경 예정~
- 위에 내용에서 22.06.14 부로 3가지 결과를 출력 ( 추천시스템보다 감정분석에 초점을 두기로 함 )
  - 부정
  - 긍정
  - 쓸모없는 데이터
## 회고
- 약 42만개정도의 데이터를 가져왔지만 약 20만개 정도는 쓸모없는 데이터 였음
- 직접 라벨링을 하는데 너무 많은 시간을 썼고 라벨링 한 데이터의 양이 충분하지 않아서 아쉬웠음.
- 추후 Bert모델에 대해 공부를 해서 프로젝트에 적용시켜 AWS로 웹 배포를 하는 것이 최종 목표
