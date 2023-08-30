import streamlit as st
from PIL import Image

def app():
    st.header('축구 선수 역할 설명')

#################################################################

    st.subheader('골기퍼')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/1_g_양한빈.png')
        image = image.resize((140, 180))
        st.image(image, caption='양한빈')
    with col2:
        image = Image.open('./data/activation_pic/1_g_오승훈.png')
        image = image.resize((140, 180))
        st.image(image, caption='오승훈')
    with col3:
        image = Image.open('./data/activation_pic/1_g_조현우.png')
        image = image.resize((140, 180))
        st.image(image, caption='조현우')
    st.write('역할 : Goalkeeper')
    st.write('상대 슈팅을 막는 역할. 주로 슛을 방어한다.')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/2_sg_노동건.png')
        image = image.resize((140, 180))
        st.image(image, caption='노동건')
    with col2:
        image = Image.open('./data/activation_pic/2_sg_안준수.png')
        image = image.resize((140, 180))
        st.image(image, caption='안준수')
    with col3:
        image = Image.open('./data/activation_pic/2_sg_이창근.png')
        image = image.resize((140, 180))
        st.image(image, caption='이창근')

    st.write('역할 : Swiper Goalkeeper')
    st.write('슛을 방어하기도 하지만 패스능력이 뛰어나 수비지역 빌드업에 가담한다. 가끔 긴 롱패스도 한다.')

##############################################################

    st.subheader('측면 수비수')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/3_ove_김륜성.png')
        image = image.resize((140, 180))
        st.image(image, caption='김륜성')
    with col2:
        image = Image.open('./data/activation_pic/3_ove_송준석.png')
        image = image.resize((140, 180))
        st.image(image, caption='송준석')
    with col3:
        image = Image.open('./data/activation_pic/3_ove_조현택.png')
        image = image.resize((140, 180))
        st.image(image, caption='조현택')
    st.write('역할 : Overlapper')
    st.write('팀 공격시 공격지역까지 올라가 공격작업에 도움을 주는 수비수, 크로스 능력이 좋다.')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/4_saf_김태현.png')
        image = image.resize((140, 180))
        st.image(image, caption='김태현')
    with col2:
        image = Image.open('./data/activation_pic/4_saf_김태환.png')
        image = image.resize((140, 180))
        st.image(image, caption='김태환')
    with col3:
        image = Image.open('./data/activation_pic/4_saf_이기제.png')
        image = image.resize((140, 180))
        st.image(image, caption='이기제')
    st.write('역할 : Safety')
    st.write('뒤에 머무르며 최후방에서 벌어지는 상황에 관여하고 공이 본인에게 있던 없던 위험을 감수하지 않는다.')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/5_pro_설영우.png')
        image = image.resize((140, 180))
        st.image(image, caption='설영우')
    with col2:
        image = Image.open('./data/activation_pic/5_pro_윤종규.png')
        image = image.resize((140, 180))
        st.image(image, caption='윤종규')
    with col3:
        image = Image.open('./data/activation_pic/5_pro_임창우.png')
        image = image.resize((140, 180))
        st.image(image, caption='임창우')
    st.write('역할 : Progressor')
    st.write('긴 패스와 전진 패스를 자주 시도한다. 볼을 점유하고있는 상황에 활발하게 움직인다.')

