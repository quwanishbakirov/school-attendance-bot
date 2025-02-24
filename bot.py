import asyncio
import requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

allowed_users = {
    627323197,
    397917674,
    1252374577,
    697721362,
    683398043,
    350903115,
    728439868,
    807324500,
    526069424,
    552748332,
    627184876,
    595290440,
    1970808374,
    5519477078,
    658761788,
    890365625,
    547827399,
    1178154284,
    572545005,
    538617925,
    1877264435,
    879673877,
    1341260641,
    1171480740,
    1031689949,
    606079734,
    890982781,
    920251526,
    862199308,
    668108270,
    1798974368,
    924259718,
    6731977483,
    714827415,
    204258436,
    236734254,
    780773600,
    588334573,
    525950622,
    630157076,
    320542707,
    329859361,
    848368265,
    1039280110,
    327288019,
    6343400326,
    6901726739,
    377040542,
    1064466543,
    685415424,
}

# Statik talaba va fanlar ma'lumotlari
subjects = [
    {"subject_id": 1, "name": "Qaraqalpaqstan tarıyxı"},
    {"subject_id": 2, "name": "Tarıyx"},
    {"subject_id": 3, "name": "JSHSHBT"},
    {"subject_id": 4, "name": "Tárbiya"},
    {"subject_id": 5, "name": "Informatika"},
    {"subject_id": 6, "name": "Tábiyiy pánler"},
    {"subject_id": 7, "name": "Geografıya"},
    {"subject_id": 8, "name": "Dene tárbiya"},
    {"subject_id": 9, "name": "Art"},
    {"subject_id": 11, "name": "Texnologıya"},
    {"subject_id": 12, "name": "Matematika"},
    {"subject_id": 13, "name": "Algebra"},
    {"subject_id": 14, "name": "Geometriya"},
    {"subject_id": 15, "name": "Fizika"},
    {"subject_id": 16, "name": "Biologiya"},
    {"subject_id": 17, "name": "Ximiya"},
    {"subject_id": 18, "name": "Inglis tili"},
    {"subject_id": 19, "name": "Ózbekstan tarıyxı"},
    {"subject_id": 20, "name": "Jáhán tarıyxı"},
    {"subject_id": 21, "name": "Tarıyxtan hikayalar"},
    {"subject_id": 22, "name": "Ózbek tili(Davlat tili)"},
    {"subject_id": 23, "name": "Rus tili"},
    {"subject_id": 24, "name": "Ádebiyat"},
    {"subject_id": 24, "name": "Ana tili"}
]

