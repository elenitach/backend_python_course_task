from bs4 import BeautifulSoup
import re
import requests


# получаем коды регионов регистации путем парсинга веб-страницы
def get_regions_codes():
    url = 'https://ru.wikipedia.org/wiki/Регистрационные_знаки_транспортных_средств_в_России'
    resp = requests.get(url)
    page = resp.text
    soup = BeautifulSoup(page, 'lxml')
    table = soup.find_all('table')[3].tbody
    cells_content = []
    for row in table.find_all('tr')[1:-1]:
        cells_content.extend(row.td.b.text.split(','))
    codes = []
    for cell in cells_content:
        code = re.sub(r'\[.+\]', '', cell)
        code = re.sub(r'[^\d]', '', code)
        codes.append(code)
    return codes


# проверка валидности регистрационного знака
# валидный формат = цифра + 3 буквы из списка + 2 цифры + код региона из списка
def is_valid(sign, reg_series_letters, reg_numbers, regions_codes):
    return all(sign[i] in reg_series_letters for i in [0, 4, 5]) \
           and all(sign[i] in reg_numbers for i in [1, 2, 3]) \
           and sign[6:] in regions_codes


def solve():
    # regions_codes = get_regions_codes()
    # сохраним полученные коды
    regions_codes = ['01', '02', '102', '702', '03', '04', '05', '06', '07', '08',
                     '09', '10', '11', '12', '13', '113', '14', '15', '16', '116',
                     '716', '17', '18', '19', '21', '121', '22', '122', '23', '93',
                     '123', '193', '24', '84', '88', '124', '25', '125', '26', '126',
                     '27', '28', '29', '30', '31', '32', '33', '34', '134', '35', '36',
                     '136', '37', '38', '85', '138', '39', '91', '40', '41', '82', '42',
                     '142', '43', '44', '45', '46', '47', '147', '48', '49', '50', '90',
                     '150', '190', '750', '790', '51', '52', '152', '53', '54', '154', '55',
                     '56', '156', '57', '58', '59', '81', '159', '60', '61', '161', '761', '62',
                     '63', '163', '763', '64', '164', '65', '66', '96', '196', '67', '68', '69',
                     '70', '71', '72', '73', '173', '74', '174', '774', '75', '80', '76', '77',
                     '97', '99', '177', '197', '199', '777', '78', '98', '178', '79', '82', '83',
                     '86', '186', '87', '89', '92', '94', '20', '95']

    # латинские и кириллические символы, используемые для записи серии
    reg_series_letters = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х',
                          'A', 'B', 'E', 'K', 'M', 'H', 'O', 'P', 'C', 'T', 'Y', 'X']
    # набор цифр, используемый для регистрационного номера
    reg_numbers = [str(num) for num in range(10)]

    # список знаков для проверки
    reg_signs_list = [
        "A123AA11",
        "А222АА123",
        "A12AA123",
        "A123CC1234",
        "AA123A12",
        "G122TT01",
        "Г444НН11",
        "Н146ШШ45",
        "A546OQ46"
        "ААА56778",
        "12345678",
        "Р146ОО2",
        "Е098ТТ25",
        "У567ЕА777",
        "С394ХО190",
        "К520ВВ02"
    ]

    valid_signs = list(filter(lambda x: is_valid(x, reg_series_letters, reg_numbers, regions_codes), reg_signs_list))
    print(valid_signs)


if __name__ == '__main__':
    solve()
