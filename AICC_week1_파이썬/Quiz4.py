names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
print(names)
print(type(names))

# Ans.2
print(names.count("이재영"))
name_list = names.split(",")
print(name_list)

# Ans.3
uniq_name = list(set(name_list))
print(uniq_name)

# Ans.4
print("정렬")
uniq_name.sort()
print(uniq_name)

# Ans.1
print(names.count("이"))
print(name_list[0][0])
sung = []
for i in name_list:
    #print(i[0])
    sung.append(i[0])
print(sung)
print("김씨 인원 :", sung.count("김"))
print("이씨 인원 :", sung.count("이"))