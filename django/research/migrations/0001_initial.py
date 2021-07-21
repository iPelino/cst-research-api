# Generated by Django 3.2.3 on 2021-06-07 14:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djmoney.models.fields
import isbn_field.fields
import isbn_field.validators
import research.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colaborator',
            fields=[
                ('colaborator_id', models.CharField(default=research.models.Colaborator.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityEngagement',
            fields=[
                ('engagementId', models.CharField(default=research.models.CommunityEngagement.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('specializedArea', models.CharField(max_length=100)),
                ('communityActivity', models.CharField(max_length=100)),
                ('output', models.CharField(max_length=200)),
                ('planEngagementUsed', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JournalTb',
            fields=[
                ('journal_id', models.CharField(default=research.models.JournalTb.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('[A-Za-z ]+', 'Only alphabetic characters are allowed.')])),
                ('author', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('[A-Za-z ]+', 'Only alphabetic characters are allowed.')])),
                ('publication_year', models.DateField()),
                ('journal', models.CharField(max_length=100)),
                ('Volume', models.CharField(max_length=100)),
                ('series', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('pages', models.PositiveSmallIntegerField()),
                ('issn', models.CharField(max_length=100)),
                ('impact_factor', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MentorShip',
            fields=[
                ('mentorshipId', models.CharField(default=research.models.MentorShip.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('level', models.CharField(max_length=100)),
                ('projectTitle', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PeerReviewedInternational',
            fields=[
                ('serialNumber', models.CharField(default=research.models.PeerReviewedInternational.sn, max_length=200, primary_key=True, serialize=False, unique=True)),
                ('college', models.CharField(choices=[('CST', 'COLLEGE OF SCIENCE AND TECHNOLOGY'), ('CBE', 'COLLEGE OF BUSINESS AND ECONOMY')], max_length=100)),
                ('nameOfConference', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=50)),
                ('theme', models.CharField(max_length=50)),
                ('datesOfPublication', models.DateField(default=django.utils.timezone.now)),
                ('place', models.CharField(max_length=100)),
                ('editor', models.CharField(max_length=30)),
                ('noOfPages', models.IntegerField(default=0)),
                ('isbn', isbn_field.fields.ISBNField(clean_isbn=False, max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN')),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_Research',
            fields=[
                ('id', models.CharField(default=research.models.Tbl_Research.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('research_title', models.CharField(max_length=100)),
                ('starting_date', models.DateTimeField(auto_now_add=True)),
                ('ending_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_conference',
            fields=[
                ('confer_id', models.CharField(default=research.models.Tbl_conference.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('confer_name', models.CharField(max_length=100)),
                ('author', models.EmailField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('theme', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('editor', models.CharField(max_length=100)),
                ('no_of_pages', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=100)),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.tbl_research')),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_chap_based',
            fields=[
                ('chap_based_id', models.CharField(default=research.models.Tbl_chap_based.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('chapter_title', models.CharField(max_length=100)),
                ('author', models.EmailField(max_length=100)),
                ('publication_year', models.DateTimeField(auto_now_add=True)),
                ('book_title', models.CharField(max_length=100)),
                ('chap_pages', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('editor', models.CharField(max_length=100)),
                ('no_of_pages', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=100)),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.tbl_research')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchInnovation',
            fields=[
                ('serialNumber', models.CharField(default=research.models.ResearchInnovation.sn, max_length=200, primary_key=True, serialize=False, unique=True)),
                ('fundingResource', models.CharField(max_length=50)),
                ('fundingAmount_currency', djmoney.models.fields.CurrencyField(choices=[('XUA', 'ADB Unit of Account'), ('AFN', 'Afghan Afghani'), ('AFA', 'Afghan Afghani (1927–2002)'), ('ALL', 'Albanian Lek'), ('ALK', 'Albanian Lek (1946–1965)'), ('DZD', 'Algerian Dinar'), ('ADP', 'Andorran Peseta'), ('AOA', 'Angolan Kwanza'), ('AOK', 'Angolan Kwanza (1977–1991)'), ('AON', 'Angolan New Kwanza (1990–2000)'), ('AOR', 'Angolan Readjusted Kwanza (1995–1999)'), ('ARA', 'Argentine Austral'), ('ARS', 'Argentine Peso'), ('ARM', 'Argentine Peso (1881–1970)'), ('ARP', 'Argentine Peso (1983–1985)'), ('ARL', 'Argentine Peso Ley (1970–1983)'), ('AMD', 'Armenian Dram'), ('AWG', 'Aruban Florin'), ('AUD', 'Australian Dollar'), ('ATS', 'Austrian Schilling'), ('AZN', 'Azerbaijani Manat'), ('AZM', 'Azerbaijani Manat (1993–2006)'), ('BSD', 'Bahamian Dollar'), ('BHD', 'Bahraini Dinar'), ('BDT', 'Bangladeshi Taka'), ('BBD', 'Barbadian Dollar'), ('BYN', 'Belarusian Ruble'), ('BYB', 'Belarusian Ruble (1994–1999)'), ('BYR', 'Belarusian Ruble (2000–2016)'), ('BEF', 'Belgian Franc'), ('BEC', 'Belgian Franc (convertible)'), ('BEL', 'Belgian Franc (financial)'), ('BZD', 'Belize Dollar'), ('BMD', 'Bermudan Dollar'), ('BTN', 'Bhutanese Ngultrum'), ('BOB', 'Bolivian Boliviano'), ('BOL', 'Bolivian Boliviano (1863–1963)'), ('BOV', 'Bolivian Mvdol'), ('BOP', 'Bolivian Peso'), ('BAM', 'Bosnia-Herzegovina Convertible Mark'), ('BAD', 'Bosnia-Herzegovina Dinar (1992–1994)'), ('BAN', 'Bosnia-Herzegovina New Dinar (1994–1997)'), ('BWP', 'Botswanan Pula'), ('BRC', 'Brazilian Cruzado (1986–1989)'), ('BRZ', 'Brazilian Cruzeiro (1942–1967)'), ('BRE', 'Brazilian Cruzeiro (1990–1993)'), ('BRR', 'Brazilian Cruzeiro (1993–1994)'), ('BRN', 'Brazilian New Cruzado (1989–1990)'), ('BRB', 'Brazilian New Cruzeiro (1967–1986)'), ('BRL', 'Brazilian Real'), ('GBP', 'British Pound'), ('BND', 'Brunei Dollar'), ('BGL', 'Bulgarian Hard Lev'), ('BGN', 'Bulgarian Lev'), ('BGO', 'Bulgarian Lev (1879–1952)'), ('BGM', 'Bulgarian Socialist Lev'), ('BUK', 'Burmese Kyat'), ('BIF', 'Burundian Franc'), ('XPF', 'CFP Franc'), ('KHR', 'Cambodian Riel'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verdean Escudo'), ('KYD', 'Cayman Islands Dollar'), ('XAF', 'Central African CFA Franc'), ('CLE', 'Chilean Escudo'), ('CLP', 'Chilean Peso'), ('CLF', 'Chilean Unit of Account (UF)'), ('CNX', 'Chinese People’s Bank Dollar'), ('CNY', 'Chinese Yuan'), ('CNH', 'Chinese Yuan (offshore)'), ('COP', 'Colombian Peso'), ('COU', 'Colombian Real Value Unit'), ('KMF', 'Comorian Franc'), ('CDF', 'Congolese Franc'), ('CRC', 'Costa Rican Colón'), ('HRD', 'Croatian Dinar'), ('HRK', 'Croatian Kuna'), ('CUC', 'Cuban Convertible Peso'), ('CUP', 'Cuban Peso'), ('CYP', 'Cypriot Pound'), ('CZK', 'Czech Koruna'), ('CSK', 'Czechoslovak Hard Koruna'), ('DKK', 'Danish Krone'), ('DJF', 'Djiboutian Franc'), ('DOP', 'Dominican Peso'), ('NLG', 'Dutch Guilder'), ('XCD', 'East Caribbean Dollar'), ('DDM', 'East German Mark'), ('ECS', 'Ecuadorian Sucre'), ('ECV', 'Ecuadorian Unit of Constant Value'), ('EGP', 'Egyptian Pound'), ('GQE', 'Equatorial Guinean Ekwele'), ('ERN', 'Eritrean Nakfa'), ('EEK', 'Estonian Kroon'), ('ETB', 'Ethiopian Birr'), ('EUR', 'Euro'), ('XBA', 'European Composite Unit'), ('XEU', 'European Currency Unit'), ('XBB', 'European Monetary Unit'), ('XBC', 'European Unit of Account (XBC)'), ('XBD', 'European Unit of Account (XBD)'), ('FKP', 'Falkland Islands Pound'), ('FJD', 'Fijian Dollar'), ('FIM', 'Finnish Markka'), ('FRF', 'French Franc'), ('XFO', 'French Gold Franc'), ('XFU', 'French UIC-Franc'), ('GMD', 'Gambian Dalasi'), ('GEK', 'Georgian Kupon Larit'), ('GEL', 'Georgian Lari'), ('DEM', 'German Mark'), ('GHS', 'Ghanaian Cedi'), ('GHC', 'Ghanaian Cedi (1979–2007)'), ('GIP', 'Gibraltar Pound'), ('XAU', 'Gold'), ('GRD', 'Greek Drachma'), ('GTQ', 'Guatemalan Quetzal'), ('GWP', 'Guinea-Bissau Peso'), ('GNF', 'Guinean Franc'), ('GNS', 'Guinean Syli'), ('GYD', 'Guyanaese Dollar'), ('HTG', 'Haitian Gourde'), ('HNL', 'Honduran Lempira'), ('HKD', 'Hong Kong Dollar'), ('HUF', 'Hungarian Forint'), ('IMP', 'IMP'), ('ISK', 'Icelandic Króna'), ('ISJ', 'Icelandic Króna (1918–1981)'), ('INR', 'Indian Rupee'), ('IDR', 'Indonesian Rupiah'), ('IRR', 'Iranian Rial'), ('IQD', 'Iraqi Dinar'), ('IEP', 'Irish Pound'), ('ILS', 'Israeli New Shekel'), ('ILP', 'Israeli Pound'), ('ILR', 'Israeli Shekel (1980–1985)'), ('ITL', 'Italian Lira'), ('JMD', 'Jamaican Dollar'), ('JPY', 'Japanese Yen'), ('JOD', 'Jordanian Dinar'), ('KZT', 'Kazakhstani Tenge'), ('KES', 'Kenyan Shilling'), ('KWD', 'Kuwaiti Dinar'), ('KGS', 'Kyrgystani Som'), ('LAK', 'Laotian Kip'), ('LVL', 'Latvian Lats'), ('LVR', 'Latvian Ruble'), ('LBP', 'Lebanese Pound'), ('LSL', 'Lesotho Loti'), ('LRD', 'Liberian Dollar'), ('LYD', 'Libyan Dinar'), ('LTL', 'Lithuanian Litas'), ('LTT', 'Lithuanian Talonas'), ('LUL', 'Luxembourg Financial Franc'), ('LUC', 'Luxembourgian Convertible Franc'), ('LUF', 'Luxembourgian Franc'), ('MOP', 'Macanese Pataca'), ('MKD', 'Macedonian Denar'), ('MKN', 'Macedonian Denar (1992–1993)'), ('MGA', 'Malagasy Ariary'), ('MGF', 'Malagasy Franc'), ('MWK', 'Malawian Kwacha'), ('MYR', 'Malaysian Ringgit'), ('MVR', 'Maldivian Rufiyaa'), ('MVP', 'Maldivian Rupee (1947–1981)'), ('MLF', 'Malian Franc'), ('MTL', 'Maltese Lira'), ('MTP', 'Maltese Pound'), ('MRU', 'Mauritanian Ouguiya'), ('MRO', 'Mauritanian Ouguiya (1973–2017)'), ('MUR', 'Mauritian Rupee'), ('MXV', 'Mexican Investment Unit'), ('MXN', 'Mexican Peso'), ('MXP', 'Mexican Silver Peso (1861–1992)'), ('MDC', 'Moldovan Cupon'), ('MDL', 'Moldovan Leu'), ('MCF', 'Monegasque Franc'), ('MNT', 'Mongolian Tugrik'), ('MAD', 'Moroccan Dirham'), ('MAF', 'Moroccan Franc'), ('MZE', 'Mozambican Escudo'), ('MZN', 'Mozambican Metical'), ('MZM', 'Mozambican Metical (1980–2006)'), ('MMK', 'Myanmar Kyat'), ('NAD', 'Namibian Dollar'), ('NPR', 'Nepalese Rupee'), ('ANG', 'Netherlands Antillean Guilder'), ('TWD', 'New Taiwan Dollar'), ('NZD', 'New Zealand Dollar'), ('NIO', 'Nicaraguan Córdoba'), ('NIC', 'Nicaraguan Córdoba (1988–1991)'), ('NGN', 'Nigerian Naira'), ('KPW', 'North Korean Won'), ('NOK', 'Norwegian Krone'), ('OMR', 'Omani Rial'), ('PKR', 'Pakistani Rupee'), ('XPD', 'Palladium'), ('PAB', 'Panamanian Balboa'), ('PGK', 'Papua New Guinean Kina'), ('PYG', 'Paraguayan Guarani'), ('PEI', 'Peruvian Inti'), ('PEN', 'Peruvian Sol'), ('PES', 'Peruvian Sol (1863–1965)'), ('PHP', 'Philippine Piso'), ('XPT', 'Platinum'), ('PLN', 'Polish Zloty'), ('PLZ', 'Polish Zloty (1950–1995)'), ('PTE', 'Portuguese Escudo'), ('GWE', 'Portuguese Guinea Escudo'), ('QAR', 'Qatari Rial'), ('XRE', 'RINET Funds'), ('RHD', 'Rhodesian Dollar'), ('RON', 'Romanian Leu'), ('ROL', 'Romanian Leu (1952–2006)'), ('RUB', 'Russian Ruble'), ('RUR', 'Russian Ruble (1991–1998)'), ('RWF', 'Rwandan Franc'), ('SVC', 'Salvadoran Colón'), ('WST', 'Samoan Tala'), ('SAR', 'Saudi Riyal'), ('RSD', 'Serbian Dinar'), ('CSD', 'Serbian Dinar (2002–2006)'), ('SCR', 'Seychellois Rupee'), ('SLL', 'Sierra Leonean Leone'), ('XAG', 'Silver'), ('SGD', 'Singapore Dollar'), ('SKK', 'Slovak Koruna'), ('SIT', 'Slovenian Tolar'), ('SBD', 'Solomon Islands Dollar'), ('SOS', 'Somali Shilling'), ('ZAR', 'South African Rand'), ('ZAL', 'South African Rand (financial)'), ('KRH', 'South Korean Hwan (1953–1962)'), ('KRW', 'South Korean Won'), ('KRO', 'South Korean Won (1945–1953)'), ('SSP', 'South Sudanese Pound'), ('SUR', 'Soviet Rouble'), ('ESP', 'Spanish Peseta'), ('ESA', 'Spanish Peseta (A account)'), ('ESB', 'Spanish Peseta (convertible account)'), ('XDR', 'Special Drawing Rights'), ('LKR', 'Sri Lankan Rupee'), ('SHP', 'St. Helena Pound'), ('XSU', 'Sucre'), ('SDD', 'Sudanese Dinar (1992–2007)'), ('SDG', 'Sudanese Pound'), ('SDP', 'Sudanese Pound (1957–1998)'), ('SRD', 'Surinamese Dollar'), ('SRG', 'Surinamese Guilder'), ('SZL', 'Swazi Lilangeni'), ('SEK', 'Swedish Krona'), ('CHF', 'Swiss Franc'), ('SYP', 'Syrian Pound'), ('STN', 'São Tomé & Príncipe Dobra'), ('STD', 'São Tomé & Príncipe Dobra (1977–2017)'), ('TVD', 'TVD'), ('TJR', 'Tajikistani Ruble'), ('TJS', 'Tajikistani Somoni'), ('TZS', 'Tanzanian Shilling'), ('XTS', 'Testing Currency Code'), ('THB', 'Thai Baht'), ('XXX', 'The codes assigned for transactions where no currency is involved'), ('TPE', 'Timorese Escudo'), ('TOP', 'Tongan Paʻanga'), ('TTD', 'Trinidad & Tobago Dollar'), ('TND', 'Tunisian Dinar'), ('TRY', 'Turkish Lira'), ('TRL', 'Turkish Lira (1922–2005)'), ('TMT', 'Turkmenistani Manat'), ('TMM', 'Turkmenistani Manat (1993–2009)'), ('USD', 'US Dollar'), ('USN', 'US Dollar (Next day)'), ('USS', 'US Dollar (Same day)'), ('UGX', 'Ugandan Shilling'), ('UGS', 'Ugandan Shilling (1966–1987)'), ('UAH', 'Ukrainian Hryvnia'), ('UAK', 'Ukrainian Karbovanets'), ('AED', 'United Arab Emirates Dirham'), ('UYW', 'Uruguayan Nominal Wage Index Unit'), ('UYU', 'Uruguayan Peso'), ('UYP', 'Uruguayan Peso (1975–1993)'), ('UYI', 'Uruguayan Peso (Indexed Units)'), ('UZS', 'Uzbekistani Som'), ('VUV', 'Vanuatu Vatu'), ('VES', 'Venezuelan Bolívar'), ('VEB', 'Venezuelan Bolívar (1871–2008)'), ('VEF', 'Venezuelan Bolívar (2008–2018)'), ('VND', 'Vietnamese Dong'), ('VNN', 'Vietnamese Dong (1978–1985)'), ('CHE', 'WIR Euro'), ('CHW', 'WIR Franc'), ('XOF', 'West African CFA Franc'), ('YDD', 'Yemeni Dinar'), ('YER', 'Yemeni Rial'), ('YUN', 'Yugoslavian Convertible Dinar (1990–1992)'), ('YUD', 'Yugoslavian Hard Dinar (1966–1990)'), ('YUM', 'Yugoslavian New Dinar (1994–2002)'), ('YUR', 'Yugoslavian Reformed Dinar (1992–1993)'), ('ZWN', 'ZWN'), ('ZRN', 'Zairean New Zaire (1993–1998)'), ('ZRZ', 'Zairean Zaire (1971–1993)'), ('ZMW', 'Zambian Kwacha'), ('ZMK', 'Zambian Kwacha (1968–2012)'), ('ZWD', 'Zimbabwean Dollar (1980–2008)'), ('ZWR', 'Zimbabwean Dollar (2008)'), ('ZWL', 'Zimbabwean Dollar (2009)')], default='RWF', editable=False, max_length=3)),
                ('fundingAmount', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='RWF', max_digits=14)),
                ('collaborators', models.ManyToManyField(to='research.Colaborator')),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.tbl_research')),
            ],
        ),
        migrations.AddField(
            model_name='colaborator',
            name='research',
            field=models.ManyToManyField(to='research.Tbl_Research'),
        ),
        migrations.CreateModel(
            name='BookBased',
            fields=[
                ('bookbased_id', models.CharField(default=research.models.BookBased.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('[A-Za-z ]+', 'Only alphabetic characters are allowed.')])),
                ('author', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('[A-Za-z ]+', 'Only alphabetic characters are allowed.')])),
                ('publication_year', models.DateField()),
                ('editor', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('pages', models.PositiveSmallIntegerField()),
                ('isbn', models.CharField(max_length=100)),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.tbl_research')),
            ],
        ),
    ]