students = [
    {'id': 2, 'full_name': 'AYPOLATOV RAMZAN JALGASOVICH', 'class': '5 - A'},
    {'id': 3, 'full_name': 'USERBAYEV BUNYODBEK BAYRAMBAY ULI', 'class': '5 - A'},
    {'id': 4, 'full_name': 'DAUILBAEV JASUR MAXMUDOVICH', 'class': '5 - A'},
    {'id': 5, 'full_name': 'SALAUATOVA GULAYIM SALAUATOVNA', 'class': '5 - A'},
    {'id': 6, 'full_name': 'JUMANIYAZOV ERDAWLET ATANIYAZOVICH', 'class': '5 - A'},
    {'id': 7, 'full_name': 'KAYIPNAZAROVA TUMARIS JUMAMBETOVNA', 'class': '5 - A'},
    {'id': 8, 'full_name': 'SAPARBAEVA NILUFAR ABILOVNA', 'class': '5 - A'},
    {'id': 9, 'full_name': 'RASBERGENOV ALISHER JIGEROVICH', 'class': '5 - A'},
    {'id': 10, 'full_name': 'MURATBAYEV ARMAN ROMANOVICH', 'class': '5 - A'},
    {'id': 11, 'full_name': 'ALIEVA NURZADA FARIDATDIN QIZI', 'class': '5 - A'},
    {'id': 12, 'full_name': 'QULAMETOVA AYZADA AYMBETOVNA', 'class': '5 - A'},
    {'id': 13, 'full_name': 'AYTMURATOV DAWRANBEK SULTANBEKOVICH', 'class': '5 - A'},
    {'id': 14, 'full_name': 'ADILBAEV ALLAYAR MOYNAQOVICH', 'class': '5 - A'},
    {'id': 15, 'full_name': 'XOSHNIYAZOVA A?SIRGUL SABITOVNA', 'class': '5 - A'},
    {'id': 16, 'full_name': 'MARATOV ARSLAN PARAXATOVICH', 'class': '5 - A'},
    {'id': 17, 'full_name': 'MAXSETBAEV MUSABEK SULTANBEKOVICH', 'class': '5 - A'},
    {'id': 18, 'full_name': 'POLATOV DANIYAR SADIQOVICH', 'class': '5 - A'},
    {'id': 19, 'full_name': 'ESEMURATOV ALPAMIS KEUNIMJAEVICH', 'class': '5 - A'},
    {'id': 20, 'full_name': 'BAZARBAEV MIYIRBEK SULTANBAY ULI', 'class': '5 - A'},
    {'id': 21, 'full_name': 'WORALBAEV NAWRIZBAY MEDEUBAEVICH', 'class': '5 - B'},
    {'id': 22, 'full_name': 'SHARAPOV AZAMAT AYBEKOVICH', 'class': '5 - B'},
    {'id': 23, 'full_name': 'JANGABAEVA RAYHAN UMIRBAYEVNA', 'class': '5 - B'},
    {'id': 24, 'full_name': 'SHARAPOV KARAMAT SALAMAT ULI', 'class': '5 - B'},
    {'id': 25, 'full_name': 'XOJANIYAZOV NURLAN NURNIYAZOVICH', 'class': '5 - B'},
    {'id': 26, 'full_name': 'KENESBAEV QIYAS RUSTEM ULI?', 'class': '5 - B'},
    {'id': 27, 'full_name': 'ALLAMBERGENOVA ARZAYIM TURSINBAEVNA', 'class': '5 - B'},
    {'id': 28, 'full_name': 'KEUNIMJAEVA SOFIYA QONISBAEVNA', 'class': '5 - B'},
    {'id': 29, 'full_name': 'BAZARBAEV NURDAULET SADATDINOVICH', 'class': '5 - B'},
    {'id': 30, 'full_name': 'UTEMURATOVA FATIMA ISLAMBEKOVNA', 'class': '5 - B'},
    {'id': 31, 'full_name': 'KARLIBAEV TALGAT ABATOVICH', 'class': '5 - B'},
    {'id': 32, 'full_name': 'DJUBATKANOV ALIBEK NURDAULETOVICH', 'class': '5 - B'},
    {'id': 33, 'full_name': 'XODJANIYAZOV SARDORBEK SADULLAEVICH', 'class': '5 - B'},
    {'id': 34, 'full_name': 'JANABAEV DAULETNIYAZ DAULETMURADOVICH', 'class': '5 - B'},
    {'id': 35, 'full_name': 'JUMANAZAROVA LILIYA BAXI?TBAEVNA', 'class': '5 - B'},
    {'id': 36, 'full_name': 'ADAM YOUSIF OMAR KHALID', 'class': '5 - B'},
    {'id': 37, 'full_name': 'KENJEBAEVA AYZADA AZIZOVNA', 'class': '5 - B'},
    {'id': 38, 'full_name': 'YUSUPBAEV FARRUXJON JAMILJANOVICH', 'class': '5 - B'},
    {'id': 39, 'full_name': 'WONGARBAEV YERKEBULAN YERBOL ULI', 'class': '5 - B'},
    {'id': 40, 'full_name': 'URAZBAEV RUSLAN SHAVKATOVICH', 'class': '5 - B'},
    {'id': 41, 'full_name': 'ABDIMURATOV AYDOS RAXATOVICH', 'class': '5 - B'},
    {'id': 42, 'full_name': 'NURJANOV NURDAWLET BERDAX ULI', 'class': '5 - B'},
    {'id': 43, 'full_name': 'JUMABAEV ADILBEK RUSLANOVICH', 'class': '5 - B'},
    {'id': 44, 'full_name': 'MAXAMATULLAEVA TUMARIS POLATOVNA', 'class': '5 - B'},
    {'id': 45, 'full_name': 'SABIRBAEVA ALBINA AMANKELDIEVNA', 'class': '5 - C'},
    {'id': 46, 'full_name': 'MAXMUDJONOV IBROHIM JAXONGIROVICH', 'class': '5 - C'},
    {'id': 47, 'full_name': 'MAXSETBAEV DIANAT MANSUR ULI', 'class': '5 - C'},
    {'id': 48, 'full_name': 'XALILLAYEV MUSTOFO INAMJON OGLI', 'class': '5 - C'},
    {'id': 49, 'full_name': 'JOLDASBAYEV SHAXMIRZA AZIRBAYEVICH', 'class': '5 - C'},
    {'id': 50, 'full_name': 'TILEPBAEV ARTUR SALAVATOVICH', 'class': '5 - C'},
    {'id': 51, 'full_name': 'QAYPNIYAZOV SIRLIBEK BERDAXOVICH', 'class': '5 - C'},
    {'id': 52, 'full_name': 'BEKIMBETOV ATABEK FARXADOVICH', 'class': '5 - C'},
    {'id': 53, 'full_name': 'ISMAILOV SHAHRIYOR NURBEK O?G?LI', 'class': '5 - C'},
    {'id': 54, 'full_name': 'XODJAMETOVA XURLIMAN KUATBAEVNA', 'class': '5 - C'},
    {'id': 55, 'full_name': 'ABDULLAYEVA SUNBUL SHERZOD QIZI', 'class': '5 - C'},
    {'id': 56, 'full_name': 'UTEMURATOVA UMIDA BAXTIBAY QIZI', 'class': '5 - C'},
    {'id': 57, 'full_name': 'SAPAROV XURSHID KUMEKBAY ULI', 'class': '5 - C'},
    {'id': 58, 'full_name': 'YAKUPBAEVA NILUFAR ANVAROVNA', 'class': '5 - C'},
    {'id': 59, 'full_name': 'JAKSIBAEV YERNAR AMANKELDIEVICH', 'class': '5 - C'},
    {'id': 60, 'full_name': 'PERDEBAYEV ILXAM KUTLIMURAT ULI', 'class': '5 - C'},
    {'id': 61, 'full_name': 'XO?JAMURODOVA DAJONA OTAJON QIZI', 'class': '5 - C'},
    {'id': 62, 'full_name': 'NURGALIEVA NURJAMAL RASULOVNA', 'class': '5 - C'},
    {'id': 63, 'full_name': 'NAZARBAEVA NILUFAR AYBEK QIZI', 'class': '5 - C'},
    {'id': 64, 'full_name': 'SAGIDULLAEV YERNAZAR MARATOVICH', 'class': '5 - C'},
    {'id': 65, 'full_name': 'SULTANBAYEV DIYORBEK DILMURAD O?G?LI', 'class': '5 - C'},
    {'id': 66, 'full_name': 'ABILLAYEV SAYID ZAFAR O?G?LI', 'class': '5 - C'},
    {'id': 67, 'full_name': 'KOSHAYEV IQLASBEK MAXSET O?G?LI', 'class': '5 - C'},
    {'id': 68, 'full_name': 'BEKIMBETOV SULAYMAN NASIROVICH', 'class': '6 - A'},
    {'id': 69, 'full_name': 'ATABAYEV SARDORBEK MAKSETBAYEVICH', 'class': '6 - A'},
    {'id': 70, 'full_name': 'NURMUXANBETOV YERASIL RAXAT ULI', 'class': '6 - A'},
    {'id': 71, 'full_name': 'KALLIBEKOVA BEGZADA ATABEKOVNA', 'class': '6 - A'},
    {'id': 72, 'full_name': 'Joldasbaeva Jasmina Jalgasovna', 'class': '6 - A'},
    {'id': 73, 'full_name': 'KALIBAYEV AJINIYAZ BATIRBAYEVICH', 'class': '6 - A'},
    {'id': 74, 'full_name': 'ODILJONOV MAHMUD AKMAL O?G?LI', 'class': '6 - A'},
    {'id': 75, 'full_name': 'YUSUPOVA AYDANA TIMUROVNA', 'class': '6 - A'},
    {'id': 76, 'full_name': 'JANABAYEV BEGZAD AZAMAT ULI', 'class': '6 - A'},
    {'id': 77, 'full_name': 'JOLDASBAYEV AZIZBEK ALISHER ULI', 'class': '6 - A'},
    {'id': 78, 'full_name': 'KURBANBOYEV RAHMATJON OMONBOY O?G?LI', 'class': '6 - A'},
    {'id': 79, 'full_name': 'NIYETULLAYEVA ZARAFSHAN ADILBEKOVNA', 'class': '6 - A'},
    {'id': 80, 'full_name': 'ALLAMBERGENOV AYDOSBIY AZAMATOVICH', 'class': '6 - A'},
    {'id': 81, 'full_name': 'Kerimbaeva Barshinay Berdaxovna', 'class': '6 - A'},
    {'id': 82, 'full_name': 'YESHMURATOV ISLAMJAN MUXAMMEDJANOVICH', 'class': '6 - A'},
    {'id': 83, 'full_name': 'Maxsetbaeva Aseliya Timurovna', 'class': '6 - A'},
    {'id': 84, 'full_name': 'JUMABAYEV KAMAL BAXITBAYEVICH', 'class': '6 - A'},
    {'id': 85, 'full_name': 'POLATBEKOV BEKSULTAN RAXAT ULI', 'class': '6 - A'},
    {'id': 86, 'full_name': 'JOLMURZAYEVA AISULIU NURLIBAY KIZI', 'class': '6 - A'},
    {'id': 87, 'full_name': 'RAXIMOV ELDORBEK AZIZBEKOVICH', 'class': '6 - A'},
    {'id': 88, 'full_name': 'DARYABAYEVA ZARINA NIYETBAYEVNA', 'class': '6 - A'},
    {'id': 89, 'full_name': 'ATAMURATOV BEXRUZBEK SAFARBOYEVICH', 'class': '6 - A'},
    {'id': 90, 'full_name': 'ALPAMISOV TEMUR AZAMAT ULI', 'class': '6 - A'},
    {'id': 91, 'full_name': 'MEDETBAYEVA TUMARIS DAULETBAYEVNA', 'class': '6 - A'},
    {'id': 92, 'full_name': 'MAXSETOV DAMIR TIMUR ULI', 'class': '6 - B'},
    {'id': 93, 'full_name': 'ABDULLAYEVA PERIZAD MADIYAROVNA', 'class': '6 - B'},
    {'id': 94, 'full_name': 'JAKSILIKOVA BIYBINUR ULUGBEKOVNA', 'class': '6 - B'},
    {'id': 95, 'full_name': 'OSERBAYEVA NARGIZA GAYRATDINOVNA', 'class': '6 - B'},
    {'id': 96, 'full_name': 'SABIROV FARXAD ISMATOVICH', 'class': '6 - B'},
    {'id': 97, 'full_name': 'BAZARBAYEV JANDARBEK AZAMATOVICH', 'class': '6 - B'},
    {'id': 98, 'full_name': 'YULDASHEV JURATBEK JASURBEK OGLI', 'class': '6 - B'},
    {'id': 99, 'full_name': 'RISBAYEVA JANNUR RINATOVNA', 'class': '6 - B'},
    {'id': 100, 'full_name': 'NAZAROVA OYNISA UTKIRBEKOVNA', 'class': '6 - B'},
    {'id': 101, 'full_name': 'DAMIROVA MARJONA FAXRIDDINOVNA', 'class': '6 - B'},
    {'id': 102, 'full_name': 'TOREBAYEV MIYRASBEK MAXSETOVICH', 'class': '6 - B'},
    {'id': 103, 'full_name': 'JOLDASBAYEV BEKZAT GAMZAT ULI', 'class': '6 - B'},
    {'id': 104, 'full_name': 'PARAXATDINOV AZIZBEK MUXTAR ULI', 'class': '6 - B'},
    {'id': 105, 'full_name': 'KOMEKBAYEVA ELINA ELDAROVNA', 'class': '6 - B'},
    {'id': 106, 'full_name': 'MURATBAYEVA NURZADA PIYSHENBAYEVNA', 'class': '6 - B'},
    {'id': 107, 'full_name': 'REYMBAYEV BOBUR SHARAFATOVICH', 'class': '6 - B'},
    {'id': 108, 'full_name': 'ISMAYLOV AYDOS JUZIMBETOVICH', 'class': '6 - B'},
    {'id': 109, 'full_name': 'ABDUKADIROV ABBOS ABDUVAXID UGLI', 'class': '6 - B'},
    {'id': 110, 'full_name': "TURSUNOV MASHXURBEK ELDOR O'G'LI", 'class': '6 - B'},
    {'id': 111, 'full_name': 'JUZBAYEV AYBEK ABATBAYEVICH', 'class': '6 - B'},
    {'id': 112, 'full_name': 'KIDIRBAYEVA MIYASSAR JALGASBAYEVNA', 'class': '6 - B'},
    {'id': 113, 'full_name': 'SAFARBAYEV BAXADIR MAJITOVICH', 'class': '6 - B'},
    {'id': 114, 'full_name': 'ILALATDINOVA DINARA BAXADIR KIZI', 'class': '6 - B'},
    {'id': 115, 'full_name': 'DAULETBAEV ISLAM SALAUATOVICH', 'class': '6 - B'},
    {'id': 116, 'full_name': 'SAPARBAYEV AZIZBEK BERDAX ULI', 'class': '6 - C'},
    {'id': 117, 'full_name': 'KAZAXBAYEVA MAYRA KURALBAYEVNA', 'class': '6 - C'},
    {'id': 118, 'full_name': 'TOREMURATOV MURAT MIRAS ULI', 'class': '6 - C'},
    {'id': 119, 'full_name': 'POLATOV AZIZBEK ZAMIROVICH', 'class': '6 - C'},
    {'id': 120, 'full_name': 'NAJIMATDINOV JASURBEK RUSTEM ULI', 'class': '6 - C'},
    {'id': 121, 'full_name': 'ABATBAYEVA SARBINAZ PARAXATOVNA', 'class': '6 - C'},
    {'id': 122, 'full_name': 'OTEPOV BAXITBEK BAZARBAY ULI', 'class': '6 - C'},
    {'id': 123, 'full_name': 'XALBAYEV TANER MANSURBEK ULI', 'class': '6 - C'},
    {'id': 124, 'full_name': 'TURSIMURATOVA VENERA SULAIMAN KIZI', 'class': '6 - C'},
    {'id': 125, 'full_name': 'POLATOV DAULETYAR SADIKOVICH', 'class': '6 - C'},
    {'id': 126, 'full_name': 'JOLDASBAYEVA AYNURA RAXAT QIZI', 'class': '6 - C'},
    {'id': 127, 'full_name': 'NAJIMOV UMAR YERNAZAROVICH', 'class': '6 - C'},
    {'id': 128, 'full_name': 'BEKBAYEVA XAMIDA RINAT KIZI', 'class': '6 - C'},
    {'id': 129, 'full_name': 'AXMETJANOV ZUXRITDIN SRAJATDIN ULI', 'class': '6 - C'},
    {'id': 130, 'full_name': 'AYTBAYEV DAULET IBRAYIM ULI', 'class': '6 - C'},
    {'id': 131, 'full_name': 'SULTANBAYEVA MEXRIBANU SULTANBAYEVNA', 'class': '6 - C'},
    {'id': 132, 'full_name': 'ASHIMOV DAMIR MAXSUDOVICH', 'class': '6 - C'},
    {'id': 133, 'full_name': 'KARIMBAYEV RAXIMBAY POLATBAYEVICH', 'class': '6 - C'},
    {'id': 134, 'full_name': 'DJUMAMURATOV ARSLANBEK G?AFUROVICH', 'class': '6 - C'},
    {'id': 135, 'full_name': 'ABATBAYEV SULTANBEK DARYABAY ULI', 'class': '6 - C'},
    {'id': 136, 'full_name': 'SANETULLAYEV ALISHER SALAMAT ULI', 'class': '6 - C'},
    {'id': 137, 'full_name': 'UTENAZAROVA SHAXRIZADA REYPNAZAROVNA', 'class': '6 - C'},
    {'id': 138, 'full_name': 'RUSTAMOV BOTIRJON MANSURBEK G?O?LI', 'class': '6 - C'},
    {'id': 139, 'full_name': 'SAFARBAYEV MUXAMMADALI G?AYRAT O?G?LI', 'class': '6 - C'},
    {'id': 140, 'full_name': 'JAMIYEV AZIM BAXTIBAYEVICH', 'class': '7 - A'},
    {'id': 141, 'full_name': 'ADILBAEVA ZUBAYDA NURPOLAT QIZI', 'class': '7 - A'},
    {'id': 142, 'full_name': 'Alewatdinova Ayjamal Timur qizi', 'class': '7 - A'},
    {'id': 143, 'full_name': 'Sultansuynov Mirtimur Polatovich', 'class': '7 - A'},
    {'id': 144, 'full_name': 'Maxsetbaeva Gulfira Muratbay qizi', 'class': '7 - A'},
    {'id': 145, 'full_name': 'JOLDASBAYEVA PERIZAT AJINIYAZOVNA', 'class': '7 - A'},
    {'id': 146, 'full_name': 'Abilaev Abdimajit Jenisbaevich', 'class': '7 - A'},
    {'id': 147, 'full_name': 'ABUTALIPOVA GULAYIM ABUBAKIROVNA', 'class': '7 - A'},
    {'id': 148, 'full_name': 'ASHREPOV AZATBEK ADILBEK O?G?LI', 'class': '7 - A'},
    {'id': 149, 'full_name': 'BERDIBAYEV TORE XAMRAKULOVICH', 'class': '7 - A'},
    {'id': 150, 'full_name': 'RASULJONOVA MUNIBAXON HASANJON QIZI', 'class': '7 - A'},
    {'id': 151, 'full_name': 'JUMABAYEVA AYIDA YUSUPBAYEVNA', 'class': '7 - A'},
    {'id': 152, 'full_name': 'JADIGEROVA BIYBIASIYA DAURANBEKOVNA', 'class': '7 - A'},
    {'id': 153, 'full_name': 'SARSENBAYEVA JASMINA NOKUSBAYEVNA', 'class': '7 - A'},
    {'id': 154, 'full_name': 'ARALBAYEV BEXRUZ BAXTIYAROVICH', 'class': '7 - A'},
    {'id': 155, 'full_name': 'JUZBAYEVA DILFUZA NIYETBAYEVNA', 'class': '7 - A'},
    {'id': 156, 'full_name': 'ATAVULLAYEV BEHRUZBEK JURABEK O?G?LI', 'class': '7 - A'},
    {'id': 157, 'full_name': 'YERBOLGANOV XAMIT BAXTIBAYEVICH', 'class': '7 - A'},
    {'id': 158, 'full_name': 'KDIRBAYEVA JASMINA BAYRAMBAYEVNA', 'class': '7 - A'},
    {'id': 159, 'full_name': 'KAMALOV NODIRBEK HAMZA O?G?LI', 'class': '7 - A'},
    {'id': 160, 'full_name': 'MURATBAYEV NURSEYT AXMEDOVICH', 'class': '7 - A'},
    {'id': 161, 'full_name': "MADRIMOV ELYORBEK ZAFARJON O'G'LI", 'class': '7 - A'},
    {'id': 162, 'full_name': 'KALLIBEKOVA NAZLIMXAN TIMUROVNA', 'class': '7 - A'},
    {'id': 163, 'full_name': 'KALBAYEV AZIZBEK RAXATOVICH', 'class': '7 - A'},
    {'id': 164, 'full_name': 'ABIBULLAYEV YERASIL ABAYEVICH', 'class': '7 - B'},
    {'id': 165, 'full_name': 'SARSENBAYEV RINAT MOLDABAYEVICH', 'class': '7 - B'},
    {'id': 166, 'full_name': 'ARISTANBEKOVA BIYBINUR ASILBEKOVNA', 'class': '7 - B'},
    {'id': 167, 'full_name': 'XOJABAYEV BAXTIYAR BAYRAMBAYEVICH', 'class': '7 - B'},
    {'id': 168, 'full_name': 'KAIRATDINOV USNATDIN SALAUATOVICH', 'class': '7 - B'},
    {'id': 169, 'full_name': 'OMIRZAKOVA ALBINA SALAMATOVNA', 'class': '7 - B'},
    {'id': 170, 'full_name': 'SADIKOV XAKIMBEK SULTANBEKOVICH', 'class': '7 - B'},
    {'id': 171, 'full_name': 'NURKASINOV JASURBEK FAZILBEKOVICH', 'class': '7 - B'},
    {'id': 172, 'full_name': 'BAYMURATOVA BIYBISANEM JANIBEKOVNA', 'class': '7 - B'},
    {'id': 173, 'full_name': 'ORALBAYEVA SHAXNOZA DAMIROVNA', 'class': '7 - B'},
    {'id': 174, 'full_name': 'ABATBAYEV ALLAYAR ADILBAYEVICH', 'class': '7 - B'},
    {'id': 175, 'full_name': 'JUMANIYAZOVA NURJAMAL ORAZBAYEVNA', 'class': '7 - B'},
    {'id': 176, 'full_name': 'AZERBAYEV JASARBEK DAURANOVICH', 'class': '7 - B'},
    {'id': 177, 'full_name': 'BAYMURATOVA SHAXSANEM JANIBEKOVNA', 'class': '7 - B'},
    {'id': 178, 'full_name': 'Muratbaev Islambek Batirbekovich', 'class': '7 - B'},
    {'id': 179, 'full_name': 'Muratbaeva Jansuliw Salawat qizi', 'class': '7 - B'},
    {'id': 180, 'full_name': 'SHUKIRBAYEVA AYSANEM KEULIMJAYEVNA', 'class': '7 - B'},
    {'id': 181, 'full_name': 'AYMURATOV KALMURAT TILEUMURAT ULI', 'class': '7 - B'},
    {'id': 182, 'full_name': 'ADILBAYEVA GULCHEXRA TOREBAY KIZI', 'class': '7 - B'},
    {'id': 183, 'full_name': 'JOLDASBEKOVA SHAXZADA ARISLANBEKOVNA', 'class': '7 - B'},
    {'id': 184, 'full_name': 'MAQSETOV QAYRAT TEMUR ULI', 'class': '7 - B'},
    {'id': 185, 'full_name': 'Azilxanov Almat Raxat uli', 'class': '7 - B'},
    {'id': 186, 'full_name': 'ALLAMURATOV SALAMAT RASHIDOVICH', 'class': '7 - C'},
    {'id': 187, 'full_name': 'SHUKIRILLAYEVA GULMARJAN ZAFAR QIZI', 'class': '7 - C'},
    {'id': 188, 'full_name': 'OMIRZAKOV BABUR BAYRAMOVICH', 'class': '7 - C'},
    {'id': 189, 'full_name': 'URAZALIYEVA MAFTUNA ULUGBEK QIZI', 'class': '7 - C'},
    {'id': 190, 'full_name': 'KOMEKBAYEVA AYSANEM RASHID QIZI', 'class': '7 - C'},
    {'id': 191, 'full_name': 'TAXIROVA SEVINCH NURIDDIN QIZI', 'class': '7 - C'},
    {'id': 192, 'full_name': 'SARSENBAYEV KAMAL JUBANISHBAYEVICH', 'class': '7 - C'},
    {'id': 193, 'full_name': 'DJUMABAYEV YERNAZAR DOSNAZAR ULI', 'class': '7 - C'},
    {'id': 194, 'full_name': 'SULTANBAYEVA NILUFAR ALISHER QIZI', 'class': '7 - C'},
    {'id': 195, 'full_name': 'REYMOV NURLIBAY BARLIKBAYEVICH', 'class': '7 - C'},
    {'id': 196, 'full_name': 'GAYRATDINOV MIYRAS KONISBAY ULI', 'class': '7 - C'},
    {'id': 197, 'full_name': 'KIDIRBAYEVA XANSAYAT AJINIYAZ KIZI', 'class': '7 - C'},
    {'id': 198, 'full_name': 'MEXRIDINOV JA?FARJON ZUXRIDDIN O?G?LI', 'class': '7 - C'},
    {'id': 199, 'full_name': 'YAKUPBAYEV OXUNJON JASUR O?G?LI', 'class': '7 - C'},
    {'id': 200, 'full_name': 'LEPESBAYEVA MALIKA KOMEKBAY KIZI', 'class': '7 - C'},
    {'id': 201, 'full_name': 'BAZARBAYEVA KUMUSHBIBI MAXSETOVNA', 'class': '7 - C'},
    {'id': 202, 'full_name': 'SHUKURLAYEV DIYORBEK MARIMBAY O?G?LI', 'class': '7 - C'},
    {'id': 203, 'full_name': 'ABATBAYEVA ULDAULET BAXITBAY KIZI', 'class': '7 - C'},
    {'id': 204, 'full_name': 'KURBANIYAZOV TIMUR MANSUROVICH', 'class': '7 - C'},
    {'id': 205, 'full_name': 'CHORIYEV ASILBEK OTABEKOVICH', 'class': '7 - C'},
    {'id': 206, 'full_name': 'Orazova Xanbiybi Adilbaevna', 'class': '7 - C'},
    {'id': 207, 'full_name': 'Erniyazova Zulfiya Ajiniyazovna', 'class': '7 - C'},
    {'id': 208, 'full_name': 'POLATOV ALIBEK KAZBEK O?G?LI', 'class': '8 - A'},
    {'id': 209, 'full_name': 'Baxitiyarova Dilnoza Damir qizi', 'class': '8 - A'},
    {'id': 210, 'full_name': 'Ismailova Sabina Jamshid qizi', 'class': '8 - A'},
    {'id': 211, 'full_name': 'Abdimuratova Ariwxan Taumuratovna', 'class': '8 - A'},
    {'id': 212, 'full_name': 'JUMABOYEV MIRSAID IN?OMJON O?G?LI', 'class': '8 - A'},
    {'id': 213, 'full_name': 'UMIRBAYEV FARRUX FARXADOVICH', 'class': '8 - A'},
    {'id': 214, 'full_name': 'ABDURAXMANOV SAPARBEK BAXRAMOVICH', 'class': '8 - A'},
    {'id': 215, 'full_name': 'XOJANBERGENOV BAXBERGEN ONGARBAYEVICH', 'class': '8 - A'},
    {'id': 216, 'full_name': 'SARSENBAYEV ALISHER RUSLANOVICH', 'class': '8 - A'},
    {'id': 217, 'full_name': 'AZIMJANOV ASROR KAXRAMAN ULI', 'class': '8 - A'},
    {'id': 218, 'full_name': 'JIYEMURATOVA ZAYTUNA TURGANBAYEVNA', 'class': '8 - A'},
    {'id': 219, 'full_name': 'AMANIYAZOVA ASEM JENISOVNA', 'class': '8 - A'},
    {'id': 220, 'full_name': 'ARSLANOVA NAFISA AZAMATOVNA', 'class': '8 - A'},
    {'id': 221, 'full_name': 'OTEULIYEVA UG?ILAY REYMBAYEVNA', 'class': '8 - A'},
    {'id': 222, 'full_name': 'MADENBAYEV ALBERT BAYRAMBAYEVICH', 'class': '8 - A'},
    {'id': 223, 'full_name': 'BEKTURSINOV AZIZBEK ANSATBAY ULI', 'class': '8 - A'},
    {'id': 224, 'full_name': 'AYAPBERGENOV DAURAN BAHADIROVICH', 'class': '8 - A'},
    {'id': 225, 'full_name': 'TLEPOVA DINARA TAJIGALI QIZI', 'class': '8 - A'},
    {'id': 226, 'full_name': 'XALMURATOVA FERUZA MIRASOVNA', 'class': '8 - A'},
    {'id': 227, 'full_name': 'Sarsengalieva Aygerim Maksetovich', 'class': '8 - A'},
    {'id': 228, 'full_name': 'TEMIRBAYEVA SHIYRINGUL OMIRBAYEVNA', 'class': '8 - A'},
    {'id': 229, 'full_name': 'BISENBAYEV DAURANBEK ORALBAY ULI', 'class': '8 - A'},
    {'id': 230, 'full_name': 'JUMABAYEVA AIDANA RASHIDOVNA', 'class': '8 - A'},
    {'id': 231, 'full_name': "Polatov Almat Talg'at o'g'li", 'class': '8 - A'},
    {'id': 232, 'full_name': 'QUDAYBERGENOVA AYAULIM QIDIRBAY KIZI', 'class': '8 - B'},
    {'id': 233, 'full_name': 'Jullibayeva Shodiyona Davronbek qizi', 'class': '8 - B'},
    {'id': 234, 'full_name': 'NIYETULLAEVA ZULXUMAR QURALBEKOVNA', 'class': '8 - B'},
    {'id': 235, 'full_name': 'BEGDULLAEVA GULZADA AZAMATOVNA', 'class': '8 - B'},
    {'id': 236, 'full_name': 'TURSINBAYEVA DIANA BAYRAMBAYEVNA', 'class': '8 - B'},
    {'id': 237, 'full_name': 'ILYASOV ROMAN RUSLANOVICH', 'class': '8 - B'},
    {'id': 238, 'full_name': 'JAKSIBAYEVA DINARA MAXSET QIZI', 'class': '8 - B'},
    {'id': 239, 'full_name': 'MAXSETBAYEV MAXMUDJAN MUXAMMED ULI', 'class': '8 - B'},
    {'id': 240, 'full_name': 'ZARIPBAYEVA CHAROS MANSUROVNA', 'class': '8 - B'},
    {'id': 241, 'full_name': 'ERKINBAYEVA NODIRA AZAMATOVNA', 'class': '8 - B'},
    {'id': 242, 'full_name': 'KURALBAYEVA MOLDIR SHARAFATDIN QIZI', 'class': '8 - B'},
    {'id': 243, 'full_name': 'MARKABAYEVA AZIZA ALPISBAY KIZI', 'class': '8 - B'},
    {'id': 244, 'full_name': 'SARSENBAYEVA ALFIYA ONGARBAY KIZI', 'class': '8 - B'},
    {'id': 245, 'full_name': 'MURATBAYEVA GULSANEM ATABEKOVNA', 'class': '8 - B'},
    {'id': 246, 'full_name': 'SARSENBAYEVA GULKUMAR ZUXRAT KIZI', 'class': '8 - B'},
    {'id': 247, 'full_name': 'Tangatarova Dildora Genjebaevna', 'class': '8 - B'},
    {'id': 248, 'full_name': 'JANABAYEV SARDARBEK SALAMATOVICH', 'class': '8 - C'},
    {'id': 249, 'full_name': 'BORANBAYEVA GULDANA KONIRATBAY QIZI', 'class': '8 - C'},
    {'id': 250, 'full_name': 'IBODULLAYEV ASADBEK DAVRONBEK O?G?LI', 'class': '8 - C'},
    {'id': 251, 'full_name': 'TURGANBAYEV USMAN RASHIDOVICH', 'class': '8 - C'},
    {'id': 252, 'full_name': 'KALANDAROV BUNYODBEK RASHIDBEK O?G?LI', 'class': '8 - C'},
    {'id': 253, 'full_name': 'JAMGIRBAYEV ALEUATDIN JETKERBAY ULI', 'class': '8 - C'},
    {'id': 254, 'full_name': 'QUATBAYEV ARISLANBEK QUATBAY ULI', 'class': '8 - C'},
    {'id': 255, 'full_name': 'AYMURATOVA ALBINA BAXTIYAROVNA', 'class': '8 - C'},
    {'id': 256, 'full_name': 'XUDAYBERGENOV JAVLANBEK URAZBAY O?G?LI', 'class': '8 - C'},
    {'id': 257, 'full_name': 'AYAPBERGENOV KADIRBERGEN YERKINBAYEVICH', 'class': '8 - C'},
    {'id': 258, 'full_name': 'BABAJANOV JAVOHIR NEMATULLA O?G?LI', 'class': '8 - C'},
    {'id': 259, 'full_name': 'KUATBAYEV ARISLANBEK MURATBAY ULI', 'class': '8 - C'},
    {'id': 260, 'full_name': 'BAXTIYAROV ILYOSBEK O?TKIRBEK O?G?LI', 'class': '8 - C'},
    {'id': 261, 'full_name': 'ABDULLAYEVA SABRINA SABITBEK QIZI', 'class': '8 - C'},
    {'id': 262, 'full_name': 'Amanbaev Azizbek Baxadirovich', 'class': '8 - C'},
    {'id': 263, 'full_name': 'XAKIMBAYEVA KOMILA BAXTIYAROVNA', 'class': '8 - C'},
    {'id': 264, 'full_name': 'SARSENBAYEVA JASMINA RUSTAMOVNA', 'class': '8 - C'},
    {'id': 265, 'full_name': 'AZATOVA JULDIZ SALAVATOVNA', 'class': '8 - C'},
    {'id': 266, 'full_name': 'SHAMSHEDOVA AZIZA MAULENBERGENOVNA', 'class': '8 - C'},
    {'id': 267, 'full_name': 'Fayzullayeva Sugdiyona Davronbek kizi', 'class': '8 - C'},
    {'id': 268, 'full_name': 'Seytnazarova Sapura Hamirniyaz qizi', 'class': '8 - C'},
    {'id': 269, 'full_name': 'Ziynatdinova Ayziya Ruslan qizi', 'class': '8 - C'},
    {'id': 270, 'full_name': 'Orazxanova Xanzada Sharibay qizi', 'class': '8 - C'},
    {'id': 271, 'full_name': 'TILEUBAYEV DAULET SALAMATOVICH', 'class': '9 - A'},
    {'id': 272, 'full_name': 'JOLDASBAYEVA ANORA NURLAN QIZI', 'class': '9 - A'},
    {'id': 273, 'full_name': 'Nasiredinov Dawitbay Muratbay uli', 'class': '9 - A'},
    {'id': 274, 'full_name': 'Umirbekov Erhasil Iskender uli', 'class': '9 - A'},
    {'id': 275, 'full_name': 'GULIMBETOVA MIYASAR MAXSETBAYEVNA', 'class': '9 - A'},
    {'id': 276, 'full_name': 'YESIMBETOV BERDAK AMETBEKOVICH', 'class': '9 - A'},
    {'id': 277, 'full_name': 'Bektleuov Jandos Azamat uli', 'class': '9 - A'},
    {'id': 278, 'full_name': 'AJIMURATOVA DILNOZA AYTMURATOVNA', 'class': '9 - A'},
    {'id': 279, 'full_name': 'AYAPBERGENOV KARAMATDIN BAXITBERGENOVICH', 'class': '9 - A'},
    {'id': 280, 'full_name': 'Bazarbaeva Eleonora Azat qizi', 'class': '9 - A'},
    {'id': 281, 'full_name': 'TOLIBAYEVA GULSANEM KUANISHBAYEVNA', 'class': '9 - A'},
    {'id': 282, 'full_name': 'JOLDASBAYEV DANIYAR KALJANBAYEVICH', 'class': '9 - A'},
    {'id': 283, 'full_name': 'ALLAYAROVA ARAY SANDIBEKOVNA', 'class': '9 - A'},
    {'id': 284, 'full_name': 'KENGESHOVA MUNIRA SHAVKAT QIZI', 'class': '9 - A'},
    {'id': 285, 'full_name': 'ABUBAKIROV ABDIRASUL ABDIJAMILOVICH', 'class': '9 - A'},
    {'id': 286, 'full_name': 'BAXBERGENOVA SARBINAZ BEKBERGENOVNA', 'class': '9 - A'},
    {'id': 287, 'full_name': 'TILEPBAYEV AQILBEK MIRAS ULI', 'class': '9 - A'},
    {'id': 288, 'full_name': 'YESHIMBETOVA SHODIYONA MUZAFFAR KIZI', 'class': '9 - A'},
    {'id': 289, 'full_name': 'JUMABAYEVA RAYXAN JARASBAYEVNA', 'class': '9 - A'},
    {'id': 290, 'full_name': 'MADENBAYEVA SARAXAN MAMAN KIZI', 'class': '9 - A'},
    {'id': 291, 'full_name': 'ALIMBAYEVA NILUFAR ABATOVNA', 'class': '9 - A'},
    {'id': 292, 'full_name': "To'rebaev Qudaybergen Tolibaevich", 'class': '9 - A'},
    {'id': 293, 'full_name': "Po'latov Mirfayz Mansurjonovich", 'class': '9 - A'},
    {'id': 294, 'full_name': 'AZATBAYEV ADILBEK NURLIBEKOVICH', 'class': '9 - B'},
    {'id': 295, 'full_name': 'INYATOVA SEVARA KAXIRAMANOVNA', 'class': '9 - B'},
    {'id': 296, 'full_name': 'Ismetullaeva Dinara Genjebaevna', 'class': '9 - B'},
    {'id': 297, 'full_name': 'Kengesbaeva Ayjarqin Bayrambay qizi', 'class': '9 - B'},
    {'id': 298, 'full_name': 'JUMABAYEVA GULZADA KIDIRBAY QIZI', 'class': '9 - B'},
    {'id': 299, 'full_name': 'VALEREVA GULNAZ BERIK KIZI', 'class': '9 - B'},
    {'id': 300, 'full_name': 'Kenesbaev Kuwanish Azamatovich', 'class': '9 - B'},
    {'id': 301, 'full_name': 'KARIMBAYEVA MADINA MARDONBEK KIZI', 'class': '9 - B'},
    {'id': 302, 'full_name': 'Djamuratova Aziza Paraxat qizi', 'class': '9 - B'},
    {'id': 303, 'full_name': 'AYTMURATOVA BIYBINAZ KURBANBAYEVNA', 'class': '9 - B'},
    {'id': 304, 'full_name': 'USNATDINOVA AISANEM MIRAS QIZI', 'class': '9 - B'},
    {'id': 305, 'full_name': 'SARSENBAYEV MIYIRBEK ASILBEKOVICH', 'class': '9 - B'},
    {'id': 306, 'full_name': 'REYIMBAYEVA SEVINCH JAPPARBERGEN QIZI', 'class': '9 - B'},
    {'id': 307, 'full_name': 'MAVLENBERGENOVA ZEBINISO ILXOM KIZI', 'class': '9 - B'},
    {'id': 308, 'full_name': 'JANIBEKOV RASUL KABILBEK ULI', 'class': '9 - B'},
    {'id': 309, 'full_name': 'ASENOVA JAZIRA BOTIRBAY QIZI', 'class': '9 - B'},
    {'id': 310, 'full_name': 'MURODOVA MO??TABAR MUZAFFAR QIZI', 'class': '9 - B'},
    {'id': 311, 'full_name': 'ABABEKOVA SHAXNOZA ISMAILOVNA', 'class': '9 - B'},
    {'id': 312, 'full_name': 'AMETOV AMIRBEK TOREBEKOVICH', 'class': '9 - B'},
    {'id': 313, 'full_name': 'ALLABERGENOV ALLAYAR SAPARBAY ULI', 'class': '9 - C'},
    {'id': 314, 'full_name': 'MAXSETBAYEV JAKSILIK ORINBAYEVICH', 'class': '9 - C'},
    {'id': 315, 'full_name': 'KEULIMJAYEVA SAXIBJAMAL RUSTEMBEK QIZI', 'class': '9 - C'},
    {'id': 316, 'full_name': 'ABDUKARIMOVA RAYXONA ABDIRAXIMOVNA', 'class': '9 - C'},
    {'id': 317, 'full_name': 'MIRZABEKOV DIAR KOMEKBAYEVICH', 'class': '9 - C'},
    {'id': 318, 'full_name': 'KADIRBERGENOV ATABEK TANGIRBERGENOVICH', 'class': '9 - C'},
    {'id': 319, 'full_name': 'TENGELOVA GULJAMILA ADILBEKOVNA', 'class': '9 - C'},
    {'id': 320, 'full_name': 'MAKSETBAYEV NAGMET AZAMAT ULI', 'class': '9 - C'},
    {'id': 321, 'full_name': 'XOJABAYEVA NODIRA ADIL KIZI', 'class': '9 - C'},
    {'id': 322, 'full_name': 'SAATBAYEVA SHAXINA NURLIBAY QIZI', 'class': '9 - C'},
    {'id': 323, 'full_name': 'JANGABAYEV NODIRBEK MANSUROVICH', 'class': '9 - C'},
    {'id': 324, 'full_name': 'KUANISHBAYEVA ZILALA BERDAXOVNA', 'class': '9 - C'},
    {'id': 325, 'full_name': 'TLEUMURATOV SANJARBEK DAVLETBAY ULI', 'class': '9 - C'},
    {'id': 326, 'full_name': 'JALGASBAYEV ALLAYAR RAXATOVICH', 'class': '9 - C'},
    {'id': 327, 'full_name': 'JAKSIMURATOVA TUMARIS XUDAYBERGENOVNA', 'class': '9 - C'},
    {'id': 328, 'full_name': 'SABITOV MUSLIMBEK MANSUROVICH', 'class': '9 - C'},
    {'id': 329, 'full_name': 'KAKABAYEV AYBEK RUSTAM OGLI', 'class': '9 - C'},
    {'id': 330, 'full_name': 'AMETOV AYBEK TOREBEKOVICH', 'class': '9 - C'},
    {'id': 331, 'full_name': 'Kadirbekov Muxammed Ali Anvarbekovich', 'class': '9 - C'},
    {'id': 332, 'full_name': 'Allanazarov Jalaladdin Ziuaddinovich', 'class': '9 - C'},
    {'id': 333, 'full_name': 'Paluaniyazov Polatbek Rustambek uli', 'class': '9 - C'},
    {'id': 334, 'full_name': 'Ziynatdinov Rasul Ruslan uli', 'class': '9 - C'},
    {'id': 335, 'full_name': 'Jienbaev Ramazan Satimurat uli', 'class': '10 - A'},
    {'id': 336, 'full_name': 'Saparbaev Sultanbek Shimbergenovich', 'class': '10 - A'},
    {'id': 337, 'full_name': 'Yakubova Nilufar Farxod qizi', 'class': '10 - A'},
    {'id': 338, 'full_name': 'XOJALEPESOV SHAXRUX SHARAPATDIN ULI', 'class': '10 - A'},
    {'id': 339, 'full_name': 'LEPESBAYEVA UMIDA KOMEKBAY KIZI', 'class': '10 - A'},
    {'id': 340, 'full_name': 'Sharapatdinova Nabira Bayrambaevna', 'class': '10 - A'},
    {'id': 341, 'full_name': 'GOBENOVA AYJAMAL ARISLANBAYEVNA', 'class': '10 - A'},
    {'id': 342, 'full_name': 'Jaqsiboyev Toxir Baxadirovich', 'class': '10 - A'},
    {'id': 343, 'full_name': 'Joldasbaeva Dilnoza Paraxat q?z?', 'class': '10 - A'},
    {'id': 344, 'full_name': 'KEUNIMJAYEVA DURDANA ASAN QIZI', 'class': '10 - A'},
    {'id': 345, 'full_name': 'BAZARBAYEV SHAXRIYOR AZATOVICH', 'class': '10 - A'},
    {'id': 346, 'full_name': 'MAMBETKARIMOV ULUGBEK AMANBAY ULI', 'class': '10 - A'},
    {'id': 347, 'full_name': 'AYMURATOV MIRABAD JOLMURATOVICH', 'class': '10 - A'},
    {'id': 348, 'full_name': 'ADILBEKOVA AKSUNGUL ARISLANBEKOVNA', 'class': '10 - A'},
    {'id': 349, 'full_name': 'TOREMURATOVA TUMARIS RUSTEMOVNA', 'class': '10 - A'},
    {'id': 350, 'full_name': 'KAMALOVA SARBINAZ TIMUR KIZI', 'class': '10 - A'},
    {'id': 351, 'full_name': 'OTEULIYEVA ELEONORA REYMBAYEVNA', 'class': '10 - A'},
    {'id': 352, 'full_name': 'SAMANDAROV ASADBEK JURABEK-OGLI', 'class': '10 - A'},
    {'id': 353, 'full_name': 'MEDETOVA AYSHA ABDIKARIMOVNA', 'class': '10 - A'},
    {'id': 354, 'full_name': 'KEUNIMJAYEVA SANDUGASH AZAMAT QIZI', 'class': '10 - A'},
    {'id': 355, 'full_name': 'TURGANBAYEV ALISHER RASHIDOVICH', 'class': '10 - A'},
    {'id': 356, 'full_name': 'VALEREV DARYABAY BERIK ULI', 'class': '10 - A'},
    {'id': 357, 'full_name': 'Komekbaev Hasilbek Maxsetbaevich', 'class': '10 - A'},
    {'id': 358, 'full_name': 'DJIYENBAYEV JASURBEK TURSINBAY ULI', 'class': '10 - B'},
    {'id': 359, 'full_name': 'BAYTURSINOVA ULDANAY DJENGIS QIZI', 'class': '10 - B'},
    {'id': 360, 'full_name': 'QALBAYEVA MANZURA SHUXRAT QIZI', 'class': '10 - B'},
    {'id': 361, 'full_name': 'JUMABAYEVA NAVBAXOR SHAVKETJAN KIZI', 'class': '10 - B'},
    {'id': 362, 'full_name': 'KOSNAZAROVA NURSULIO? KOSNAZAROVNA', 'class': '10 - B'},
    {'id': 363, 'full_name': 'ORINBAYEVA JASMINA SUNNETBAYEVNA', 'class': '10 - B'},
    {'id': 364, 'full_name': 'ABATBAYEVA MALIKA POLATBAYEVNA', 'class': '10 - B'},
    {'id': 365, 'full_name': 'JANABAYEVA DURDANA SHRAZATDIN KIZI', 'class': '10 - B'},
    {'id': 366, 'full_name': 'AZATOVA GULZADA RINATOVNA', 'class': '10 - B'},
    {'id': 367, 'full_name': 'CHASHEMBAYEVA G?UNCHA ABATOVNA', 'class': '11 - A'},
    {'id': 368, 'full_name': 'TOREBAYEV SULTANBEK BERIKOVICH', 'class': '11 - A'},
    {'id': 369, 'full_name': 'SADADDINOVA AYJAMAL DAULETBAY QIZI', 'class': '11 - A'},
    {'id': 370, 'full_name': 'BAXIYEV RAXIMBEK KONIRATBAY ULI', 'class': '11 - A'},
    {'id': 371, 'full_name': 'Niyazbaev Miyrbek Risatdin uli', 'class': '11 - A'},
    {'id': 372, 'full_name': 'BAXTIYOROV IZZATBEK G?AYRAT O?G?LI', 'class': '11 - A'},
    {'id': 373, 'full_name': 'NIYAZOVA GULAYIM MAXSETBAYEVNA', 'class': '11 - A'},
    {'id': 374, 'full_name': 'YESBOSINOVA GULNAZ TOLIBAYEVNA', 'class': '11 - A'},
    {'id': 375, 'full_name': 'Jangabaeva Mehriban Reimbergenovna', 'class': '11 - A'},
    {'id': 376, 'full_name': 'YAKIPBAYEVA SHAZADA QARJAUBAY QIZI', 'class': '11 - A'},
    {'id': 377, 'full_name': 'KAYIPBERGENOV NURDAULET BEKBERGEN ULI', 'class': '11 - A'},
    {'id': 378, 'full_name': 'BAXTIYAROV AZATBEK RASHIDOVICH', 'class': '11 - A'},
    {'id': 379, 'full_name': 'SHAVKATOVA MAFTUNA SHAVKAT QIZI', 'class': '11 - A'},
    {'id': 380, 'full_name': 'JANDULLAYEVA ARZIGUL TOLIBEKOVNA', 'class': '11 - A'},
    {'id': 381, 'full_name': 'ALLAMBERGENOV DAULETYAR BAXBERGENOVICH', 'class': '11 - A'},
    {'id': 382, 'full_name': 'ORINBAYEVA SHAHLO AMANTAY QIZI', 'class': '11 - A'},
    {'id': 383, 'full_name': 'AMETOVA MAFTUNA BAHADIROVNA', 'class': '11 - A'},
    {'id': 384, 'full_name': 'URAZALIYEV UMRIUZOQ ULUGBEK UG?LI', 'class': '11 - A'},
    {'id': 385, 'full_name': 'TAZABAYEV AMANLIQ TAZABAYEVICH', 'class': '11 - A'},
    {'id': 386, 'full_name': 'SULTAMURATOVA DILNOZA GULMURATOVNA', 'class': '11 - A'},
    {'id': 387, 'full_name': 'Jaksilikova Gulsanem Abdulaxmet', 'class': '11 - B'},
    {'id': 388, 'full_name': 'KAMALOVA XILOLA PALVANBAYEVNA', 'class': '11 - B'},
    {'id': 389, 'full_name': 'BAYMURATOVA AYJAMAL ARISLANBEKOVNA', 'class': '11 - B'},
    {'id': 390, 'full_name': 'AXMEDULLAYEVA DILAFRUZA AYBEK QIZI', 'class': '11 - B'},
    {'id': 391, 'full_name': "Rustamov Ulug'bek Mansurbek o'g'li", 'class': '11 - B'},
    {'id': 392, 'full_name': 'URAZIMBAYEVA FLORA JAKSIBAY QIZI', 'class': '11 - B'},
    {'id': 393, 'full_name': 'BEGJANOVA GULSHAT NURJANOVNA', 'class': '11 - B'},
    {'id': 394, 'full_name': 'RAHIMBOYEVA DILSHODA ANVAR QIZI', 'class': '11 - B'},
    {'id': 395, 'full_name': 'QURBONBOYEVA SHOHISTA ZAFAR QIZI', 'class': '11 - B'},
    {'id': 396, 'full_name': 'ATABAYEV DIYAR AMANMURATOVICH', 'class': '11 - B'},
    {'id': 397, 'full_name': 'SARSENBAYEVA NURIYA RUSTEMOVNA', 'class': '11 - B'},
    {'id': 398, 'full_name': 'Sultansuynova Sogdiana Polat qizi', 'class': '11 - B'},
]

