# import re
#
# pattern = r"^(19|20)\d\d([- /.])(0[1-9]|1[012])\2(0[1-9]|[12][0-9]|3[01])$"
#
# A = ["2003-12-11", "192,168.0.3", "***", "abc"]
# for i in A:
#     result = re.match(pattern, i, re.IGNORECASE)
#     if result:
#         print("Search successful")
#     else:
#         print("Search unsuccessful")



import re

pattern = r"(18|19|20|21|22|23)(.*864|.*806)\d{5}$"
A=["1986400330","2180625555","1780622033"]
for mssv in A:
    result = re.match(pattern, mssv)

    if result:
        print("Search successful")
    else:
        print("Search unsuccessful")


