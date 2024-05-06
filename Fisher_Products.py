from module_package import *

if __name__ == '__main__':
    timestamp = datetime.now().date().strftime('%Y%m%d')
    file_name = os.path.basename(__file__).rstrip('.py')
    all_data = []
    url = 'https://www.fishersci.com/us/en/browse/products'
    base_url = 'https://www.fishersci.com'
    headers = {
        'authority': 'www.fishersci.com',
        'method': 'GET',
        'path': '/us/en/home.html',
        'scheme': 'https',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        # 'Cookie': 'new_hf=true; new_cart=true; new_overlay=true; f_num=gmr; estore=estore-scientific; mdLogger=false; kampyle_userid=3cc8-fbfb-d62f-9006-dc00-3c93-3bdc-21c7; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; cmapi_cookie_privacy=permit 1,2,3; s_vi=[CS]v1|330F088F363E0F9D-40001AC782A03632[CE]; s_ecid=MCMID%7C37161450081914606704547458763525740027; _gcl_au=1.1.1721032353.1713246496; QuantumMetricUserID=833703007cfee3fe1bd5ef1002d272d4; _hjSessionUser_341846=eyJpZCI6IjZlMzQ0MDQ1LWNkZTMtNWE1NS05YzczLTNhNTc2NDc1NzkxNSIsImNyZWF0ZWQiOjE3MTMyNDY0OTU2NjAsImV4aXN0aW5nIjp0cnVlfQ==; aam_uuid=40520749103498727913797215346890034770; WCXUID=35760512971517138714287; preventSingleResultRedirect=true; _gid=GA1.2.273275572.1714052867; locale=en_US; usertype=G; formSecurity=sv2cer9z3ul; akacd_FS_US_ProdA_Search_LucidWorks=3891575502~rv=10~id=1ff70e092d28aa94c023c341544a4939; AMCVS_8FED67C25245B39C0A490D4C%40AdobeOrg=1; AMCV_8FED67C25245B39C0A490D4C%40AdobeOrg=359503849%7CMCIDTS%7C19839%7CMCMID%7C37161450081914606704547458763525740027%7CMCAAMLH-1714727504%7C12%7CMCAAMB-1714727504%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1714129904s%7CNONE%7CMCAID%7C330F088F363E0F9D-40001AC782A03632%7CvVersion%7C5.0.1%7CMCCIDH%7C-1997303517; akacd_FS_Prod_AWS_EKS=3891575503~rv=70~id=78d608c4b1e6e7d51523efc10909b204; BIGipServerwww.fishersci.com_magellan_pool=1288357898.37919.0000; vcCookie=1; testTLD=test; WCXSID=00007737851171412270517166666666; userTypeDescription=guest; akacd_FS_Prod_AWS_EKS_Users=3891575503~rv=48~id=dc1fd6e52d24b3f40fdfb308193fcccc; memberId_AAM=; at_check=true; PFM=unsorted; accountId_AAM=Guest%20or%20No%20Account%20Chosen; com.ibm.commerce.ubx.idsync.DSPID_ADOBE%2CaaUserId%2CmcId%2Cx1VisitorId=com.ibm.commerce.ubx.idsync.DSPID_ADOBE%2CaaUserId%2CmcId%2Cx1VisitorId; bm_mi=A1B64201425E6D725F37E26F190F73BC~YAAQdDkgFzxaqBWPAQAAnwmtGRf3pU/gt8nqSvSytoynTAstbxQLcdnkVfrk/0OKxnml3vjgEntEWpB+M2XlBxZsM13g1AEyg9nuqwvUGjhDYuZMkc6z8L++DodS2lEV4/37mFfAVuY9b84NUVbJkVACBWH3RPqEICroDl0/k6EmjfIwIYc11l/tM7FM7bzwMx1V/DwdG8WB9YyKHIqIkX2sXTGSc1sLQRgYSqRTpKDiu+tCS3zuuoROAZQZUXR/30SG2C0raPkXlHfmic8ZPqauVPl2qvA5v6uK67s1LCpKHnd67qIzzzW1wGBBIbKB0VM4yyv31mecUGaNuEM=~1; WCXSID_expiry=1714123073316; TAsessionID=6bfaa024-0300-4019-8b07-e8294456460c|EXISTING; _hjSession_341846=eyJpZCI6Ijk2MGRmZTRjLWU4ZTUtNDRkZC1iYmJhLTZlYzUwMWYwYzc3NyIsImMiOjE3MTQxMjYyNjMwMzAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; s_days_since_new_s=Less than 1 day; dmdbase_cdc=DBSET; QuantumMetricSessionID=69d1356ac01e048f5f2e8fe90226cf63; adcloud={%22_les_v%22:%22c%2Cy%2Cfishersci.com%2C1714128068%22}; notice_behavior=implied,eu; new_quote=true; new_checkout=gmr; cmapi_gtm_bl=; s_days_since_new=1714126681820; s_pers=%20s_fid%3D14A195C2B6AD3030-11BBF514B556C1B0%7C1871012895376%3B%20gpv_pn%3Dhome%7C1714128482190%3B; _ga_TX98RX25ZK=GS1.1.1714126263.5.1.1714126682.58.0.0; _ga=GA1.1.573004469.1713246496; kampyleUserSession=1714126682365; kampyleUserSessionsCount=10; kampyleSessionPageCounter=1; mbox=PC#a38a87586d78400a8f67559b29c65b00.41_0#1777371483|session#5dc60f80a46b42d390f715ea7176ed40#1714128124; ak_bmsc=D8688914345F53570EFBDCDD4A60A8BB~000000000000000000000000000000~YAAQdDkgF8McqxWPAQAAwIXpGReAE0uBCMsGdjRMkKYoLDb7Bpm/MGhth0UXa5X0rpiduwas4Om5wZcOH9ZoUsbbmto+a2KxIV1n6Z/ivcaTFzAqpFxZ83PqvbuFoiedM76WvdCjZ6RplHHBLAeEgSrxSMposV19B48xF4XVC3Ot075eZTolInyS46J7mdk9Vkry9zKM21ECZwzU9x/0I25NUlHsolsbxk0m24YyemvQQIfRlfSjxkZ48FNO6k/UkcdM9hsel3dAcrAP3M7xlfSDixy7kYlMDEUsHl0FVkNALiaWswNPNKuusEECCjS9DdH/R2MpwaklmzCtkF6crZAeU2N97rMnyo0zU8GGi7RKeyc6nDG6n29jSrBnnESZBOTDZPqyxVi/X8aROFdJDhy7WU6LiVGwRisdh0LTQ8+sSnhG6JqKC2fjIkGe5fWJCcsmdpLfHs+zdcgO14SzVyfYs5GqpE0Ae3mTBYAo8Ys7mdSmnxO54R+cLataBsJQlLBk6O39kJC5ApG3/GaP3VI=; bm_sv=89AECBB20820FF8B2CA64B2B79139709~YAAQdDkgF8QcqxWPAQAAwIXpGReyb4SruJ82mMiMatFUEaN0LKBtB/wAZ3bw3nDA5Blf/H39K6tLCG/y99qHj8Y7ucAjrkx9h2bQ6KtZxEEEhXKZZ+EUQCXkalj1WGqcjL9UJ4X6Hah5z1i7LJubD/cxpft3t48o9Yex/uMBY0o4c049YXQ7btPGWAo5m0lgS+iR3HYeVQ7KNeYqdAxfIawmr7Q+7JeYvGYlbIu6RUJdNUcKGts4RRkJps3X5DD95FtmEg==~1; cto_bundle=OOIu2V9SeEo2c0E0U3owbW01NmJYUlNpQ0pMZHo2UHhSVnRsd0p2UHJveGJNRyUyRiUyRlZPWklJJTJGTVVNdHBaSnh4QVRTVDBxaUpLdCUyQlhIU3ZLeThnNHVOU0tveE41MWVaJTJCdmJ2cHQ5OWt4VEY2RDNIUk43bTkwcWlWcUd1RUtKMUdLZEVJSmgxUzhGRlVBam1XYUVKWlhTNGl4eFJZaVdMckdCakU1elFETVVSVWFTVmFCN3NkZ0VxSXoxWEljcko2RWV4Und6Zkg4R3JNTGx6TThBaXJMMFFsZEpFQSUzRCUzRA; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3Dthermofisherfishersciprod%253D%252526pid%25253Dhome%252526pidt%25253D1%252526oid%25253D%2525250A%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%2525250A%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%252526oidt%25253D3%252526ot%25253DSUBMIT%3B',
        'Priority': 'u=0, i',
        'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }
    soup = get_soup(url, headers)
    all_products = soup.find_all('ul', class_='ul_categories_list list-categories')
    for single_products in all_products:
        inner_href = single_products.find_all('a')
        for single_href in inner_href:
            href_split = str(single_href).split('/browse/', 1)[-1].split('/', 1)[0].strip()
            main_url = f'{base_url}{single_href["href"]}'
            if main_url in read_log_file():
                continue
            inner_request = get_soup(main_url, headers)
            if inner_request is None:
                continue
            if inner_request.find('h3', class_='result_title'):
                '''PAGINATION'''
                page_content = strip_it(inner_request.find('div', class_='results_count').text.replace('results', '').replace(',', ''))
                count = page_content.split('of', 1)[0].split('–', 1)[-1].strip()
                page_count = page_content.split('of', 1)[-1].strip()
                total_pages = math.ceil(int(page_count) / int(count))
                for i in range(1, int(total_pages) + 1):
                    page_link = f'{main_url}?categoryKey={href_split}&page={i}'
                    page_soup = get_soup(page_link, headers)
                    content_url = page_soup.find_all('h3', class_='result_title')
                    for single_url in content_url:
                        product_url = f'{base_url}{single_url.a["href"]}'
                        print(product_url)
                        product_request = get_soup(product_url, headers)
                        if product_request is None:
                            continue
                        if product_request.find('table', class_='general_table product_table responsive_product_table'):
                            other_content = product_request.find('table',
                                                                 class_='general_table product_table responsive_product_table').find_all(
                                'tbody', class_='itemRowContent')
                            for single_content in other_content:
                                '''PRODUCT URL'''
                                product_url = f'{base_url}{single_content.find('a', class_='chemical_fmly_glyph')['href']}'
                                print(product_url)
                                '''PRODUCT ID'''
                                try:
                                    product_id = strip_it(single_content.find('a', class_='chemical_fmly_glyph').text)
                                except Exception as e:
                                    print('product id:', e)
                                    product_id = ''
                                if product_id in read_log_file():
                                    continue
                                '''PRODUCT NAME'''
                                try:
                                    if product_request.find('h1', id='qa_product_description'):
                                        main_name = product_request.find('h1', id='qa_product_description').text.strip()
                                    elif product_request.find('h1', id='item_header_text'):
                                        main_name = product_request.find('h1', id='item_header_text').text.strip()
                                    else:
                                        main_name = ''
                                except:
                                    main_name = ''
                                if single_content.find('td', attrs={'data-title': 'Mfr. No.'}):
                                    inner_name = strip_it(single_content.find('td', attrs={'data-title': 'Mfr. No.'}).text.strip())
                                    content_name = f'{main_name} {inner_name}'
                                    if single_content.find('td', attrs={'data-title': 'Temperature (Metric) Range'}):
                                        other_name = single_content.find('td', attrs={'data-title': 'Temperature (Metric) Range'}).text.strip()
                                        product_name = f'{content_name} {other_name}'
                                    elif single_content.find('td', attrs={'data-title': 'Gauge'}):
                                        Gauge_name = single_content.find('td', attrs={'data-title': 'Gauge'}).text.strip()
                                        Gauge_name = f'{content_name} {Gauge_name}'
                                        if single_content.find('td', attrs={'data-title': 'Nozzle Diameter (Metric)'}):
                                            inner_data = single_content.find('td', attrs={'data-title': 'Nozzle Diameter (Metric)'}).text.strip()
                                            nozzle_name = f'{Gauge_name} {inner_data}'
                                            if single_content.find('td', attrs={'data-title': 'Color'}):
                                                color_data = single_content.find('td', attrs={'data-title': 'Color'}).text.strip()
                                                product_name = f'{nozzle_name} {color_data}'
                                            else:
                                                product_name = nozzle_name
                                        else:
                                            product_name = Gauge_name
                                    else:
                                        product_name = content_name
                                else:
                                    product_name = main_name
                                '''PRODUCT PRICE AND PRODUCT QUANTITY'''
                                try:
                                    price_content = single_content.find('td', attrs={'data-title': 'Price'}).text.split('for', 1)
                                    product_price = price_content[-1].strip()
                                    if product_price == '':
                                        product_quantity = ''
                                    else:
                                        product_quantity = price_content[0].replace('Each of', '').replace('Case of', '').replace('Pack of', '')
                                except:
                                    product_price = ''
                                    product_quantity = '1'
                                print('current datetime------>', datetime.now())
                                dictionary = get_dictionary(product_ids=product_id, product_names=product_name,
                                                            product_quantities=product_quantity,
                                                            product_prices=product_price, product_urls=product_url)
                                articles_df = pd.DataFrame([dictionary])
                                articles_df.drop_duplicates(subset=['product_id', 'product_name'], keep='first',
                                                            inplace=True)
                                if os.path.isfile(f'{file_name}.csv'):
                                    articles_df.to_csv(f'{file_name}.csv', index=False, header=False, mode='a')
                                else:
                                    articles_df.to_csv(f'{file_name}.csv', index=False)
                                write_visited_log(product_id)
                        else:
                            product_content = product_request.find('div', id='ProductDescriptionContainer')
                            '''PRODUCT NAME'''
                            try:
                                product_name = strip_it(product_content.find('h1', id='item_header_text').text.strip())
                            except:
                                product_name = ''
                            '''PRODUCT ID'''
                            try:
                                product_id = strip_it(product_content.find('p', class_='rightProductCode').span.text)
                            except:
                                product_id = ''
                            if product_id in read_log_file():
                                continue
                            '''PRODUCT PRICE'''
                            try:
                                product_price = f'$ {strip_it(product_content.find('span', itemprop='price')['content'].strip())}'
                            except:
                                product_price = ''
                            '''PRODUCT QUANTITY'''
                            try:
                                if product_price == '':
                                    product_quantity = ''
                                else:
                                    product_quantity = product_content.find('span', itemprop='price').find('span', itemprop='unitText')['content'].replace('Each of', '').replace('Case of', '').replace('Pack of', '').strip()
                            except:
                                product_quantity = '1'
                            print('current datetime------>', datetime.now())
                            dictionary = get_dictionary(product_ids=product_id, product_names=product_name,
                                                        product_quantities=product_quantity,
                                                        product_prices=product_price, product_urls=product_url)
                            articles_df = pd.DataFrame([dictionary])
                            articles_df.drop_duplicates(subset=['product_id', 'product_name'], keep='first',
                                                        inplace=True)
                            if os.path.isfile(f'{file_name}.csv'):
                                articles_df.to_csv(f'{file_name}.csv', index=False, header=False, mode='a')
                            else:
                                articles_df.to_csv(f'{file_name}.csv', index=False)
                            write_visited_log(product_id)
            write_visited_log(main_url)