# Qatnashgan talabalarni saqlash
attendance_data = {}

keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/start")]],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id in allowed_users:
        await message.answer("📚 Dáslep pándi tańlań:", reply_markup=await get_subject_buttons())
    else:
        await message.answer("❌ Siz botdan paydalana almaysız!", reply_markup=keyboard)

@dp.message()
async def default_message_handler(message: Message):
    await message.answer("Qatnastı belgilew ushın /start buyrıǵın jiberiń. ❌")

async def get_subject_buttons():
    keyboard = InlineKeyboardBuilder()
    [keyboard.button(text=sub["name"], callback_data=f"subject_{sub['name']}") for sub in subjects]
    return keyboard.adjust(2).as_markup()

@dp.callback_query(F.data.startswith("subject_"))
async def select_lesson_number(call: CallbackQuery):
    subject = call.data.split("_")[1]
    keyboard = InlineKeyboardBuilder()
    [keyboard.button(text=str(i), callback_data=f"lesson_{subject}_{i}") for i in range(1, 8)]
    await call.message.answer(f"📘 {subject} tańlandı. Neshinshi sabaq ekenin tańlań:",
                              reply_markup=keyboard.adjust(2).as_markup())

@dp.callback_query(F.data.startswith("lesson_"))
async def select_class(call: CallbackQuery):
    await call.message.delete()
    _, subject, lesson_number = call.data.split("_")
    classes = {s["class"] for s in students}
    classes = sorted({s["class"] for s in students}, key=lambda x: (int(x.split(" - ")[0]), x.split(" - ")[1]))

    keyboard = InlineKeyboardBuilder()
    [keyboard.button(text=cls, callback_data=f"class_{subject}_{lesson_number}_{cls}") for cls in classes]
    await call.message.answer(f"📘 {subject} - {lesson_number}-sabaq. Endi klasstı tańlań:",
                              reply_markup=keyboard.adjust(2).as_markup())


