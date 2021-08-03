import requests
from bs4 import BeautifulSoup as bs

REQ_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}


def check_BestBuy():
    REQ_HEADERS['cookie'] = 'pst2=425|N; oid=1423846647; vt=7cb918e2-ecab-11eb-a720-0a91360987bd; CTT=0e931c05c3ec470e1a91dbef6b7b6e35; s_ecid=MCMID|85987423195269957421390455061551331441; __gads=ID=dbcd7fe1e6359436:T=1627150694:S=ALNI_MbI6sIBkB3SJHTmnDGI82qZ0ByqYA; aam_uuid=91125552748924964441903177300308595027; sc-location-v2={"meta":{"CreatedAt":"2021-07-24T18:18:17.199Z","ModifiedAt":"2021-07-24T18:18:17.200Z","ExpiresAt":"2022-07-24T18:18:17.200Z"},"value":"{\"physical\":{\"zipCode\":\"28655\",\"source\":\"A\",\"captureTime\":\"2021-07-24T18:18:17.198Z\"},\"destination\":{\"zipCode\":\"28655\"}}"}; locDestZip=28655; locStoreId=425; sto__vuid=91f7237477da1f109461f6bd43740814; _cs_c=1; _gcl_au=1.1.1228245178.1627150715; physical_dma=517; customerZipCode=28655|N; bby_rdp=l; SID=6471489f-e5d6-400d-8629-9d345568e8bd; bm_sz=7FAFB61657B03B9829FD47BDB0065BF5~YAAQva8GYMdEeAp7AQAACmv1DQzvNoV3+78pKD1GAj1XI6bwrCc4Eah/nkISA06P69YxctpYSG8U3zQYdRrrxoUGP5qB/PaXqJGFjgnaZSbNj6c5Wl9y2xuyBFPb92893wLqmBPNQwSIf+HhgQxdLNj+jbcc9bDoAq/XqIBLZIM3mAl7LYSMciWLRU5XXGsM31q6cMy7szUARI6gxzP4POZhsdO4cmCIrAF0OumX2o/97pFmYH6YMBdgwiBWryDiT8ggsCNwy2rAOfioOnl/hnRfSzBSj2zh+JPGTaE0AzOMsaT6z4ppFjfmb7Is2DcAJJcGECTHLE0VbQf4U6H5FjpmqE9KjKV3icfTUuue9F+C0wFrGr9Hq6tqNaqy43sC5Pjh/vahmd/lVeBfcFj6cr9b7Q==~3228997~3687491; _abck=CD27BAB124493C988FD8973F96DD6C2D~0~YAAQva8GYMZEeAp7AQAACmv1DQZJM+sasNoblvZIe/8hLXxio2/UIZurBanI48pM2cwB3WW+NCmUEMo0aUWCXzMwtVaTREipQHYy6d35HOsz5jP3pGk/XBprHkfr8lpgIpe2Dp0hOwNjzhfnx5srwPhWeIwJZ2wWNeNLh+mUmG59ij+gMmEHZ7fuuqQHeRzbwGI6c+jZMSw42GsDBVXcL99XOhA47apPjdsAc+6pgJBE/ore2fD1O3niNn+8/4IKCcuIRmcEEX3hKwyEHiByJ0tt2GinoQ0BmSTwMJxqwVcTiNBQKlcklI8vhDmu8Lom5bVg02a1M0spsYPnJV6N9uV9IVdS1ljP/spViK2wb/GpHtb2QTdkdFD+wQlzDNyaXNJwNnmO2q4xleb2+eyWARlZTpf9/1rMROtYbKdEiinl4eQYqdPmxl+HjxCaikxL~-1~-1~-1; COM_TEST_FIX=2021-08-03T21:40:07.356Z; sto__session=1628026808786; campaign=198_Hatch_0; s_cc=true; s_fid=7C4486548ECBE740-1F65A60E40234CA5; AMCVS_F6301253512D2BDB0A490D45@AdobeOrg=1; AMCV_F6301253512D2BDB0A490D45@AdobeOrg=1585540135|MCMID|85987423195269957421390455061551331441|MCAAMLH-1628631612|7|MCAAMB-1628631612|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1628034012s|NONE|MCAID|NONE|MCCIDH|1233887400|vVersion|4.4.0; _cs_mk=0.6957957905906778_1628026812364; CTE22=T; surveyDisabled=true; CTE5=T; rxVisitor=1628028162288AQNC1PGHVDHRLM0QDUDP3K7S2BF25JIK; lux_uid=162802816230560231; 52245=; dtCookie=v_4_srv_9_sn_SBFDAO2BEN3U1U7N43HC6Q681D4CJQPN_app-3Aea7c4b59f27d43eb_1_app-3A1b02c17e3de73d2a_1_ol_0_perc_100000_mul_1; dtSa=-; bby_cbc_lb=p-browse-e; partner=198&Hatch&2021-08-03+17:22:58.000; ltc= ; basketTimestamp=1628029380187; sto__count=10; campaign_date=1628029383992; s_sq=[[B]]; bby_prc_lb=p-prc-e; cto_bundle=rIAfFF9lSWFOWFJtS2VjMWwxa3VvWW1FYnlER0dkUWt0cmp1NCUyQnphNU04RFVzeFVMSUxGMmMlMkJ4MFkySmxUNyUyQjklMkJhVVJIbTZLZmNSelFydW82UVlWUFVTM24yOTAlMkJlT3R5TkZHcG5lNU5KQkx1cmRQbVhwSkNVNlR5WXolMkJuOW12TVhYaTIlMkJQNUk1Qnk1cnZwallWdElFc1JTdyUzRCUzRA; rxvt=1628031185982|1628028162290; dtPC=9$229384965_394h-vGUIHDSPJPPHEFCGRHRRRSPSTCPAHEOBC-0e4; c2=Video Games: Xbox Series X|S: Xbox Series X|S Consoles: pdp; dtLatC=1; _cs_id=b0108af8-dc4a-af0d-f8f7-7316aca1877e.1627150714.2.1628029401.1628026830.1614963257.1661314714338.Lax.0; _cs_s=9.1'
    url_x = "https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/b6d5d68c-5320-4719-9d64-3afb423f6b86"
    url_s = "https://www.bestbuy.com/site/combo/xbox-series-x-and-s-consoles/ab90fc02-495b-4e64-9760-3945f28f3e00"

    response_x = requests.get(url_x, headers=REQ_HEADERS)
    soup_x = bs(response_x.content, 'lxml')

    btn_add_x = soup_x.find(class_="add-to-cart-button")

    response_s = requests.get(url_s, headers=REQ_HEADERS)
    soup_s = bs(response_s.content, 'lxml')

    btn_add_s = soup_s.find(class_="add-to-cart-button")
    print("Best Buy:")

    if btn_add_x.has_attr("disabled"):
        print("Xbox Series X: Unavailable")
    else:
        print("Xbox Series X: Available")

    if btn_add_s.has_attr("disabled"):
        print("Xbox Series S: Unavailable")
    else:
        print("Xbox Series S: Available")

