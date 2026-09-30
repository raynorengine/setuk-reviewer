"""공통 타입. 구현보다 먼저 이 파일을 고정한다.

검토기의 출력은 생성기가 그대로 재사용한다(design.md 4.2).
여기가 흔들리면 두 모듈이 같이 무너진다.
"""
from dataclasses import dataclass
from typing import Literal

판정 = Literal["위반", "주의", "권고", "해당없음"]
규칙구분 = Literal["regulation", "practice"]
입력출처 = Literal["교사직접", "외부LLM", "자체생성"]


@dataclass(frozen=True)
class 문서조각:
    """검색 단위. 규정 md 파일의 `##` 절 하나가 기본 단위"""
    조각id: str          # 파일명 + 절 번호
    본문: str
    출처파일: str        # data/regulations/... 상대 경로
    근거줄: str          # 절의 `> 근거:` 줄 원문
    구분: 규칙구분
    적용학년: str        # "1·2학년" / "3학년" / "공통"


@dataclass(frozen=True)
class 검토결과:
    """검토기의 출력. design.md 4.1 출력 형식을 그대로 옮긴 것.

    출처파일을 담는 이유 — 테스트가 그 파일을 열어 근거 문장이 실제로 있는지
    확인할 수 있게 하기 위해서다. LLM이 그럴듯한 조항 번호를 지어내는 것이
    이 프로젝트 최악의 실패다(design.md 3.3).
    """
    문장: str
    판정: 판정
    구분: 규칙구분 | None      # 해당없음이면 None
    근거: str                  # 조항 원문 인용 또는 관습 출처
    출처파일: str | None       # 근거가 실제로 있는 파일. 검증 대상
    조각id: str | None
    수정안: str | None
