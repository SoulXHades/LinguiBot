#####################################
#		For InlineKeyBoard   	 	#
#-----------------------------------#
#	- All inline buttons goes here  #
#####################################

from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_about_help_targetlang = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='About us', callback_data='/about'), 
InlineKeyboardButton(text='Help', callback_data='/help')],
[InlineKeyboardButton(text='Set target language', callback_data='/targetlang')],
])

keyboard_Cat_A_F = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='A', callback_data='A'),
InlineKeyboardButton(text='B', callback_data='B')],
[InlineKeyboardButton(text='C', callback_data='C'),
InlineKeyboardButton(text='D', callback_data='D')],
[InlineKeyboardButton(text='E', callback_data='E'),
InlineKeyboardButton(text='F', callback_data='F')],
[InlineKeyboardButton(text='Main Menu', callback_data='/start'),
InlineKeyboardButton(text='Next', callback_data='G_K')],
])

keyboard_Cat_G_K = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='G', callback_data='G'),
InlineKeyboardButton(text='H', callback_data='H')],
[InlineKeyboardButton(text='I', callback_data='I'),
InlineKeyboardButton(text='J', callback_data='J')],
[InlineKeyboardButton(text='K', callback_data='K'),
InlineKeyboardButton(text='Main Menu', callback_data='/start')],
[InlineKeyboardButton(text='Previous', callback_data='/targetlang'),
InlineKeyboardButton(text='Next', callback_data='L_P')],
])

keyboard_Cat_L_P = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='L', callback_data='L'),
InlineKeyboardButton(text='M', callback_data='M')],
[InlineKeyboardButton(text='N', callback_data='N'),
InlineKeyboardButton(text='P', callback_data='P')],
[InlineKeyboardButton(text='Previous', callback_data='G_K'),
InlineKeyboardButton(text='Next', callback_data='R_U')],
[InlineKeyboardButton(text='Main Menu', callback_data='/start')],
])

keyboard_Cat_R_U = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='R', callback_data='R'),
InlineKeyboardButton(text='S', callback_data='S')],
[InlineKeyboardButton(text='T', callback_data='T'),
InlineKeyboardButton(text='U', callback_data='U')],
[InlineKeyboardButton(text='Previous', callback_data='L_P'),
InlineKeyboardButton(text='Next', callback_data='V_Z')],
[InlineKeyboardButton(text='Main Menu', callback_data='/start')],
])

keyboard_Cat_V_Z = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='V', callback_data='V'),
InlineKeyboardButton(text='W', callback_data='W')],
[InlineKeyboardButton(text='X', callback_data='X'),
InlineKeyboardButton(text='Y', callback_data='Y')],
[InlineKeyboardButton(text='Z', callback_data='Z'),
InlineKeyboardButton(text='Previous', callback_data='R_U')],
[InlineKeyboardButton(text='Main Menu', callback_data='/start')],
])

keyboard_mainpage = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Main Menu', callback_data='/start')],
])

keyboard_lang_A = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Afrikaans', callback_data='/afri'),
InlineKeyboardButton(text='Albanian', callback_data='/al')],
[InlineKeyboardButton(text='Amharic', callback_data='/am'),
InlineKeyboardButton(text='Arabic', callback_data='/arab')],
[InlineKeyboardButton(text='Armenian', callback_data='/armen'),
InlineKeyboardButton(text='Azeerbaijani', callback_data='/azeer')],
[InlineKeyboardButton(text='Back to Cat List', callback_data='/targetlang')],
])

keyboard_lang_B = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Basque', callback_data='/bas'),
InlineKeyboardButton(text='Belarusian', callback_data='/bel')],
[InlineKeyboardButton(text='Bengali', callback_data='/ben'),
InlineKeyboardButton(text='Bosnian', callback_data='/bos')],
[InlineKeyboardButton(text='Bulgarian', callback_data='/bul'),
InlineKeyboardButton(text='Back to Cat List', callback_data='/targetlang')],
])

keyboard_lang_C = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Catalan', callback_data='/cat'),
InlineKeyboardButton(text='Cebuano', callback_data='/ceb')],
[InlineKeyboardButton(text='Chinese Simplified', callback_data='/chisimp'),
InlineKeyboardButton(text='Chinese Traditional', callback_data='/chitrad')],
[InlineKeyboardButton(text='Corsican', callback_data='/corsi'),
InlineKeyboardButton(text='Croatian', callback_data='/croat')],
[InlineKeyboardButton(text='Czech', callback_data='/czech'),
InlineKeyboardButton(text='Back to Cat List', callback_data='/targetlang')],
])

keyboard_lang_D = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Danish', callback_data='/danish'),
InlineKeyboardButton(text='Dutch', callback_data='/dutch')],
[InlineKeyboardButton(text='Back to Cat List', callback_data='/targetlang')],
])

keyboard_lang_E = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='English', callback_data='/eng'),
InlineKeyboardButton(text='Esperanto', callback_data='/esp')],
[InlineKeyboardButton(text='Estonian', callback_data='/est'),
InlineKeyboardButton(text='Back to Cat List', callback_data='/targetlang')],
])

