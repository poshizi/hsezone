import streamlit as st
import pandas as pd
import numpy as np
import requests
import io 
import streamlit.components.v1 as components



st.set_page_config(
    page_title="HSE.zone法规标准更新平台v1",
    page_icon="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG1jOZVsYTi/bGE4v2xhOL9sYTi/bGE4v4B2UhZvZDpEbGE4v2xhOL9sYTi/bGE4v2xhOL9vZT1mAAAAAAAAAABsYTjHamA3/2pgN/9qYDf/amA3/2pgN/9/dlEebmM5WmpgN/9qYDf/amA3/2pgN/9qYDf/bmQ8iwAAAAAAAAAAbGE4x2pgN/9qYDf/amA3/2pgN/9qYDf/f3ZRHm5jOVpqYDf/amA3/2pgN/9qYDf/amA3/25kPIsAAAAAAAAAAGxhOMdqYDf/amA3/2pgN/9qYDf/amA3/392UR5uYzlaamA3/2pgN/9qYDf/amA3/2pgN/9uZDyLAAAAAAAAAABsYTjHamA3/2pgN/9qYDf/amA3/2pgN/9/dlEebmM5WmpgN/9qYDf/amA3/2pgN/9qYDf/bmQ8iwAAAAAAAAAAbGE4x2pgN/9qYDf/amA3/2pgN/9qYDf/gHZSHm5jOlpqYDf/amA3/2pgN/9qYDf/amA3/25kPIsAAAAAAAAAAHpvRxh5bkYeeW5GHnluRh55bkYeeW5GHn90TAJ6bkYKeW9GHnluRh55bkYeeW5GHnluRh57cEcQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbWM6p2xiOelsYjnpbGI56WxiOelsYjnpcmc8JAAAAAAAAAAAAAAAAGh9+GRqfvcoAAAAAAAAAAAAAAAAAAAAAGthOLVqYDf/amA3/2pgN/9qYDf/amA3/3NpQC4AAAAAAAAAAGh8+HJme/n/Znv542h89yQAAAAAAAAAAAAAAABrYTi1amA3/2pgN/9qYDf/amA3/2pgN/91a0MwAAAAAGh8+HZme/n/Znv5/2Z7+f9me/njan73JAAAAAAAAAAAa2E4tWpgN/9qYDf/amA3/2pgN/9qYDf/dWtDMAAAAABoffh+Znv5/2Z7+f9me/n/Znv56Wh8+CwAAAAAAAAAAGthOLVqYDf/amA3/2pgN/9qYDf/amA3/3FmOygAAAAAAAAAAGh8+IFme/n/Znv552l99ywAAAAAAAAAAAAAAABrYTitamA382pgOPNrYTn3amA382pgN/NxZTokAAAAAAAAAAAAAAAAZ3z4cmh89ygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAIGDAACBgQAAgYEAAIGBAACBgQAAgYEAAP//AAD//wAAgf8AAIHnAACBwwAAgcMAAIHHAACB/wAA//8AAA==",
    layout="wide",
    menu_items={
        'Get Help': 'https://hse.zone/',
        'About': "最好用的HSE法规标准更新平台"
    }
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #GithubIcon {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
#st.header('HSE.zone法规标准更新平台v1')



# 设置页面布局
row0_space0,row0_space5,row0_space1, row0_space2, row0_space3 =st.columns([2,1,5,2,2])
with row0_space0:  # 使用第三列
    st.markdown("[![Foo](https://hse.zone/assets/img/clients/client-8.png)](https://hse.zone/)")
with row0_space1:  # 使用第一列
    st.markdown("<h2 style='text-align: left; color: #37606A;'>HSE.Zone法规标准更新平台</h2>", unsafe_allow_html=True)
with row0_space2:  # 使用第二列
    x = st.text_input("输入更新码【test】")
    if x == "":
        x = "mini"
    else:
        
        response = requests.get("https://d.dl0.net/"+x)
        if response.status_code != 200:
            x = "mini"
    x = "https://d.dl0.net/"+x    
with row0_space3:  # 使用第三a列
    st.image("https://hse.zone/assets/img/team/team-5.png",caption='扫码关注，获取更新码')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip',
    'DNT' : '1', # Do Not Track Request Header
    'Connection' : 'close'
}
tab1, tab2 = st.tabs(["说明", "**:pushpin:在线清单**"])
with tab1:
    row6_space0,row6_space2,row6_space1 =st.columns([5,1,5])
    with row6_space0:
        st.markdown("#### <span style='color:#37606A;'>三句话,会使用</span> ####",unsafe_allow_html=True)
        st.markdown("1. 微信扫码关注 **<span style='color:#F97B66;'>HSE法规标准</span>** 公众号，在对话栏发送 **<span style='color:#37606A;'>更新码</span>** ，获取更新码，填入上方，右上角 显示RUNNING 代表运行中",unsafe_allow_html=True)
        st.markdown("2. 点击 **<span style='color:#37606A;'>:pushpin:在线清单</span>** 标签，更新完成后，表格上方显示清单数量及更新日期",unsafe_allow_html=True)
        st.markdown("3. 输入法规标准的名称或者标准号 搜索，可通过体系分类、专业分类、文件类型等进行筛选，可ctrl+c复制")
        st.image("https://hse.zone/assets/img/team/team-5.png",caption='扫码关注，获取更新码')
    with row6_space1:    
        st.markdown("#### <span style='color:#37606A;'>一张图,下全文</span> ####",unsafe_allow_html=True)
        st.markdown("关注 **<span style='color:#F97B66;'>HSE法规标准</span>** 公众号，在对话栏发送【安全生产法】等标准名或标准号即可" , unsafe_allow_html=True)
        st.image("https://img.name/yk/2024/342996f2bcdb35c8.png" ,caption="扫码关注[HSE法规标准]公众号", width=305,)

