"""
data.txt faylını oxuyun və məlumatları dict-də saxlayın və dict-i print edin.
Ad key, qalan melumatlar ise key: value sheklinde hemin key-in altinda olmalidir

Print edilən dict belə görünməlidir:
{
    'Farhad': {
        'yaş': 25,
        'şəhər': 'Bakı'
    },
    'Aygün': {
        'yaş': 30,
        'şəhər': 'Gəncə'
    },
    'Murad': {
        'yaş': 22,
        'şəhər': 'Sumqayıt'
    },
    'Zəhra': {
        'yaş': 28,
        'şəhər': 'Naxçıvan'
    }
}
"""

with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

headers = lines[0].strip().split(", ")

print(headers)

data = {}
for line in lines[1:]:
    values = line.strip().split(", ")
    ad = values[0]
    data[ad] = {
        headers[1]: int(values[1]),
        headers[2]: values[2]
    }

print(data)