@dp.callback_query(F.data.startswith("class_"))
async def show_students(call: CallbackQuery):
    await call.message.delete()
    _, subject, lesson_number, selected_class = call.data.split("_")
    class_students = [s for s in students if s["class"] == selected_class]

    if not class_students:
        return await call.message.answer("❌ Bul klassta oqıwshılar joq!")

    keyboard = InlineKeyboardBuilder()
    [keyboard.button(text=s["full_name"], callback_data=f"student_{subject}_{lesson_number}_{s['id']}") for s in class_students]
    keyboard.button(text="✅ Hámme tolıq", callback_data=f"allstudentsareinclass_{subject}_{lesson_number}_{selected_class}")
    keyboard.button(text="✅ Juwmaqlaw", callback_data="finish")

    await call.message.answer(f"📋 {selected_class}-klass. {subject} ({lesson_number}-sabaq) ushın qatnastı belgileń:",
                              reply_markup=keyboard.adjust(2).as_markup())

@dp.callback_query(F.data.startswith("student_"))
async def mark_attendance(call: CallbackQuery):
    _, subject, lesson_number, student_id = call.data.split("_")
    student_id = int(student_id)
    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        await call.answer("❌ Oqıwshı tabılmadı!", show_alert=True)
        return

    key = (student_id, subject, lesson_number)
    if key in attendance_data:
        await call.answer(f"⚠️ {student['full_name']} álle qashan belgilengen!", show_alert=True)
    else:
        attendance_data[key] = True
        asyncio.create_task(send_to_google_sheets(student["full_name"], student["class"], subject, lesson_number))
        await call.answer("✅ Qatnas belgilendi!", show_alert=True)

