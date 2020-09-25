from selenium import webdriver as wd
import pandas as pd

def init_driver():
    driver = wd.Chrome(executable_path='./chromedriver')
    return driver

def first_feature():
    filter_word = input('Input keyword: ')
    filter_word_length = len(filter_word)
    df = pd.read_excel('urls-list.xlsx')
    link_list = []
    count_list = []
    first_result_list = []
    links = df['website_link']
    keyword_list = []
    order = 0
    for each_link in links:
        keyword_list.append(filter_word)
        order = order + 1
        print('%s' % order + ' being sent to scraper')
        link_list.append(each_link)
        driver = init_driver()
        driver.get(each_link)
        try:
            soup = driver.page_source
            # counting the numbers
            real_count = 0
            for i in range(0, len(str(soup)) - filter_word_length):
                if soup[i:i + filter_word_length] == filter_word:
                    real_count = real_count + 1
            if real_count == 0:
                first_result_list.append('no result')
            count_list.append(real_count)
            # finding the first result
            soup_list = str(soup).split('>')
            count = 0
            for each_soup in soup_list:
                length = len(each_soup)
                for i in range(0, length - filter_word_length):
                    if each_soup[i:i + filter_word_length] == filter_word:
                        count = count + 1
                        if count == 1:
                            first_result = str(each_soup + '>').strip()
                            first_result_list.append(first_result)
        except:
            count_list.append('error')
            first_result_list.append('error')
        driver.close()
        wp_information = pd.DataFrame(
            {
                "Keyword": keyword_list,
                'Website Url': link_list,
                'Count': count_list,
                'First Result': first_result_list
            }
        )
        wp_information.to_csv('first_feature.csv', encoding="utf-8")
    print('1st feature CSV is outputted')
def second_feature():
    filter_word = input('Input keyword: ')
    filter_word_length = len(filter_word)
    df =pd.read_excel('urls-list.xlsx')
    link_list = []
    count_list = []
    first_result_list = []
    keyword_list = []
    links = df['website_link']
    order = 0
    for each_link in links:
        filter_link = str(each_link).split('://')
        filter_url = filter_link[1]
        if filter_url[-1] == '/' and filter_word[0] =='/':
           filter = filter_url + filter_word[1:]
        if filter_url[-1] == '/' and filter_word[0] !='/':
            filter = filter_url + filter_word
        if filter_url[-1] != '/' and filter_word[0] =='/':
            filter = filter_url + filter_word
        if filter_url[-1] != '/' and filter_word[0] != '/':
            filter = filter_url +'/'+ filter_word
        keyword_list.append(filter)
        filter_length = len(filter)
        order = order + 1
        print('%s' % order + ' being sent to scraper')
        link_list.append(each_link)
        driver = init_driver()
        driver.get(each_link)
        try:
            soup = driver.page_source
            # counting the numbers
            real_count = 0
            for i in range(0, len(str(soup)) - filter_length):
                if soup[i:i + filter_length] == filter:
                    real_count = real_count + 1
            if real_count == 0:
                first_result_list.append('no result')
            count_list.append(real_count)
            # finding the first result
            soup_list = str(soup).split('>')
            count = 0
            for each_soup in soup_list:
                length = len(each_soup)
                for i in range(0, length - filter_length):
                    if each_soup[i:i + filter_length] == filter:
                        count = count + 1
                        if count == 1:
                            first_result = str(each_soup + '>').strip()
                            first_result_list.append(first_result)
        except:
            count_list.append('error')
            first_result_list.append('error')
        driver.close()
        wp_information = pd.DataFrame(
            {
                "Two_Keywords": keyword_list,
                'Website Url': link_list,
                'Count': count_list,
                'First Result': first_result_list
            }
        )
        wp_information.to_csv('second_feature.csv', encoding="utf-8")
    print('2th feature csv is outputted')

def third_feature():
    filter_word = input('Input first keyword: ')
    second_filter_word = input('Input second keyword: ')
    filter_word_length = len(filter_word)
    second_filter_word_length = len(second_filter_word)
    df = pd.read_excel('urls-list.xlsx')
    link_list = []
    count_list = []
    middle_result_list = []
    final_result_list = []
    first_keyword_list = []
    second_keyword_list = []
    links = df['website_link']
    order = 0
    for each_link in links:
        middle_result_list = []
        filter_link = str(each_link).split('://')
        filter_url = filter_link[1]
        if filter_url[-1] == '/' and filter_word[0] == '/':
           filter = filter_url + filter_word[1:]
        if filter_url[-1] == '/' and filter_word[0] != '/':
            filter = filter_url + filter_word
        if filter_url[-1] != '/' and filter_word[0] == '/':
            filter = filter_url + filter_word
        if filter_url[-1] != '/' and filter_word[0] != '/':
            filter = filter_url + '/' + filter_word
        first_keyword_list.append(filter)
        second_keyword_list.append(second_filter_word)
        filter_length = len(filter)
        order = order + 1
        print('%s' % order + ' being sent to scraper')
        link_list.append(each_link)
        driver = init_driver()
        driver.get(each_link)
        try:
            soup = driver.page_source
            # counting the numbers
            soup_list = str(soup).split('>')
            for each_soup in soup_list:
                length = len(each_soup)
                for i in range(0, length - filter_length):
                    if each_soup[i:i + filter_length] == filter:
                        middle_result = str(each_soup + '>').strip()
                        middle_result_list.append(middle_result)
            count = 0
            for each_middle_soup in middle_result_list:
                middle_length = len(each_middle_soup)
                for i in range(0, middle_length - second_filter_word_length):
                    if each_middle_soup[i:i + second_filter_word_length] == second_filter_word:
                        count = count + 1
                        if count == 1:
                            final_result = str(each_middle_soup).strip()
                            print(final_result)
                            final_result_list.append(final_result)
            if count == 0:
                count_list.append('no result')
                final_result_list.append('no result')
            else:
                count_list.append(count)
        except :
            count_list.append('error')
            final_result_list.append('error')

        driver.close()
        wp_information = pd.DataFrame(
            {
                "First_Keywords": first_keyword_list,
                "Second keyword": second_keyword_list,
                'Website Url': link_list,
                'Count': count_list,
                'First Result': final_result_list
            }
        )
        wp_information.to_csv('third_feature..csv', encoding="utf-8")

    print('3th feature csv is outputted')

if __name__== "__main__":
   feature_number = input('Input feature number: ')
   if feature_number == '1':
       first_feature()
   elif  feature_number == '2':
       second_feature()
   elif feature_number == '3':
       third_feature()
   else:
       print('please input number correctly (1,2,3)')