import streamlit as st
st.set_page_config('Vuong quoc mo hinh',':sparkles:')
st.title('Vuong quoc mo hinh')
chu_de = ['Dragon ball','Naruto','one Piece']
cols = st.columns(len(chu_de))
chon = None
for i, cd in enumerate(chu_de):
    with cols[i]:
        if st.button(cd):
            chon = cd
if chon:
    st.header(f'Danh sach mo hinh {chon}:')
    cols = st.columns(3)
    for i in range(3):
        with cols[i]:
            st.image(f'{chon}.png',caption=f'MS: 00{i+1}')
st.divider()
st.subheader('Đat hang')
with st.form('Don dat hang'):
    loai = st.selectbox('chu de:',chu_de)
    ma = st.selectbox('ma so:',['001','002','003'])
    slg = st.slider('so luong:',1,10,1)
    name = st.text_input('Ho ten KH:')
    sdt = st.text_input('sdt:')
    add = st.text_input('Dia chi:')
    bill = {
        'Mo hinh': loai, 'Ma so': ma, 'So luong': slg, 'Ho ten KH': name, 'sdt': sdt, 'Dia chi': add
    }
    if st.form_submit_button('Xác nhận'):
        st.subheader('Ban da chon:')
        for k, v in bill.items():
            st.write(k, v)
with st.sidebar:
    st.title('Vuong quoc mo hinh')
    st.image('hinh1.jpg')
    st.info(':house: Dia chi:'); st.info(':phone: Dien thoai: ')