keyboard_lang_F = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Finnish', callback_data='/fin'),
InlineKeyboardButton(text='French', callback_data='/french')],
[InlineKeyboardButton(text='Frisian', callback_data='/fri'),
InlineKeyboardButton(text='Back to Cat List', callback_data='/targetlang')],
])

keyboard_lang_G = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Galician', callback_data='/gali'),
InlineKeyboardButton(text='Georgian', callback_data='/geo')],
[InlineKeyboardButton(text='Greekman', callback_data='/greekman'),
InlineKeyboardButton(text='Greek', callback_data='/greek')],
[InlineKeyboardButton(text='Gujarati', callback_data='/guja'),
InlineKeyboardButton(text='Back to Cat List', callback_data='G_K')],
])

keyboard_lang_H = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Haitian Creole', callback_data='/haiti'),
InlineKeyboardButton(text='Hausa', callback_data='/hausa')],
[InlineKeyboardButton(text='Hawaiian', callback_data='/haw'),
InlineKeyboardButton(text='Hebrew', callback_data='/heb')],
[InlineKeyboardButton(text='Hindi', callback_data='/hindi'),
InlineKeyboardButton(text='Hmong', callback_data='/hmong')],
[InlineKeyboardButton(text='Hungarian', callback_data='/hung'),
InlineKeyboardButton(text='Back to Cat List', callback_data='G_K')],
])

keyboard_lang_I = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Icelandic', callback_data='/ice'),
InlineKeyboardButton(text='Igbo', callback_data='/igbo')],
[InlineKeyboardButton(text='Indonesian', callback_data='/indo'),
InlineKeyboardButton(text='Irish', callback_data='/irish')],
[InlineKeyboardButton(text='Italian', callback_data='/italian'),
InlineKeyboardButton(text='Back to Cat List', callback_data='G_K')],
])

keyboard_lang_J = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Japanese', callback_data='/jap'),
InlineKeyboardButton(text='Javanese', callback_data='/java')],
[InlineKeyboardButton(text='Back to Cat List', callback_data='G_K')],
])

keyboard_lang_K = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Kannada', callback_data='/kan'),
InlineKeyboardButton(text='Kazakh', callback_data='/kaz')],
[InlineKeyboardButton(text='Khmer', callback_data='/khmer'),
InlineKeyboardButton(text='Korean', callback_data='/kor')],
[InlineKeyboardButton(text='Kurdish', callback_data='/kur'),
InlineKeyboardButton(text='Kyrgyz', callback_data='/kyrgyz')],
[InlineKeyboardButton(text='Back to Cat List', callback_data='G_K')],
])

keyboard_lang_L = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Lao', callback_data='/lao'),
InlineKeyboardButton(text='Latin', callback_data='/latin')],
[InlineKeyboardButton(text='Latvian', callback_data='/latvian'),
InlineKeyboardButton(text='Lithuanian', callback_data='/lit')],
[InlineKeyboardButton(text='Luxembourgish', callback_data='/lux'),
InlineKeyboardButton(text='Back to Cat List', callback_data='L_P')],
])

keyboard_lang_M = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Macedonian', callback_data='/mace'),
InlineKeyboardButton(text='Malagasy', callback_data='/malagasy')],
[InlineKeyboardButton(text='Malay', callback_data='/malay'),
InlineKeyboardButton(text='Malayalam', callback_data='/malayalam')],
[InlineKeyboardButton(text='Maltese', callback_data='/malt'),
InlineKeyboardButton(text='Maori', callback_data='/maori')],
[InlineKeyboardButton(text='Back to Cat List', callback_data='L_P'),
InlineKeyboardButton(text='Next', callback_data='M1')],
])

keyboard_lang_M1 = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Marathi', callback_data='/mara'),
InlineKeyboardButton(text='Mongolian', callback_data='/mongo')],
[InlineKeyboardButton(text='Myanmar', callback_data='/myan'),
InlineKeyboardButton(text='Previous', callback_data='M')],
[InlineKeyboardButton(text='Back to Cat List', callback_data='L_P')],
])

keyboard_lang_N = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Nepali', callback_data='/nepa'),
InlineKeyboardButton(text='Norwegian', callback_data='/nor')],
[InlineKeyboardButton(text='Nyanja', callback_data='/nyan'),
InlineKeyboardButton(text='Back to Cat List', callback_data='L_P')],
])

keyboard_lang_P = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Pashto', callback_data='/pash'),
InlineKeyboardButton(text='Persian', callback_data='/per')],
[InlineKeyboardButton(text='Polish', callback_data='/pol'),
InlineKeyboardButton(text='Portuguese', callback_data='/port')],
[InlineKeyboardButton(text='Punjabi', callback_data='/pun'),
InlineKeyboardButton(text='Back to Cat List', callback_data='L_P')],
])

