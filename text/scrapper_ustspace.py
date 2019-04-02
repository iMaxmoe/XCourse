import spider
import click
import atexit

atexit.register(spider.quit)

course_list_comp = {
    '1001','1021','1022p','1022q','1029a','1029c','1029j','1029p','1029v','1941',
    '1942','2011','2012','2012h','2021','2521','2611','2711','2711h','3021','3031',
    '3111','3111h','3211','3311','3511','3632','3711','3711h','3721','4021','4211',
    '4221','4311','4331','4332','4411','4421','4431','4441','4451','4511','4521',
    '4621','4631','4632','4651','4900'
}   #have filtered those without comments

course_list_ceng = {
	'1000', '1500', '1600', '1700', '1800', '2110', '2210', '2220','3230', '4130',
	'4620', '4710', '5210'
} 

course_list_civl= {
	'1100', '1140', '1160', '1170', '2020', '2110', '2120', '2150', '2160', '2170',
	'2410', '2510', '2810', '3310', '3320', '3510', '4470', '4620', '4700', '4750'
}

course_list_elec= {
	'1010', '1020', '1100', '1200', '2100', '2100H', '2200', '2300', '2400', '2420',
	'2600', '2600H', '3100', '3200', '3300', '3400', '3500'
}

course_list_engg = {
	'1010', '1100', '1110', '1130', '1150', '1200', '2010', '2990D'
}

course_list_ielm = {
	'2010', '2150', '2200', '2510', '3010', '3130', '3150', '3300', '3330', '4200',
	'4320', '4410'
}

course_list_mech = {
	'1901', '1902', '1905', '1906', '1907', '2020', '2040', '2210', '2310', '2410',
	'2520', '3030', '3300', '3310', '3420', '3520', '3610', '3630','3640', '3650',
	'3830', '4000F'
}

course_list_chem = {
	'1002', '1004', '1010', '1020', '1030', '1050', '1055', '2110', '2210', '2310',
	'2311', '2410', '3120', '3220', '3320', '3420', '4320', 
}

course_list_envs = {
	'2001', '3003'
}

course_list_lifs = {
	'1010', '1020', '1030', '1901', '1902', '1903', '1904', '1930', '2010', '2040',
	'2060', '2070', '2080', '2210', '2220', '2280', '2720', '3010', '3040', '3060',
	'3070', '3110', '3130', '3140', '3150', '3160', '3260', '3330', '4150', '4200',
	'4370', '4580', '4760', '4950'
}

course_list_math = {
	'1003', '1012', '1013', '1014', '1020', '1023', '1024', '2011', '2023', '2033',
	'2111', '2121', '2131', '2343', '2350', '2351', '2352', '2411', '2421', '2511', 
	'2741', '3033', '3121', '3312', '3423', '4052', '4141', '4223', '4511'
}

course_list_phys = {
	'1001', '1002', '1003', '1006', '1111', '1112', '1113', '1114', '1312', '1314',
	'2022', '2023', '2080', '2124', '3032', '3033', '3034', '3036', '3037', '3040',
	'3053', '3071', '3142', '3153', '4050', '4051', '4058'
}

course_list_scie = {
	'1000', '1050', '1110', '1120', '1130', '1500', '2000'
}

course_list_hart = {
	'1001', '1012', '1013', '1017', '1018', '1020', '1027', '1030', '1032', '1036',
	'1039', '1040', '1041', '1045'
}

course_list_huma = {
	'1000', '1000A', '1000B', '1001', '1001A', '1010', '1020', '1030', '1060','1100',
	'1102', '1200', '1231', '1250', '1300', '1440', '1650', '1660', '1710', '1810', 
	'1811', '1920', '2010', '2031', '2050', '2103', '2050', '2103', '2104', '2105',
	'2210', '2320', '2400', '2420', '2430', '2589', '2590', '2633', '2660', '2670',
	'2680', '2830', '2840', '2921', '3000A', '3030', '3101', '3200', '3202', '3203',
	'3210', '3220', '3430', '3630', '3660', '3800', '3810', '4020'
}

course_list_sosc = {
	'1100', '1110', '1130', '1150', '1170', '1190', '1200', '1210', '1270', '1300',
	'1340', '1350', '1420', '1440', '1460', '1661', '1662', '1780', '1840', '1850',
	'1960', '1980', '2120', '2130', '2170', '2280', '2290', '2310', '2640', '2740',
	'2780', '2980', '3000C', '3120', '3130', '3240', '3520', '4260', '4290'
}

course_list_acct = {
	'1010', '2010', '2200', '3010', '3020', '3030', '3210', '3610', '3880', '4010',
	'4510'
}

course_list_econ = {
	'2103', '2113', '2123', '2174', '2310', '3014', '3024', '3113', '3123', '3143',
	'3334', '4124', '4284'
}

course_list_fina = {
	'1203', '1303', '2203', '2303', '3103', '3104', '3203', '3204', '3303', '3403',
	'3404', '3504', '4104', '4403', '4503'
}

course_list_isom = {
	'1090', '1380', '1500', '1700', '2010', '2030', '2310', '2400', '2500', '2700',	
	'3010', '3100', '3180', '3210', '3230', '3260', '3310', '3320', '3360', '3370',
	'3540', '3710', '3730', '3760', '4020', '4100', '4300', '4740', '4750', '4810',
	'4820'
}

course_list_mark = {
	'1220', '1230', '1330', '2120', '3220', '3410', '3420', '3430', '3470', '3510',
	'3520', '4290D', '4290E', '4450'
}

course_list_mgmt = {
	'1110', '1120', '1130', '2010', '2110', '2130', '3110', '3120', '3130', '3140',
	'3170', '4210', '4220', '4240'
}