@dp.callback_query(F.data == "finish")
async def finish_attendance(call: CallbackQuery):
    await call.message.delete()
    await call.answer("✅ Qatnas jiberildi!", show_alert=True)

@dp.callback_query(F.data.startswith("allstudentsareinclass_"))
async def all_students_present(call: CallbackQuery):
    _, subject, lesson_number, student_class = call.data.split("_", 3)

    asyncio.create_task(send_to_google_sheets("Hámme tolıq", student_class, subject, lesson_number))

    await call.answer("✅ Qatnas jiberildi!", show_alert=True)
    await call.message.delete()

@dp.message(Command("report"))
async def send_report(message: types.Message):
    user_id = message.from_user.id
    if user_id in allowed_users:
        if not attendance_data:
            return await message.answer("✅ Búgin barlıq oqıwshılar sabaqta!")

        report_text = "📌 Búgin joqlar:\n" + "\n".join(
            [f"✅ {s['full_name']} ({s['class']}) - {subj} - {lesson} - sabaq"
             for (sid, subj, lesson), _ in attendance_data.items()
             for s in students if s["id"] == sid]
        )
        await message.answer(report_text)
    else:
        await message.answer("❌ Siz botdan paydalana almaysız!")

async def send_to_google_sheets(full_name, student_class, subject, lesson_number):
    url = "https://script.google.com/macros/s/AKfycby4wOMkOf___3VaaBaVI8Iq-mWv6VpBEbitGjCIiaNt0PSnlTLiL37NHHOw52YTRFlx5Q/exec"
    data = {"full_name": full_name, "student_class": student_class, "subject": subject, "lesson_number": lesson_number}
    try:
        requests.post(url, json=data, timeout=5)
    except requests.RequestException as e:
        print("❌ Google Sheetsqa jiberiwde qátelik:", e)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