keyboard_lang_R = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Romanian', callback_data='/rom'),
InlineKeyboardButton(text='Russian', callback_data='/ru')],
[InlineKeyboardButton(text='Back to Cat List', callback_data='R_U')],
])

keyboard_lang_S = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Samoan', callback_data='/sam'),
InlineKeyboardButton(text='ScotsGaelic', callback_data='/scots')],
[InlineKeyboardButton(text='Serbian', callback_data='/ser'),
InlineKeyboardButton(text='Sesotho', callback_data='/ses')],
[InlineKeyboardButton(text='Shona', callback_data='/shona'),
InlineKeyboardButton(text='Sindhi', callback_data='/sindhi')],
[InlineKeyboardButton(text='Back to Cat List', callback_data='R_U'),
InlineKeyboardButton(text='Next', callback_data='S1')],
])

keyboard_lang_S1 = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Sinhala', callback_data='/sinhala'),
InlineKeyboardButton(text='Slovak', callback_data='/slovak')],
[InlineKeyboardButton(text='Slovenian', callback_data='/sloven'),
InlineKeyboardButton(text='Somali', callback_data='/somali')],
[InlineKeyboardButton(text='Spanish', callback_data='/span'),
InlineKeyboardButton(text='Back to Cat List', callback_data='R_U')],
[InlineKeyboardButton(text='Previous', callback_data='S'),
InlineKeyboardButton(text='Next', callback_data='S2')],
])

keyboard_lang_S2 = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Sundanese', callback_data='/sun'),
InlineKeyboardButton(text='Swahili', callback_data='/swa')],
[InlineKeyboardButton(text='Swedish', callback_data='/swed'),
InlineKeyboardButton(text='Previous', callback_data='S1')],
[InlineKeyboardButton(text='Back to Cat List', callback_data='R_U')],
])

keyboard_lang_T = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Tagalog', callback_data='/taga'),
InlineKeyboardButton(text='Tajik', callback_data='/tajik')],
[InlineKeyboardButton(text='Tamil', callback_data='/tamil'),
InlineKeyboardButton(text='Telugu', callback_data='/telugu')],
[InlineKeyboardButton(text='Thai', callback_data='/thai'),
InlineKeyboardButton(text='Turkish', callback_data='/turk')],
[InlineKeyboardButton(text='Back to Cat List', callback_data='R_U')],
])

keyboard_lang_U = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Ukrainian', callback_data='/uk'),
InlineKeyboardButton(text='Urdu', callback_data='/urdu')],
[InlineKeyboardButton(text='Uzbek', callback_data='/uzbek'),
InlineKeyboardButton(text='Back to Cat List', callback_data='R_U')],
])

keyboard_lang_V = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Vietnamese', callback_data='/viet'),
InlineKeyboardButton(text='Back to Cat List', callback_data='V_Z')],
])

keyboard_lang_W = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Welsh', callback_data='/welsh'),
InlineKeyboardButton(text='Back to Cat List', callback_data='V_Z')],
])

keyboard_lang_X = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Xhosa', callback_data='/xhosa'),
InlineKeyboardButton(text='Back to Cat List', callback_data='V_Z')],
])

keyboard_lang_Y = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Yiddish', callback_data='/yid'),
InlineKeyboardButton(text='Yoruba', callback_data='/yoru')],
[InlineKeyboardButton(text='Back to Cat List', callback_data='V_Z')],
])

keyboard_lang_Z = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Zulu', callback_data='/zulu'),
InlineKeyboardButton(text='Back to Cat List', callback_data='V_Z')],
])

inLineKeyboardDict = \
	{'about_help_targetlang': keyboard_about_help_targetlang, 
	'G_K': keyboard_Cat_G_K, 
	'L_P': keyboard_Cat_L_P,
	'R_U': keyboard_Cat_R_U,
	'V_Z': keyboard_Cat_V_Z,
	'A': keyboard_lang_A,
	'B': keyboard_lang_B,
	'C': keyboard_lang_C,
	'D': keyboard_lang_D,
	'E': keyboard_lang_E,
	'F': keyboard_lang_F,
	'G': keyboard_lang_G,
	'H': keyboard_lang_H,
	'I': keyboard_lang_I,
	'J': keyboard_lang_J,
	'K': keyboard_lang_K,
	'L': keyboard_lang_L,
	'M': keyboard_lang_M,
	'M1': keyboard_lang_M1,
	'N': keyboard_lang_N,
	'P': keyboard_lang_P,
	'R': keyboard_lang_R,
	'S': keyboard_lang_S,
	'S1': keyboard_lang_S1,
	'S2': keyboard_lang_S2,
	'T': keyboard_lang_T,
	'U': keyboard_lang_U,
	'V': keyboard_lang_V,
	'W': keyboard_lang_W,
	'X': keyboard_lang_X,
	'Y': keyboard_lang_Y,
	'Z': keyboard_lang_Z,
 	'mainmenu': keyboard_mainpage, 
 	'targetlang': keyboard_Cat_A_F}