course_list_sbmt = {
	'1111', '2010', '2020', '3300', '5010'
}

"""type_list_seng = {
	course_list_engg, course_list_comp, course_list_ceng, course_list_ielm,
	course_list_civl, course_list_mech
}

type_list_sci = {
	course_list_chem, course_list_math, course_list_phys, course_list_scie,
	course_list_envs, course_list_lifs
}

type_list_sbm = {
	course_list_acct, course_list_sbmt, course_list_mark, course_list_mgmt, 
	course_list_fina, course_list_econ, course_list_isom
}

type_list_shss = {
	course_list_huma, course_list_sosc, course_list_hart
}"""

spider.login(username, password)

grade_file_seng = open("seng_grade.txt","a",encoding= 'utf-8')
grade_file_sci = open("sci_grade.txt","a",encoding= 'utf-8')
grade_file_sbm = open("sbm_grade.txt","a",encoding= 'utf-8')
grade_file_shss = open("shss_grade.txt","a",encoding= 'utf-8')

def formatted_course_info(name, ratings):
    return '\n'.join(("",
                "Rating of {course}:",
                "Content:\t{0}",
                "Teaching:\t{1}",
                "Grading:\t{2}",
                "Workload:\t{3}",
                "")).format(*ratings, course=name)

"""comment_file_seng = open('seng.txt',"a",encoding= 'utf-8') 
comment_file_sbm = open('sbm.txt',"a",encoding= 'utf-8') 
comment_file_sci = open('sci.txt',"a",encoding= 'utf-8') 
comment_file_shss = open('shss.txt',"a",encoding= 'utf-8') 
"""


for course in course_list_comp:
    course = 'COMP'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_seng)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_seng.write(formatted_course_info(course, course_rating))
    grade_file_seng.write("\n")
    
for course in course_list_ceng:
    course = 'CENG'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_seng)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_seng.write(formatted_course_info(course, course_rating))
    grade_file_seng.write("\n")

for course in course_list_civl:
    course = 'civl'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_seng)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_seng.write(formatted_course_info(course, course_rating))
    grade_file_seng.write("\n")
    
for course in course_list_engg:
    course = 'ENGG'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_seng)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_seng.write(formatted_course_info(course, course_rating))
    grade_file_seng.write("\n")

for course in course_list_ielm:
    course = 'IELM'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_seng)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_seng.write(formatted_course_info(course, course_rating))
    grade_file_seng.write("\n")

for course in course_list_elec:
    course = 'ELEC'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_seng)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_seng.write(formatted_course_info(course, course_rating))
    grade_file_seng.write("\n")

for course in course_list_mech:
    course = 'MECH'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_seng)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_seng.write(formatted_course_info(course, course_rating))
    grade_file_seng.write("\n")

for course in course_list_chem:
    course = 'CHEM'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sci)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sci.write(formatted_course_info(course, course_rating))
    grade_file_sci.write("\n")

for course in course_list_envs:
    course = 'ENVS'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sci)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sci.write(formatted_course_info(course, course_rating))
    grade_file_sci.write("\n")

for course in course_list_lifs:
    course = 'LIFS'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sci)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sci.write(formatted_course_info(course, course_rating))
    grade_file_sci.write("\n")

for course in course_list_math:
    course = 'MATH'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sci)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sci.write(formatted_course_info(course, course_rating))
    grade_file_sci.write("\n")

for course in course_list_phys:
    course = 'PHYS'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sci)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sci.write(formatted_course_info(course, course_rating))
    grade_file_sci.write("\n")

for course in course_list_scie:
    course = 'SCIE'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sci)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sci.write(formatted_course_info(course, course_rating))
    grade_file_sci.write("\n")

for course in course_list_hart:
    course = 'HART'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_shss)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_shss.write(formatted_course_info(course, course_rating))
    grade_file_shss.write("\n")

for course in course_list_huma:
    course = 'HUMA'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_shss)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_shss.write(formatted_course_info(course, course_rating))
    grade_file_shss.write("\n")

for course in course_list_sosc:
    course = 'SOSC'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_shss)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_shss.write(formatted_course_info(course, course_rating))
    grade_file_shss.write("\n")

for course in course_list_acct:
    course = 'ACCT'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sbm)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sbm.write(formatted_course_info(course, course_rating))
    grade_file_sbm.write("\n")

for course in course_list_isom:
    course = 'ISOM'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sbm)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sbm.write(formatted_course_info(course, course_rating))
    grade_file_sbm.write("\n")

for course in course_list_econ:
    course = 'ECON'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sbm)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sbm.write(formatted_course_info(course, course_rating))
    grade_file_sbm.write("\n")

for course in course_list_fina:
    course = 'FINA'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sbm)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sbm.write(formatted_course_info(course, course_rating))
    grade_file_sbm.write("\n")

for course in course_list_mark:
    course = 'MARK'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sbm)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sbm.write(formatted_course_info(course, course_rating))
    grade_file_sbm.write("\n")

for course in course_list_sbmt:
    course = 'SBMT'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sbm)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sbm.write(formatted_course_info(course, course_rating))
    grade_file_sbm.write("\n")

for course in course_list_mgmt:
    course = 'MGMT'+course.upper()
    overall_soup, has_full_access = spider.request_review_page_soup(course)
    #spider.write_comment(overall_soup,comment_file_sbm)
    course_rating = spider.get_course_rating(overall_soup)
    grade_file_sbm.write(formatted_course_info(course, course_rating))
    grade_file_sbm.write("\n")

"""comment_file_seng.close()
comment_file_sci.close()
comment_file_shss.close()
comment_file_sbm.close()"""
    
grade_file_seng.close()
grade_file_sci.close()
grade_file_shss.close()
grade_file_sbm.close()
   