###########################################################################

    st.subheader('중앙 수비수')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/6_agg_김영권.png')
        image = image.resize((140, 180))
        st.image(image, caption='김영권')
    with col2:
        image = Image.open('./data/activation_pic/6_agg_김오규.png')
        image = image.resize((140, 180))
        st.image(image, caption='김오규')
    with col3:
        image = Image.open('./data/activation_pic/6_agg_이한범.png')
        image = image.resize((140, 180))
        st.image(image, caption='이한범')
    st.write('역할 : Aggressor')
    st.write('수비 빌드업시 많이 관여하며, 짧은 패스와 긴패스를 주로 한다. 가끔씩 전방 패스를 한다.')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/7_SCB_닐손주니어.png')
        image = image.resize((140, 180))
        st.image(image, caption='닐손주니어')
    with col2:
        image = Image.open('./data/activation_pic/7_SCB_불투이스.png')
        image = image.resize((140, 180))
        st.image(image, caption='불투이스')
    with col3:
        image = Image.open('./data/activation_pic/7_SCB_정태욱.png')
        image = image.resize((140, 180))
        st.image(image, caption='정태욱')
    st.write('역할 : SCB')
    st.write('수비 반경을 골문으로 잡고, 걷어내기나 슛 차단을 잘한다.')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/8_spr_김영빈.png')
        image = image.resize((140, 180))
        st.image(image, caption='김영빈')
    with col2:
        image = Image.open('./data/activation_pic/8_spr_안영규.png')
        image = image.resize((140, 180))
        st.image(image, caption='안영규')
    with col3:
        image = Image.open('./data/activation_pic/8_spr_조유민.png')
        image = image.resize((140, 180))
        st.image(image, caption='조유민')
    st.write('역할 : Spreader')
    st.write('길고 다이렉트한 패스를 자주 시도한다. 때로 볼을 점유하고 있을 때나 수비하기 위해 자리를 이탈한다.')

#############################################################################

    st.subheader('수비형 미드필더')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/9_btb_김강국.png')
        image = image.resize((140, 180))
        st.image(image, caption='김강국')
    with col2:
        image = Image.open('./data/activation_pic/9_btb_김도혁.png')
        image = image.resize((140, 180))
        st.image(image, caption='김도혁')
    with col3:
        image = Image.open('./data/activation_pic/9_btb_팔로세비치.png')
        image = image.resize((140, 180))
        st.image(image, caption='팔로세비치')
    st.write('역할 : Box to Box')
    st.write('공격과 수비 모두 훌륭한 육각형 미드필더')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/10_bui_강상윤.png')
        image = image.resize((140, 180))
        st.image(image, caption='강상윤')
    with col2:
        image = Image.open('./data/activation_pic/10_bui_니실라.png')
        image = image.resize((140, 180))
        st.image(image, caption='니실라')
    with col3:
        image = Image.open('./data/activation_pic/10_bui_황문기.png')
        image = image.resize((140, 180))
        st.image(image, caption='황문기')
    st.write('역할 : Builder')
    st.write('빌드업 과정에서 중추적인 순환 허브 담당을 하고 중원 아래쪽부터 스토퍼 역할을 한다.')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/11_dis_이규성.png')
        image = image.resize((140, 180))
        st.image(image, caption='이규성')
    with col2:
        image = Image.open('./data/activation_pic/11_dis_이영재.png')
        image = image.resize((140, 180))
        st.image(image, caption='이영재')
    with col3:
        image = Image.open('./data/activation_pic/11_dis_이창민.png')
        image = image.resize((140, 180))
        st.image(image, caption='이창민')
    st.write('역할 : Distributor')
    st.write('더 직선적이고 긴 전환 패스를 선호한다. 매우 활동적이다.')

#############################################################################

    st.subheader('공격형 미드필더')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/12_cre_기성용.png')
        image = image.resize((140, 180))
        st.image(image, caption='기성용')
    with col2:
        image = Image.open('./data/activation_pic/12_cre_신진호.png')
        image = image.resize((140, 180))
        st.image(image, caption='신진호')
    with col3:
        image = Image.open('./data/activation_pic/12_cre_정호연.png')
        image = image.resize((140, 180))
        st.image(image, caption='정호연')
    st.write('역할 : Creator')
    st.write('본인 팀의 공격 진영에서 중심이 된다. 패스 성공률이 높으며 침투패스를 잘하는 유형이다.')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/13_bc_김종석.png')
        image = image.resize((140, 180))
        st.image(image, caption='김종석')
    with col2:
        image = Image.open('./data/activation_pic/13_bc_안드리고.png')
        image = image.resize((140, 180))
        st.image(image, caption='안드리고')
    with col3:
        image = Image.open('./data/activation_pic/13_bc_이승기.png')
        image = image.resize((140, 180))
        st.image(image, caption='이승기')
    st.write('역할 : Box Crasher')
    st.write('패스보단 침투를 많이 하며 드리블을 즐겨하는 유형이다.')