# print(soup.prettify())

def check_walmart():
    REQ_HEADERS['cookie'] = ""
    url = "https://www.walmart.com/cp/xbox-all-access/8571041"

    response = requests.get(url, headers=REQ_HEADERS)
    soup = bs(response.content, 'lxml')

    anchor_x = soup.select("a[aria-label='Xbox Series X']")[0]
    anchor_s = soup.select("a[aria-label='Xbox Series S']")[0]

    print("Walmart:")

    if not anchor_x.has_attr("href"):
        print("Xbox Series X: Unavailable")
    else:
        print("Xbox Series X: Available")

    if not anchor_s.has_attr("href"):
        print("Xbox Series S: Unavailable")
    else:
        print("Xbox Series S: Available")


def check_GameStop():
    REQ_HEADERS['cookie'] = 'akaas_ChatThrottling=2147483647~rv=27~id=15d054b81a3c79360491be29d6ba7e82~rn=; bm_sz=791395B97A787322AE6B4BDFB92250B3~YAAQFwDorJ3MeZt6AQAAjWr1DQxg1QOYhrIoHUm0bmqR8lYS/RKwYmGbMvp8rnBGwFsXpzm89PazdF3CzKvcEu0sn3nDXTBthoIxSdTAFmHxgPe49wGqZ3xkVXBD8plbZlFNzsRCPz7qr7OxJZhycHWbEMHnzK7fRqhdomkUOglB2nXWYCnDcFH99zmpFn+HF7u4UzXqmsnVclydmE0cU8BnzxiQCJJo3SWUuXpTwzao5R22WDeHgU9J5FYDytoEDXDPI7hki7WDXhHGMaXivl6pLPWJI8gvpaRybDI/P9fOrpRJsA==~4535602~3225412; sid=svLnEKJuWstJ_iS_-2koJd1C9Di_YqNBpVs; dwanonymous_420142ceefb9f0c103b3815e84e9fcef=abxHVAWI8aE6eKyageDN6aUx51; dwac_a78eb5a11975e4c9cbc84f55ad=svLnEKJuWstJ_iS_-2koJd1C9Di_YqNBpVs=|dw-only|||USD|false|US/Central|true; cquid=||; __cq_dnt=0; dw_dnt=0; dwsid=BqnI-XZZNDr56uTAo7FzWWkZ29FrVc2wFU8qGbLVUxOnXbkEj8ore9EwOh4w_69H1J4Db9pdZpkKZXtfCBBlTw==; cqcid=abxHVAWI8aE6eKyageDN6aUx51; customergroups=Everyone; userInfo=S=N|R=N|C=0; lastVisitedCgid=xbox-all-access; notice_behavior=implied,eu; bm_mi=014258DF9B64D64DD088CA8CE03270FA~38A9NsSDxVP0ILgBXi64a5rN4d8e80SGr80P25kvcbsl6p3q/4mu8bLXyiX+YS3SOLoM946gAr7VPkcq3442fiwYloioeh4kdHwvfeRd3pfP1H3TpGi7X92ZqSx57t8OALqBckiA1YZ0TQVF0J2IOOF58CDrgWEncpo3sLcsxF7EvQEhW1437cz2rQuMy10q2mjNBgnSIqMv7LtSOy0mGw/LzelrRpi5gKI3xPU4V7ClEl4qqsA4G5MNQuAfaNHI1S46tbqyZJCFTFGHHwUF3fjdEzN0px4fg8yyaSTvHa0r7nkcEDe198OofGYkES65; _ga=GA1.2.499744899.1628028576; _gid=GA1.2.1365338041.1628028576; ak_bmsc=32F6C91B726F22B39388009047AADE31~000000000000000000000000000000~YAAQFwDorEF1ept6AQAA66MQDgxb9EPNr4jOIJi+66OF1XuY1oQWGvOwPlvLTI7fxVbFsAYfRgCvQaCWDkvMZDOPsoMPue9cAc+mx46y9F/zK+uIBdkoN9iKCiQQjnu32Fy/AoxJVDprgj265RYZ5uXQBjI2dfmfoYwz2qFnsGUwyrxdcpAwrvtB3j9cGQwJ2/PFKwVgykUONPjExiDZNtCgo5fm/ZpeeCEl/AtP8io2FP6eW+RGnIJE6Oyvc9jogD0j2ByRz20tt1X2hxVgfH4ebeVtSpLPvMPL/xISgRC3z68/oq0n3K18pBvyX2cbjLIoFW4WWTvypPdVBOhoLu+1vSVvmEpJnWwnRTN4PQ4bwDFbffn8/4ueJjpuAVwQ1mbPfkc8DEXYz+NYqtAMj4dzqohkdV+jewpFk4WSoLgxKM1Fiqxjrh56XnwfqzkAgrQ5T6bygQwXHA==; linkshareAffiliateID=77777; linkshareSiteID=9SHw.8narkE-OlK9L_ZNH27nGXGElSZuHg; _gcl_au=1.1.2100527425.1628028577; QuantumMetricUserID=c80d46a856e182d76bf442e213dccb3f; QuantumMetricSessionID=cb21c21687630e136cdc8a3252fd85f7; _caid=1c4db105-996e-4753-8afc-38443cf8bd30; _cavisit=17b0e10a541|; _mibhv=anon-1628028577093-1977850376_6874; __cq_uuid=abiYci3obSvyWZGVia6aLuFmI3; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; _fbp=fb.1.1628028577207.97257992; _aeaid=84845e52-c215-4536-b8e6-83956ed6c4ec; aeatstartmessage=true; sto__session=1628028577741; sto__vuid=91f7237477da1f109461f6bd43740814; zc1=28655; BVBRANDID=9786fe36-f464-454d-85ea-ece2d2ef7946; BVBRANDSID=62823dae-bb03-4094-a516-42fddefa7c72; __cq_bc={"bcpk-gamestop-us":[{"id":"B224746A"}]}; _uetsid=7dbcab00f4a711eba3193de28a989201; _uetvid=7dbcc670f4a711ebad87896e1549612d; stc118903=tsa:1628028577331.2022397798.0850883.9719543327503222.:20210803223950|env:1|20210903220937|20210803223950|3|1084111:20220803220950|uid:1628028577331.966139438.9618883.118903.938043761.5:20220803220950|srchist:1084111:1:20210903220937:20220803220950; sto__count=2; cto_bundle=qXgAzV93eEQlMkJwVXZUMmRjJTJGZWd4UDVFeHkwJTJCeFBNU25PN1dkRU43JTJCdXRRUzRSRVZJY05QS25vcGRBWVM4dDRQYk1UdDJIejIyQjd6VXRrMGhLTVVIb2MxM3RvQ09CMVA5eTRKWWZ0Y3VIblFkMUREUzZwNm9BMXQ4dDhmckpMYlBqeXhZVEUyVnhabHF5WDZTJTJGJTJGZ2JhSHVCZ3clM0QlM0Q; _abck=5F41ADB012099F14D7CD001BC126FE33~-1~YAAQFwDorGSiept6AQAAr0UaDgZxnXX306+nz4JOSmUs7UC3cZgxffq3VVLxj4prI9cBIvu55L0KSw8xKzkr2PYSisG1liuPit8s/PPbBbJ4OPE8AW4WW96Q+E96Sphr21Fb6yL60sScpN7oeKE9eShYRNTobckQePF+oiS2ssIiXYmMz7PxUGa2ibwN7bBP+Lts8Qv1mZHdgW/byRNy9n/wcNlggPTZE9uw7nIro3Dc51bz3LyVWSqbw4YqLnXPziGC4Z8rnP0kSMwrwzt5mRu6+4sqepmpdvf30+WXrtsxSvPzedvgUSk6ncJCn/I8D0qNYE1Owfc56d+HbsMWnFgPpd2HeWtNuaB+WT+dQqopjC/N15JfAWYFFzrR/ZeBozNx5zGYfOgi49cKvLQvjPU5Bi7R+PxNqfZKhcxIalKR2RbwVKKf~-1~-1~1628032788'

    url_x = "https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-x-xbox-all-access/B224744A.html"
    url_s = "https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-s-xbox-all-access/B224746A.html"

    response_x = requests.get(url_x, headers=REQ_HEADERS)
    soup_x = bs(response_x.content, 'lxml')

    btn_add_x = soup_x.find("button", {"id": "getting-started-btn"})

    response_s = requests.get(url_s, headers=REQ_HEADERS)
    soup_s = bs(response_s.content, 'lxml')

    btn_add_s = soup_s.find("button", {"id": "getting-started-btn"})

    print("GameStop:")

    if btn_add_x.has_attr("disabled"):
        print("Xbox Series X: Unavailable")
    else:
        print("Xbox Series X: Available")

    if btn_add_s.has_attr("disabled"):
        print("Xbox Series S: Unavailable")
    else:
        print("Xbox Series S: Available")


check_BestBuy()
check_walmart()
check_GameStop()