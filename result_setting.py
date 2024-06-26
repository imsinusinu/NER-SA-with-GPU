neg_= 2 # "다소 부정적입니다."
pos_= 1 # "다소 긍정적입니다."
mid_= 0 # "중립적입니다."

def sa_organizer(base):

    result_sa = {
        "부정": 0,  # 2
        "긍정": 0,  # 1
        "중립": 0   # 0
    }

    for sentiment in base['감성분류']:
        if sentiment == "부정":
            result_sa["부정"]+=1
        elif sentiment == "긍정":
            result_sa["긍정"]+=1
        else:
            result_sa["중립"]+=1

    # 확률 정리
    pos_per = round((result_sa["긍정"]) / (len(base['감성분류'])) * 100, 2)
    neg_per = round((result_sa["부정"]) / (len(base['감성분류'])) * 100, 2)

    # 한 줄 정리
    if result_sa["부정"] > result_sa["긍정"]:
        return(neg_, pos_per, neg_per)
    elif result_sa["부정"] < result_sa["긍정"]:
        return(pos_, pos_per, neg_per)
    else:
        return(mid_, pos_per, neg_per)

# NER 정리
def ner_organizer(base):
    result_ner=[]
    for ner in base["기업명"]:
        if ner == "":   # 인식된 개체가 없는 경우
            continue
        else:
            if ner in result_ner:
                continue
            else:
                result_ner.append(ner)

    # 한 줄 정리
    if len(result_ner) == 0:
        return("인식된 개체가 없습니다.")
    else:
        print("인식된 개체는 다음과 같습니다.")
        return(result_ner)