with tab2:
    # 获取数据
    @st.cache_data()
    def load_data(x):
        try:
            response = requests.get(x, headers=headers)
            data = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
            return data.iloc[:, :13]
        except Exception as e:
            st.error(f"读取数据出错: {e}")
            response = requests.get("https://d.dl0.net/mini", headers=headers)
            data = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
            return data.iloc[:, :13]

    data_load_state = st.text('法规标准清单更新中...')
    df = load_data(x)
    total_rows = df.shape[0]
    last_row = df.iloc[-1]
    data_load_state.markdown(f"<span style='color:#37606A;'>当前更新码，后台清单总量：</span><span style='color:#F97B66;'>{total_rows}条</span><span style='color:#37606A;'>, 更新日期：</span></span><span style='color:#F97B66;'>{last_row[4]}</span><span style='color:#37606A;'>，更新日期如超1个月，请扫码获取更新码</span>", unsafe_allow_html=True)


    # 在表格顶部设置的筛选功能

    
          
            
    

    
    
  
    #st.header('筛选功能')
    # 创建两行三列布局
    row1_space0,row1_space1, row1_space2, row1_space3, row1_space4 ,row1_space5 = st.columns([2,1,1,1,1,1])
    # 第一行
    # 关键词搜索框
    keyword = row1_space0.text_input('法规标准名称或标准号')
    if keyword:
        df = df[df['文件名称'].fillna("").str.contains(keyword) | df['标准号'].fillna("").str.contains(keyword)]
    # 文件类型多选框
    file_type_options = ['ALL','国家法律', '行政法规',  '地方性法规', '行政规章', '政策文件', '国家标准', '行业标准', '地方标准', '团体标准']
    selected_file_type = row1_space1.selectbox('文件类型', file_type_options)
    if selected_file_type != 'ALL':
        df = df[df['文件类型'].fillna("").str.contains(selected_file_type)]
    # 适用范围多选框
    file_loca_options = ['ALL','全国', '北京市',  '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省', '吉林省', '黑龙江省','上海市', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省','重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区']
    selected_loca_type = row1_space2.selectbox('适用范围', file_loca_options)
    if selected_loca_type != 'ALL':
        df = df[df['适用范围'].fillna("").str.contains(selected_loca_type)]
    # 体系分类的筛选框
    system_classification_options = ['ALL','安全', '环境', '职业健康', '能源管理', '工程', '质量', '食品', 'GSP', 'GMP', '医疗器械', '实验室', '社会', '网络']
    system_classification = row1_space3.selectbox('体系分类', system_classification_options)
    if system_classification != 'ALL':
        df = df[df['体系分类'].fillna("").str.contains(system_classification)]
    # 专业分类的筛选框
    system_classification_options = ['ALL','通用安全', '机械安全', '电气安全', '特种设备', '事故工伤', '劳动防护', '消防', '燃气', '应急管理', '煤矿非煤', '危险化学品', '交通安全', '建筑施工','危险作业', '烟花爆竹', '通用环境', '水环境', '大气环境', '噪声与振动', '土壤环境', '固体废物', '核辐射与电磁辐射', '生态环境保护', '环境影响评价', '排污许可', '清洁生产', '环境标志产品', '污染防治技术']
    system_classification = row1_space4.selectbox('专业分类', system_classification_options)
    if system_classification != 'ALL':
        df = df[df['专业分类'].fillna("").str.contains(system_classification)]
    # 有效性多选框
    file_type_options = ['ALL','现行', '废止', '已修改', '即将实施', '即将废止']
    selected_file_type = row1_space5.selectbox('有效性', file_type_options)
    if selected_file_type != 'ALL':
        df = df[df['有效性'].fillna("").str.contains(selected_file_type)]
    # 显示数据
    st.caption(f"符合条件的法规标准有： {len(df)}条")
    st.dataframe(df,use_container_width=True, height=620)  # 设置数据框的高度
