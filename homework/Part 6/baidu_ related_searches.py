#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-28 23:17:42
# @Author  : killingwolf (killingwolf@qq.com)
import re
import urllib
import urllib2
import cookielib
import chardet

get_url = 'https://www.baidu.com/s?ie=utf-8&newi=1&mod=1&isbd=1&isid=c50b42ab00069608&wd=%E7%A7%91%E6%8A%80&rsv_spt=1&rsv_iqid=0xca25602a0006fcd9&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=0&oq=%E7%A7%91%E6%8A%80&rsv_t=c803Hq%2FHhhxUS9mrZNCsrYBeJ4IhjX3caSPyrZQCt2TVe52jR1pWzt9doF29T4efWu1x&rsv_pq=c50b42ab00069608&rsv_sug7=000&rsv_sug=1&bs=%E7%A7%91%E6%8A%80&rsv_sid=17518_18285_1458_18283_18534_12824_18546_17001_17072_14979_12420_18649_17997_10634&_ss=1&clist=353effd14ca34665&hsug=&f4s=1&csor=2&_cr1=36797'
header = {
    'Cookie': 'BDUSS=FQZH5BbWluNzcyT0picUx3ZXJRLTVJY3MtOU90SjlGU2tLeDNyV25QTHU3WUJXQVFBQUFBJCQAAAAAAAAAAAEAAAB16W0Wa2lsbGluZ3dvbGYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO5gWVbuYFlWZU; BAIDUID=419F387E3C6B1D8ACCC15BDC602B6882:FG=1; PSTM=1448700425; BDSFRCVID=BaLsJeCCxG3z00O4fnZ7Jawu-XmlDWkbmpPg3J; H_BDCLCKID_SF=tRk8oKPyJKvhKROmK4r2q4tehH4HXUoeWDTm5-nTt-c4j4_mM6JVWhKJLfTPalQbL6chBlvlylI5OCF9Dj0WDTJyepJf-K625CoJL4oX-JT-etonKRoEKPLyqxby26nibbneaJ5n0-nnhIbNyRDMbtIz-f6U3Mk8Kb6nLJoE-bTHjt0Ry6CbDjoWDaDqqbJ3HJCOV6rJaDvqelvRy4oTj6DjhnQp0tCJWI3m0f5vaDK-OPT1WJA53MvB-fngQbQeWR6PW-3o0ROhORv3Qft20b0BhbQjXx0LW57AWJ7jWhk2eq72y-4b05TLjNuetTLHf5vfL5rSbRjbeJIk-PnVeTt35qbZKxJmMgke_p3OKDb1JlcGyl7a-qK0eMJXLlQx2g7J2KOFfDD5bKDlD6035n-Wqxb3-4oX2KIX3b7EfhRnOtO_bf--DlDrK-cu553JBKTa-l78JCLK8Un5WJjxy5K_yfvE-6okaGcn_ComBRvosRcHQT3my6-j0q3k0IrgtJbkWb3cWKJq8UbSMTJme6oQjGDjq60HfK73L4OSa-K_f-LryTjdKUI8LNDHtTjTJNAt_pFaLDol8nuGjx5T5tt7hnO7ttoA3Nb43qkMWn70sbOwjxTabxL1Db3Zt-7I-N5RslrKLfboepvoD-oc3Mkfjn0EJ68DJbCtVCPQb-3bKRvx2R-_-P4Den-tqnJZ5mAqoDbSQIjdVDb_yh3c3f4HjHDHb53OWK7naIQqWC5Ben3OMUIMK5-0hecz04T43bRTaq7sL4JZs56nLP7xhP-UyN3-Wh372bvTVDD5fCt5MILrKITMK4_Ebxr2atoLHD7XVb_h3tOkeqOJ2Mt526OQXNOhQPQ42DJNQJcwaRRUSnvPhJ3mbTtpeGLfq68eJbFsQ5r2-JjteRTnM4QVq4tHeP5KWnJZ5m7mXp0bMDt28IbIhlCby4_W5ecv247RQK3aW4Jx5KOkbRO4-TF5DjvWDU5; BIDUPSID=42FB37C3ECB65CDB840A9F8492ADE5EB; ispeed_lsm=2; BD_UPN=12314353; H_PS_645EC=c803Hq%2FHhhxUS9mrZNCsrYBeJ4IhjX3caSPyrZQCt2TVe52jR1pWzt9doF29T4efWu1x; BD_CK_SAM=1; BDSVRTM=247; H_PS_PSSID=17518_18285_1458_18283_18534_12824_18546_17001_17072_14979_12420_18649_17997_10634; WWW_ST=1451316035465',
    'Host': 'www.baidu.com',
    'Referer': 'https://www.baidu.com/s?wd=%E7%A7%91%E6%8A%80&rsv_spt=1&rsv_iqid=0xca25602a0006fcd9&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=0&oq=%E7%A7%91%E6%8A%80&rsv_t=c803Hq%2FHhhxUS9mrZNCsrYBeJ4IhjX3caSPyrZQCt2TVe52jR1pWzt9doF29T4efWu1x&rsv_pq=c50b42ab00069608&rsv_sug7=000&rsv_sug=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
}
# keyword = '科技'
# keyword = urllib2.quote(keyword)
# data = {
#     'ie': 'utf-8',
#     'newi': 1,
#     'mod': 1,
#     'isbd': 1,
#     'isid': 'c50b42ab00069608',
#     'wd': keyword,
#     'rsv_spt': 1,
#     'rsv_iqid': '0xca25602a0006fcd9',
#     'issp': 1,
#     'f': 8,
#     'rsv_bp': 1,
#     'rsv_idx': 2,
#     'tn': 'baiduhome_pg',
#     'rsv_enter': 0,
#     'oq': keyword,
#     'rsv_t':
#         'c803Hq/HhhxUS9mrZNCsrYBeJ4IhjX3caSPyrZQCt2TVe52jR1pWzt9doF29T4efWu1x',
#     'rsv_pq': 'c50b42ab00069608',
#     'rsv_sug7': 000,
#     'rsv_sug': 1,
#     'bs': keyword,
#     'rsv_sid':
#         "17518'_18285_14'58_18283_18534_12824_18546_17001_17072_14979_12420_18649_ '17997_106'34",
#     '_ss': 1,
#     'clist': "353e'ffd14ca34665",
#     'hsug': None,
#     'f4s': 1,
#     'csor': 2,
#     '_cr1': 36797,
# }

# data = urllib.urlencode(data)

req = urllib2.Request(get_url, headers=header)
rsp = urllib2.urlopen(req).read()
ss = re.findall(r'rsv_t=.*?">(.*?)</a></th>', rsp)
for i in ss:
    print i