#############################################################################

    st.subheader('측면 공격수')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/14_wt_이승우.png')
        image = image.resize((140, 180))
        st.image(image, caption='이승우')
    with col2:
        image = Image.open('./data/activation_pic/14_wt_김대원.png')
        image = image.resize((140, 180))
        st.image(image, caption='김대원')
    with col3:
        image = Image.open('./data/activation_pic/14_wt_조영욱.png')
        image = image.resize((140, 180))
        st.image(image, caption='조영욱')
    st.write('역할 : Wide Threat')
    st.write('상대 수비 라인을 늘리며 패널티 박스로 들어간다. 가끔 크로스도 올리지만, 슛 기회를 노린다.')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/15_unl_라마스.png')
        image = image.resize((140, 180))
        st.image(image, caption='라마스')
    with col2:
        image = Image.open('./data/activation_pic/15_unl_정승원.png')
        image = image.resize((140, 180))
        st.image(image, caption='정승원')
    with col3:
        image = Image.open('./data/activation_pic/15_unl_헤이스.png')
        image = image.resize((140, 180))
        st.image(image, caption='헤이스')
    st.write('역할 : Unlocker')
    st.write('크로스, 전환 패스, 전진패스를 자주 한다. 침투 패스를 넣어주는 유형이다.')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/16_out_까뇨뚜.png')
        image = image.resize((140, 180))
        st.image(image, caption='까뇨뚜')
    with col2:
        image = Image.open('./data/activation_pic/16_out_송승민.png')
        image = image.resize((140, 180))
        st.image(image, caption='송승민')
    with col3:
        image = Image.open('./data/activation_pic/16_out_팔라시오스.png')
        image = image.resize((140, 180))
        st.image(image, caption='팔라시오스')
    st.write('역할 : Outlet')
    st.write('공 소유시 안정적인 플레이를 가져간다. 중원과 골문 근처에서 다수의 터치를하며 파울을 이끌어낸다.')

#############################################################################

    st.subheader('중앙 공격수')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/17_fi_고재현.png')
        image = image.resize((140, 180))
        st.image(image, caption='고재현')
    with col2:
        image = Image.open('./data/activation_pic/17_fi_레오나르도.png')
        image = image.resize((140, 180))
        st.image(image, caption='레오나르도')
    with col3:
        image = Image.open('./data/activation_pic/17_fi_오현규.png')
        image = image.resize((140, 180))
        st.image(image, caption='오현규')
    st.write('역할 : Finisher')
    st.write('슛 기회를 찾는 데 중점을 둔다.')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/18_roa_라스.png')
        image = image.resize((140, 180))
        st.image(image, caption='라스')
    with col2:
        image = Image.open('./data/activation_pic/18_roa_조규성.png')
        image = image.resize((140, 180))
        st.image(image, caption='조규성')
    with col3:
        image = Image.open('./data/activation_pic/18_roa_주민규.png')
        image = image.resize((140, 180))
        st.image(image, caption='주민규')
    st.write('역할 : Roamer')
    st.write('공을 오래 소유하며 공격하지 않을 때 내려오거나 공간을 벌려주기를 즐겨하는 유형이다.')

    st.subheader('')
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image = Image.open('./data/activation_pic/19_tar_바코.png')
        image = image.resize((140, 180))
        st.image(image, caption='바코')
    with col2:
        image = Image.open('./data/activation_pic/19_tar_일류첸코.png')
        image = image.resize((140, 180))
        st.image(image, caption='일류첸코')
    with col3:
        image = Image.open('./data/activation_pic/19_tar_정한민.png')
        image = image.resize((140, 180))
        st.image(image, caption='정한민')
    st.write('역할 : Target')
    st.write('팀의 빌드업에 관여하며, 공중볼이나 앞에 떨어지는 공에 많이 관여한다.')